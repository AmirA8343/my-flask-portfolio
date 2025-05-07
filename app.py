from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

# ⚠️ Replace this with your real API key from https://www.api-football.com/
API_KEY = "3ff6f8d0f787b634c70f33aadb6ba6a4"
API_URL = "https://v3.football.api-sports.io/fixtures?live=all"
# API_URL = "https://v3.football.api-sports.io/fixtures?date=2025-04-08"

headers = {
    "x-apisports-key": API_KEY
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/scores')
def scores():
    try:
        response = requests.get(API_URL, headers=headers)
        data = response.json()
        matches = data.get('response', [])[:5]
        return jsonify(matches)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)



# @app.route('/scores')
# def scores():
#     try:
#         response = requests.get(API_URL, headers=headers)
#         data = response.json()
#         matches = []
#
#         for fixture in data.get('response', [])[:5]:  # First 5 matches
#             status = fixture['fixture']['status']['short']
#             if status in ['NS', '1H', 'HT', '2H', 'LIVE', 'FT']:  # Show any status
#                 home_team = fixture['teams']['home']['name']
#                 away_team = fixture['teams']['away']['name']
#                 home_score = fixture['goals']['home']
#                 away_score = fixture['goals']['away']
#                 league = fixture['league']['name']
#                 date = fixture['fixture']['date']
#
#                 matches.append({
#                     'home_team': home_team,
#                     'away_team': away_team,
#                     'home_score': home_score,
#                     'away_score': away_score,
#                     'league': league,
#                     'date': date
#                 })
#
#         return jsonify(matches)
#     except Exception as e:
#         return jsonify({"error": str(e)})


