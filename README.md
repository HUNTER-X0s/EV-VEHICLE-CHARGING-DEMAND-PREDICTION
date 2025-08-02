
# 🚗 EV-VEHICLE-CHARGING-DEMAND-PREDICTION
## AICTE INTERNSHIP CYCLE - 2

> 🔋 **EV Vehicle / Charging Demand Prediction**  
> Forecasting electric vehicle adoption across counties using machine learning, with a scalable and interactive dashboard to support infrastructure planning.

---

## 📌 Project Overview

This project addresses a critical need in sustainable mobility: forecasting the **future demand for electric vehicles (EVs)** to assist in **charging station planning** and **infrastructure investment**.

Using real-world county-wise data from **Washington State**, the project:

- Analyzes historical EV adoption patterns
- Builds predictive models using machine learning
- Deploys an **interactive Streamlit dashboard** to visualize results

---

## 🎯 Problem Statement

The rapid growth of EVs is outpacing the readiness of infrastructure. Decision-makers often:

- **Underestimate** demand → leads to charging station shortages and congestion
- **Overestimate** demand → leads to under-utilization and wasted investment

This project offers an **AI-powered solution** to forecast EV growth and enable data-driven decisions.

---

## 🚀 Project Goals

- 📈 Understand EV adoption trends by county  
- 🤖 Train ML models for accurate forecasting  
- 📊 Visualize 3-year forecasts interactively  
- 🧠 Support stakeholders in strategic planning  

---

## 🔧 Tools & Technologies Used

| Category           | Tools                                |
|--------------------|----------------------------------------|
| Programming        | Python 3.10.8                         |
| Data Handling      | Pandas, NumPy, SciPy                  |
| Machine Learning   | Scikit-learn, Statsmodels             |
| Visualization      | Matplotlib, Streamlit                 |
| Deployment         | Streamlit                             |
| Model I/O          | Joblib                                |
| Version Control    | GitHub                                |
| Requirements       | See `requirements.txt`               |

---

## 🧠 Methodology

- **Data Collection**: County-wise EV population dataset from Washington State  
- **Preprocessing**: Date parsing, duplicate removal, county encoding  
- **Feature Engineering**: Lag features, rolling averages, % change, growth slopes  
- **Model Training**: Regression model using Scikit-learn, saved as `forecasting_ev_model.pkl`  
- **Forecasting**: Generate 36-month EV adoption predictions  
- **Visualization**: Streamlit app to visualize forecasts and compare counties  

---

## 💻 How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/HUNTER-X0s/EV-VEHICLE-CHARGING-DEMAND-PREDICTION.git
cd EV-VEHICLE-CHARGING-DEMAND-PREDICTION
```

### 2️⃣ Install Requirements
```bash
pip install -r requirements.txt
```

### 3️⃣ Launch the App
```bash
streamlit run app.py
```

---

## 🧪 Model Files

- `forecasting_ev_model.pkl`: Trained forecasting model  
- `preprocessed_ev_data.csv`: Feature-engineered dataset  
- `Electric_Vehicle_Population_By_County.csv`: Raw data source  

---

## 📊 Dashboard Features

- ✅ Select any county from Washington State  
- ✅ View historical and predicted adoption trends  
- ✅ Compare up to **3 counties** side by side  
- ✅ Visualize 3-year growth in EV adoption  

---

## 🎯 Key Outcomes

- 📌 Forecasts county-level EV adoption for the next 36 months  
- 📈 Displays trends in a clean, responsive dashboard  
- 🧠 Supports decisions by policymakers, investors, and planners  
- 🌍 Scalable to other states, countries, or new data sources  

---

## 📚 Acknowledgment

- **Internship Program**: AICTE Virtual Internship (Cycle 2)  
- **Intern ID**: INTERNSHIP_175040797468551b2636342  
- **Student ID**: STU6843599c1709e1749244316  
- **Author**: *Anurag Swain*

---

## 🔗 GitHub Repository

[🔗 View on GitHub](https://github.com/HUNTER-X0s/EV-VEHICLE-CHARGING-DEMAND-PREDICTION)

---

## ⚡ Final Note

> _"We are not just predicting the future of electric vehicles — we are engineering it."_  
> — 💡 *Anurag Swain*
