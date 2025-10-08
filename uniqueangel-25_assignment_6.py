# uniqueangel-25_assignment_6.py 
# Student: Angel Drake 
# Assignment 6: Contact Information Formatter 
# Demonstrates mastery of string methods for data cleaning and formatting

def main():
  print("Enter contact information (format: name|phone|email|address):")
  contacts = [] 

  while True:
    line = input()
    if line.strip().upper() == "DONE":
      break
    if line.strip() == "":
      continue
    contacts.append(line) 

  print("\n=== CONTACT DIRECTORY ===\n")

  for i, contact in enumerate(contacts,start = 1):
    name, phone, email, address = contact.split('|') 

    print(f"CONTACT {i}: ") 
    print(f"Name :    {name.strip()}")
    print(f"Phone :   {phone.strip()}")
    print(f"Email :   {email.strip()}")
    print(f"Address : {address.strip()}")

main()
    
