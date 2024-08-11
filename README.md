# Data Extractor

This project is a Django-based web application that allows users to upload Excel or CSV files, processes the data to generate a summary report, and sends the summary via email to specified recipients. The project is deployed on [Render](https://render.com/).

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Running the Project Locally](#running-the-project-locally)
- [Deploying on Render](#deploying-on-render)
- [Usage](#usage)
- [License](#license)

## Features

- Upload Excel (`.xlsx`) or CSV (`.csv`) files.
- Process the uploaded file to generate a summary report based on customer state, pin, and DPD.
- Send the summary report via email to specified recipients with CC options.
- Deployable on Render with `gunicorn` as the WSGI server.

## Project Structure

```
data-extractor/
│
├── DevTest/ # Main Django project directory
│ ├── settings.py # Project settings
│ ├── urls.py # URL routing
│ ├── wsgi.py # WSGI application
│ └── ...
│
├── fileupload/ # Django app for handling file uploads and processing
│ ├── views.py # Main view logic
│ ├── forms.py # Forms for handling file upload
│ ├── templates/
│ │ ├── upload.html # Template for file upload page
│ │ ├── summary.html # Template for displaying summary report
│ │ └── email_summary.html # Template for summary report email
│ └── ...
│
├── .env # Environment variables (not tracked by Git)
├── .gitignore # Git ignore file
├── manage.py # Django management script
├── Procfile # Procfile for deploying on Render
├── README.md # Project documentation
├── requirements.txt # Python dependencies
└── 
```


## Installation

### Prerequisites

- Python 3.10+
- Git

### Clone the Repository

```bash
git clone https://github.com/kumarshivesh/data-extractor.git
cd data-extractor
```

### Create and Activate a Virtual Environment

```
python -m venv .venv
source .venv/bin/activate   # On Windows use `.venv\Scripts\activate`
```

### Install Dependencies

```
pip install -r requirements.txt
```

## Environment Variables

Create a .env file in the root directory of the project and add the following variables:

```
# Email configuration
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password

# Django configuration
ALLOWED_HOSTS=data-extractor-l1c7.onrender.com,localhost,127.0.0.1

# Recipients
RECIPIENT_LIST=recipient@example.com
CC_LIST=cc_recipient@example.com
```

## Running the Project Locally

#### 1. Apply database migrations:

```
python manage.py migrate
```

#### 2. Start the development server:
```
python manage.py runserver
```

#### 3. Open your web browser and go to 

http://127.0.0.1:8000/fileupload/upload/

## Deploying on Render

This project is configured to deploy on `Render`. Follow these steps:

1. Sign in to Render and create a new Web Service connected to your GitHub repository.
2. Set the environment variables on Render as specified above.
3. Deploy the project using the provided Procfile.

### Build Command

Render will automatically install dependencies from requirements.txt.

### Start Command

The start command specified in Procfile is:

```
gunicorn DevTest.wsgi --log-file -
```

Replace DevTest with your Django project name if different.

## Usage

1. Navigate to the upload page.
2. Upload an Excel or CSV file.
3. The summary report will be generated and displayed on the website.
4. The summary report will also be emailed to the specified recipients.

## License

This project is licensed under the MIT License. 



