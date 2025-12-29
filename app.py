import streamlit as st
import folium
from streamlit_folium import st_folium
from google import genai
import requests
import random
import time

# --- INITIAL SETUP ---
st.set_page_config(page_title="Vazhi-Safe AI Dashboard", page_icon="🚰", layout="wide")

# Replace these with your actual details
FIREBASE_URL = "https://vazhisafe02-default-rtdb.asia-southeast1.firebasedatabase.app/.json"
GEMINI_KEY = "AIzaSyATIYrO-mqYqiI0ybtJ1RqaU2u-XSsWAVg"
client = genai.Client(api_key=GEMINI_KEY)

# --- LOCATIONS FOR KERALA MAP ---
WARD_COORDINATES = {
    "Ward_1_Haripad": [9.2875, 76.4442],
    "Ward_2_Nangiarkulangara": [9.2985, 76.4350],
    "Ward_3_Munnar": [10.0889, 77.0595]
}

st.title("🚰 Vazhi-Safe: Kerala Water Grid Intelligence")

# --- SIDEBAR: SIMULATION CONTROLS ---
with st.sidebar:
    st.header("Simulator Controls")
    if st.button("🚀 Run One Simulation Step"):
        for ward in WARD_COORDINATES.keys():
            pressure = random.randint(10, 95)
            requests.patch(FIREBASE_URL, json={ward: {"pressure": pressure, "time": time.time()}})
        st.success("New sensor data pushed to Firebase!")

# --- MAIN DASHBOARD ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📍 Live Kerala Heat Map")
    data = requests.get(FIREBASE_URL).json() or {}
    
    # Create the Map centered on Kerala
    m = folium.Map(location=[9.5, 76.8], zoom_start=8, tiles="CartoDB positron")
    
    for ward, coords in WARD_COORDINATES.items():
        # Get live pressure from Firebase
        pressure = data.get(ward, {}).get('pressure', 0)
        
        # Color Logic: Red for Danger, Green for Safe
        color = 'red' if pressure < 20 or pressure > 80 else 'green'
        
        folium.CircleMarker(
            location=coords, radius=12, color=color, fill=True,
            popup=f"<b>{ward}</b><br>Pressure: {pressure} PSI"
        ).add_to(m)
    
    st_folium(m, width=700, height=450)

with col2:
    st.subheader("🧠 Gemini AI Safety Advisory")
    if data:
        prompt = f"Analyze these Kerala water pressures: {data}. Identify red zones and provide a 1-sentence technician fix."
        try:
            with st.spinner("AI is analyzing..."):
                response = client.models.generate_content(model='gemini-2.5-flash-lite', contents=prompt)
                st.info(response.text)
        except Exception as e:
            st.warning("AI Limit reached. Please wait 60s.")
    else:
        st.write("Click 'Run' in the sidebar to start.")

st.divider()
st.subheader("📊 Raw Sensor Stream")
st.json(data)