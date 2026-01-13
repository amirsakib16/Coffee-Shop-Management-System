# ☕ Brew & Bite | Restaurant Management System

A robust, lightweight POS (Point of Sale) and Menu Management system. This application allows for digital menu browsing, real-time order processing, and automated billing calculation using a Flask backend.

---

# Brew & Bite | Digital Restaurant System
<p align="center">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask Badge" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge" />
  <br />
  <img src="https://img.shields.io/badge/status-active-brightgreen?style=flat-square" alt="Status" />
</p>

---

## Features

* **Dynamic Menu:** Categorized items (Hot/Cold Coffee, Snacks, Desserts) with live descriptions and pricing.
* **Smart Billing:** Integrated cart logic that calculates sub-totals and grand totals dynamically.
* **Order History:** Tracks customer names, itemized receipts, and precise transaction timestamps.
* **Automated POS:** Unique order ID generation and real-time backend processing.
* **Clean UI:** A high-performance, responsive interface styled with **Tailwind CSS**.

---

## Technical Stack

* **Backend:** Python 3.10.7, Flask
* **Frontend:** HTML5, Tailwind CSS, JavaScript (Fetch API)
* **Data Structure:** Object-Oriented Programming (OOP) with custom `RestaurantSystem` class logic for state management.

---

## Installation & Setup

1. **Clone the Repository:**
    ```bash
    git clone [https://github.com/amirsakib16/Restaurant-Management-System.git](https://github.com/amirsakib16/Restaurant-Management-System.git)
    ```

2. **Install Dependencies:**
    Ensure you have Python installed, then install the necessary micro-framework:
    ```bash
    pip install flask
    ```

3. **Project Structure:**
    Ensure your folders are organized as follows:
    ```text
    /restaurant-system
    ├── app.py              # Backend logic, API, and Data
    └── templates/
        └── index.html      # Frontend POS Interface
    ```

4. **Run the Application:**
    ```bash
    python app.py
    ```

5. **Access the Web Interface:**
    Open your browser and navigate to:
    `http://127.0.0.1:5000`

---
**Virtual Environment Activation**
```text
python -m venv env
# Windows
env\Scripts\activate
# Mac/Linux
source env/bin/activate
