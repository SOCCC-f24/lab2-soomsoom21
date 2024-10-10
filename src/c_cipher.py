import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email="abc012"):
    """
    Encrypts the email by shifting the first 3 letters up by 3 ASCII positions.

    Args:
        email (str): The email string to encrypt, expected to be 6 characters long,
                     with the first 3 characters as letters and the last 3 as digits.
 
    Returns:
        str: The encrypted email, or an error message if validation fails.
    """
    # Input validation
    if len(email) != 6:
        return "Email must be 6 characters long."    
    if not (email[:3].isalpha() and email[3:].isdigit()):
        return "Email must have 3 letters followed by 3 digits."
    
    # Process email string into a list of characters
    email_lst = list(email)
    
    # Shift the first 3 characters (letters) up by 3 in the ASCII table
    for i in range(3):
        email_lst[i] = chr(ord(email_lst[i]) + 3)
        
    # Convert the list back into a string
    encrypted_email = ''.join(email_lst)
    
    return encrypted_email

def decrypt(email="def345"):
    """
    Decrypts the email by shifting the first 3 letters down by 3 ASCII positions.

    Args:
        email (str): The email string to decrypt, expected to be 6 characters long,
                     with the first 3 characters as letters and the last 3 as digits.
 
    Returns:
        str: The decrypted email, or an error message if validation fails.
    """
    # Input validation
    if len(email) != 6:
        return "Email must be 6 characters long."
    
    if not (email[:3].isalpha() and email[3:].isdigit()):
        return "Email must have 3 letters followed by 3 digits."
    
    # Process email string into a list of characters
    email_lst = list(email)
    
    # Shift the first 3 characters (letters) down by 3 in the ASCII table
    for i in range(3):
        email_lst[i] = chr(ord(email_lst[i]) - 3)
        
    # Convert the list back into a string
    decrypted_email = ''.join(email_lst)
    
    return decrypted_email

# Example usage
logging.info(f"Encrypted 'abc012' -> {encrypt('abc012')}")   # Expected: def345
logging.info(f"Decrypted 'def345' -> {decrypt('def345')}")   # Expected: abc012

