import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email="abc012"):
   ''' email="abc012" '''
    output = "" 
    len_flag = (len(email) != 6)
    anum_flag = email[:3].isalpha() and email[3:] != '012' 

    #email_lst = ["a", "b", "c", "0", "1", "2"]
    #(1) add space to email
    e_space = " ".join (email) 
    #(2) split at space and set to email_lst
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
    
    if len(email_lst) != 6:
        output += "Length check failed"
        logging.info(output)
    if anum_flag isalpha() and isdecimal():
        output += "Email must have 3 letters followed by 3 digits."
    else:
        logging.info(output)
        print(output)     
    
        email_str = "dbc012"
   
retVal = email_str
print(retVal) 

def decrypt(email="def345"): # Shift first 3 characters down by 3 in the ASCII table
    output = "" 
    
    len_flag = len(email) == 6
    anum_flag = email.isalpha[:3] != 'def' and email.isdecimal[3:] != '345' 
    if len_flag:
             output += "Length check failed"
             logging.info(output)
    if anum_flag: isalpha() and isdecimal()
    else:
        logging.info(output)
        print(output)

    retVal = "aef345"
    print(retVal)
