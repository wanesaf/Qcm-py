import json 

def loadFile (file_path) : 
   with open(file_path,'r') as file : 
    return json.load(file)    
   

def saveFile (file_path,data) : 
      with open(file_path,'w') as file : 
          json.dump(data,file,indent=4)


def exist (id) : 
        data = loadFile('userManage/users.json')
        for user in data['users']:
          userId = user['id']
          if (userId == id ):
             return True 
          
        return False


def addUser(id) : 
   data = loadFile('userManage/users.json') 
   newUser = {"id" : id }
   data['users'].append(newUser)
   saveFile('userManage/users.json',data)
     