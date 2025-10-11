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
    
cleaned_contacts = []

for i, contact in enumerate(contacts,start = 1):
    name, phone, email, address = contact.split('|') 

    name = name.title().replace("  ", "  ")
    n_phone = ""
    for n in phone:
        if n.isdigit():
            n_phone += n
    
    phone = n_phone
    phone = f"({phone[0:3]}) {phone[3:6]}-{phone[6:10]}"

    email = email.lower().strip()
    
    address = address.strip().replace(",", "")
    n_address = address.split()
    f_address = ""
    for word in n_address:
        if len(word) == 2:
            f_address += " " + word.upper()
        else:
            f_address += " "+ word.title()

    address = f_address.replace(" ,", ",").strip()
