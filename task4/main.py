from phone_bot_handler import add_contact, change_contact, show_phone, show_all_contacts   

def parse_input(user_input: str) -> tuple:  
    """  
    Parses user input into command and arguments.  
    Args:  
        user_input (str): input string from user.  
    Returns:  
        tuple: (command, args)  
    """  
    parts = user_input.strip().split()  
    if not parts:  
        return '', []  
    cmd = parts[0].lower()  
    args = parts[1:]  
    return cmd, args  

def main():  
    """  
    Main loop of the contact assistant.  
    Handles user input and command execution.  
    """  
    contacts = {}  
    print("Welcome to the contact assistant!")  
    print("Type 'help' for commands, 'exit' or 'close' to quit.")  

    while True:  
        user_input = input(">>> ").strip()  
        if not user_input:  
            continue  

        try:  
            command, args = parse_input(user_input)  
        except ValueError  as e:  
            print(f"Value Error: {e}")  
            continue  

        # Process commands  
        if command in ["exit", "close"]:  
            print("Good bye!")  
            break  
        elif command == "hello":  
            print("How can I help you?")  
        elif command == "add":  
            print(add_contact(args, contacts))  
        elif command == "change":  
            print(change_contact(args, contacts))  
        elif command == "phone":  
            print(show_phone(args, contacts))  
        elif command == "all":  
            print(show_all_contacts(contacts))  
        elif command == "help":  
            print(  
                "Commands:\n"  
                "hello - Greet the assistant\n"  
                "add username phone - Add a new contact\n"  
                "change username phone - Change existing contact's phone\n"  
                "phone username - Show contact's phone number\n"  
                "all - Show all contacts\n"  
                "exit or close - Exit the program"  
            )  
        else:  
            print("Unknown command. Please try again.")  

if __name__ == "__main__":  
    main()