"""

Name: Sophia Weinert
Course: CSC 138
Date: 10/24/2024
Class Section: EG
"""

import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email="abc012"):
    """
    TODO: What is the objective? 
        This should take an email address and encrypt it using a
        ceasar cipher.

    Args:
        email (string)

    Returns:
        encrpyted email (string)  
    """
    
    output = "" 
    len_flag = len(email) != 6
    
    A = email[:3] # (check first half)
    B = email[3:] # (check second half)

    anum_flag = not (A.isalpha() and B.isdecimal())

    # provide input validation on len
    if len_flag:
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output   

    # provide input validation of alpha/num
    if anum_flag:
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output     

    # unpack string email into list of characters
    email_lst = [*email]

    for i in range(len(email_lst)):
        new_ascii = ord(email_lst[i]) + 3
        email_lst[i] = chr(new_ascii)

    # convert list into a string
    email_str = "".join(email_lst)

    retVal = email_str
    return retVal 

def decrypt(email="def345"):
    """
    TODO: What is the objective? 
        Reverse the cipher. This function should take an encrypted
        email and return it to the original state.

    Args:
        encrpyted email (string)

    Returns:
        decrypted email (string)  
    """
    
    # input validation
    output = "" 
    len_flag = len(email) != 6
    
    A = email[:3] # (check first half)
    B = email[3:] # (check second half)
    anum_flag = not (A.isalpha() and B.isdecimal())

    # provide input validation on len
    if len_flag:
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output    

    # provide input validation of alpha/num
    if anum_flag:
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output   

    # unpack string email into list of characters
    email_lst = [*email]

    for i in range(len(email_lst)):
        new_ascii = ord(email_lst[i]) - 3
        email_lst[i] = chr(new_ascii)

    # convert list into a string
    email_str = "".join(email_lst)

    retVal = email_str
    return retVal
