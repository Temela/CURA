# CURA: A Compassion-Driven Health Monitoring System for Elderly Clergy

<p align="center">
  <img src="banner.png" alt="CURA Banner" />
</p>


## ✨ About CURA

**CURA** is a Human-Centered Computing (HCC) initiative that integrates technology, ethics, and pastoral sensitivity to monitor and support the health of elderly clergy. Designed by a Catholic priest and data scientist, it captures not just physical metrics but also emotional and spiritual well-being—offering compassionate care through code.

---

## 🎯 Project Goals

- Provide a health dashboard for elderly religious members  
- Predict early signs of health deterioration (e.g., cardiovascular issues)  
- Respect spiritual life and emotional states through daily reflections  
- Design for accessibility: large font, low-tech interfaces, and voice options  
- Center care, privacy, and dignity in all AI decisions

---

## 🧰 Tools Used

| Area | Tools |
|------|-------|
| **Data Analysis** | Python, Pandas, Matplotlib, Seaborn |
| **Modeling** | Scikit-learn, GridSearchCV |
| **Interface** | Streamlit, HTML/CSS (for later deployment) |
| **Data** | Synthetic dataset for 45 elderly clergy over 60 days |
| **Ethics** | Catholic Social Teaching + HCC Design Principles |

---

## 📊 Key Features

- 🧓 Daily logs of mood, heart rate, activity, and spiritual reflections  
- 📈 Predictive model for cardiovascular risk  
- 📉 Visual analysis of health trends  
- 🗣 Voice-based journaling prototype  
- 📜 Ethical whitepaper accompanying the system

---

## 🧪 Data (Simulated)

The dataset includes daily logs from **45 elderly clergy members** with:
- Age, Sex, Residence
- Blood Pressure (SBP/DBP)
- Glucose, Pulse, SPO2
- Energy levels, Mood scores

📁 `data/cura_45_elderly_health_data.csv`

---

## 🧠 Features

- ✅ Simple **Streamlit dashboard**
- 📊 Visual summaries for each health metric
- 🧘🏽 Mood and energy tracking
- 🔐 No personal identifiers (privacy-aware)
- 📖 Built-in ethical rationale (see whitepaper)

---

## 📂 Project Structure

```bash
CURA/
│
├── data/
│   └── cura_45_elderly_health_data.csv
│
├── app/
│   └── CURA_app.py  ← Launch dashboard with `streamlit run CURA_app.py`
│
├── notebooks/
│   └── CURA_Health_Data_Analysis.ipynb
│
├── figures/
│   └── [summary charts + visual insights]
│
└── docs/
    └── CURA_HCC_Ethics_Whitepaper.md
```

---

## 🧑🏽‍⚖️ Ethical Considerations

- Designed to **respect aging populations**
- Avoids profiling or prediction of end-of-life risk
- Prioritizes **transparency**, **data dignity**, and **contextual care**
- Grounded in Catholic social teaching and HCC research

See full write-up: [`docs/CURA_HCC_Ethics_Whitepaper.md`](./docs/CURA_HCC_Ethics_Whitepaper.md)

---

## 🚀 Run the App Locally

Install Streamlit and run:

```bash
pip install -r requirements.txt
streamlit run app/CURA_app.py
```

---

## 📚 Citation

If you're citing this project, please use:

> TChiemela, ND. (2025). *CURA: Compassionate Health Monitoring Platform for Elderly Clergy*. GitHub. https://github.com/Temela/CURA

---

## 📥 Quick Access

- 📓 [Jupyter Notebook](./CURA_Health_Data_Analysis.ipynb)  
- 📄 [Ethical Design Whitepaper](./CURA_HCC_Ethics_Whitepaper.md)  
- 🖥️ [Streamlit App Code](./CURA_app.py)  
- 📈 [Sample Dataset](./data/cura_45_elderly_health_data.csv)

---

## ✝️ About the Author

**Fr. ND**  
Catholic Priest • Data Scientist • Advocate for Human-Centered Technology  
Focused on AI for social good, healthcare ethics, and inclusive civic tech.  
[LinkedIn](https://www.linkedin.com/in/tchiemela) • [GitHub](https://github.com/Temela) • tchiemela@gmail.com

---

## 💡 Future Work

- Pilot deployment in religious healthcare settings  
- Expansion to multi-lingual, cross-cultural elderly monitoring  
- Academic publication on CURA in HCI/AI ethics journals

---

> “Use tech to reach the forgotten. Use code to amplify care. Use joy, always.” – Fr. ND
