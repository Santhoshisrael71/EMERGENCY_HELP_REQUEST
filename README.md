#  Emergency Help Request System (Hackathon Project)

A **Flask-based web application** that allows citizens to report emergency situations and enables authorities to review, analyze, and approve requests through an admin dashboard.  
The system supports **multi-language emergency messages**, **NLP-based urgency detection**, and **real-time monitoring**.

---

##  Hackathon Project Overview

This project was developed as part of a **hackathon** to solve real-world emergency communication challenges by:

- Making emergency reporting **simple and fast**
- Supporting **any language input**
- Helping authorities **prioritize urgent cases**
- Providing **structured emergency insights**

---

##  Key Features

###  Citizen (Client) Side
- Submit emergency requests via a web form
- Enter:
  - Name
  - Emergency type
  - Message (any language)
  - Location (latitude & longitude)
- Redirected to a **read-only status page**

###  Authority (Admin) Side
- Central **Government Dashboard**
- View all emergency requests
- Displays:
  - Translated message (English)
  - Urgency level (Low / Medium / High)
  - Issue type (Fire, Medical, Flood, etc.)
  - People affected (if detected)
  - Extracted location text
- Approve emergencies with admin notes

###  Intelligent Processing
-  Automatic language translation
-  Urgency detection
-  Issue classification
-  People count extraction
-  Text-based location detection

---

##  Technologies Used

- **Python**
- **Flask**
- **HTML / CSS**
- **deep-translator**
- **Regex (re)**
- **Gunicorn**
- **Render (Deployment)**

---

##  Project Structure

```
Emergency-Help-Request-hackathon/
│
├── app.py                 # Entry point (runs the server)
├── server.py              # Flask app logic and routes
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
│
├── templates/
│   ├── index.html         # Emergency submission page
│   ├── user_list.html     # Client status page
│   └── dashboard.html     # Government dashboard
│
└── static/
    └── style.css          # Styling

```

## Installation & Setup (Local)
 Clone the Repository
 
```
git clone https://github.com/your-username/Emergency-Help-Request-hackathon.git
cd Emergency-Help-Request-hackathon
```

## Install Dependencies

```
pip install -r requirements.txt
```

## Run the Application
```
python app.py
```

## Open in Browser

````
http://127.0.0.1:5000
````

## Deployment on Render
### Build Command

```
pip install -r requirements.txt
```

## Start Command

```
gunicorn app:app
```

## requirements.txt

```
Flask
deep-translator
gunicorn
```

## Security & Limitations

No authentication (hackathon prototype)

In-memory storage (data resets on restart)

Not intended for production emergency use without enhancements

## Future Enhancements

User & admin authentication

Database integration (PostgreSQL / MongoDB)

SMS / Email alerts

Google Maps integration

Machine Learning-based emergency classification

Role-based access control

## Learning Outcomes

Flask app structuring (app.py vs server.py)

Cloud deployment using Render

REST-style routing

NLP basics using regex

Handling multi-language inputs

GitHub project organization

## Developed By

Santhosh P,Jude Clement Jose G,Rayash 
GRAPS Hackathon Participant
PROBLEM 1:
Emergency Response System Developer

## Acknowledgements

Hackathon organizers

Open-source Flask community

Render deployment platform

