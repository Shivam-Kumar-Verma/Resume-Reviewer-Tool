from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from utils.resume_parser import extract_text_from_pdf, extract_text_from_docx, score_resume

app = FastAPI()

# Enable frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; limit in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-resume/")
async def upload_resume(
    file: UploadFile = File(...),
    job_role: str = Form(default=None)
):
    text = ""

    # Detect file type and extract content
    if file.content_type == "application/pdf":
        text = extract_text_from_pdf(file)
    elif file.content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text = extract_text_from_docx(file)
    else:
        return {"error": "Only PDF and DOCX files are supported."}

    # Score resume based on job role
    scoring = score_resume(text, job_role)

    return {
        "text": text,
        "score": scoring["score"],
        "matched_keywords": scoring["matched_keywords"],
        "job_role": job_role
    }