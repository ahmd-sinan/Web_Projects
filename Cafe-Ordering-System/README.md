# ☕ Cafe Ordering System

A lightweight web application built with Python and Flask that simulates a restaurant order management system. This project demonstrates backend data handling using nested Python dictionaries, form processing via POST requests, and dynamic HTML rendering.

## ✨ Features
* **Order Placement:** Users can input their name and select both a food item and a drink from dynamic dropdown menus.
* **Backend Validation:** The Flask server validates the form data to ensure no empty submissions or invalid menu/drink items are processed.
* **In-Memory Storage:** Uses a nested Python dictionary to temporarily store and manage active customer orders (e.g., storing both food and drink under the customer's name).
* **Kitchen Dashboard:** A dedicated route (`/orders`) that renders a clean HTML table displaying all current food and beverage orders for the staff.

## 🛠️ Tech Stack
* **Backend:** Python, Flask
* **Frontend:** HTML5, CSS (Inline Styling)
* **Data Structure:** Nested Python Dictionaries 

## 📁 Project Structure
```text
Cafe-Ordering-System/
├── app.py               
├── requirements.txt    
└── templates/           
    ├── layout.html       
    ├── index.html       
    ├── orders.html     
    └── error.html
```

## How to Run Locally
**Navigate to the project directory:**

```Bash
cd Cafe-Ordering-System
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
Navigate to the local address provided in your terminal (usually http://127.0.0.1:5000)