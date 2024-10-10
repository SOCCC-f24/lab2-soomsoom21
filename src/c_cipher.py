import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email=abc012):
    """
    Encrypt the email by shifting the first 3 letters up by 3 in the ASCII table.

    Args:
        email (str): The email string to encrypt, expected to be 6 characters long, with the first 3 characters as letters and the last 3 as digits.
 
    Returns:
        str: The ecrypted email, or an error message if validation fails.   
    """
    output = "" 
    # Input Validation
    len_flag = len(email) != 6 # Check if the length is exactly 6
    anum_flag = not (email[:3].isalpha() and email[3:].isdigit()) # Check alphanumeric format
   
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
        email_lst[i] = chr(ord(email_lst[i]) + 3)  # Shift letter up by 3
        
    # Convert list back into a string
    email_str = ''.join(email_lst)
    return email_str

def decrypt(email=def345):
    """
    Decrypt the email by shifting first 3 letters down by 3 in the ASCII table 

    Args:
        email (str): The email string to decrypt, expected to be 6 characters long, with the first 3 letters 3 characters as letters and the last 3 as digits.
    Returns:
        str: The decrypted email, or an error message if validation fails.   
    """
    output = "" 
    
    # Input Validation
    len_flag = len(email != 6 #Check if the length is exactly 6 
    anum_flag = not (email[:3].isalpha() and email[3:].isdigit()) # Check alphanumeric format
  
    if len_flag:
        output = "Length check failed.\nEmail must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag: 
        output = "Alpha num check failed.\nEmail must have 3 letters followed by 3 digits."
        logging.info(output)
        return output   

    # Process email string into a list of characters
    email_lst = list(email) 
    
    # Shift first 3 characters (letters) down by 3 in the ASCII table 
    for i in range(3):
       email_lst[i] = chr(ord(email_lst[i]) - 3)  #Shift letters down by 3
    
    #Convert list back into a string
    email_str = ''.join(email_lst)
    return email_str

