package com.biker.ui

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.biker.ble.BleManager

class MainActivity : AppCompatActivity() {

    private lateinit var bleManager: BleManager

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // Placeholder: ustaw layout, np. setContentView(R.layout.activity_main)
        // setContentView(R.layout.activity_main)

        // Placeholder: inicjalizacja BLE
        bleManager = BleManager(this)
        bleManager.initialize()
    }
}