package com.biker.ble

import android.bluetooth.BluetoothDevice
import android.content.Context
import androidx.arch.core.executor.testing.InstantTaskExecutorRule
import androidx.lifecycle.Observer
import io.mockk.*
import no.nordicsemi.android.ble.ConnectRequest
import no.nordicsemi.android.ble.livedata.state.ConnectionState
import org.junit.Before
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.RobolectricTestRunner
import org.robolectric.RuntimeEnvironment

@RunWith(RobolectricTestRunner::class) // Use Robolectric for Android context
class BleManagerTest {

    // Rule to execute LiveData operations synchronously
    @get:Rule
    val instantExecutorRule = InstantTaskExecutorRule()

    private lateinit var context: Context
    private lateinit var bleManager: BleManager
    private lateinit var mockDevice: BluetoothDevice
    private lateinit var mockConnectRequest: ConnectRequest

    @Before
    fun setUp() {
        context = RuntimeEnvironment.getApplication() // Get context from Robolectric
        bleManager = spyk(BleManager(context)) // Use spyk to allow mocking specific methods

        // Mock BluetoothDevice and ConnectRequest
        mockDevice = mockk(relaxed = true)
        mockConnectRequest = mockk(relaxed = true)

        // Mock the connect method to return our mocked ConnectRequest
        every { bleManager.connect(any<BluetoothDevice>()) } returns mockConnectRequest
        // Mock enqueue to do nothing for now
        every { mockConnectRequest.enqueue() } just Runs
        // Mock other chained methods if needed
        every { mockConnectRequest.retry(any(), any()) } returns mockConnectRequest
        every { mockConnectRequest.useAutoConnect(any()) } returns mockConnectRequest
        every { mockConnectRequest.done(any()) } returns mockConnectRequest
        every { mockConnectRequest.fail(any()) } returns mockConnectRequest
    }

    @Test
    fun `connect should initiate connection process`() {
        // Arrange
        val observer = mockk<Observer<ConnectionState>>(relaxed = true)
        bleManager.connectionState.observeForever(observer) // Observe LiveData

        // Act
        bleManager.connect(mockDevice)

        // Assert
        // Verify that the connect method on the BleManager (superclass) was called
        verify { bleManager.connect(mockDevice) }
        // Verify that enqueue was called on the ConnectRequest
        verify { mockConnectRequest.enqueue() }

        // Optional: Verify state changes if you mock the callback behavior
        // For a simple test, verifying the initiation is often sufficient.

        bleManager.connectionState.removeObserver(observer) // Clean up observer
    }

    // Add more tests for disconnect, data sending/receiving (when implemented)
}