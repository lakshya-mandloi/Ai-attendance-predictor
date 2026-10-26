import pandas as pd
import random

random.seed(42)

records = []

for i in range(200):

    total_classes = random.randint(35, 60)

    classes_attended = random.randint(
        int(total_classes * 0.40),
        total_classes
    )

    assignment_score = random.randint(40, 100)

    internal_marks = random.randint(40, 95)

    # Calculate actual attendance
    attendance_percentage = (
        classes_attended / total_classes
    ) * 100

    # Determine attendance risk
    risk_score = 0

    if attendance_percentage < 60:
        risk_score += 3

    elif attendance_percentage < 75:
        risk_score += 2

    if assignment_score < 50:
        risk_score += 1

    if internal_marks < 50:
        risk_score += 1

    # Final target
    low_attendance = 1 if risk_score >= 3 else 0

    records.append([
        classes_attended,
        total_classes,
        assignment_score,
        internal_marks,
        low_attendance
    ])


columns = [
    "classes_attended",
    "total_classes",
    "assignment_score",
    "internal_marks",
    "low_attendance"
]


df = pd.DataFrame(
    records,
    columns=columns
)


df.to_csv(
    "attendance_data.csv",
    index=False
)


print("Dataset generated successfully!")
print("Total records:", len(df))

print("\nDataset columns:")
print(df.columns.tolist())

print("\nFirst 10 records:")
print(df.head(10))