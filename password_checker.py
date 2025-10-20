import re

def check_password_strength(password):
    strength = 0
    remarks = ""
    
    # Conditions
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[@$!%*?&]", password):
        strength += 1

    # Rating
    if strength <= 2:
        remarks = "Weak 🔴"
    elif strength == 3 or strength == 4:
        remarks = "Moderate 🟡"
    else:
        remarks = "Strong 🟢"

    return remarks


# --- Main ---
if __name__ == "__main__":
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(f"Your password strength is: {result}")
