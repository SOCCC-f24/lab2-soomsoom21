"""

Name: Sophia Weinert
Course: CSC 138
Date: 10/24/2024
Class Section: EG
"""

import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email="abc012"):

    # this function works now
    # check decrypt function for more changes made to improve the code
    # everything is explained there.
    
    output = "" 
    len_flag = (len(email) != 6)
    anum_flag = email[3:].isdecimal() and email[3:] != '012' 
    # email_lst = ["a", "b", "c", "0", "1", "2"] 
    # (1) add space to email
    #(2) split at space and set to email_lst

    if len_flag:
        output = "Length check failed"
        output += "Email must be 6 character long."
        logging.info(output)
        return output      
    if anum_flag:
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output

    email_lst = [*email]

    for i in range(len(email_lst)):
        # len of email_lst sets a range
        
        new_ascii = ord(email_lst[i]) - 3
        # this variable sets a new ascii with the value of the decrypted
        # character

        email_lst[i] = chr(new_ascii)
        # update email_lst with the new decrypted character

        
    email_str = "".join(email_lst)
    
    retVal = email_str
    return(retVal) 

"""
def decrypt(email="def345"): 
    # Shift first 3 characters down by 3 in the ASCII table
    # Shift 4  e_lst = email.split
    output = "" 
    e_space = ''.join(email) 
    e_lst = e_space.split()

    email_lst = e_space.split(" ")
    
    len_flag = len(email) != 6
    anum_flag = email[:3].isalpha() and email.isdecimal[3:].isdecimal() 
    
    if len_flag:
        output += "Length check failed"
        logging.info(output)
        
    if not anum_flag:
        new_ascii = ord(email_lst[0]) - 3
        email_lst[0] = chr(new_ascii)
        new_ascii = ord(email_lst[1]) - 3    
        email_lst[1] = chr(new_ascii)  
        new_ascii = ord(email_lst[2]) - 3    
        email_lst[2] = chr(new_ascii) 
        new_ascii = ord(email_lst[3]) - 3    
        email_lst[3] = chr(new_ascii)  
        new_ascii = ord(email_lst[4]) - 3    
        email_lst[4] = chr(new_ascii)  
        new_ascii = ord(email_lst[5]) - 3    
        email_lst[5] = chr(new_ascii)  

    logging.info(output)
    print(output)

    retVal = "".join(email_lst)
    return retVal

Going to comment out all of this decrypt function
Since decrypt is the same as encrypt, it should be the exact same
for simplicity. The replacement below is the encrypt function working in reverse.
"""

def decrypt(email="def345"):
    output = "" 
    len_flag = (len(email) != 6)
    
    # anum_flag = email[3:].isdecimal() and email[3:] != '012'
    # 
    # line 97 doesn't work correctly as a flag. It should check both
    # parts of the email and see if they are alphabetical and numeric
    # respectively. This use of anum_flag checks if the last part of 
    # the email is a decimal and doesn't equal 012, nothing about the
    # first part though.
    # Try this instead:

    anum_flag = not (email[:3].isalpha() and email[3:].isdecimal())

    # this use checks both the first and last parts of the email to
    # ensure it's valid.
    

    if len_flag:
        output = "Length check failed"
        output += "Email must be 6 character long."
        logging.info(output)
        return output      
    if anum_flag:
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output

    email_lst = [*email]
        
    # Check line 172

    
    # e_space = " ".join (email) 
    
    # email_lst = e_space.split(" ")
    # These aren't needed in order to extract each individual element
    # of the string. Although it works you could also use [*email]
    # which does the same thing. (learned that online lmao)

    """
    new_ascii = ord(email_lst[0]) + 3
    email_lst[0] = chr(new_ascii)
    new_ascii = ord(email_lst[1]) + 3
    email_lst[1] = chr(new_ascii)
    new_ascii = ord(email_lst[2]) + 3
    email_lst[2] = chr(new_ascii)
    new_ascii = ord(email_lst[3]) + 3
    email_lst[3] = chr(new_ascii)
    new_ascii = ord(email_lst[4]) + 3
    email_lst[4] = chr(new_ascii)
    new_ascii = ord(email_lst[5]) + 3
    email_lst[5] = chr(new_ascii)

    Instead of using multiple statements over and over again
    use a for loop.
    """

    for i in range(len(email_lst)):
        # len of email_lst sets a range
        
        new_ascii = ord(email_lst[i]) - 3
        # this variable sets a new ascii with the value of the decrypted
        # character

        email_lst[i] = chr(new_ascii)
        # update email_lst with the new decrypted character
    
    """
    if len_flag:
        output += "Length check failed"
        logging.info(output)

    if not anum_flag:
        output += "Email must have 3 letters followed by 3 digits."

    else:
        logging.info(output)
        print(output)

    You should move this to before the manipulation of the email
    this way incase theres a weird input it doesn't crash the code.
    """
    
    email_str = "".join(email_lst)

    retVal = email_str
    return(retVal) 
