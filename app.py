from flask import Flask, render_template, request, redirect, url_for, send_file
import os
from utils import extract_text_from_pdf, get_ats_score, analyze_skills, generate_pdf_report
from skills_db import CSE_ROLES   # <-- NEW IMPORT

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure uploads folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Global variable for export
latest_results = []


@app.route('/')
def index():
    return render_template('index.html')


# ================= HR DASHBOARD =================
@app.route('/hr', methods=['GET', 'POST'])
def hr_dashboard():
    global latest_results
    results = []

    if request.method == 'POST':

        jd = request.form.get('jd')
        files = request.files.getlist('resumes')

        for file in files:
            if file.filename != '':

                path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(path)

                text = extract_text_from_pdf(path)

                score = get_ats_score(text, jd)

                results.append({
                    'name': file.filename,
                    'score': score
                })

        # Sort candidates by ATS score
        results = sorted(results, key=lambda x: x['score'], reverse=True)

        latest_results = results

    return render_template('hr.html', results=results)



# ================= CANDIDATE DASHBOARD =================
@app.route('/candidate', methods=['GET', 'POST'])
def candidate_dashboard():

    analysis = None

    if request.method == 'POST':

        role = request.form.get('role')
        file = request.files.get('resume')

        # 🔹 AUTO GENERATE JD FROM SKILL DATABASE
        role_jds = {role: ", ".join(skills) for role, skills in CSE_ROLES.items()}

        jd = role_jds.get(role, "Professional skills and experience")

        if file:

            path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(path)

            text = extract_text_from_pdf(path)

            score = get_ats_score(text, jd)

            found, missing = analyze_skills(text, jd)

            analysis = {
                'score': score,
                'found': found,
                'missing': missing,
                'role': role
            }

    return render_template('candidate.html', analysis=analysis)



# ================= EXPORT REPORT =================
@app.route('/export')
def export_report():

    if not latest_results:
        return redirect(url_for('hr_dashboard'))

    report_path = generate_pdf_report(latest_results)

    return send_file(report_path, as_attachment=True)



# ================= RUN APP =================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)