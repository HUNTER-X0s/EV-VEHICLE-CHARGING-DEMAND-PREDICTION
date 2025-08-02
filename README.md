# EV-VEHICLE-CHARGING-DEMAND-PREDICTION

AICTE INTERNSHIP CYCLE - 2

🔋 EV Vehicle / Charging Demand Prediction
Forecasting electric vehicle adoption across counties using machine learning, with a scalable and interactive dashboard to support infrastructure planning.


📌 Project Overview
This project addresses a critical need in sustainable mobility: forecasting the future demand for electric vehicles (EVs) to assist in charging station planning and infrastructure investment. Using real-world county-wise data from Washington State, the project:

Analyzes historical EV adoption patterns,

Builds predictive models using machine learning,

And deploys an interactive Streamlit dashboard to visualize results.

🎯 Problem Statement
The rapid growth of EVs is outpacing the readiness of infrastructure. Decision-makers often underestimate or overestimate demand, leading to:

Charging station shortages or congestion, or

Wasted investments in under-utilized infrastructure.

This project provides an AI-powered solution to forecast EV growth and guide data-driven decision-making.

🚀 Project Goals
📈 Understand EV adoption trends by county

🤖 Train machine learning models for accurate forecasting

📊 Visualize 3-year forecasts in an interactive dashboard

🧠 Empower stakeholders to optimize infrastructure planning

🔧 Tools & Technologies Used
Category	Tools
Programming	Python 3.10.8
Data Handling	Pandas, NumPy, SciPy
Machine Learning	Scikit-learn, Statsmodels
Visualization	Matplotlib, Streamlit
Deployment	Streamlit
Model Serialization	Joblib
Version Control	GitHub
Requirements	See requirements.txt

🧠 Methodology
Data Collection

County-level EV population dataset from Washington State.

Data Preprocessing

Cleaned dates, handled duplicates, and encoded categorical variables.

Feature Engineering

Added lag features, rolling averages, percentage change, and growth slope metrics.

Model Training

Built a regression forecasting model using Scikit-learn, saved as forecasting_ev_model.pkl.

Forecasting

Generated 36-month predictions for EV adoption per county.

Visualization

Created a Streamlit dashboard for user interaction and visual comparison between counties.

💻 How to Run Locally
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/HUNTER-X0s/EV-VEHICLE-CHARGING-DEMAND-PREDICTION.git
cd EV-VEHICLE-CHARGING-DEMAND-PREDICTION
2. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
3. Launch the Streamlit App
bash
Copy
Edit
streamlit run app.py
🧪 Model File Info
forecasting_ev_model.pkl: Pre-trained model used for forecasting

preprocessed_ev_data.csv: Cleaned dataset with engineered features

Electric_Vehicle_Population_By_County.csv: Original dataset

📊 Dashboard Features
✅ Select any county in Washington State
✅ View historical + forecasted EV adoption
✅ Compare up to 3 counties side-by-side
✅ Analyze growth percentage over 3 years

🎯 Key Outcomes
📌 Forecasts EV growth 36 months ahead

📈 Displays trends in a clean, responsive dashboard

🧠 Helps policy-makers, utility providers, and investors

🌎 Scalable to other regions, data sources, or demographics

📷 Screenshots
(Available inside the Streamlit dashboard)

📚 Acknowledgment
This project was developed under the AICTE Virtual Internship (Cycle 2)
Intern ID: INTERNSHIP_175040797468551b2636342
Student ID: STU6843599c1709e1749244316
Author: ANURAG SWAIN

🔗 GitHub Repository
🔗 Click here to view the project on GitHub
(https://github.com/HUNTER-X0s/EV-VEHICLE-CHARGING-DEMAND-PREDICTION)

⚡ Final Note
"We are not just predicting the future of electric vehicles — we are engineering it."
— 💡 Anurag Swain

