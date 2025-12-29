# 🚰 Vellam-Safe: AI-Powered Water Grid Monitoring

[**🔗 View Live Demo on Streamlit**](https://vellam-safe-ai-5fp6gf8megthp23ima8zet.streamlit.app/)


**Vellam-Safe** is an intelligent monitoring system designed for Kerala Panchayats. It bridges the gap between raw IoT sensor data and actionable human intelligence using the Google Gemini AI ecosystem.

---

## 📌 Project Overview
- **The Problem**: Local water authorities in Kerala often struggle with undetected pipe bursts and unequal water distribution due to manual monitoring methods.
- **The Solution**: A real-time dashboard that visualizes water pressure across different wards and uses AI to provide instant safety protocols and maintenance advice.
- **Target Audience**: Panchayat engineers, water authority technicians, and local administrators in regions like Haripad and Munnar.

---

## 🚀 Key Features
- **AI Safety Analysis**: Leverages **Google Gemini 2.5 Flash-Lite** to interpret pressure spikes or drops and provide 1-sentence actionable advice.
- **Real-Time Data Sync**: Powered by **Google Firebase Realtime Database** for sub-second updates between sensors and the dashboard.
- **Interactive Geospatial Map**: A custom-built **Folium** heat map centered on Kerala wards (Haripad, Nangiarkulangara, and Munnar).
- **Smart Caching**: Implements `st.cache_data` with a **120-second TTL** to optimize API usage and ensure system responsiveness.

---

## 🛠️ Tech Stack
- **Frontend**: Streamlit (Python-based Web Framework).
- **Artificial Intelligence**: Google Gemini AI (Generative Analysis).
- **Database**: Google Firebase (NoSQL Realtime Database).
- **Mapping**: Folium & Streamlit-Folium.
- **Hosting**: Streamlit Community Cloud.

---

## ⚙️ Setup & Installation
1. **Clone the Repo**:
   ```bash
   git clone [https://github.com/your-username/Vazhi-Safe-AI.git](https://github.com/your-username/Vazhi-Safe-AI.git)

pip install -r requirements.txt
streamlit run app.py
## 🗺️ Future Roadmap
* **Hardware Integration**: Connecting real ESP32 sensors to the Firebase DB.
* **SMS Alerts**: Using Twilio to send AI alerts directly to Panchayat members' phones.
* **Predictive Maintenance**: Training a custom model to predict pipe aging.
*

