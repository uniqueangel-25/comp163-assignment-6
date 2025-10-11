# uniqueangel-25_assignment_6.py 
# Student: Angel Drake 
# Assignment 6: Contact Information Formatter 
# Demonstrates mastery of string methods for data cleaning and formatting

contacts = [] 

while True:
    line = input()
    if line.strip().upper() == "DONE":
      break
    if line.strip() == "":
      continue
    contacts.append(line)

print("Enter contact information (format: name|phone|email|address):")
print("\n=== CONTACT DIRECTORY ===\n")
    
