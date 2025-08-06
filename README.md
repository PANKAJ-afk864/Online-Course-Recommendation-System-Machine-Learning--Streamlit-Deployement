# Online Course Recommendation System

This project is a fully functional, interactive **web application** developed using **Streamlit** that allows users to receive personalized course recommendations based on their interests, difficulty preferences, and quality metrics such as ratings and feedback scores. It’s ideal for learners who want to navigate large volumes of course content quickly and intelligently.

---

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Tech Stack](#tech-stack)
- [Dataset Overview](#dataset-overview)
- [How It Works](#how-it-works)
- [Installation & Local Setup](#installation--local-setup)
- [Deployment (Streamlit Cloud)](#deployment-streamlit-cloud)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Use Cases](#use-cases)
- [Contributing](#contributing)
- [Contact](#contact)

---

##  Features

- Search for courses by keyword (e.g., Python, AI, Marketing)
-  Select preferred difficulty level (Beginner, Intermediate, Advanced)
-  Sort recommendations by Rating, Feedback Score, or Enrollment Numbers
- Option to include Instructor Details and Feedback Scores in output
-  Download recommendations as a CSV file
-  Preview the entire course catalog on demand

---

##  Demo

You can deploy this app live using [Streamlit Cloud] https://prldkhtzrbqrntapx8ffia.streamlit.app/. Once hosted, users can access it via a public URL.

---

## 🛠 Tech Stack

- **Python 3.7+**
- **Streamlit** – for building the frontend UI
- **Pandas** – for data handling and transformation
- **OpenPyXL** – for reading Excel data

---

## Dataset Overview

The dataset used (`online_course_recommendation_v2.xlsx`) contains structured information about online courses, including:

- `course_name`: Title of the course  
- `instructor`: Name of the instructor  
- `rating`: User-generated rating of the course  
- `feedback_score`: Aggregated feedback score 
- `difficulty_level`: Difficulty level of the course (Beginner, Intermediate, Advanced)  
- `enrollment_numbers`: Number of learners enrolled  

---

##  How It Works

1. User inputs a keyword (e.g., "python")  
2. The app filters course titles that match the keyword  
3. User selects difficulty level and sorting preference from the sidebar  
4. Filtered and sorted results are displayed in a dataframe  
5. User can optionally include instructor and feedback details  
6. Results can be downloaded as a CSV file  

---

##  Installation & Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/online-course-recommender.git
cd online-course-recommender

### 2. Install Required Packages
pip install -r requirements.txt

### 3. Run the Streamlit App
streamlit run app.py

🗂 Project Structure
bash
Copy
Edit
online-course-recommender/
│
├── app.py                           # Main application logic
├── online_course_recommendation_v2.xlsx   # Dataset file
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
└── .gitignore                      # Ignored files & folders

🖼 Screenshots


💼 Use Cases
Educational platforms that want to suggest relevant courses to learners

Learners overwhelmed with course overload on platforms like Coursera, Udemy, etc.

Colleges/universities building personalized recommendation engines for their LMS


🤝 Contributing
If you’d like to improve this app, feel free to fork the repo and submit a pull request.

Fork the repository

Create your branch: git checkout -b feature-name

Commit your changes: git commit -m "Add some feature"

Push to the branch: git push origin feature-name

Open a pull request


📬 Contact
Name: Pankaj Kumar Singh

LinkedIn: www.linkedin.com/in/pankaj-kumar-singh-396162325

Email: pankajjsinghh376@gmail.com


