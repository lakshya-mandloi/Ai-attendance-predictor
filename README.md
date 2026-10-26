# AI Attendance Predictor

## About the Project
AI Attendance Predictor is a web-based mini project developed to help students monitor their attendance and understand their attendance risk. It uses Machine Learning to predict attendance-related risk based on attendance percentage, assignment score, and internal marks.

## Features
- Automatically calculates attendance percentage.
- Predicts attendance risk.
- Displays Low Risk, Medium Risk, and High Risk categories.
- Calculates how many consecutive classes a student needs to attend to reach 75% attendance.
- Provides a simple and user-friendly web interface.

## Technologies Used
- Python
- Flask
- Pandas
- Scikit-learn
- HTML
- CSS
- JavaScript

## Machine Learning
The project uses a Decision Tree Classifier trained on a generated dataset of 200 records. The prediction is intended for educational demonstration and may not represent real-world outcomes.

## How to Run Locally
1. Install Python.
2. Install the required libraries:

   `pip install -r requirements.txt`

3. Run the application:

   `python app.py`

4. Open your browser and visit:

   `http://127.0.0.1:5000`

## Project Purpose
This project was created as a student mini project to demonstrate the use of Machine Learning and web development in an educational application.

## Future Improvements
- Use real and anonymized attendance data.
- Improve model accuracy through testing.
- Add student dashboards and attendance reports.

## Disclaimer
This project is for educational purposes only. Predictions are estimates and should not be treated as official attendance records.

## Author
Developed as a student mini project.
