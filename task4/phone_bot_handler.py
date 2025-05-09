def add_contact(args: list, contacts: dict) -> str:  
    """  
    Adds a new contact or updates an existing one.  
    Args:  
        args (list): [name, phone]  
        contacts (dict): Dictionary of contacts.  
    Returns:  
        str: Success or error message.  
    """  
    if len(args) != 2:  
        return "Error: 'add' command must include exactly two arguments: name and phone."  
    name, phone = args  
    contacts[name] = phone  
    return f"Contact '{name}' has been added or updated."  

def change_contact(args: list, contacts: dict) -> str:  
    """  
    Changes existing contact's phone number.  
    Args:  
        args (list): [name, new_phone]  
        contacts (dict): Dictionary of contacts.  
    Returns:  
        str: Success message or error if contact not found.  
    """  
    if len(args) != 2:  
        return "Error: 'change' command must include exactly two arguments: name and new phone."  
    name, phone = args  
    if name not in contacts:  
        return f"Contact '{name}' not found."  
    contacts[name] = phone  
    return f"Phone number for '{name}' has been successfully changed."  

def show_phone(args: list, contacts: dict) -> str:  
    """  
    Shows phone number for a contact.  
    Args:  
        args (list): [name]  
        contacts (dict): Dictionary of contacts.  
    Returns:  
        str: Phone number or not found message.  
    """  
    if len(args) != 1:  
        return "Error: 'phone' command must include exactly one contact name."  
    name = args[0]  
    if name in contacts:  
        return f"Phone number for '{name}': {contacts[name]}"  
    else:  
        return f"Contact '{name}' not found."  

def show_all_contacts(contacts: dict) -> str:  
    """  
    Returns a string with all contacts.  
    Args:  
        contacts (dict): Dictionary of contacts.  
    Returns:  
        str: List of all contacts.  
    """  
    if not contacts:  
        return "No contacts stored."  
    result_lines = ["All contacts:"]  
    for name, phone in contacts.items():  
        result_lines.append(f"{name}: {phone}")  
    return "\n".join(result_lines)  