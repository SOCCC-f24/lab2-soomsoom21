"""

Name: Sophia Weinert
Course: CSC 138
Date: 10/24/2024
Class Section: EG
"""

import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email="abc012"):
    """Encrypts an email address by shifting ASCII values of its characters.
    
    Args:
        email (str): The email string to encrypt. Default is 'abc012'.
    
    Returns:
        str: The encrypted email string.
    """
    output = ""
    
    # Validate length
    if len(email) != 6:
        output += "Length check failed. Must be 6 characters.\n"
        logging.info(output)
        return None  # Early return if validation fails

    # Validate alphanumeric combination
    if not (email[:3].isalpha() and email[3:].isdigit()):
        output += "Email must have 3 letters followed by 3 digits.\n"
        logging.info(output)
        return None  # Early return if validation fails

    # Encrypt the email by shifting ASCII values up by 3
    email_lst = list(email)  # Convert to a list for easier manipulation
    for i in range(len(email_lst)):
        new_ascii = ord(email_lst[i]) + 3
        email_lst[i] = chr(new_ascii)
    
    encrypted_email = ''.join(email_lst)  # Join the list back into a string
    logging.info(f"Encrypted email: {encrypted_email}")
    return encrypted_email  # Return the encrypted email

def decrypt(email="def345"):
    """Decrypts an email address by shifting ASCII values of its characters down.
    
    Args:
        email (str): The email string to decrypt. Default is 'def345'.
    
    Returns:
        str: The decrypted email string.
    """
    output = ""
    
    # Validate length
    if len(email) != 6:
        output += "Length check failed. Must be 6 characters.\n"
        logging.info(output)
        return None  # Early return if validation fails

    # Validate alphanumeric combination
    if not (email[:3].isalpha() and email[3:].isdigit()):
        output += "Email must have 3 letters followed by 3 digits.\n"
        logging.info(output)
        return None  # Early return if validation fails

    # Decrypt the email by shifting ASCII values down by 3
    email_lst = list(email)  # Convert to a list for easier manipulation
    for i in range(len(email_lst)):
        new_ascii = ord(email_lst[i]) - 3
        email_lst[i] = chr(new_ascii)
    
    decrypted_email = ''.join(email_lst)  # Join the list back into a string
    logging.info(f"Decrypted email: {decrypted_email}")
    return decrypted_email  # Return the decrypted email

# Example usage
if __name__ == "__main__":
    encrypted = encrypt("abc012")
    print("Encrypted:", encrypted)

    decrypted = decrypt("def345")
    print("Decrypted:", decrypted)
