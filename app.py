from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import datetime

app = Flask(__name__)
# CORS allows your HTML file to securely send data to this Python server
CORS(app) 

# --- NEW: This route loads the webpage when you visit the main link ---
@app.route('/')
def home():
    # Flask will look inside the 'templates' folder for this file
    return render_template('index.html')

# --- Your existing save route ---
@app.route('/save_response', methods=['POST'])
def save_response():
    data = request.json
    name = data.get('name', 'Unknown')
    answer = data.get('answer', 'Unknown')
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Player: {name} | Answer: {answer}\n"
    
    with open("proposal_results.txt", "a") as file:
        file.write(log_entry)

    try:
        print(f"🎉 SECURE ALERT: {name} just clicked {answer}!")
    except UnicodeEncodeError:
        print(f"SECURE ALERT: {name} just clicked {answer.encode('ascii', 'ignore').decode('ascii')}!")
    
    return jsonify({"status": "success", "message": "Answer locked in."})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
