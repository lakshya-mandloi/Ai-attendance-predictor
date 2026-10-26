from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

# Load dataset
data = pd.read_csv("attendance_data.csv")

# Features
features = [
    "classes_attended",
    "total_classes",
    "assignment_score",
    "internal_marks"
]

X = data[features]
y = data["low_attendance"]

# Train model
model = DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)

model.fit(X, y)


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction
@app.route("/predict", methods=["POST"])
def predict():

    student_data = request.json

    classes_attended = int(
        student_data["classes_attended"]
    )

    total_classes = int(
        student_data["total_classes"]
    )

    assignment_score = float(
        student_data["assignment_score"]
    )

    internal_marks = float(
        student_data["internal_marks"]
    )

    # Calculate attendance
    attendance = (
        classes_attended / total_classes
    ) * 100

    attendance = round(attendance, 2)

    # AI input
    input_data = pd.DataFrame(
        [[
            classes_attended,
            total_classes,
            assignment_score,
            internal_marks
        ]],
        columns=features
    )

    # AI prediction
    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0]

    confidence = round(
        max(probability) * 100,
        2
    )

    # Risk level
    if attendance < 60:

        risk_level = "HIGH RISK"

    elif attendance < 75:

        risk_level = "MEDIUM RISK"

    else:

        risk_level = "LOW RISK"

    # Classes required for 75%
    target_attendance = 75

    if attendance >= target_attendance:

        required_classes = 0

    else:

        required_classes = 0

        while (
            (classes_attended + required_classes)
            / (total_classes + required_classes)
        ) * 100 < target_attendance:

            required_classes += 1

    # Recommendation
    if attendance >= 75:

        recommendation = (
            "Your attendance has already reached the "
            "required 75% criteria. Maintain regular attendance."
        )

    else:

        recommendation = (
            f"Attend the next {required_classes} classes continuously "
            "to reach the required 75% attendance."
        )

    # Final result
    if prediction == 1:

        result = "Low Attendance Risk Detected"

    else:

        result = "Attendance is on Track"

    return jsonify({

        "result": result,

        "attendance": attendance,

        "criteria": target_attendance,

        "classes_attended": classes_attended,

        "total_classes": total_classes,

        "risk_level": risk_level,

        "required_classes": required_classes,

        "confidence": confidence,

        "recommendation": recommendation

    })


# Run server
if __name__ == "__main__":

    app.run(debug=True)