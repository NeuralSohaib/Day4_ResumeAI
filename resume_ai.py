import os
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from textblob import TextBlob
# Setup paths
TEMPLATES_DIR = "templates"
OUTPUT_DIR = "output"

# Ensure output folder exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load Jinja2 environment
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
template = env.get_template("resume_template.txt")

# Sample user data (later we’ll make this interactive)
user_data =  {
    "name": "Sohaib",
    "email": "sohaib@example.com",
    "phone": "+92-300-1234567",
    "skills": ["Python", "AI/ML", "Data Analysis", "Problem Solving"],
    "experience": [
        {"role": "AI Student", "company": "Self-Learning", "years": "2025-Present", "details": "Building AI projects and learning machine learning."},
        {"role": "Software Tester", "company": "XYZ Pvt Ltd", "years": "2022-2024", "details": "Worked on test automation and bug tracking."}
    ],
    "education": [
        {"degree": "Self-Taught AI Path", "institution": "Online & Projects", "year": "Ongoing"},
        {"degree": "High School Diploma", "institution": "ABC School", "year": "2020"}
    ]
}

# Render the template with data
output_text = template.render(user_data)

# Save to file
filename = f"resume_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
output_path = os.path.join(OUTPUT_DIR, filename)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(output_text)

print(f"✅ Resume generated: {output_path}")


def generate_resume(user_data):
    resume = f"# {user_data['name']}\n\n"
    resume += f"📧 {user_data['email']} | 📱 {user_data['phone']}\n\n"

    resume += "## Skills\n"
    resume += ", ".join(user_data['skills']) + "\n\n"

    resume += "## Experience\n"
    for exp in user_data["experience"]:
        resume += f"**{exp['role']}** – {exp['company']} ({exp['duration']})\n"
        resume += f"- {exp['details']}\n\n"

    resume += "## Education\n"
    for edu in user_data["education"]:
        resume += f"- {edu['degree']} – {edu['institution']} ({edu['year']})\n"

    return resume

def generate_cover_letter(user_data, job_description):
    cover_letter = f"""
Dear Hiring Manager,

I am excited to apply for the opportunity you have posted. With a strong foundation in {", ".join(user_data['skills'])}, 
and hands-on experience at {user_data['experience'][0]['company']}, I am confident in my ability to contribute effectively to your team.

In my recent role as {user_data['experience'][0]['role']}, I {user_data['experience'][0]['details']}.
This experience has sharpened my problem-solving abilities and my passion for building impactful solutions.

Your job description mentions: "{job_description[:100]}..."  
I believe my background and expertise make me a strong fit for these requirements.

I would be thrilled to bring my skills and enthusiasm to your organization and contribute to its success.

Sincerely,  
{user_data['name']}
    """
    return cover_letter.strip()


def analyze_tone(text):
    blob = TextBlob (text)
    polarity = blob.sentiment.polarity  # -1 to +1

    if polarity > 0.3:
        tone = "Confident & Positive ✅"
        suggestion = "Great tone! You sound motivated and professional."
    elif polarity < -0.1:
        tone = "Negative or Weak ⚠️"
        suggestion = "Try to reframe sentences to highlight strengths and optimism."
    else:
        tone = "Neutral 😐"
        suggestion = "Your tone is balanced, but you could add more enthusiasm."

    return {
        "polarity": round(polarity, 2),
        "tone": tone,
        "suggestion": suggestion
    }

def main():
    print("🚀 AI Resume & Cover Letter Builder\n")
    user_data # for now, using sample

    while True:
        print("\nChoose an option:")
        print("1. Generate Resume")
        print("2. Generate Cover Letter")
        print("3. Analyze Cover Letter Tone")
        print("4. Exit")

        choice = input("> ")

        if choice == "1":
            resume = generate_resume(user_data)
            print("\n--- Generated Resume ---\n")
            print(resume)
            with open("resume.md", "w", encoding="utf-8") as f:
                f.write(resume)
            print("✅ Resume saved as resume.md")

        elif choice == "2":
            job_desc = input("\nPaste Job Description:\n> ")
            global last_cover_letter
            last_cover_letter = generate_cover_letter(user_data, job_desc)
            print("\n--- Generated Cover Letter ---\n")
            print(last_cover_letter)
            with open("cover_letter.md", "w", encoding="utf-8") as f:
                f.write(last_cover_letter)
            print("✅ Cover Letter saved as cover_letter.md")

        elif choice == "3":
            if "last_cover_letter" not in globals():
                print("⚠️ Please generate a cover letter first (Option 2).")
            else:
                analysis = analyze_tone(last_cover_letter)
                print("\n--- Tone Analysis ---\n")
                print(f"Sentiment Score: {analysis['polarity']}")
                print(f"Tone: {analysis['tone']}")
                print(f"Suggestion: {analysis['suggestion']}")

        elif choice == "4":
            print("👋 Exiting. Good luck with your applications!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    main()