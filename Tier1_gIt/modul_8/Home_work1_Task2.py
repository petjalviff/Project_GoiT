def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_username_phone(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."

def main():
    contacts = {}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "all":
            print(contacts)
        elif command == "phone":
            for name in args:
                print(name, ":", contacts.get(name))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()