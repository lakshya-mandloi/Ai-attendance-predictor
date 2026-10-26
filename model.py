import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("attendance_data.csv")

# Features used by the AI model
features = [
    "classes_attended",
    "total_classes",
    "assignment_score",
    "internal_marks"
]

# Input and output
X = data[features]
y = data["low_attendance"]

# Create AI model
model = DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)

# Train model
model.fit(X, y)

print("AI Attendance Model trained successfully!")
print("Features used:", features)