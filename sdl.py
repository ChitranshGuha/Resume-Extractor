#github link read
#feeature to determine ki kon kon se column chahiye
#Orr columns add karo
import os
import re
import openpyxl
from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_information(text):
    email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email_match = re.search(email_regex, text)
    email = email_match.group() if email_match else "N/A"
    
    phone = re.search(r'(\b\d{10}\b|\(\d{3}\)\s*\d{3}-\d{4}|\d{3}-\d{3}-\d{4})', text)
    phone_number = phone.group() if phone else "N/A"
    email_id = email if email else "N/A"

    # Extract Bachelor and Master Degrees
    bachelor_degrees = re.findall(r'\b(UG|BBA|B\.Tech|BS|BSc|B\.Sc|Bachelor of [a-zA-Z]+)\b', text, re.IGNORECASE)
    master_degrees = re.findall(r'\b(PG|MBA|M\.Tech|MS|MSc|M\.Sc|Master of [a-zA-Z]+)\b', text, re.IGNORECASE)
    bachelor_degree = ', '.join(bachelor_degrees) if bachelor_degrees else "N/A"
    master_degree = ', '.join(master_degrees) if master_degrees else "N/A"
    
    # Extract Skills
    skills_keywords = ['full stack developer', 'python', 'javascript', 'java', 'sql', 'react', 'angular', 'node.js']
    found_skills = [skill for skill in skills_keywords if skill.lower() in text.lower()]
    skills = ', '.join(found_skills) if found_skills else "N/A"
    
    # Extract GitHub and LinkedIn Links
    # print(repr(text))
    cleaned_text = ' '.join(text.split())

    github_link = re.search(r'(https?://[^\s]+github\.com/[^\s]+)', cleaned_text, re.IGNORECASE)
    linkedin_link = re.search(r'(https?://[^\s]+linkedin\.com/in/[^\s]+)', cleaned_text, re.IGNORECASE)
    github = github_link.group() if github_link else "N/A"
    linkedin = linkedin_link.group() if linkedin_link else "N/A"
    
    return phone_number, email_id, bachelor_degree, master_degree, skills, github, linkedin

def process_resumes(folder_path):
    resume_data = []
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            first_name, last_name = filename.split('.')[0].split('_')
            file_path = os.path.join(folder_path, filename)
            text = extract_text_from_pdf(file_path)
            phone_number, email_id, bachelor_degree, master_degree, skills, github, linkedin = extract_information(text)
            resume_data.append((first_name, last_name, phone_number, email_id, bachelor_degree, master_degree, skills, github, linkedin))
    
    # Debugging: Print resume data before saving to Excel
    print("Resume data before saving to Excel:")
    for data in resume_data:
        print(data)  # Print each row of data to check the structure

    return resume_data

# def save_to_excel(resume_data, excel_file):
#     wb = openpyxl.Workbook()
#     ws = wb.active
#     # Append the headers
#     ws.append(["First Name", "Last Name", "Phone Number", "Email ID", "Bachelor Degree", "Master Degree", "Skills", "GitHub Link", "LinkedIn Link"])
    
#     # Append each row of data
#     for data in resume_data:
#         print(f"Appending data to Excel: {data}")  # Debugging: Check each row before it's written
#         ws.append(data)
    
#     # Ensure folder exists before saving
#     os.makedirs(os.path.dirname(excel_file), exist_ok=True)
#     wb.save(excel_file)
#     print(f"Excel file saved at: {excel_file}")

def save_to_excel(resume_data, excel_file):
    wb = openpyxl.Workbook()
    ws = wb.active
    # Append the headers
    headers = ["First Name", "Last Name", "Phone Number", "Email ID", "Bachelor Degree", "Master Degree", "Skills", "GitHub Link", "LinkedIn Link"]
    ws.append(headers)
    
    # Append each row of data
    for data in resume_data:
        ws.append(list(data))  # Convert the tuple to a list before appending
    
    # Ensure folder exists before saving
    os.makedirs(os.path.dirname(excel_file), exist_ok=True)
    wb.save(excel_file)

def main():
    folder_path = r"C:\Users\chitr\Desktop\resumes_sdl"
    excel_file = r"C:\Users\chitr\Desktop\resumes_sdl\resume_data.xlsx" 

    resume_data = process_resumes(folder_path)
    save_to_excel(resume_data, excel_file)

    print("Data has been successfully extracted and saved to Excel.")

if __name__ == "__main__":
    main()