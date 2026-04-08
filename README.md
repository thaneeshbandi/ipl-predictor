# 🏏 IPL Win Predictor

A Machine Learning-powered web application that predicts the **real-time win probability** of IPL matches based on live match conditions.

🔗 **Live App:** https://ipl--predictor.streamlit.app

---

## 🚀 Features

* Predicts win probability during a live IPL match
* Takes real-time inputs like:

  * Batting & Bowling teams
  * Host city
  * Target score
  * Current score, overs, and wickets
* Displays **winning probability (%)** for both teams
* Interactive UI built with Streamlit

---

## 🧠 Machine Learning Approach

* Trained on **ball-by-ball IPL dataset**
* Feature engineering includes:

  * Runs left
  * Balls left
  * Wickets remaining
  * Current Run Rate (CRR)
  * Required Run Rate (RRR)
* Model used:

  * Logistic Regression
* Pipeline includes:

  * OneHotEncoding for categorical features
  * End-to-end preprocessing + prediction

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit

---

## 📂 Project Structure

```
ipl-predictor/
│
├── app.py               # Streamlit application
├── train_model.py      # Model training script
├── pipe.pkl            # Trained ML model
├── matches.csv         # IPL match data
├── deliveries.csv      # Ball-by-ball data
├── requirements.txt    # Dependencies
├── Procfile            # Deployment config
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/thaneeshbandi/ipl-predictor.git
cd ipl-predictor
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## 📊 How It Works

1. User inputs match details
2. Features are computed dynamically:

   * Runs left
   * Balls left
   * Run rates
3. Data is passed to trained ML pipeline
4. Model predicts win probability

---

## 📌 Future Improvements

* Add advanced models (XGBoost, Random Forest)
* Improve UI with graphs and visualizations
* Deploy with CI/CD pipeline
* Add match history tracking

---

## 👨‍💻 Author

**Thaneesh Bandi**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
