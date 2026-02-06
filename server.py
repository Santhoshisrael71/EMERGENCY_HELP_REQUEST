from flask import Flask, request, render_template, redirect, url_for
from datetime import datetime

# ================== ADDED IMPORTS ==================
import os
import re
from deep_translator import GoogleTranslator
# ===================================================

app = Flask(__name__)

# Shared dataset (client + admin)
emergency_data = []

# ================== ADDED FUNCTIONS ==================

def translate_to_english(text):
    """
    Translates any language text to English.
    Safe for Python 3.13.
    """
    try:
        return GoogleTranslator(source="auto", target="en").translate(text)
    except Exception:
        return text


def structure_emergency_request(text):
    """
    NLP processing for emergency text.
    Extracts urgency, issue type, people count, and location text.
    """
    original_text = text
    translated_text = translate_to_english(text)
    text_lower = translated_text.lower()

    structured = {
        "urgency": "low",
        "issue_type": "unknown",
        "people_affected": None,
        "text_location": None,
        "translated_message": translated_text,
        "raw_message": original_text
    }

    # Urgency detection
    if any(word in text_lower for word in ["urgent", "immediately", "asap", "now", "help", "emergency"]):
        structured["urgency"] = "high"
    elif any(word in text_lower for word in ["soon", "please"]):
        structured["urgency"] = "medium"

    # Issue detection
    issue_map = {
        "fire": ["fire", "smoke", "burning"],
        "medical": ["injured", "hurt", "bleeding", "unconscious"],
        "flood": ["flood", "overflow", "water entered"],
        "earthquake": ["earthquake", "tremor"],
        "power_outage": ["power", "electricity", "outage"]
    }

    for issue, keywords in issue_map.items():
        if any(word in text_lower for word in keywords):
            structured["issue_type"] = issue
            break

    # People affected
    people_match = re.search(r"(\d+)\s+(people|persons|members)", text_lower)
    if people_match:
        structured["people_affected"] = int(people_match.group(1))

    # Location detection (text-based)
    location_patterns = [
        r"at ([a-z0-9\s]+)",
        r"near ([a-z0-9\s]+)",
        r"in ([a-z0-9\s]+)"
    ]

    for pattern in location_patterns:
        match = re.search(pattern, text_lower)
        if match:
            structured["text_location"] = match.group(1).strip()
            break

    return structured

# =====================================================


@app.route('/')
def home():
    return render_template("index.html")


# -------- CLIENT SUBMITS EMERGENCY --------
@app.route('/report', methods=['POST'])
def report():

    # ================== ADDED PROCESSING ==================
    structured = structure_emergency_request(request.form['message'])
    # =====================================================

    alert = {
        "id": len(emergency_data),
        "name": request.form['name'],
        "type": request.form['type'],

        # ORIGINAL MESSAGE (UNCHANGED)
        "message": request.form['message'],

        # ================== ADDED DATA ==================
        "translated_message": structured["translated_message"],
        "urgency": structured["urgency"],
        "issue_type": structured["issue_type"],
        "people_affected": structured["people_affected"],
        "text_location": structured["text_location"],
        # ================================================

        "latitude": request.form['latitude'],
        "longitude": request.form['longitude'],
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        # EXTRA ATTRIBUTES (ADDED ONLY)
        "status": "Pending",
        "admin_note": "",
        "approved_at": ""
    }

    emergency_data.append(alert)
    return redirect(url_for('user_list'))


# -------- CLIENT VIEW (READ ONLY) --------
@app.route('/user-list')
def user_list():
    return render_template("user_list.html", alerts=emergency_data)


# -------- GOVERNMENT DASHBOARD --------
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", alerts=emergency_data)


# -------- GOVERNMENT APPROVAL --------
@app.route('/approve/<int:alert_id>', methods=['POST'])
def approve(alert_id):
    if alert_id < len(emergency_data):
        emergency_data[alert_id]['status'] = "Approved"
        emergency_data[alert_id]['admin_note'] = request.form['admin_note']
        emergency_data[alert_id]['approved_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return redirect(url_for('dashboard'))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
