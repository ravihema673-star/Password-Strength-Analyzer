print("================================")
print("     PASSWORD STRENGTH ANALYZER")
print("================================")

password = input("Enter your password: ")

score = 0
suggestions = []

# Check password length
if len(password) >= 8:
    score += 1
else:
    suggestions.append("Use at least 8 characters.")

# Check uppercase letters
if any(char.isupper() for char in password):
    score += 1
else:
    suggestions.append("Add uppercase letters (A-Z).")

# Check lowercase letters
if any(char.islower() for char in password):
    score += 1
else:
    suggestions.append("Add lowercase letters (a-z).")

# Check numbers
if any(char.isdigit() for char in password):
    score += 1
else:
    suggestions.append("Add numbers (0-9).")

# Check special characters
if any(not char.isalnum() for char in password):
    score += 1
else:
    suggestions.append("Add special characters (@, #, !).")

# Check common passwords
common_passwords = ["password", "12345678", "qwerty123", "admin123"]

print("\n----- ANALYSIS RESULT -----")

if password.lower() in common_passwords:
    print("Password Strength: WEAK")
    print("This is a commonly used password.")

elif score >= 5 and len(password) >= 12:
    print("Password Strength: STRONG")

elif score >= 3:
    print("Password Strength: MEDIUM")

else:
    print("Password Strength: WEAK")

# Display suggestions
if suggestions:
    print("\nSuggestions to improve your password:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("\nGood! Your password meets all basic checks.")

print("\n================================")
print("       ANALYSIS COMPLETED")
print("================================")