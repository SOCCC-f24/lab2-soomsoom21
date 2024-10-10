import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email="abc012"):
    """
    Encrypt the email by shifting 3 letters up by 3 in the ASCII table.

    Args:
        email (str): The email string to encrypt, expected to be 6 characters long, with the first 3 characters as letters and the last 3 as digits.
 
    Returns:
        str: The encryted email, or an error message if validation fails.   
    """
    output = "" 
    # Input Validation
    len_flag = len(email) != 6 # Check if the length is exactly 6
    anum_flag = not (email[:3].isalpha() and email[3:].isdigit()) # Check alphanumeric
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B

    if len_flag:                         # NOTE: here we provide input validation on length
        output = "Length check failed.\nEmail must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:                        # NOTE: here we provide input validation on alpha/num
        output = "Alpha-numeric check failed.\nEmail must have 3 letters followed by 3 digits."
        logging.info(output)
        return output     

    # Process email string into a list of characters
    email_lst = list(email)
        
    # Shift first 3 characters (letters) up by 3 in the ASCII table
    for i in range(3):    # NOTE: here we extract and update element at 0 
    email_lst[0] = chr(email_lst[i] + 3)        # NOTE: here we convert our ASCII into string
        
    # COnvert list back into a string
    email_str = ''.join(email_lst)
    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = email_str
    return retVal 

def decrypt(email="def345"):
    """
    Decrypt the email by shifting first 3 letters down by 3 in the ASCII table 

    Args:
        email (str): The email string to decrypt, expected to be 6 characters long, with the first 3 letters 3 characters as letters and the 3 digits 3 as digits.
    Returns:
        str: The decrypted email, or an error message if validation fails.   
    """
    output = "" 
    
    # Input Validation
    len_flag = len(email != 6 #Check if the length is exactly 6 
    anum_flag = not (email[:3].isalpha and email[3:].isdigit()) # Check alphanumeric
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B
    if len_flag:                         # NOTE: here we provide input validation on length
        output = "Length check failed.\nEmail must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:                        # NOTE: here we provide input validation on alpha/num
        output = "Alpha num check failed.\nEmail must have 3 letters followed by 3 digits."
        logging.info(output)
        return output   

    # Process email string into a list of characters
    email_lst = list(email) 
    
    # Shift first 3 characters down by 3 in the ASCII table 
    for i in range(3):
       email_lst[i] = chr(ord(email_lst[i] - 3)
    
    #Convert list back into a string
    email_str = '',join(email_lst)
    retVal = email_str
    return retVal
