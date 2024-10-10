import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email="abc012"):
    """
    Encrypt the email by shifting the first 3 letters up by 3 in the ASCII table.

    Args:
        email (str): The email string to encrypt, expected to be 6 characters long, 
                     with the first 3 characters as letters and the last 3 as digits.
 
    Returns:
        str: The encrypted email, or an error message if validation fails.
    """
    output = "" 
    # Input Validation
    len_flag = len(email) != 6  # Check if the length is exactly 6
    anum_flag = not (email[:3].isalpha() and email[3:].isdigit())  # Check alphanumeric

    if len_flag:  # Length validation
        output = "Length check failed.\nEmail must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:  # Alphanumeric validation
        output = "Alpha-numeric check failed.\nEmail must have 3 letters followed by 3 digits."
        logging.info(output)
        return output     

    # Process email string into a list of characters
    email_lst = list(email)
        
    # Shift first 3 characters (letters) up by 3 in the ASCII table
    for i in range(3):
        email_lst[i] = chr(ord(email_lst[i]) + 3)  # Corrected: use ord to get ASCII value and shift

    # Convert list back into a string
    email_str = ''.join(email_lst)  # Fixed: use join correctly
    retVal = email_str
    return retVal 

def decrypt(email="def345"):
    """
    Decrypt the email by shifting the first 3 letters down by 3 in the ASCII table.

    Args:
        email (str): The email string to decrypt, expected to be 6 characters long, 
                     with the first 3 characters as letters and the last 3 as digits.

    Returns:
        str: The decrypted email, or an error message if validation fails.
    """
    output = "" 
    
    # Input Validation
    len_flag = len(email) != 6  # Fixed parentheses
    anum_flag = not (email[:3].isalpha() and email[3:].isdigit())  # Check alphanumeric

    if len_flag:  # Length validation
        output = "Length check failed.\nEmail must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:  # Alphanumeric validation
        output = "Alpha-numeric check failed.\nEmail must have 3 letters followed by 3 digits."
        logging.info(output)
        return output   

    # Process email string into a list of characters
    email_lst = list(email) 
    
    # Shift first 3 characters (letters) down by 3 in the ASCII table 
    for i in range(3):
        email_lst[i] = chr(ord(email_lst[i]) - 3)  # Fixed: use ord to get ASCII value and shift

    # Convert list back into a string
    email_str = ''.join(email_lst)  # Fixed: use join correctly
    retVal = email_str
    return retVal

def test_encrypt():
    print(encrypt("abc012"))  # Expected: "def012"
    print(encrypt("def345"))  # Expected: "Invalid input length"
    print(encrypt("abc12a"))  # Expected: "Invalid alpha-numeric format"

def test_decrypt():
    print(decrypt("def345"))  # Expected: "abc345"
    print(decrypt("abc012"))  # Expected: "Invalid input length"
    print(decrypt("def34a"))  # Expected: "Invalid alpha-numeric format"

test_encrypt()
test_decrypt()
