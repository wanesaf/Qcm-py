import json

#Charger les questions depuis JSON.
def load_questions(file_path):
    
    with open(file_path, 'r') as file:
        categories = json.load(file)
    return categories["categories"]




