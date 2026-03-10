# TalentRank AI — Intelligent Resume Screening & ATS Optimization Platform

An **AI-driven Resume Ranking and ATS Analysis System** that helps recruiters efficiently screen candidates and helps job seekers optimize their resumes for specific roles.

This project leverages **Natural Language Processing (NLP)** and **Machine Learning techniques** to evaluate resumes, compute ATS scores, detect skill gaps, and rank candidates based on job descriptions.

---

# 🌐 Live Demo

🔗 **Deployed Application:**
https://web-production-f3ccb.up.railway.app

---

# 🧠 Project Overview

Recruiters often receive **hundreds of resumes** for a single job role. Manually reviewing them is time-consuming and inefficient.

This system automates resume screening by:

* Extracting text from resumes
* Matching skills against job descriptions
* Computing ATS compatibility scores
* Ranking candidates automatically
* Providing actionable insights to candidates

The platform includes **two dashboards**:

### 👨‍💼 HR Dashboard

Designed for recruiters to quickly identify the best candidates.

Features:

* Upload multiple resumes
* Rank candidates automatically
* ATS score for each resume
* Candidate match percentage
* Downloadable PDF report for HR review

---

### 👩‍💻 Candidate Dashboard

Helps candidates optimize their resumes for ATS systems.

Features:

* Resume ATS scoring
* Skill detection
* Missing keyword identification
* Personalized skill improvement roadmap
* Skill radar visualization

---

# 🏗 System Architecture

Resume Upload
↓
PDF Text Extraction
↓
NLP Preprocessing (SpaCy)
↓
TF-IDF Vectorization
↓
Keyword Matching & Skill Extraction
↓
ATS Scoring Algorithm
↓
Candidate Ranking & Visualization

---

# ⚙️ Tech Stack

### Backend

* Python
* Flask

### NLP & Machine Learning

* SpaCy
* Scikit-learn
* TF-IDF Vectorization

### Data Processing

* PDFPlumber

### Frontend

* HTML5
* CSS3
* Bootstrap
* Chart.js

### Deployment

* Railway
* GitHub

---

# 📊 ATS Scoring Methodology

The ATS score is calculated using:

1. **Keyword Matching**
2. **Skill Extraction**
3. **TF-IDF Similarity with Job Description**
4. **Engineering Skill Database Matching**

Score Formula:

ATS Score =
(Number of Matched Skills / Total Required Skills) × 100

---

# 📁 Project Structure

```
AI-ATS-System
│
├── app.py
├── utils.py
├── skills_db.py
├── requirements.txt
│
├── templates
│   ├── index.html
│   ├── hr.html
│   └── candidate.html
│
├── static
│   └── style.css
│
└── uploads
```

---

# 🎯 Use Cases

Recruiters:

* Automated resume screening
* Candidate ranking
* Skill-based hiring

Job Seekers:

* Resume optimization
* ATS compatibility analysis
* Skill gap identification

---
