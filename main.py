from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import re

app = FastAPI(
    title="Password Strength Checker API",
    description="Checks password strength using real-world security rules",
    version="1.0"
)


class PasswordRequest(BaseModel):
    password: str


class PasswordChecker:

    def __init__(self, password: str):
        self.password = password

    def calculate_score(self):
        score = 0

        if len(self.password) >= 8:
            score += 1

        if len(self.password) >= 12:
            score += 1

        if re.search(r"[A-Z]", self.password):
            score += 1

        if re.search(r"[a-z]", self.password):
            score += 1

        if re.search(r"\d", self.password):
            score += 1

        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", self.password):
            score += 1

        return score

    def strength(self):
        score = self.calculate_score()

        if score <= 2:
            return "Weak"

        elif score <= 4:
            return "Medium"

        else:
            return "Strong"

    def feedback(self):
        suggestions = []

        if len(self.password) < 8:
            suggestions.append(
                "Password should be at least 8 characters long."
            )

        if not re.search(r"[A-Z]", self.password):
            suggestions.append(
                "Add at least one uppercase letter."
            )

        if not re.search(r"[a-z]", self.password):
            suggestions.append(
                "Add at least one lowercase letter."
            )

        if not re.search(r"\d", self.password):
            suggestions.append(
                "Add at least one number."
            )

        if not re.search(
            r"[!@#$%^&*(),.?\":{}|<>]",
            self.password
        ):
            suggestions.append(
                "Add at least one special character."
            )

        return suggestions


@app.get("/")
def home():
    return {
        "message": "Password Strength Checker API"
    }


@app.post("/check-password")
def check_password(data: PasswordRequest):

    password = data.password

    if not password:
        raise HTTPException(
            status_code=400,
            detail="Password cannot be empty."
        )

    checker = PasswordChecker(password)

    return {
        "password_length": len(password),
        "strength": checker.strength(),
        "score": checker.calculate_score(),
        "feedback": checker.feedback()
    }
