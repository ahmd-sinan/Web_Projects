# Movie Ticket Booking

A simple web application built with Python and Flask that allows users to simulate booking movie tickets. This project was built to practice backend routing, form submission handling (POST requests), and HTML template rendering.

## Features
* **User Input:** Simple text field for the user's name.
* **Dynamic Selection:** Dropdown menu featuring popular blockbuster movies.
* **Backend Validation:** Basic checks to ensure both a name and a movie are selected before processing the booking.
* **Conditional Routing:** Custom success and error pages rendered based on the form submission data.

## 🛠️ Tech Stack
* **Backend:** Python, Flask
* **Frontend:** HTML5
* **Server:** Werkzeug (Development Server)

## 📁 Project Structure
```text
Movie-Ticket-Booking/
├── app.py                
├── requirements.txt      
└── templates/            
    ├── layout.html     
    ├── index.html       
    ├── success.html     
    └── failure.html      
```

## How to Run Locally
**Navigate to the project directory:**

```Bash
cd Movie-Ticket-Booking
```

**Install the required dependencies:**

```Bash
pip install -r requirements.txt
```

**Start the Flask development server:**

```Bash
python -m flask run
```

**Open your browser:**
Navigate to the local address provided in your terminal (usually `http://127.0.0.1:5000`).

