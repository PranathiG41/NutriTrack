from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load diet data
with open("diet_data.json", "r") as f:
    diet_data = json.load(f)


def generate_meal_plan(goal, diet_type):
    goal = goal.lower().replace(" ", "_")
    diet_type = diet_type.lower().replace(" ", "_")
    return diet_data.get(goal, {}).get(diet_type, {})


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get-plan", methods=["POST"])
def get_plan():
    user = {
        "name": request.form["name"],
        "age": request.form["age"],
        "gender": request.form["gender"],
        "height": request.form["height"],
        "weight": request.form["weight"],
        "goal": request.form["goal"],
        "diet_type": request.form["diet_type"]
    }

    meal_plan = generate_meal_plan(user["goal"], user["diet_type"])

    return render_template("result.html", user=user, meal_plan=meal_plan)


if __name__ == "__main__":
    app.run(debug=True)
