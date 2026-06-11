# Password Strength Checker API

## Overview

The Password Strength Checker API is a web application built using FastAPI and Object-Oriented Programming (OOP) principles. It evaluates the strength of a user's password based on common cybersecurity best practices and returns a score along with feedback for improvement.

This project demonstrates the use of:

* FastAPI for backend development
* OOP design principles
* RESTful API development
* Input validation using Pydantic
* Unit testing with Pytest

---

## Features

* Password strength evaluation
* Checks password length
* Detects uppercase letters
* Detects lowercase letters
* Detects numbers
* Detects special characters
* Returns strength score and feedback
* FastAPI interactive documentation
* Automated testing with Pytest

---

## Technologies Used

* Python 3
* FastAPI
* Pydantic
* Uvicorn
* Pytest

---

## Project Structure

```text
password-strength-checker/
│
├── main.py
├── test_main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/password-strength-checker.git
```

Navigate to the project folder:

```bash
cd password-strength-checker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## API Endpoint

### Check Password Strength

**Endpoint**

```http
POST /check-password
```

**Request Body**

```json
{
    "password": "StrongPassword123!"
}
```

**Example Response**

```json
{
    "score": 5,
    "strength": "Strong",
    "feedback": "Your password is secure."
}
```

---

## Password Evaluation Criteria

The password is evaluated based on:

1. Minimum length requirement
2. Presence of uppercase letters
3. Presence of lowercase letters
4. Presence of numeric digits
5. Presence of special characters

A higher score indicates a stronger password.

---

## Testing

Run unit tests using Pytest:

```bash
pytest
```

Example output:

```text
================== test session starts ==================
collected 5 items

test_main.py .....                           [100%]

================== 5 passed ==================
```

---

## Learning Objectives

This project was developed to demonstrate:

* REST API development using FastAPI
* Object-Oriented Programming concepts
* Input validation
* Software testing practices
* Secure password validation techniques
* Version control using Git and GitHub

---

## Future Improvements

* Password breach detection
* Password entropy calculation
* User authentication system
* Frontend user interface
* Database integration
* Password history checks

---

## Author

Created as part of a software development and API design project using Python, FastAPI, and Pytest.

