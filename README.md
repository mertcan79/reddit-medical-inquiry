# Reddit Medical Inquiry Analyzer

This project utilizes the Google Gemini API to analyze medical inquiries from the Reddit community, extracting symptoms, medications used, and possible diagnoses. The extracted information is presented in a user-friendly dashboard for easy analysis and filtering.

## Features

- **Extraction of Medical Information**: The system extracts relevant medical information, including symptoms, medications, and possible diagnoses, from Reddit posts in the "AskDocs" subreddit.

- **Dashboard Filtering**: The extracted data is presented in a dashboard where users can filter and analyze information based on symptoms, medications, and other relevant factors.

- **User Interface Components**: The UI includes components for displaying medical inquiry details, symptoms, medications, and possible diagnoses. Users can interact with badges to filter and analyze data.

## Tech stack
- FastAPI
- Google Gemini 
- React
- Docker
- Python

## Setup

1. **Clone the Repository**: Clone this repository to your local machine.

```bash
   git clone https://github.com/mertcan79/reddit-medical-inquiry.git
```
Install Dependencies: Navigate to the project directory and install the necessary dependencies.

```bash
cd reddit-medical-inquiry
npm install
```
Configure API Key: Get your Google Gemini API key and replace YOUR_API_KEY in the configuration file.

Open the .env file and replace keys with your actual Reddit and Google API keys.

Run the backend
```bash
pip install -r requirements.txt
uvicorn app.main:app --port 5002 --reload
```

Run the Application: Start the development server.

```bash
npm start
```
The application will be accessible at http://localhost:3000.