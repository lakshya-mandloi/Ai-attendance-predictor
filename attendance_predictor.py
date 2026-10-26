import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# ---------------------------------------
# 1. LOAD ATTENDANCE DATA
# ---------------------------------------

data = pd.read_csv("attendance_data.csv")

print("\n===== AI ATTENDANCE PREDICTOR =====")
print("\nTraining data loaded successfully!")
print(data)

# ---------------------------------------
# 2. SELECT INPUT AND OUTPUT
# ---------------------------------------

features = [
    "attendance_percentage",
    "classes_attended",
    "total_classes",
    "previous_attendance",
    "assignment_score",
    "internal_marks",
    "study_hours"
]

X = data[features]
y = data["low_attendance"]

# ---------------------------------------
# 3. SPLIT DATA
# ---------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ---------------------------------------
# 4. CREATE AI MODEL
# ---------------------------------------

model = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)

model.fit(X_train, y_train)

# ---------------------------------------
# 5. TEST MODEL
# ---------------------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

# ---------------------------------------
# 6. TAKE STUDENT INPUT
# ---------------------------------------

print("\n===== STUDENT ATTENDANCE PREDICTION =====")

attendance = float(input("Enter attendance percentage: "))
classes_attended = int(input("Enter classes attended: "))
total_classes = int(input("Enter total classes: "))
previous_attendance = float(input("Enter previous attendance percentage: "))
assignment_score = float(input("Enter assignment score: "))
internal_marks = float(input("Enter internal marks: "))
study_hours = float(input("Enter average daily study hours: "))

# ---------------------------------------
# 7. PREDICT
# ---------------------------------------

student_data = pd.DataFrame([[
    attendance,
    classes_attended,
    total_classes,
    previous_attendance,
    assignment_score,
    internal_marks,
    study_hours
]], columns=features)

prediction = model.predict(student_data)[0]

probability = model.predict_proba(student_data)[0]

# ---------------------------------------
# 8. DISPLAY RESULT
# ---------------------------------------

print("\n===== PREDICTION RESULT =====")

if prediction == 1:
    print("⚠️ WARNING: Low attendance risk detected!")
else:
    print("✅ Attendance status is satisfactory.")

print("Attendance:", attendance, "%")

print(
    "Prediction Confidence:",
    round(max(probability) * 100, 2),
    "%"
)

print("\n===== END =====")