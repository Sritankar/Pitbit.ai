Explanation:
Extracting Text from Resume File:

extract_text_from_pdf: Uses PyMuPDF (fitz) to extract text from a PDF file.
extract_text_from_docx: Uses python-docx (Document class) to extract text from a Word document.
Parsing to JSON Format:

parse_resume_to_json: Takes the extracted text (dummy content for illustration purposes) and structures it into a JSON format.
Handling Different File Formats:

The script checks the file extension to determine whether the resume file is a PDF or DOCX. Other formats can be added with additional libraries or custom parsing logic.
Replace 'path_to_your_resume_file.pdf' with the actual path to your resume file. Adjust the resume_data dictionary within parse_resume_to_json according to the actual structure and details present in your resume.

This script provides a basic framework for parsing and converting resume content from various file formats into JSON format using Python.
