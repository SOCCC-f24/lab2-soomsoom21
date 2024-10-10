import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Frame : Encrypt Function - Shifts the first 3 letters of the email up by 3 ASCII positions.
def encrypt(email="abc012"):
    """
    Encrypt the email by shifting the first 3 letters up by 3 in the ASCII table.

    Args:
        email (str): The email string to encrypt, expected to be 6 characters long, with the first 3 characters as letters and the last 3 as digits.
 
    Returns:
        str: The encrypted email, or an error message if validation fails.   
    """
    # Input Validation for length and alphanumeric combination
    if len(email) != 6:
        return "Error: Email must be 6 characters long."
    
    if not (email[:3].isalpha() and email[3:].isdigit())  
        return "Error: Email must have 3 letters followed by 3 digits."
    
    # Process email string into a list of characters
    email_lst = list(email)
        
    # Shift first 3 characters (letters) up by 3 in the ASCII table
    for i in range(3):
        email_lst[i] = chr(ord(email_lst[i]) + 3)  
        
    # Convert list back into a string
    encrypted_email = ''.join(email_lst)
    return encrypted_email

#Frame: Decrypt Function - SHifts the first 3 letters of the email by 3 ASCII positions.
def decrypt(email="def345"):
    """
    Decrypt the email by shifting the first 3 letters down by 3 in the ASCII table.

    Args:
        email (str): The email string to decrypt, expected to be 6 characters long, with the first 3 letters as letters and the last 3 as digits.
    Returns:
        str: The decrypted email, or an error message if validation fails.   
    """
    
    # Input Validation for length and alphanumeric combinations
    len_flag = len(email) != 6: 
    return "Error: Email must be 6 characters long."
    
    if not (email[:3].isalpha() and email[3:].isdigit()):
        return "Error: Email must have 3 letters followed by 3 digits."
    
    # Process the string into a list of characters
    email_lst = list(email) 
    
    # Shift first 3 characters (letters) down by 3 in the ASCII table 
    for i in range(3):
       email_lst[i] = chr(ord(email_lst[i]) - 3)
    
    # Convert list back into a string
   decrypted_email = ''.join(email_lst)
    return decrypted_email


