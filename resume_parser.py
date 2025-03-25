import PyPDF2
import re

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

# Function to extract name from the text
def extract_name(text):
    name_pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"  # Simple pattern for two words (First and Last Name)
    match = re.search(name_pattern, text)
    return match.group() if match else None

# Function to extract contact info (email and phone)
def extract_contact_info(text):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    phone_pattern = r"\(?\+?[0-9]*\)?[-.\s]?[0-9]+[-.\s]?[0-9]+[-.\s]?[0-9]+"
    
    email = re.findall(email_pattern, text)
    phone = re.findall(phone_pattern, text)
    
    return email, phone

# Function to extract skills from the resume (basic example)
def extract_skills(text):
    skills_keywords = ["Python", "Java", "C++", "JavaScript", "SQL", "HTML", "CSS", "Machine Learning", "Django", "Flask"]
    skills_found = [skill for skill in skills_keywords if skill.lower() in text.lower()]
    return skills_found

# Function to extract experience (basic extraction based on some keywords)
def extract_experience(text):
    experience_pattern = r"(?i)(experience|work\s+experience|professional\s+experience).*?(?=\n\n|\Z)"
    experience_section = re.search(experience_pattern, text, re.DOTALL)
    return experience_section.group() if experience_section else "Experience section not found."

# Main function to parse the resume and extract details
def parse_resume(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    
    # Extract details
    name = extract_name(text)
    email, phone = extract_contact_info(text)
    skills = extract_skills(text)
    experience = extract_experience(text)
    
    # Display results
    print("Name:", name if name else "Not found")
    print("Email:", email if email else "Not found")
    print("Phone:", phone if phone else "Not found")
    print("Skills:", skills if skills else "Not found")
    print("Experience:", experience if experience else "Not found")

# Example usage
if __name__ == "__main__":
    pdf_path = 'resume.pdf'  # Change this to your PDF resume file
    parse_resume(pdf_path)
