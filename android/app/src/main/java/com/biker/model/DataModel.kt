package com.biker.model

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "data_table")
data class DataModel(
    @PrimaryKey(autoGenerate = true) val id: Int = 0,
    val timestamp: Long = 0L,
    val value: Float = 0f
)