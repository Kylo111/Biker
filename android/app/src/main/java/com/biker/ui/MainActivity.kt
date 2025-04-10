package com.biker.ui

import android.Manifest
import android.bluetooth.BluetoothAdapter
import android.bluetooth.BluetoothDevice
import android.content.Intent
import android.content.pm.PackageManager
import android.os.Build
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import androidx.lifecycle.Observer
import com.biker.R // Upewnij się, że R jest poprawnie zaimportowane
import com.biker.ble.BleManager
import no.nordicsemi.android.ble.livedata.state.ConnectionState

// Tag for logging
private const val TAG = "MainActivity"

// Request codes for permissions
private const val REQUEST_ENABLE_BT = 1
// private const val REQUEST_PERMISSIONS = 2 // Nie jest już potrzebne z nowym API

class MainActivity : AppCompatActivity() {

    private lateinit var bleManager: BleManager
    private lateinit var connectionStatusTextView: TextView
    private lateinit var connectButton: Button // Przycisk do łączenia/rozłączania

    // Example: Hardcoded device address for testing - ZASTĄP ADRESEM SWOJEGO ESP8266
    private val TARGET_DEVICE_ADDRESS = "XX:XX:XX:XX:XX:XX" // <-- ZASTĄP TO!

    // Activity Result Launcher for enabling Bluetooth
    private val enableBtLauncher = registerForActivityResult(
        ActivityResultContracts.StartActivityForResult()
    ) { result ->
        if (result.resultCode == RESULT_OK) {
            Log.d(TAG, "Bluetooth enabled")
            checkPermissionsAndConnect() // Sprawdź uprawnienia po włączeniu BT
        } else {
            Log.w(TAG, "Bluetooth not enabled by user")
            Toast.makeText(this, R.string.bluetooth_required, Toast.LENGTH_SHORT).show()
        }
    }

    // Activity Result Launcher for requesting permissions
    private val requestPermissionsLauncher = registerForActivityResult(
        ActivityResultContracts.RequestMultiplePermissions()
    ) { permissions ->
        if (permissions.all { it.value }) {
            Log.d(TAG, "All required permissions granted")
            // Uprawnienia przyznane, spróbuj połączyć
            connectToDevice()
        } else {
            Log.w(TAG, "Not all permissions granted by user")
            Toast.makeText(this, R.string.permissions_required, Toast.LENGTH_SHORT).show()
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main) // Ustaw layout

        // Znajdź widoki w layoucie
        connectionStatusTextView = findViewById(R.id.connectionStatusTextView) // Upewnij się, że masz TextView z tym ID
        connectButton = findViewById(R.id.connectButton) // Upewnij się, że masz Button z tym ID

        // Inicjalizacja BleManager
        bleManager = BleManager(this)

        // Obserwuj zmiany stanu połączenia
        bleManager.connectionState.observe(this, Observer { state ->
            updateConnectionStatus(state)
        })

        // Ustaw listener dla przycisku
        connectButton.setOnClickListener {
            if (bleManager.isConnected) {
                bleManager.disconnectDevice()
            } else {
                // Rozpocznij proces sprawdzania BT i uprawnień przed połączeniem
                checkBluetoothAndPermissions()
            }
        }
    }

