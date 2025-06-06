from io import BytesIO
import fitz  # PyMuPDF
from docx import Document
import re

# Normalized keyword dictionary (all lowercase, no special formatting issues)
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
    ],
    "ui-ux designer": [
        "figma", "adobe xd", "sketch", "invision", "adobe photoshop", "illustrator", "html", "css",
        "webflow", "framer", "design systems", "typography", "responsive design", "color theory"
    ],
    "data analyst": [
        "excel", "sql", "r", "python", "pandas", "numpy", "tableau", "oracle", "mongodb", "hadoop",
        "talend", "alteryx", "apache nifi", "spark"
    ],
    "cloud architect": [
        "aws", "microsoft azure", "google cloud platform", "docker", "linux", "terraform", "monitoring", "kubernetes"
    ],
    "machine learning engineer": [
        "python", "r", "java", "ci/cd", "c++", "pandas", "numpy", "pytorch", "tensorflow", "docker",
        "fastapi", "kubernetes", "airflow", "terraform", "luigi"
    ],
    "electronics engineer": [
        "circuit design", "pcb design", "microcontrollers", "embedded systems", "iot", "rf", 
        "wireless communication", "power electronics", "signal processing", "matlab", "simulink",
        "vhdl", "verilog", "python", "c", "c++", "labview", "ltspice", "pspice", 
        "autocad electrical", "proteus"
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

def clean_and_tokenize(text):
    # Remove special characters and tokenize
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    tokens = set(text.split())
    return tokens

def score_resume(text, job_role=None):
    tokens = clean_and_tokenize(text)

    if not job_role:
        return {
            "score": 0,
            "matched_keywords": [],
            "total_keywords": []
        }

    role = job_role.strip().lower()
    keywords = job_keywords.get(role, [])

    matched = [kw for kw in keywords if all(word in tokens for word in kw.split())]

    score = len(matched) / len(keywords) * 100 if keywords else 0

    return {
        "score": round(score, 2),
        "matched_keywords": matched,
        "total_keywords": keywords
    }