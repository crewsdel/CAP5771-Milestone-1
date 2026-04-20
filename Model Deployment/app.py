from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd
from tensorflow import keras
import json
import requests

app = Flask(__name__)

models = {
    'linear_regression': joblib.load('models/linear_regression.pkl'),
    'random_forest': joblib.load('models/random_forest.pkl'),
}

feature_columns = [
    "aqi_mean", "aqi_p90", "aqi_max", "days_reported",
    "year", "month", "week_of_year", "quarter",
    "aqi_mean_lag1", "aqi_mean_lag2",
    "aqi_max_lag1", "aqi_max_lag2",
    "aqi_p90_lag1", "aqi_p90_lag2",
    "aqi_mean_rolling_3"
]

@app.route('/')
def home():
    return render_template('app.html')

def to_float(val):
    try:
        return float(val)
    except (ValueError, TypeError):
        return float('nan')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    f = data['features']

    raw = pd.DataFrame([{
        'aqi_w1_1': to_float(f['aqi_w1_1']),
        'aqi_w1_2': to_float(f['aqi_w1_2']),
        'aqi_w1_3': to_float(f['aqi_w1_3']),
        'aqi_w1_4': to_float(f['aqi_w1_4']),
        'aqi_w1_5': to_float(f['aqi_w1_5']),
        'aqi_w1_6': to_float(f['aqi_w1_6']),
        'aqi_w1_7': to_float(f['aqi_w1_7']),
        'aqi_w2_1': to_float(f['aqi_w2_1']),
        'aqi_w2_2': to_float(f['aqi_w2_2']),
        'aqi_w2_3': to_float(f['aqi_w2_3']),
        'aqi_w2_4': to_float(f['aqi_w2_4']),
        'aqi_w2_5': to_float(f['aqi_w2_5']),
        'aqi_w2_6': to_float(f['aqi_w2_6']),
        'aqi_w2_7': to_float(f['aqi_w2_7']),
        'aqi_w3_1': to_float(f['aqi_w3_1']),
        'aqi_w3_2': to_float(f['aqi_w3_2']),
        'aqi_w3_3': to_float(f['aqi_w3_3']),
        'aqi_w3_4': to_float(f['aqi_w3_4']),
        'aqi_w3_5': to_float(f['aqi_w3_5']),
        'aqi_w3_6': to_float(f['aqi_w3_6']),
        'aqi_w3_7': to_float(f['aqi_w3_7']),
    }])

    date = pd.to_datetime(f['date'])

    w1 = raw[[f'aqi_w1_{i}' for i in range(1, 8)]].values.flatten()
    w2 = raw[[f'aqi_w2_{i}' for i in range(1, 8)]].values.flatten()
    w3 = raw[[f'aqi_w3_{i}' for i in range(1, 8)]].values.flatten()

    w1 = w1[~np.isnan(w1)]
    w2 = w2[~np.isnan(w2)]
    w3 = w3[~np.isnan(w3)]

    model_input = pd.DataFrame([{
        'year':               date.year,
        'month':              date.month,
        'week_of_year':       date.isocalendar().week,
        'quarter':            date.quarter,
        'days_reported':      len(w1) + len(w2) + len(w3),

        'aqi_mean':           float(w1.mean()),
        'aqi_max':            float(w1.max()),
        'aqi_p90':            float(pd.Series(w1).quantile(0.90)),

        'aqi_mean_lag1':      float(w2.mean()),
        'aqi_max_lag1':       float(w2.max()),
        'aqi_p90_lag1':       float(pd.Series(w2).quantile(0.90)),

        'aqi_mean_lag2':      float(w3.mean()),
        'aqi_max_lag2':       float(w3.max()),
        'aqi_p90_lag2':       float(pd.Series(w3).quantile(0.90)),

        'aqi_mean_rolling_3': float(np.mean([w3.mean(), w2.mean(), w1.mean()])),
    }])

    model_input = model_input.reindex(columns=feature_columns, fill_value=0)

    model = models['random_forest']
    total_cases = model.predict(model_input)[0]

    prompt = f""" You are an advisor helping explain total expected respiratory hospitalizations for a given area.
    Do NOT use alarming or urgent langauge. Do not roleplay as a medical professional.
    
    In 2 to 3 sentences MAX, explain how many total respiratory hospitalizations are expected for the user's area and
    what they can do to prepare their community.

    Total respiratory hospitalizations expected for this area: {total_cases}
    """

    llm_response = call_ollama(prompt)

    return jsonify({
        'total_cases': round(total_cases, 4),
        'llm_response': llm_response
    })

def call_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": 200,
                    "temperature": 0.1
                }
            },
            timeout=120
        )
        if response.status_code == 200:
            return response.json()["response"].strip()
        else:
            return "Unable to generate response at this time."
    except requests.exceptions.ConnectionError:
        return "Service unavailable. Please ensure Ollama is running."
    except requests.exceptions.Timeout:
        return "Request timed out. Please try again."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)