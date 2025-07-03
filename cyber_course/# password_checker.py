# password_checker.py 🔐

import re

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score == 5:
        strength = "Very Strong 💪"
    elif score == 4:
        strength = "Strong ✅"
    elif score == 3:
        strength = "Moderate ⚠️"
    elif score == 2:
        strength = "Weak ⚡"
    else:
        strength = "Very Weak ❌"

    return strength

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    result = check_password_strength(pwd)
    print(f"Password Strength: {result}")
