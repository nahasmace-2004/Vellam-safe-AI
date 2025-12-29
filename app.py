import streamlit as st
import folium
from streamlit_folium import st_folium
from google import genai
import requests
import random
import time

# --- INITIAL SETUP ---
st.set_page_config(page_title="Vazhi-Safe AI Dashboard", page_icon="🚰", layout="wide")

# Securely fetch credentials from Streamlit Secrets
FIREBASE_URL = "https://vazhisafe02-default-rtdb.asia-southeast1.firebasedatabase.app/.json"
try:
    GEMINI_KEY = st.secrets["AIzaSyATIYrO-mqYqiI0ybtJ1RqaU2u-XSsWAVg"]
    client = genai.Client(api_key=GEMINI_KEY)
except Exception:
    st.error("Missing API Key! Please configure GEMINI_KEY in Streamlit Secrets.")
    st.stop()

# --- LOCATIONS FOR KERALA MAP ---
WARD_COORDINATES = {
    "Ward_1_Haripad": [9.2875, 76.4442],
    "Ward_2_Nangiarkulangara": [9.2985, 76.4350],
    "Ward_3_Munnar": [10.0889, 77.0595]
}

# --- CACHED AI FUNCTION ---
@st.cache_data(ttl=120) # Prevents redundant calls for 2 minutes
def get_ai_advice(sensor_data):
    prompt = f"Analyze these Kerala water pressures: {sensor_data}. Identify danger zones and provide a 1-sentence fix."
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash-lite', # High-quota model
            contents=prompt
        )
        return response.text
    except Exception as e:
        return "⚠️ AI is resting. Please try again in 60 seconds."

st.title("🚰 Vazhi-Safe: AI Water Grid Command Center")

# --- SIDEBAR: SIMULATION CONTROL ---
with st.sidebar:
    st.header("Simulator Controls")
    if st.button("🚀 Push New Data to Firebase"):
        for ward in WARD_COORDINATES.keys():
            pressure = random.randint(10, 95)
            requests.patch(FIREBASE_URL, json={ward: {"pressure": pressure, "time": time.time()}})
        st.success("Data Sent!")

# --- MAIN LAYOUT ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📍 Live Kerala Heat Map")
    data = requests.get(FIREBASE_URL).json() or {}
    
    m = folium.Map(location=[9.5, 76.8], zoom_start=8, tiles="CartoDB positron")
    for ward, coords in WARD_COORDINATES.items():
        pressure = data.get(ward, {}).get('pressure', 0)
        color = 'red' if pressure < 20 or pressure > 80 else 'green'
        folium.CircleMarker(
            location=coords, radius=12, color=color, fill=True,
            popup=f"<b>{ward}</b>: {pressure} PSI"
        ).add_to(m)
    st_folium(m, width=700, height=450)

with col2:
    st.subheader("🧠 Gemini AI Safety Analysis")
    if data:
        if st.button("🔍 Get New AI Analysis"):
            with st.spinner("Analyzing..."):
                analysis = get_ai_advice(data)
                st.info(analysis)
        else:
            st.write("Click button for AI analysis.")
    else:
        st.write("No data found. Push data from sidebar.")

st.divider()
st.subheader("📊 Raw Firebase Data")
st.json(data)

