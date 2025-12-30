import streamlit as st
import folium
from streamlit_folium import st_folium
from google import genai
import requests
import random
import time

# --- INITIAL SETUP ---
st.set_page_config(page_title="Vellam-Safe AI Dashboard", page_icon="🚰", layout="wide")

# Securely fetch credentials from Streamlit Secrets
FIREBASE_URL = "https://vazhisafe02-default-rtdb.asia-southeast1.firebasedatabase.app/.json"

try:
    # Use the Secret key you pasted in the Streamlit Cloud dashboard
    GEMINI_KEY = st.secrets["GEMINI_KEY"]
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
@st.cache_data(ttl=120) # Prevents redundant calls and saves quota
def get_ai_advice(sensor_data):
    # Prompt optimized in Google AI Studio
    prompt = f"Analyze these Kerala water pressures: {sensor_data}. Identify danger zones and provide a 1-sentence fix."
    try:
        # Using Flash-Lite for high-speed analysis and better free-tier limits
        response = client.models.generate_content(
            model='gemini-2.5-flash-lite', 
            contents=prompt
        )
        return response.text
    except Exception as e:
        return "⚠️ AI is resting. The daily quota is exhausted. Please try again tomorrow."

st.title("🚰 Vellam-Safe: AI Water Grid Command Center")

# --- SIDEBAR: SIMULATION & ANALYTICS ---
with st.sidebar:
    st.header("Vellam-Safe Controls")
    st.write("Click below to send random pressure data to Firebase.")
    if st.button("🚀 Push New Data to Firebase"):
        for ward in WARD_COORDINATES.keys():
            pressure = random.randint(10, 95)
            # Syncing live data to Google Firebase
            requests.patch(FIREBASE_URL, json={ward: {"pressure": pressure, "time": time.time()}})
        st.success("Data Sent to Firebase!")
    
    st.divider()
    # Strategic Planning Link to Looker Studio
    st.subheader("📊 Strategic Planning")
    st.link_button("Open Historical Health Report", "https://lookerstudio.google.com/reporting/346599ef-19e7-45e3-9d41-f2c2a9aca8e2")
    st.caption("View long-term pressure trends and ward-wise analytics in Looker Studio.")

# --- MAIN LAYOUT ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📍 Live Kerala Heat Map")
    # Fetching real-time data from the central Firebase hub
    data = requests.get(FIREBASE_URL).json() or {}
    
    # Building the interactive Folium map
    m = folium.Map(location=[9.5, 76.8], zoom_start=8, tiles="CartoDB positron")
    for ward, coords in WARD_COORDINATES.items():
        pressure = data.get(ward, {}).get('pressure', 0)
        # Red marker for dangerous pressure levels, green for safe
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
            with st.spinner("Analyzing with Gemini..."):
                analysis = get_ai_advice(data)
                st.info(analysis)
        else:
            st.write("Click the button to receive safety advice from Vellam-Safe AI.")
    else:
        st.write("No data found. Please push data from the sidebar first.")

st.divider()
st.subheader("📊 Raw Firebase Data (JSON)")
st.json(data)
