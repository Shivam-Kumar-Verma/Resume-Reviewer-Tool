# Resume-Reviewer-Tool(AI-Powered)Add commentMore actions
OverView
 This is a lightweight, fast, and intuitive AI-powered resume reviewer built with FastAPI and a modern HTML/JS frontend. It allows users to upload a resume, select a job role, and instantly get:  
 ✅ A skill match score 
 ✅ Highlighted matched keywords
 ✅ Raw extracted resume text
 ✅ Support for PDF and DOCX files
## Overview

**Resume Reviewer Tool** is a lightweight, fast, and intuitive AI-powered resume reviewer built with FastAPI and a modern HTML/JS frontend. It allows users to upload a resume, select a job role, and instantly get.

## Features
📄 Upload PDF or DOCX resumes

🧠 **AI-based scoring** using keyword matching

💼 **Auto keyword detection** based on selected job role

🎯 Match % calculated based on how well your resume fits the selected role

💡 **Instant feedback** via a clean and responsive UI

✅ **Raw extracted resume text**

## Installation

To run this app locally, open command prompt in your desired folder and follow these steps:

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-username/resume-review-tool.git
   cd resume-review-tool

2. **Create a virtual environment and activate it:**

   ```sh
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`

3. **Install the required dependencies:**

   ```sh
   pip install -r requirements.txt

4. **Run the backend:**

   ```sh
   uvicorn main:app --reload

5.  Open **index.html** in a browser (double-click it or serve it via VSCode Live Server)

  
## Usage

1. Run the **Index.html** file in {"VS-Code" + "Live Server"} :

   If you're using Visual Studio Code(recommended):

    Open your project folder in VS Code

    Install the Live Server extension (if not already).

    Right-click on index.html and choose “Open with Live Server”.

    Your frontend will open in the browser at [http://127.0.0.1:5500/Frontend/index.html] or similar.
    
2. Open your web browser and navigate to [http://127.0.0.1:8000/docs].

3. Use the sidebar to select a Job Role and Upload your Resume by selecting Choose File(pdf,docx) , then click on the "Analyze Resume" button to get your Score and generate summary.

4. View and download the summary from the results section.

## Requirements

* Python 3.x
* python-multipart
* python-docx
* fastapi
* uvicorn
  
To ensure all dependencies are installed, check the requirements.txt file.

## Example
Here's how you can use the app:

1. User uploads a resume.
2. Selects a job role (e.g., Data Scientist, Frontend Developer,etc).
3. Resume text is extracted.
4. Keywords relevant to the selected job are matched.
5. A match score is calculated and returned with matched keywords.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request. Ensure that your contributions adhere to the coding style and add tests where appropriate.

## Why this tool?
This tool helps job seekers quickly validate how well their resume matches specific job roles, ensuring they target the right skills before applying.

## Contact
For any questions or feedback, please contact shivam@nitmanipur.ac.in 