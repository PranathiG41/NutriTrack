# NutriTrack – Personalized Diet Planner Web Application

## 📌 Project Overview

**NutriTrack** is a full-stack web application that generates a personalized diet plan based on a user’s health goals and dietary preferences. The application collects basic user information such as age, gender, height, weight, fitness goal, and diet type, and then recommends a suitable meal plan.

The system uses a rule-based approach where predefined diet plans are stored in a JSON file and selected according to the user’s input. The project demonstrates integration between frontend and backend technologies using the Flask framework.

---

## 🚀 Features

* Personalized diet recommendations
* Supports multiple health goals:

  * Weight Loss
  * Muscle Gain
  * Healthy Skin
  * Hair Growth
  * Acne Reduction
* Supports vegetarian and non-vegetarian diet plans
* Displays meals for:

  * Breakfast
  * Lunch
  * Dinner
  * Foods to Avoid
* Simple and user-friendly web interface

---

## 🛠 Technologies Used

### Frontend

* HTML
* CSS

### Backend

* Python
* Flask Framework

### Data Storage

* JSON file used to store diet plans

---

## 📂 Project Structure

```
NutriTrack/
│
├── app.py                # Main Flask application
├── diet_data.json        # Dataset containing diet plans
│
├── templates/            # HTML templates
│   ├── index.html
│   └── result.html
│
├── static/               # Static files
│   └── style.css
│
└── README.md
```

---

## ⚙️ How the Application Works

1. The user enters personal details and diet preferences on the homepage.
2. The form data is sent to the Flask backend using a POST request.
3. The backend processes the user’s goal and diet type.
4. The system retrieves the matching meal plan from the JSON dataset.
5. The personalized diet plan is displayed on the results page.

---

## ▶️ How to Run the Project

### 1. Install Python and Flask

```
pip install flask
```

### 2. Navigate to the project folder

```
cd NutriTrack
```

### 3. Run the application

```
python app.py
```

### 4. Open the browser and visit

```
http://127.0.0.1:5000/
```

---

## 🧩 Modules / Components

* **Frontend Module:** HTML and CSS pages for user interaction
* **Backend Module:** Flask application handling routing and logic
* **Data Module:** JSON file storing predefined diet plans
* **Logic Module:** Rule-based function to generate personalized meal plans

---

## 🔮 Future Enhancements

* BMI calculation for more accurate diet recommendations
* Calorie tracking feature
* Integration with a database (MySQL / MongoDB)
* Machine learning-based diet recommendation system
* User account system to save diet history

---

## 🎯 Learning Outcomes

* Understanding of full-stack web application development
* Experience with Flask routing and form handling
* Integration of frontend and backend components
* Handling structured data using JSON

---

## 📄 License

This project is developed for educational and demonstration purposes.
