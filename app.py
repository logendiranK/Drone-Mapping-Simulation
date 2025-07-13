import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from geopy.distance import geodesic

# Mock Data
data = [
    {
        "latitude": 12.9065,
        "longitude": 80.2273,
        "altitude": 15,
        "temperature": 20.5,
        "humidity": 55,
        "soil_moisture": 30,
        "ndvi": 0.8,
        "material_detected": "Concrete",
        "heat_signature": 75,
        "timestamp": "2024-08-16T10:00:00Z"
    },
    {
        "latitude": 12.9600,
        "longitude": 80.2456,
        "altitude": 7,
        "temperature": 20.7,
        "humidity": 53,
        "soil_moisture": 28,
        "ndvi": 0.7,
        "material_detected": "Asphalt",
        "heat_signature": 70,
        "timestamp": "2024-08-16T10:01:00Z"
    },
    {
        "latitude": 12.9229,
        "longitude": 80.1275,
        "altitude": 12,
        "temperature": 21.5,
        "humidity": 52,
        "soil_moisture": 33,
        "ndvi": 0.85,
        "material_detected": "Vegetation",
        "heat_signature": 68,
        "timestamp": "2024-08-16T10:03:00Z"
    },
    {
        "latitude":12.9548 ,
        "longitude":  80.1832,
        "altitude": 15,
        "temperature": 20.3,
        "humidity": 57,
        "soil_moisture": 29,
        "ndvi": 0.65,
        "material_detected": "Concrete",
        "heat_signature": 73,
        "timestamp": "2024-08-16T10:04:00Z"
    },
    {
        "latitude":  12.9444,
        "longitude":  80.2186,
        "altitude": 5,
        "temperature": 19.8,
        "humidity": 58,
        "soil_moisture": 27,
        "ndvi": 0.78,
        "material_detected": "Asphalt",
        "heat_signature": 74,
        "timestamp": "2024-08-16T10:05:00Z"
    },
    {
        "latitude": 12.8816,
        "longitude":80.1354 ,
        "altitude":8,
        "temperature": 20.9,
        "humidity": 54,
        "soil_moisture": 34,
        "ndvi": 0.88,
        "material_detected": "Vegetation",
        "heat_signature": 63,
        "timestamp": "2024-08-16T10:06:00Z"
    },
    {
        "latitude": 12.9670,
        "longitude": 80.1590,
        "altitude": 12,
        "temperature": 22.1,
        "humidity": 51,
        "soil_moisture": 31,
        "ndvi": 0.92,
        "material_detected": "Vegetation",
        "heat_signature": 66,
        "timestamp": "2024-08-16T10:07:00Z"
    },

]


df = pd.DataFrame(data)

st.title("Drone Mapping Simulation Interface")

st.header("Map Visualization")
map_center = [df['latitude'].mean(), df['longitude'].mean()]
m = folium.Map(location=map_center, zoom_start=15)

for index, row in df.iterrows():
    folium.Marker(
        [row['latitude'], row['longitude']],
        popup=f"Temperature: {row['temperature']}°C\nHumidity: {row['humidity']}%\nNDVI: {row['ndvi']}\nMaterial: {row['material_detected']}\nHeat Signature: {row['heat_signature']}°C"
    ).add_to(m)

st_folium = st.components.v1.html(m._repr_html_(), height=550)

st.header("Sensor Data Overview")
st.dataframe(df)

if st.checkbox("Show Heat Map"):
    heat_data = [[row['latitude'], row['longitude'], row['heat_signature']] for index, row in df.iterrows()]
    HeatMap(heat_data).add_to(m)
    st_folium = st.components.v1.html(m._repr_html_(), height=500)

st.header("Filter Data by Use Case")
use_case = st.selectbox("Select Use Case", ["Agriculture", "Construction", "Search & Rescue"])

if use_case == "Agriculture":
    filtered_df = df[df['material_detected'] == 'Vegetation']
elif use_case == "Construction":
    filtered_df = df[df['material_detected'].isin(['Concrete', 'Asphalt'])]
else:
    filtered_df = df[df['heat_signature'] > 70]

st.dataframe(filtered_df)
