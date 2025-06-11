# 🛰️ Drone Mapping Simulation Interface

This is a **Streamlit-based web application** that simulates real-time drone-based mapping using **mock sensor data**.

## 🌟 Features

- 🗺️ Interactive Folium map with markers
- 🌡️ Popups showing temperature, humidity, NDVI, and material type
- 🔥 Heatmap toggle based on heat signature
- 🔍 Filter data based on use cases:
  - Agriculture (Vegetation focus)
  - Construction (Concrete, Asphalt)
  - Search & Rescue (High heat signature)

## 📦 Tech Stack

- Python
- Streamlit
- Pandas
- Folium
- Geopy

## 🚀 How to Run

```bash

cd drone mapping

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run drone_mapping.py
