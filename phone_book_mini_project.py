
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

while True:
    question = input("Do you want to search contact? yes/no ")
    if question.lower() == "yes":
        search = input("Search contact: ")
        found_data = []
        for searched_contact in contacts:
            if searched_contact["Name"].lower() == search.lower():
                found_data.append(searched_contact)
                print(f"Contact found: {searched_contact}")
                break
        if searched_contact["Name"].lower() != search.lower():
            print("No contact found.")
            continue
    if question.lower() == "no":
        break
