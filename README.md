# 📝 AI Resume & Cover Letter Generator

An intelligent **Resume + Cover Letter Builder** that helps job seekers create professional, tailored applications using AI and clean templates.

Built with Python 🐍, it features:

## ✨ Features

* **Interactive CLI** → Input your details (name, skills, experience, education).
* **Smart Resume Generator** → Exports your resume in **Markdown & PDF** with professional formatting.
* **AI Cover Letter Generator** → Reads job descriptions and generates a **tailored, confident cover letter**.
* **Sentiment & Tone Analyzer** → Ensures your cover letter sounds **confident, professional, and positive**.
* **Storage & Recall** → Saves resumes & letters for reuse. Compare your mood/tone across dates.
* **CI/CD Ready** → Integrated GitHub Actions workflows for testing, building, and security scanning.

## ⚡ Tech Stack

* Python 3.10+
* TextBlob (sentiment analysis)
* ReportLab (PDF export)
* Rich (beautiful CLI output)
* GitHub Actions (CI/CD pipelines)

## 🔧 Workflows (CI/CD)

This repo comes with **3 GitHub Actions workflows**:

* ✅ **Python Package** → Installs dependencies, lints, and runs tests.
* ✅ **Build Resume** → Automatically generates your resume PDF on GitHub.
* ✅ **CodeQL** → Security scanning for vulnerabilities.

## 🚀 How to Run Locally

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows
pip install -r requirements.txt
python resume_builder.py
```

## 📸 Example Usage

```
> Enter your name: John Doe
> Enter your email: john@example.com
> Enter your skills: Python, Data Science, Machine Learning
> Paste job description: (paste text here)
```

Generates:
✅ `resume.pdf`
✅ `cover_letter.pdf`

## 🌍 Why This Project?

This project simulates **real-world developer workflows**:

* AI-driven text generation
* Professional PDF exports
* GitHub Actions pipelines
* Security + testing integration


