import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email="abc012"):
    """
    Encrypt the email by shifting the first 3 letters up by 3 in the ASCII table.

    Args:
        email (str): The email string to encrypt, expected to be 6 characters long, with the first 3 letters as letters and the last 3 as digits.
 
    Returns:
        str: The encrypted email, or an error message if validation fails.   
    """
    output = "" 
    len_flag = len(email) != 6
    anum_flag = not (email[:3].isalpha() and email[3:].isdigit())  # Check alphanumeric format

    if len_flag:
        output = "Length check failed.\nEmail must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:
        output = "Alpha-numeric check failed.\nEmail must have 3 letters followed by 3 digits."
        logging.info(output)
        return output     
        
    # Process email string into a list of characters
    email_lst = list(email)
        
    # Shift first 3 characters (letters) up by 3 in the ASCII table
    for i in range(3):
        email_lst[i] = chr(ord(email_lst[i]) + 3)  # Shift letters up by 3
        
    # Convert list back into a string
    email_str = ''.join(email_lst)
    return email_str

def decrypt(email="def345"):
    """
    Decrypt the email by shifting the first 3 letters down by 3 in the ASCII table.

    Args:
        email (str): The email string to decrypt, expected to be 6 characters long, with the first 3 letters as letters and the last 3 as digits.
 
    Returns:
        str: The decrypted email, or an error message if validation fails.   
    """
    output = "" 
    len_flag = len(email) != 6
    anum_flag = not (email[:3].isalpha() and email[3:].isdigit())  # Check alphanumeric format

    if len_flag:
        output = "Length check failed.\nEmail must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:
        output = "Alpha-numeric check failed.\nEmail must have 3 letters followed by 3 digits."
        logging.info(output)
        return output   

    # Process email string into a list of characters
    email_lst = list(email) 
    
    # Shift first 3 characters (letters) down by 3 in the ASCII table 
    for i in range(3):
       email_lst[i] = chr(ord(email_lst[i]) - 3)  # Shift letters down by 3
    
    # Convert list back into a string
    email_str = ''.join(email_lst)
    return email_str

# Test Cases
logging.info(f"Encrypted 'abc012' -> {encrypt('abc012')}")   # Expected: def345
logging.info(f"Decrypted 'def345' -> {decrypt('def345')}")   # Expected: abc012
logging.info(f"Invalid input 'abcd1234' -> {encrypt('abcd1234')}")  # Expected: error
logging.info(f"Invalid input 'abc1@3' -> {encrypt('abc1@3')}")  # Expected: error
logging.info(f"Empty input -> {encrypt('')}")  # Expected: error

