
MAX_CONTACT = int(input("Enter the amount of contacts you want to add "))
contacts = []


for i in range(MAX_CONTACT):
    print(f"\nPlease add contact {i + 1}:")
    name = input()
    number = input()
    address = input()
    email = input()
    CONTACT_INFO = {
        "Name": name,
        'Number': number,
        'Address': address,
        'E-mail': email
    }
    contacts.append(CONTACT_INFO)
    MAX_CONTACT -= 1
    if MAX_CONTACT == 0:
        print(f"ALL CONTACTS ADDED: \n{contacts}")
        break

while True:
    question = input("Do you want to search contact? yes/no ")
    if question.lower() == "yes":
        search = input("Search contact: ")
        found_data = []
        FORCE_BREAK = False
        for searched_contact in contacts:
            if searched_contact["Name"].lower() == search.lower():
                FORCE_BREAK = True
                found_data.append(searched_contact)
                print(f"Contact found: {searched_contact}")
                break
            if FORCE_BREAK:
                continue
    if question.lower() == "no":
        break
