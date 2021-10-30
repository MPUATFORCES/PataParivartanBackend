import random, string

def transactionIDGenerator():
    transactionString = string.ascii_letters+string.digits
    
    tranID = ''.join(random.choices(transactionString, k=10))
    
    # To ensure transaction ID does not start with 'U'
    while(tranID[0]=="U"):
        tranID = ''.join(random.choices(transactionString, k=10))

    return tranID
