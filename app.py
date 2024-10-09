from flask import Flask, render_template, request, redirect, url_for, send_file
import os
from werkzeug.utils import secure_filename
import sdl

app = Flask(__name__)

UPLOAD_FOLDER = r'C:\Users\chitr\Desktop\resumes_sdl\resumes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

EXCEL_FILE_PATH = r'C:\Users\chitr\Desktop\resumes_sdl\resume_data.xlsx'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'files' not in request.files:
        return redirect(request.url)

    files = request.files.getlist('files')
    if not files or all(f.filename == '' for f in files):
        return redirect(url_for('index'))

    # Clear the UPLOAD_FOLDER before saving new files
    for old_file in os.listdir(app.config['UPLOAD_FOLDER']):
        old_file_path = os.path.join(app.config['UPLOAD_FOLDER'], old_file)
        if os.path.isfile(old_file_path):
            os.remove(old_file_path)  # Remove old file

    # Save uploaded files
    for file in files:
        if file and file.filename:
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)

    # Process resumes in the upload folder
    resume_data = sdl.process_resumes(app.config['UPLOAD_FOLDER'])
    
    # Save the extracted data to Excel
    sdl.save_to_excel(resume_data, EXCEL_FILE_PATH)

    return redirect(url_for('results'))


@app.route('/results')
def results():
    if os.path.exists(EXCEL_FILE_PATH):
        return render_template('results.html', excel_file=url_for('download_excel'))
    else:
        return "No data found. Please upload resumes and try again."

@app.route('/download_excel')
def download_excel():
    return send_file(EXCEL_FILE_PATH, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
