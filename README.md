# Resume-Reviewer-Tool(AI-Powered)
OverView
 This is a lightweight, fast, and intuitive AI-powered resume reviewer built with FastAPI and a modern HTML/JS frontend. It allows users to upload a resume, select a job role, and instantly get:  
 ✅ A skill match score 
 ✅ Highlighted matched keywords
 ✅ Raw extracted resume text
 ✅ Support for PDF and DOCX files
 🚀 Features
📄 Upload PDF or DOCX resumes

🧠 AI-based scoring using keyword matching

💼 Auto keyword detection based on selected job role

🎯 Match % calculated based on how well your resume fits the selected role

💡 Instant feedback via a clean and responsive UI

🔧 Tech Stack
Backend: FastAPI (Python)

Frontend: Vanilla HTML/CSS + JavaScript

Resume Parsing: PyMuPDF (fitz) and python-docx

🛠️ How It Works
User uploads a resume

Selects a job role (e.g., Data Scientist, Frontend Developer)

Resume text is extracted

Keywords relevant to the selected job are matched

A match score is calculated and returned with matched keywords

📦 How to Run Locally
Clone the repo:

bash
Copy
Edit
git clone https://github.com/your-username/resume-review-tool.git
cd resume-review-tool
Create a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the backend:

bash
Copy
Edit
uvicorn main:app --reload
Open index.html in a browser (double-click it or serve it via VSCode Live Server)

🧠 Future Features (Planned)
Resume suggestions for missing keywords

Custom keyword inputs

Resume improvement tips using GPT

User dashboard with saved scores

💡 Why This Tool?
This tool helps job seekers quickly validate how well their resume matches specific job roles, ensuring they target the right skills before applying.


