import re

# Open and read the text file
with open("data.txt", "r") as file:
    content = file.read()

# Regular expression to find email addresses
emails = re.findall(
    r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
    content
)

# Save extracted emails to a new file
with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email addresses extracted successfully!")
