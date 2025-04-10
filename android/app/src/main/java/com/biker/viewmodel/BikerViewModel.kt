package com.biker.viewmodel

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.biker.model.DataModel
import com.biker.repository.BikerRepository

class BikerViewModel(private val repository: BikerRepository) : ViewModel() {

    private val _data = MutableLiveData<List<DataModel>>()
    val data: LiveData<List<DataModel>> = _data

    fun fetchData() {
        // Placeholder: pobierz dane z repozytorium
        _data.value = repository.getData()
    }

    fun connectToBleDevice() {
        // Placeholder: połącz z urządzeniem BLE przez repozytorium
        repository.connectBle()
    }
}