    // Sprawdza, czy Bluetooth jest włączony, jeśli nie, prosi o włączenie
    private fun checkBluetoothAndPermissions() {
        val bluetoothAdapter = BluetoothAdapter.getDefaultAdapter()
        if (bluetoothAdapter == null) {
            Toast.makeText(this, R.string.bluetooth_not_supported, Toast.LENGTH_SHORT).show()
            return
        }

        if (!bluetoothAdapter.isEnabled) {
            Log.d(TAG, "Bluetooth is disabled, requesting enable.")
            val enableBtIntent = Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE)
            enableBtLauncher.launch(enableBtIntent)
        } else {
            Log.d(TAG, "Bluetooth is enabled, checking permissions.")
            checkPermissionsAndConnect() // Bluetooth jest włączony, sprawdź uprawnienia
        }
    }

    // Sprawdza wymagane uprawnienia i prosi o nie, jeśli brakuje
    private fun checkPermissionsAndConnect() {
        val requiredPermissions = mutableListOf<String>()

        // Uprawnienia dla Android 12+
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
            if (ContextCompat.checkSelfPermission(this, Manifest.permission.BLUETOOTH_SCAN) != PackageManager.PERMISSION_GRANTED) {
                requiredPermissions.add(Manifest.permission.BLUETOOTH_SCAN)
            }
            if (ContextCompat.checkSelfPermission(this, Manifest.permission.BLUETOOTH_CONNECT) != PackageManager.PERMISSION_GRANTED) {
                requiredPermissions.add(Manifest.permission.BLUETOOTH_CONNECT)
            }
        }
        // Uprawnienia dla Android 6-11 (lokalizacja do skanowania BLE)
        else {
            if (ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
                requiredPermissions.add(Manifest.permission.ACCESS_FINE_LOCATION)
            }
            // Starsze uprawnienia BT są przyznawane automatycznie, jeśli są w manifeście
        }

        if (requiredPermissions.isNotEmpty()) {
            Log.d(TAG, "Requesting permissions: ${requiredPermissions.joinToString()}")
            requestPermissionsLauncher.launch(requiredPermissions.toTypedArray())
        } else {
            // Wszystkie wymagane uprawnienia są przyznane
            Log.d(TAG, "All permissions granted, proceeding to connect.")
            connectToDevice()
        }
    }

    // Próbuje połączyć się z urządzeniem o zadanym adresie MAC
    private fun connectToDevice() {
        if (TARGET_DEVICE_ADDRESS == "XX:XX:XX:XX:XX:XX") {
             Toast.makeText(this, "Zastąp TARGET_DEVICE_ADDRESS w MainActivity!", Toast.LENGTH_LONG).show()
             Log.e(TAG, "TARGET_DEVICE_ADDRESS not set!")
             return
        }

        val bluetoothAdapter = BluetoothAdapter.getDefaultAdapter()
        if (!bluetoothAdapter.isEnabled) {
             Log.w(TAG, "Bluetooth is not enabled, cannot connect")
             return
        }

        try {
            val device = bluetoothAdapter.getRemoteDevice(TARGET_DEVICE_ADDRESS)
            Log.i(TAG, "Attempting to connect to device: ${device.address}")
            connectionStatusTextView.text = getString(R.string.status_connecting) // Aktualizuj UI
            connectButton.isEnabled = false
            bleManager.connect(device)
        } catch (e: IllegalArgumentException) {
            Log.e(TAG, "Invalid Bluetooth address: $TARGET_DEVICE_ADDRESS", e)
            Toast.makeText(this, R.string.invalid_device_address, Toast.LENGTH_SHORT).show()
            connectionStatusTextView.text = getString(R.string.status_disconnected) // Resetuj UI
            connectButton.isEnabled = true
        }
    }

    // Aktualizuje UI na podstawie stanu połączenia
    private fun updateConnectionStatus(state: ConnectionState) {
        runOnUiThread { // Upewnij się, że aktualizacje UI są w głównym wątku
            when (state) {
                is ConnectionState.Connecting -> {
                    connectionStatusTextView.text = getString(R.string.status_connecting)
                    connectButton.text = getString(R.string.action_connecting)
                    connectButton.isEnabled = false
                }
                is ConnectionState.Initializing -> {
                    connectionStatusTextView.text = getString(R.string.status_initializing)
                    connectButton.text = getString(R.string.action_initializing)
                    connectButton.isEnabled = false
                }
                is ConnectionState.Ready -> {
                    connectionStatusTextView.text = getString(R.string.status_connected)
                    connectButton.text = getString(R.string.action_disconnect)
                    connectButton.isEnabled = true
                    Log.i(TAG, "Device Ready")
                }
                is ConnectionState.Disconnecting -> {
                    connectionStatusTextView.text = getString(R.string.status_disconnecting)
                    connectButton.text = getString(R.string.action_disconnecting)
                    connectButton.isEnabled = false
                }
                is ConnectionState.Disconnected -> {
                    connectionStatusTextView.text = getString(R.string.status_disconnected)
                    connectButton.text = getString(R.string.action_connect)
                    connectButton.isEnabled = true
                    when (state.reason) {
                        ConnectionObserver.REASON_SUCCESS -> Log.i(TAG, "Disconnected")
                        ConnectionObserver.REASON_TIMEOUT -> Log.w(TAG, "Disconnected: Timeout")
                        ConnectionObserver.REASON_TERMINATE_LOCAL_HOST -> Log.w(TAG, "Disconnected: Local host terminated connection")
                        ConnectionObserver.REASON_TERMINATE_PEER_USER -> Log.w(TAG, "Disconnected: Peer user terminated connection")
                        ConnectionObserver.REASON_LINK_LOSS -> Log.w(TAG, "Disconnected: Link loss")
                        ConnectionObserver.REASON_NOT_SUPPORTED -> Log.e(TAG, "Disconnected: Device not supported")
                        ConnectionObserver.REASON_CANCELLED -> Log.i(TAG, "Disconnected: Cancelled")
                        ConnectionObserver.REASON_UNKNOWN -> Log.w(TAG, "Disconnected: Unknown reason")
                        else -> Log.w(TAG, "Disconnected with reason: ${state.reason}")
                    }
                }
            }
        }
    }
}