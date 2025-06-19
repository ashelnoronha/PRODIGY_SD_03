import json
import os
class ContactManager:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()
    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return[]
    def save_contacts(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.contacts, file, indent=4)
        except IOError:
            print("Error saving contacts")
    def add_contact(self, name, phone, email):
        contact ={
            "name" : name,
            "phone" : phone,
            "email" : email
        }
        self.contacts.append(contact)
        self.save_contacts()
        print(f"Contact '{name}' added successfully!")
    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        
        print("\n--- Contact List ---")
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. Name: {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}\n")
    
    def edit_contact(self, index, name=None, phone=None, email=None):
        if index < 0 or index >= len(self.contacts):
            print("Invalid contact number.")
            return
        
        contact = self.contacts[index]
        if name:
            contact['name'] = name
        if phone:
            contact['phone'] = phone
        if email:
            contact['email'] = email
        
        self.save_contacts()
        print("Contact updated successfully!")
    
    def delete_contact(self, index):
        if index < 0 or index >= len(self.contacts):
            print("Invalid contact number.")
            return
        
        deleted_name = self.contacts[index]['name']
        del self.contacts[index]
        self.save_contacts()
        print(f"Contact '{deleted_name}' deleted successfully!")

def main():
    manager = ContactManager()
    
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            print("\nAdd New Contact")
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            manager.add_contact(name, phone, email)
        
        elif choice == '2':
            manager.view_contacts()
        
        elif choice == '3':
            manager.view_contacts()
            if manager.contacts:
                try:
                    index = int(input("Enter the number of the contact to edit: ")) - 1
                    print("Leave blank to keep current value")
                    name = input(f"Enter new name [{manager.contacts[index]['name']}]: ") or None
                    phone = input(f"Enter new phone [{manager.contacts[index]['phone']}]: ") or None
                    email = input(f"Enter new email [{manager.contacts[index]['email']}]: ") or None
                    manager.edit_contact(index, name, phone, email)
                except ValueError:
                    print("Please enter a valid number.")
        
        elif choice == '4':
            manager.view_contacts()
            if manager.contacts:
                try:
                    index = int(input("Enter the number of the contact to delete: ")) - 1
                    confirm = input(f"Are you sure you want to delete {manager.contacts[index]['name']}? (y/n): ")
                    if confirm.lower() == 'y':
                        manager.delete_contact(index)
                except ValueError:
                    print("Please enter a valid number.")
        
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")
main()