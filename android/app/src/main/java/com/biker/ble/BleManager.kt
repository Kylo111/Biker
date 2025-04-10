package com.biker.ble

import android.bluetooth.BluetoothDevice
import android.bluetooth.BluetoothGatt
import android.bluetooth.BluetoothGattCharacteristic
import android.content.Context
import android.util.Log
import androidx.lifecycle.LiveData
import no.nordicsemi.android.ble.BleManager
import no.nordicsemi.android.ble.callback.FailCallback
import no.nordicsemi.android.ble.callback.SuccessCallback
import no.nordicsemi.android.ble.data.Data
import no.nordicsemi.android.ble.livedata.ObservableBleManager
import no.nordicsemi.android.ble.livedata.state.ConnectionState

// Tag for logging
private const val TAG = "BleManager"

class BleManager(context: Context) : ObservableBleManager(context) {

    // LiveData for connection state and bonding state
    val connectionState: LiveData<ConnectionState> get() = state // Expose the state LiveData
    // val bondingState: LiveData<BondingState> get() = bondingState // If bonding is needed

    // Optional: LiveData for received data (replace Any with your data type)
    // private val _receivedData = MutableLiveData<Any>()
    // val receivedData: LiveData<Any> get() = _receivedData

    private var dataCharacteristic: BluetoothGattCharacteristic? = null
    // Add other characteristic variables if needed (e.g., controlCharacteristic)

    private val connectionObserver = object : BleManagerGattCallback() {

        override fun initialize() {
            // Called when the device is ready to communicate.
            // Request MTU for faster data transfer. Recommended MTU is 247 bytes.
            requestMtu(247).enqueue()
            // Enable notifications or indications if needed
            // setNotificationCallback(dataCharacteristic).with(object : DataReceivedCallback { ... })
            // enableNotifications(dataCharacteristic).enqueue()
            Log.i(TAG, "Device initialized")
        }

        override fun isRequiredServiceSupported(gatt: BluetoothGatt): Boolean {
            // Check if the required services and characteristics are supported by the device.
            // Replace YOUR_SERVICE_UUID and YOUR_CHARACTERISTIC_UUID with actual UUIDs
            // val service = gatt.getService(YOUR_SERVICE_UUID)
            // if (service != null) {
            //     dataCharacteristic = service.getCharacteristic(YOUR_CHARACTERISTIC_UUID)
            // }
            // return dataCharacteristic != null

            // For now, assume the service is supported
            Log.d(TAG, "isRequiredServiceSupported check")
            return true // Placeholder
        }

        override fun onServicesInvalidated() {
            // Called when the services are no longer valid (e.g., device disconnected).
            Log.w(TAG, "Services invalidated")
            dataCharacteristic = null
            // Potentially update UI or state here
        }

        // Optional: Override onCharacteristicChanged to handle incoming data
        // override fun onCharacteristicChanged(gatt: BluetoothGatt, characteristic: BluetoothGattCharacteristic, value: ByteArray) {
        //     Log.d(TAG, "Received data: ${value.toHexString()}")
        //     _receivedData.postValue(value) // Update LiveData
        // }

        // Optional: Override other callbacks like onMtuChanged, etc.
    }

    override fun getGattCallback(): BleManagerGattCallback = connectionObserver

    // Connect to the device
    fun connect(device: BluetoothDevice) {
        connect(device)
            .retry(3, 100) // Retry 3 times with 100ms delay
            .useAutoConnect(false) // Auto connect disabled for faster connection attempt
            .done { Log.d(TAG, "Connected to ${device.address}") }
            .fail { _, status -> Log.e(TAG, "Connection failed with status: $status") }
            .enqueue() // Enqueue the connection request
    }

    // Disconnect from the device
    fun disconnectDevice() {
        disconnect().enqueue()
        Log.i(TAG, "Disconnecting...")
    }

    // Add functions for sending data if needed
    // fun sendData(data: ByteArray) {
    //     writeCharacteristic(dataCharacteristic, data)
    //         .done { Log.d(TAG, "Data sent: ${data.toHexString()}") }
    //         .fail { _, status -> Log.e(TAG, "Failed to send data, status: $status") }
    //         .enqueue()
    // }
}