
MAX_CONTACT = int(input("Enter the amount of contacts you want to add "))
contacts = []


while True:
    print("Please add contact:")
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
    question = input("Do you want to search contact? ")
    if question.lower() == "yes":
        search = input("Search contact: ")
        found_data = []
        for searched_contact in contacts:
            if searched_contact["Name"] == search:
                found_data.append(searched_contact)
                print(f"Contact found: {searched_contact}")
                break
            else:
                continue
    MAX_CONTACT -= 1
    if MAX_CONTACT == 0:
        print(f"ALL CONTACTS ADDED: \n{contacts}")
        break
