# 🚰 Vellam-Safe: AI-Powered Water Grid Monitoring

[**🔗 View Live Demo on Streamlit**](PASTE_YOUR_STREAMLIT_URL_HERE) | [**📊 View Historical Analytics (Looker Studio)**](PASTE_YOUR_LOOKER_LINK_HERE)

**Vellam-Safe** is an intelligent monitoring solution designed for Kerala Panchayats. It bridges the gap between raw IoT sensor telemetry and actionable human intelligence using the Google Cloud and AI ecosystem.

---

## 📌 Project Overview
- **The Problem**: Local water authorities in Kerala struggle with undetected pipe bursts and unequal water distribution due to manual monitoring methods.
- **The Solution**: A real-time AIoT dashboard that visualizes water pressure across wards and provides instant safety protocols using Generative AI.
- **Target Audience**: Panchayat engineers and utility administrators in regions like Haripad, Nangiarkulangara, and Munnar.

---

## 🚀 Key Features
- **Real-Time Data Sync**: Powered by **Google Firebase Realtime Database** for sub-second synchronization between sensors and the dashboard.
- **AI-Driven Safety Analysis**: Employs **Google Gemini 2.5 Flash-Lite** to interpret pressure levels and provide natural language safety advice.
- **Historical BI Dashboard**: Integrated **Looker Studio** reports for long-term trend analysis and infrastructure health tracking.
- **Interactive Heat Map**: A dynamic **Folium** map centered on specific Kerala wards for rapid spatial awareness.

---

## 🛠️ Google Technologies Used
- **Google Gemini AI**: Specifically **Gemini 2.5 Flash-Lite** for fast, efficient predictive analysis.
- **Google AI Studio**: Used for rapid prototyping and fine-tuning the AI's system instructions.
- **Google Firebase**: Uses **Realtime Database** to act as the live hub for all IoT sensor telemetry.
- **Looker Studio**: Transforms historical data into interactive visualizations for Panchayat secretaries.
- **Google Cloud Console**: Centralized management for API security and infrastructure.

---

## 📂 System Architecture
1. **Simulated IoT Sensors**: Generates real-time pressure data.
2. **Firebase RTDB**: Acts as the central "truth" for all telemetry.
3. **Streamlit App**: The live interface that triggers Gemini AI for safety insights.
4. **Looker Studio**: Connects to the data for long-term health reporting.

---

## 🗺️ Future Roadmap
- **Physical Hardware**: Transitioning to **ESP32 and Arduino-based sensors** for real-world deployment.
- **Predictive Maintenance**: Training custom ML models to predict pipe fatigue before bursts occur.
- **Automated Alerts**: Integrating **Google Cloud Pub/Sub** for instant SMS/WhatsApp emergency notifications.
- **Water Quality Tracking**: Adding pH and turbidity sensors to monitor drinking water safety.

---

## ⚙️ Setup & Installation
1. **Clone the Repo**:
   ```bash
   git clone [https://github.com/nahasmace-2004/Vellam-Safe-AI.git](https://github.com/nahasmace-2004/Vellam-Safe-AI.git)
