
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please.\nType 'help' to see available commands."
        except IndexError:
            return "Invalid number of arguments.\nType 'help' to see available commands."
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact_command(args, contacts):
    username, phone = args
    if contacts.get(username):
        return "Contact already exists."
    contacts[username] = phone
    return "Contact added."


@input_error
def change_contact_command(args, contacts):
    username, phone = args
    if username in contacts:
        contacts[username] = phone
        return "Contact changed."
    return "Contact not found."


@input_error
def phone_command(args, contacts):
    username = args[0]
    if username in contacts:
        return f"Phone number: {contacts[username]}"
    return "Contact not found."


def all_command(contacts):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)
            match command:
                case "close" | "exit":
                    print("Good bye!")
                    break
                case "hello":
                    print("How can I help you?")
                case "add":
                    print(add_contact_command(args, contacts))
                case "change":
                    print(change_contact_command(args, contacts))
                case 'phone':
                    print(phone_command(args, contacts))
                case 'all':
                    print(all_command(contacts))
                case 'help':
                    print("""
                    Available commands:
                        hello - Greet the bot.
                        add <username> <phone> - Add a new contact.
                        change <username> <phone> - Change an existing contact.
                        phone <username> - Get phone number of a contact.
                        all - List all contacts.
                    """)
                case _:
                    print("Invalid command.")
        except KeyboardInterrupt:
            print("Good bye!")
            break


if __name__ == "__main__":
    main()
