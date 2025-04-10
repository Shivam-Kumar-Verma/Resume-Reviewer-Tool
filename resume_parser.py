from io import BytesIO
import fitz  # PyMuPDF
from docx import Document
job_keywords = {
    "data scientist": [
        "python", "machine learning", "pandas", "data visualization", "sql", "tensorflow", "statistics"
    ],
    "frontend developer": [
        "html", "css", "javascript", "react", "responsive design", "tailwind", "webpack"
    ],
    "backend developer": [
        "python", "django", "flask", "sql", "api", "rest", "postgresql", "authentication"
    ],
    "devops engineer": [
        "aws", "docker", "kubernetes", "ci/cd", "linux", "terraform", "monitoring"
    ]
}

def extract_text_from_pdf(file):
    text = ""
    with BytesIO(file.file.read()) as data:
        doc = fitz.open(stream=data, filetype="pdf")
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(file):
    text = ""
    with BytesIO(file.file.read()) as data:
        doc = Document(data)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text
def score_resume(text, job_role=None):
    text_lower = text.lower()

    keywords = job_keywords.get(job_role.lower(), []) if job_role else []

    matched = [kw for kw in keywords if kw in text_lower]

    score = len(matched) / len(keywords) * 100 if keywords else 0

    return {
        "score": round(score, 2),
        "matched_keywords": matched,
        "total_keywords": keywords
    }


