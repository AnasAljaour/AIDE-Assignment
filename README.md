# AIDE-Assignment
# Seintiment Analysis API
This project implements a sentiment analysis API using Flask and Express.js. The Flask API hosts a sentiment analysis model, while the Express.js server acts as an intermediary between users and the machine learning model.

This project consists of three main components:
1. **Flask API**: Hosts a sentiment analysis model using the Vader Sentiment Analysis tool.
2. **Express.js Server**: Acts as a backend service, exposing an endpoint to interact with the Flask API.
3. **Frontend Server**: A Streamlit-based web app interface for users to interact with the sentiment analysis model.

---

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
   - [Flask API](#flask-api)
   - [Express.js Server](#expressjs-server)
   - [Frontend Server](#frontend-server)
4. [API Endpoints](#api-endpoints)
5. [How it Works](#how-it-works)

---

## Features
- **Sentiment Analysis**: Classifies text as positive, negative, or neutral using the Vader Sentiment Analysis model.
- **RESTful APIs**: Flask and Express.js expose endpoints for sentiment analysis.
- **Streamlit Frontend Server**:  A ready-to-use web app interface that takes text as input and returns the sentiment of the text.
---

## Technologies Used
- **Flask**: Python web framework for hosting the sentiment analysis model.
- **VaderSentiment**: Python library for sentiment analysis.
- **Express.js**: Node.js framework for the backend server.
- **Axios**: For making HTTP requests from the frontend to the backend.
- **Streamlit**: For building the frontend server.

---

## Setup Instructions

### Flask API
1. Navigate to the `flask-api` directory:
   ```bash
   cd flask-api
2. Start the Flask server:
   ```bash
   flask -app app.py run

### Express.js Server

1. Navigate to the express-server directory:
   ```bash
   cd Express-Server
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the Express server:
   ```bash
   node index.js
   ```
   The server will be available at http://localhost:3000

### Frontend Server
1. Navigate to the Frontend-Server directory:
   ```bash
   cd Fronend-Server
2. Start the Streamlit server:
   ```bash
   streamlit run app.py

---

## API Endpoints

### Flask API : POST /predict:
- **Request Body**:
  ```json
  {
    "text": "Who needs version control?"
  }
  ```
- **Response**:
  ```json
  {
    "sentiment": "positive"
  }
  ```

### Express.js Server : POST /analyze-sentiment
- **Request Body**:
  ```json
  {
    "text": "Who needs version control?"
  }
  ```
- **Response**:
  ```json
  {
    "sentiment": "positive"
  }
  ```

---

## How it Works

1. The Streamlit Frontend sends user input to the Express.js Server.

2. The Express.js Server forwards the request to the Flask API.

3. The Flask API processes the text using the Vader Sentiment Analysis model and returns the sentiment.

4. The Express.js Server sends the sentiment back to the Streamlit Frontend, which displays the result to the user.


