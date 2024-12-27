import json 

from userManage.user import *

def represents_int(id): 
    try: 
        int(id)
    except ValueError:
        return False
    else:
        return True

print("Bienvenu au QCM Informatique !")


while (True) : 
    id = input(("Entrez votre id : ")) 
    if (represents_int(id)) :
       if (int(id)>0) :  
         if (exist(int(id))) :
            print("il existe")
         else : 
            addUser(int(id))   
         break
       else : 
          print("That's not a postive integer") 
    else : 
       print("That's is not an integer")


