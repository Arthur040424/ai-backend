import json

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def address(self):
        return f"Hello, here are my contact details: {self.name}, {self.phone}, {self.email}."

arthur = Contact("Arthur", "1122334455", "arthur@example.com")
print(arthur.address())

def newContact(name, phone, email):
    try:
        contacts = {
            "name": name,
            "phone": phone,
            "email": email
        }

        with open("phone_book.json", "w") as f:
            json.dump(contacts, f)

        with open("phone_book.json", "r") as f:
            loaded_contacts = json.load(f)
        print(loaded_contacts)
        return contacts
    except KeyError:
        print("Error: Missing contact information.")

def findContact(name, phone, email):
    try:
        with open("phone_book.json", "r") as f:
            loaded_contacts = json.load(f)
            if loaded_contacts["name"] == name and loaded_contacts["email"] == email and loaded_contacts["phone"] == phone:
                return f"Contact found: {loaded_contacts['name']}, {loaded_contacts['phone']}, {loaded_contacts['email']}."
            else:
                return f"Contact not found"
    except KeyError:
      print("Error: MIssing Contact Information")