import re
from pdfminer.high_level import extract_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fpdf import FPDF
from datetime import datetime
from skills_db import CSE_ROLES

def extract_text_from_pdf(pdf_path):
    try:
        return extract_text(pdf_path)
    except Exception as e:
        print(f"Error extracting PDF: {e}")
        return ""

def clean_text(text):
    # Standard NLP cleaning without heavy libraries
    text = text.lower()
    text = re.sub(r'https?://\S+|www\.\S+', '', text) # Remove URLs
    text = re.sub(r'<.*?>', '', text) # Remove HTML
    text = re.sub(r'[^a-z\s]', '', text) # Remove special chars/numbers
    text = re.sub(r'\s+', ' ', text).strip() # Remove extra whitespace
    return text

def get_ats_score(resume_text, job_description):
    # Vectorization using TF-IDF
    cleaned_resume = clean_text(resume_text)
    cleaned_jd = clean_text(job_description)
    
    texts = [cleaned_resume, cleaned_jd]
    vectorizer = TfidfVectorizer(stop_words='english')
    
    try:
        tfidf_matrix = vectorizer.fit_transform(texts)
        score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        return round(score * 100, 2)
    except:
        return 0.0

def analyze_skills(resume_text, job_description):

    resume_words = set(clean_text(resume_text).split())

    jd_words = set(clean_text(job_description).split())

    jd_keywords = {w for w in jd_words if len(w) > 3}

    found = sorted(list(jd_keywords.intersection(resume_words)))[:12]

    missing = sorted(list(jd_keywords - resume_words))[:12]

    return found, missing

def detect_best_role(resume_text):

    cleaned = clean_text(resume_text)

    scores = {}

    for role, skills in CSE_ROLES.items():

        score = 0

        for skill in skills:
            if skill in cleaned:
                score += 1

        scores[role] = score

    best_role = max(scores, key=scores.get)

    return best_role

# PDF Report Logic
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'AI Resume Ranker - HR Report', 0, 1, 'C')
        self.ln(5)

def generate_pdf_report(results):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    
    # Header Colors
    pdf.set_fill_color(59, 130, 246)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(30, 10, 'Rank', 1, 0, 'C', True)
    pdf.cell(110, 10, 'Candidate Name', 1, 0, 'C', True)
    pdf.cell(50, 10, 'Match Score', 1, 1, 'C', True)
    
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Arial', '', 10)
    for i, res in enumerate(results, 1):
        pdf.cell(30, 10, f"#{i}", 1, 0, 'C')
        pdf.cell(110, 10, f" {res['name']}", 1, 0, 'L')
        pdf.cell(50, 10, f"{res['score']}%", 1, 1, 'C')
    
    path = "uploads/Report.pdf"
    pdf.output(path)
    return path