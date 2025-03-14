# Resume Parser with Flask

This project is a Flask-based web application designed to extract key information from uploaded resumes (PDF format), such as name, email, phone number, skills, degrees, and social media links (GitHub, LinkedIn). The extracted data is then saved into an Excel file, allowing for easy viewing and further processing.

## Features

- Upload multiple PDF resumes.
- Extracts key information from resumes (e.g., name, email, phone number, skills, education).
- Supports dynamic column selection for the Excel output (e.g., you can choose which information to include in the result).
- Downloads the extracted data as an Excel file.
- Displays uploaded resumes and their processed data on a results page.

## Project Structure

```
resume-parser/
│
├── app.py                   # Main Flask application
├── static/                  # Folder for static files (CSS, JavaScript, images)
│   ├── style.css            # Stylesheet for the web pages
│
├── templates/               # Folder for HTML templates
│   ├── index.html           # Homepage with upload form
│   ├── results.html         # Page showing the results and download link
│   ├── select_columns.html  # Page for selecting columns to include in Excel output
│
├── resumes/                 # Folder where uploaded resumes will be stored (PDF files)
├── resume_data.xlsx         # Output file where extracted resume data is saved in Excel format
```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ChitranshGuha/Resume-Extractor.git
    cd Resume-Extractor
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:
    ```bash
    python app.py
    ```

4. Open your browser and go to `http://127.0.0.1:5000/` to use the application.

## Features Explained

### Upload Resumes
- Users can upload one or more PDF resumes via the file input on the homepage (`index.html`).
- The uploaded files are stored in the `resumes/` folder.

### Data Extraction
- After the upload, the application processes the resumes to extract key details:
  - **Name** (from the filename, assumed to be in "first_last.pdf" format)
  - **Email** and **Phone Number**
  - **Skills** (e.g., programming languages, frameworks)
  - **Degrees** (Bachelor’s, Master’s, etc.)
  - **Social Media Links** (GitHub, LinkedIn)

### Excel Output
- The extracted data is saved in an Excel file (`resume_data.xlsx`) in the root project directory.
- The user can select which columns (e.g., Name, Email, Phone) they want to include in the output. The data is filtered accordingly.

### Results Page
- The `results.html` page displays the link to download the generated Excel file.
  
### Static and Template Files
- **static/**: Contains the CSS and JavaScript files for the front-end styling and interactions.
- **templates/**: Contains the HTML templates for the application (index page, results page, etc.).

## Requirements

The following libraries are required to run this application:

- **Flask** - Web framework for Python.
- **openpyxl** - To create and manipulate Excel files.
- **PyPDF2** - To extract text from PDF resumes.
- **Werkzeug** - For secure file handling.
- **re** - Regular expressions for pattern matching.

You can install the dependencies using the following command:
```bash
pip install -r requirements.txt
```

### Dependencies (`requirements.txt`)
```
Flask==2.1.1
openpyxl==3.0.10
PyPDF2==1.26.0
Werkzeug==2.1.1
```

## Usage

1. Open the app in a browser (`http://127.0.0.1:5000/`).
2. Upload your resume(s) (PDF format).
3. After the file is uploaded and processed, select the columns you want to include in the final Excel report.
4. Once the data is saved, you can download the Excel file from the results page.

## Development

1. **Running in Development Mode**:  
   You can run the Flask app in development mode to see any changes you make to the code:
   ```bash
   python app.py
   ```

2. **Static Assets**:  
   - All CSS, JS, and image files should be placed in the `static/` folder.
   - The main stylesheet is located in `static/style.css`.

3. **Templates**:  
   - All HTML files should be placed in the `templates/` folder.
   - `index.html`: Homepage with the resume upload form.
   - `results.html`: Shows the link to download the processed Excel file.
   - `select_columns.html`: Allows users to select which columns to include in the Excel output.

## License

This project is open-source and available under the [MIT License](LICENSE).
