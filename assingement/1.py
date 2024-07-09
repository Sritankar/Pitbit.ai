import json
import os
import fitz  # PyMuPDF for PDF parsing
from docx import Document  # python-docx for Word document parsing

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(pdf_file)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def parse_resume_to_json(resume_file):
    _, file_extension = os.path.splitext(resume_file)

    if file_extension.lower() == '.pdf':
        resume_text = extract_text_from_pdf(resume_file)
    elif file_extension.lower() == '.docx':
        resume_text = extract_text_from_docx(resume_file)
    else:
        raise ValueError("Unsupported file format. Only PDF and DOCX files are supported.")

    # Parse the resume text into JSON format (dummy structure for illustration)
    resume_data = {
        "name": "John Doe",
        "contact_information": {
            "email": "john.doe@example.com",
            "phone": "+1234567890",
            "address": "123 Main Street, Anytown, USA"
        },
        "education": [
            {
                "degree": "Bachelor of Science in Computer Science",
                "university": "University of Example",
                "year": "2022"
            },
            {
                "degree": "High School Diploma",
                "school": "Example High School",
                "year": "2018"
            }
        ],
        "experience": [
            {
                "title": "Software Engineer Intern",
                "company": "Tech Solutions Inc.",
                "dates": "Summer 2021",
                "responsibilities": [
                    "Developed backend systems using Python and Django framework.",
                    "Collaborated with team members to implement new features and fix bugs.",
                    "Participated in code reviews and testing procedures."
                ]
            },
            {
                "title": "Customer Service Representative",
                "company": "ABC Retail",
                "dates": "2019 - 2020",
                "responsibilities": [
                    "Assisted customers with product inquiries and purchases.",
                    "Handled customer complaints and resolved issues effectively.",
                    "Maintained a positive and helpful attitude to ensure customer satisfaction."
                ]
            }
        ],
        "skills": [
            "Python",
            "Java",
            "HTML/CSS",
            "JavaScript",
            "SQL",
            "Problem Solving",
            "Team Collaboration",
            "Communication Skills"
        ]
    }

    # Convert the dictionary to JSON format
    resume_json = json.dumps(resume_data, indent=4)
    return resume_json

# Example usage:
resume_file_path = 'path_to_your_resume_file.pdf'  # Replace with your resume file path
parsed_resume_json = parse_resume_to_json(resume_file_path)
print(parsed_resume_json)
