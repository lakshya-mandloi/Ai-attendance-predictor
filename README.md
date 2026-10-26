A machine-learning web app that predicts whether a student is at risk of low attendance and tells them how many more classes they need to reach the 75% requirement.

Built with Python, scikit-learn (Decision Tree), pandas and Flask.

Features
Predicts low-attendance risk (1 = at risk, 0 = on track) with a confidence score
Calculates attendance percentage
Risk level: HIGH (below 60%), MEDIUM (60% to 75%), LOW (75% and above)
Shows how many classes to attend continuously to reach 75%
Simple web interface served by Flask
Project structure
File	Purpose
generate_dataset.py	Creates the 200-record synthetic dataset
attendance_data.csv	Training data
model.py	Trains the Decision Tree and prints the features used
app.py	Flask server with the /predict API
templates/index.html	Web page for entering student details
How it works
generate_dataset.py creates students with random class counts and scores. A risk score decides the label: attendance below 60% adds 3, 60% to 75% adds 2, assignment score below 50 adds 1, internal marks below 50 adds 1. A score of 3 or more means low attendance.
app.py trains a DecisionTreeClassifier (max_depth=5, random_state=42) on the four features when the server starts.
The page sends the student's details to POST /predict, which returns the prediction, confidence, risk level, classes needed and a recommendation as JSON.
Features: classes_attended, total_classes, assignment_score, internal_marks.

Setup and run
git clone https://github.com/kanhaiyasoni018-ctrl/ai-attendance-predictor.git
cd ai-attendance-predictor

python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

pip install -r requirements.txt

# optional: regenerate the dataset
python generate_dataset.py

# start the app
python app.py
Open http://127.0.0.1:5000 in your browser.

Example request
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"classes_attended": 20, "total_classes": 50, "assignment_score": 70, "internal_marks": 70}'
Model results
On an 80/20 train/test split the Decision Tree scores about 90% accuracy (precision 95%, recall 87%).

Limitations
The dataset is synthetic and its labels come from a rule, so the accuracy does not reflect real student behaviour.
With only 200 records the accuracy estimate is uncertain.
The model label uses a 60% cut-off plus scores, so a student at 72% attendance can be predicted "on track" while the app still shows MEDIUM RISK.
Future scope
Train on real attendance records
Compare Random Forest and Logistic Regression
Add a database, student login and alerts
# Ai-attendance-predictor
