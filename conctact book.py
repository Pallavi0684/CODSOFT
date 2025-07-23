contacts = []

# Add a new contact
def add_contact():
    print("\n📞 Add New Contact")
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("✅ Contact added successfully.")

# View all contacts
def view_contacts():
    print("\n📇 Contact List")
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} | 📞 {contact['phone']}")

# Search contact by name or phone
def search_contact():
    keyword = input("\n🔍 Enter name or phone to search: ")
    found = False
    for contact in contacts:
        if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
            print(f"\n✅ Contact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
    if not found:
        print("❌ No contact found.")

# Update a contact
def update_contact():
    name = input("\n✏️ Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Leave blank to keep existing value.")
            new_phone = input(f"New Phone [{contact['phone']}]: ") or contact['phone']
            new_email = input(f"New Email [{contact['email']}]: ") or contact['email']
            new_address = input(f"New Address [{contact['address']}]: ") or contact['address']
            contact['phone'] = new_phone
            contact['email'] = new_email
            contact['address'] = new_address
            print("✅ Contact updated.")
            return
    print("❌ Contact not found.")

# Delete a contact
def delete_contact():
    name = input("\n🗑 Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print("🗑 Contact deleted.")
            return
    print("❌ Contact not found.")

# Main menu
def main():
    while True:
        print("\n====== 📱 CONTACT MANAGER ======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
