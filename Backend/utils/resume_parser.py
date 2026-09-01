from io import BytesIO
import fitz  # PyMuPDF
from docx import Document
import re

# Normalized keyword dictionary (all lowercase, no special formatting issues)
job_keywords = {

    "data scientist": [
        "python", "machine learning", "pandas", "data visualization",
        "sql", "tensorflow", "statistics", "scikit-learn", "numpy",
        "pytorch", "deep learning", "nlp", "data preprocessing"
    ],

    "frontend developer": [
        "html", "css", "javascript", "react", "responsive design",
        "tailwind", "webpack", "typescript", "next.js", "redux",
        "bootstrap", "vite", "angular", "vue.js", "figma"
    ],

    "backend developer": [
        "python", "django", "flask", "sql", "api", "rest",
        "postgresql", "authentication", "node.js", "express.js",
        "mongodb", "redis", "microservices", "jwt", "graphql"
    ],

    "full stack developer": [
        "html", "css", "javascript", "react", "node.js",
        "express.js", "mongodb", "sql", "rest api", "git",
        "typescript", "next.js", "redux", "authentication",
        "docker", "postgresql"
    ],

    "software developer": [
        "java", "python", "c++", "javascript", "data structures",
        "algorithms", "oop", "sql", "git", "github", "debugging",
        "software development", "api", "testing"
    ],

    "software engineer": [
        "java", "python", "c++", "javascript", "data structures",
        "algorithms", "object oriented programming", "system design",
        "sql", "git", "api", "testing", "debugging", "linux"
    ],

    "devops engineer": [
        "aws", "docker", "kubernetes", "ci/cd", "linux",
        "terraform", "monitoring", "jenkins", "ansible",
        "github actions", "gitlab", "azure", "prometheus", "grafana"
    ],

    "cloud engineer": [
        "aws", "azure", "google cloud platform", "docker",
        "kubernetes", "linux", "terraform", "cloud computing",
        "ci/cd", "networking", "iam", "cloudformation"
    ],

    "cloud architect": [
        "aws", "microsoft azure", "google cloud platform",
        "docker", "linux", "terraform", "monitoring",
        "kubernetes", "cloud architecture", "networking",
        "security", "scalability"
    ],

    "ui-ux designer": [
        "figma", "adobe xd", "sketch", "invision", "adobe photoshop",
        "illustrator", "html", "css", "webflow", "framer",
        "design systems", "typography", "responsive design",
        "color theory", "user research", "wireframing", "prototyping"
    ],

    "data analyst": [
        "excel", "sql", "r", "python", "pandas", "numpy",
        "tableau", "oracle", "mongodb", "hadoop", "talend",
        "alteryx", "apache nifi", "spark", "power bi",
        "data visualization", "statistics", "data cleaning"
    ],

    "business analyst": [
        "excel", "sql", "power bi", "tableau", "data analysis",
        "business analysis", "requirements gathering",
        "stakeholder management", "business requirements",
        "process improvement", "documentation", "jira",
        "problem solving"
    ],

    "machine learning engineer": [
        "python", "r", "java", "ci/cd", "c++", "pandas",
        "numpy", "pytorch", "tensorflow", "docker", "fastapi",
        "kubernetes", "airflow", "terraform", "luigi",
        "scikit-learn", "mlops", "deep learning", "model deployment"
    ],

    "ai engineer": [
        "python", "machine learning", "deep learning", "tensorflow",
        "pytorch", "scikit-learn", "numpy", "pandas", "nlp",
        "computer vision", "generative ai", "llm", "transformers",
        "hugging face", "model deployment", "fastapi"
    ],

    "data engineer": [
        "python", "sql", "spark", "hadoop", "airflow", "kafka",
        "etl", "data pipelines", "aws", "azure", "gcp",
        "databricks", "snowflake", "postgresql", "mongodb",
        "data warehouse", "data lake"
    ],

    "database administrator": [
        "sql", "mysql", "postgresql", "oracle", "mongodb",
        "database administration", "database security",
        "backup", "recovery", "performance tuning",
        "replication", "linux", "pl/sql"
    ],

    "cybersecurity analyst": [
        "network security", "cybersecurity", "linux", "python",
        "firewalls", "siem", "penetration testing", "vulnerability assessment",
        "ethical hacking", "incident response", "wireshark",
        "nmap", "splunk", "iam", "cryptography"
    ],

    "network engineer": [
        "networking", "tcp/ip", "dns", "dhcp", "routing",
        "switching", "cisco", "ccna", "firewall", "vpn",
        "lan", "wan", "wireshark", "linux", "network security"
    ],

    "embedded systems engineer": [
        "embedded systems", "microcontrollers", "c", "c++",
        "arduino", "stm32", "esp32", "raspberry pi", "rtos",
        "firmware", "gpio", "uart", "spi", "i2c", "can",
        "pcb design", "debugging"
    ],

    "electronics engineer": [
        "circuit design", "pcb design", "microcontrollers",
        "embedded systems", "iot", "rf", "wireless communication",
        "power electronics", "signal processing", "matlab", "simulink",
        "vhdl", "verilog", "python", "c", "c++", "labview",
        "ltspice", "pspice", "autocad electrical", "proteus"
    ],

    "electrical engineer": [
        "electrical engineering", "power systems", "electrical machines",
        "power electronics", "control systems", "transformers",
        "motors", "generators", "switchgear", "relay",
        "plc", "scada", "matlab", "autocad", "maintenance"
    ],

    "instrumentation engineer": [
        "instrumentation", "process control", "plc", "scada",
        "sensors", "transducers", "control systems", "calibration",
        "industrial automation", "pid", "dcs", "hmi",
        "4-20ma", "modbus", "profibus", "labview"
    ],

    "automation engineer": [
        "plc", "scada", "hmi", "industrial automation",
        "control systems", "siemens", "allen bradley",
        "rockwell", "ladder logic", "pid", "sensors",
        "actuators", "servo motor", "vfd", "robotics"
    ],

    "maintenance engineer": [
        "preventive maintenance", "corrective maintenance",
        "predictive maintenance", "troubleshooting", "electrical maintenance",
        "mechanical maintenance", "motors", "generators", "pumps",
        "hydraulic systems", "plc", "scada", "sensors",
        "relay", "vfd", "maintenance planning", "root cause analysis"
    ],

    "control systems engineer": [
        "control systems", "plc", "scada", "dcs", "pid",
        "matlab", "simulink", "automation", "instrumentation",
        "process control", "feedback control", "industrial control",
        "ladder logic", "hmi"
    ],

    "telecommunication engineer": [
        "telecommunications", "wireless communication", "5g",
        "4g", "rf", "antenna", "fiber optics", "microwave",
        "signal processing", "networking", "lte", "gsm",
        "matlab", "communication systems"
    ],

    "rf engineer": [
        "rf", "radio frequency", "antenna", "microwave",
        "electromagnetics", "signal processing", "wireless communication",
        "5g", "4g", "spectrum analysis", "network analyzer",
        "matlab", "ads", "hfss", "cst"
    ],

    "vlsi engineer": [
        "vlsi", "verilog", "vhdl", "systemverilog", "rtl",
        "digital design", "asic", "fpga", "semiconductor",
        "soc", "static timing analysis", "synthesis",
        "physical design", "eda", "cadence", "synopsys"
    ],

    "fpga engineer": [
        "fpga", "verilog", "vhdl", "systemverilog",
        "digital design", "rtl", "xilinx", "vivado",
        "intel quartus", "timing analysis", "synthesis",
        "embedded systems", "hardware design"
    ],

    "pcb design engineer": [
        "pcb design", "altium", "kicad", "eagle",
        "orcad", "schematic", "gerber", "pcb layout",
        "signal integrity", "power integrity", "embedded systems",
        "circuit design", "electronics"
    ],

    "robotics engineer": [
        "robotics", "ros", "python", "c++", "arduino",
        "raspberry pi", "computer vision", "control systems",
        "sensors", "actuators", "kinematics", "automation",
        "embedded systems", "path planning"
    ],

    "iot engineer": [
        "iot", "internet of things", "arduino", "esp32",
        "raspberry pi", "mqtt", "sensors", "embedded systems",
        "python", "c", "c++", "aws iot", "bluetooth",
        "wifi", "lorawan"
    ],

    "product engineer": [
        "product development", "product lifecycle", "prototyping",
        "testing", "validation", "root cause analysis",
        "problem solving", "design", "manufacturing",
        "quality", "cross functional", "stakeholder management"
    ],

    "quality engineer": [
        "quality control", "quality assurance", "six sigma",
        "lean manufacturing", "root cause analysis", "8d",
        "fmea", "spc", "iso 9001", "process improvement",
        "quality inspection", "statistical analysis"
    ],

    "manufacturing engineer": [
        "manufacturing", "production", "lean manufacturing",
        "six sigma", "process optimization", "cnc",
        "automation", "quality control", "fmea", "kaizen",
        "process improvement", "industrial engineering"
    ],

    "production engineer": [
        "production planning", "manufacturing", "process optimization",
        "quality control", "lean manufacturing", "six sigma",
        "maintenance", "inventory management", "safety",
        "production management", "root cause analysis"
    ],

    "mechanical engineer": [
        "mechanical design", "solidworks", "autocad", "ansys",
        "thermodynamics", "fluid mechanics", "machine design",
        "manufacturing", "cad", "cam", "cnc", "materials",
        "maintenance", "mechanical systems"
    ],

    "oil and gas engineer": [
        "oil and gas", "well logging", "wireline",
        "drilling", "reservoir", "petroleum", "mud logging",
        "production", "formation evaluation", "well testing",
        "pressure control", "field operations", "maintenance",
        "safety", "instrumentation"
    ],

    "field engineer": [
        "field engineering", "field operations", "equipment maintenance",
        "troubleshooting", "installation", "commissioning",
        "testing", "technical support", "customer support",
        "safety", "documentation", "site operations"
    ],

    "technical support engineer": [
        "technical support", "troubleshooting", "customer support",
        "debugging", "networking", "linux", "sql", "api",
        "ticketing", "documentation", "problem solving",
        "communication skills"
    ],

    "project engineer": [
        "project management", "project planning", "engineering",
        "project execution", "documentation", "budgeting",
        "scheduling", "risk management", "stakeholder management",
        "quality", "safety", "ms project"
    ],

    "research engineer": [
        "research", "matlab", "python", "machine learning",
        "simulation", "data analysis", "signal processing",
        "algorithm development", "experimental analysis",
        "technical documentation", "research methodology"
    ],

    "business intelligence analyst": [
        "sql", "power bi", "tableau", "excel", "data visualization",
        "dashboard", "data analysis", "reporting", "kpi",
        "business intelligence", "statistics", "etl"
    ],

    "financial analyst": [
        "excel", "financial modeling", "valuation", "accounting",
        "financial analysis", "forecasting", "budgeting",
        "investment analysis", "statistics", "power bi",
        "data analysis", "corporate finance"
    ],

    "technical consultant": [
        "consulting", "problem solving", "sql", "python",
        "data analysis", "technical support", "client management",
        "stakeholder management", "requirements gathering",
        "presentation", "project management"
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