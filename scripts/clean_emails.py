import sys

# Check if the script was run with the correct number of arguments
if len(sys.argv) != 2:
    print("Usage: python clean_emails.py <filename>")
    sys.exit(1)

# Get the filename from the command-line argument
filename = sys.argv[1]

# Open the email list file
try:
    with open(filename, 'r') as file:
        emails = file.readlines()
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    sys.exit(1)

# Strip whitespace from each email
emails = [email.strip() for email in emails]

# Sort the emails alphabetically
sorted_emails = sorted(emails)

# Detect duplicates and remove them
unique_emails = []
duplicate_emails = set()

for email in sorted_emails:
    if email in unique_emails:
        duplicate_emails.add(email)  # Register duplicate email
    else:
        unique_emails.append(email)  # Add only one instance

# Save the sorted list without duplicates
with open('sorted_emails.txt', 'w') as file:
    for email in unique_emails:
        file.write(email + '\n')

# Save the duplicates in a separate file
with open('duplicate_emails.txt', 'w') as file:
    for email in duplicate_emails:
        file.write(email + '\n')

print(f"Total emails: {len(emails)}")
print(f"Unique emails: {len(unique_emails)}")
print(f"Duplicate emails removed: {len(duplicate_emails)}")
