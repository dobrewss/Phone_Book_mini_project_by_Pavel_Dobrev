
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
        searched_contact = len(name[::])
        if len(search) == searched_contact:
            print(f"Contact found - {search} - {CONTACT_INFO['Number']} - "
                  f"{CONTACT_INFO['Address']} - {CONTACT_INFO['E-mail']}")
        else:
            print(f"No contacts found.")
            pass
    MAX_CONTACT -= 1
    if MAX_CONTACT == 0:
        print(f"ALL CONTACTS ADDED: \n{contacts}")
        break
