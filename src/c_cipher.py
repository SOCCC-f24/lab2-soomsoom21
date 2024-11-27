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
    
    output = " " 
    len_flag = (len(email) != 6)
    anum_flag = email[3:].isdeccimal() and email[3:] != '012' 
    # email_lst = ["a", "b", "c", "0", "1", "2"]
    # (1) add space to email
    e_space = " ".join (email) 
    # (2) split at space and set to email_lst
    email_lst = e_space.split(" ")
    
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

    if len_flag:
        output += "Length check failed"
        logging.info(output)
  
    if not anum_flag:
        output += "Email must have 3 letters followed by 3 digits."
    else:
        logging.info(output)
        print(output)     

        email_str = "".join(email_lst)
   
        retVal = email_str
        print(retVal) 

"""
def decrypt(email="def345"): # Shift first 3 characters down by 3 in the ASCII table
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
             
        if not anum_flag: isalpha() and isdecimal():
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

        retval = " ".join(email_lst)
        return retval

  
   
