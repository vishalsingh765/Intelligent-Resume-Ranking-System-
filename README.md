# 📄 Intelligent Resume Ranking System

## Overview

The Intelligent Resume Ranking System is an AI-powered recruitment solution that automates the process of screening and ranking candidate resumes. Using Natural Language Processing (NLP) techniques, the system compares resumes against a job description, calculates similarity scores, and ranks candidates based on their relevance to the role.

This helps recruiters and hiring managers save time, reduce manual effort, and make data-driven hiring decisions.

---

## ✨ Features

* Upload and analyze multiple resumes simultaneously
* Extract text from PDF resumes
* Compare resumes with a job description
* Generate candidate match scores
* Automatically rank candidates based on relevance
* Categorize applicants as Selected, Review, or Rejected
* Interactive Streamlit dashboard
* Candidate search and filtering
* Export ranking results to CSV

---

## 🛠️ Technology Stack

* Python
* Streamlit
* Pandas
* Scikit-learn
* TF-IDF Vectorization
* Cosine Similarity
* PyPDF2 / PDF Processing Libraries

---

## ⚙️ How It Works

1. Upload candidate resumes.
2. Enter the job description.
3. The system extracts text from each resume.
4. NLP techniques convert text into numerical representations.
5. Similarity scores are calculated between resumes and the job description.
6. Candidates are ranked automatically based on their scores.
7. Hiring recommendations are generated for each applicant.

---

## 📊 Candidate Classification

| Match Score | Recommendation |
| ----------- | -------------- |
| 70% – 100%  | Selected       |
| 50% – 69%   | Review         |
| Below 50%   | Rejected       |

---

## 🎯 Use Cases

* Recruitment and Talent Acquisition
* Internship Screening
* Campus Hiring
* Resume Shortlisting
* HR Automation

---

## 🚀 Installation

```bash
git clone https://github.com/your-username/intelligent-resume-ranking-system.git

cd intelligent-resume-ranking-system

pip install -r requirements.txt

streamlit run app.py
```

---

## 📈 Benefits

* Faster resume screening
* Reduced hiring effort
* Objective candidate evaluation
* Improved recruitment efficiency
* Better hiring decisions through AI-driven insights

---

## 🔮 Future Enhancements

* AI-powered skill gap analysis
* Resume parsing using LLMs
* ATS compatibility scoring
* Interview question generation
* Advanced candidate analytics dashboard

---

## 👨‍💻 Author

**Vishal Singh**

An AI-based recruitment assistant designed to streamline candidate screening and improve hiring efficiency through intelligent resume analysis and ranking.
