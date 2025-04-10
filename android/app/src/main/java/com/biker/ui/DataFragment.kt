package com.biker.ui

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment

class DataFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Placeholder: tutaj załaduj layout z wykresem (np. Vico lub MPAndroidChart)
        // return inflater.inflate(R.layout.fragment_data, container, false)
        return super.onCreateView(inflater, container, savedInstanceState)
    }
}