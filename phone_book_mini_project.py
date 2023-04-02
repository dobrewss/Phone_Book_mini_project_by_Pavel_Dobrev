
MAX_CONTACT = int(input("Enter the amount of contacts you want to add "))
contacts = []


while True:
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

