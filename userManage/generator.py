import json
import random
from datetime import datetime
from Question_management.qcmMang import *
from userManage.user import *

# Chemin vers le fichier JSON
file_path = 'userManage/users.json'

# Charger ou créer le fichier JSON
try:
    with open(file_path, 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    data = {"users": []}

# Fonction pour trouver un utilisateur par ID
def find_user_by_id(user_id):
    for user in data["users"]:
        if user["id"] == user_id:
            return user
    return None

# Fonction pour ajouter un QCM avec score et catégorie pour un utilisateur
def add_qcm_result(user_id, score, category, qcm):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    qcm_entry = {
        "date": date,
        "score": score,
        "category": category,
        "qcm": qcm
    }
    
    user = find_user_by_id(user_id)
    if user:
        user["qcm_results"].append(qcm_entry)
    else:
        new_user = {
            "id": int(user_id),
            "qcm_results": [qcm_entry]
        }
        data["users"].append(new_user)
    
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def represents_int(id): 
    try: 
        int(id)
    except ValueError:
        return False
    else:
        return True


def new_qcm(user_id):
    # Charger les questions par catégories
    questions_file = "Question_management/questions.json"
    categories = load_questions_by_category(questions_file)

    if not categories:
        print("Aucune question disponible.")
        return

    # Sélectionner une catégorie
    chosen_category = select_category(categories)
    print(f"\nVous avez choisi la catégorie : {chosen_category}")

    # Charger les questions de la catégorie choisie
    questions = categories[chosen_category]

    # Mélanger et limiter les questions
    questions = shuffle_questions(questions)
    num_questions = min(len(questions), 10)
    questions = limit_questions(questions, num_questions)

    # Poser les questions et calculer le score
    score = 0
    qcm_result = []
    for i, question in enumerate(questions, start=1):
        display_question(question, i)
        user_choice = ask_for_valid_answer(question)
        correct = check_answer(user_choice, question["correct_option"])
        if correct:
            score += 1
        
        # Ajouter la question et les réponses au QCM result
        qcm_result.append({
            "question": question["question"],
            "user_answer": user_choice,
            "correct_answer": question["correct_option"]
        })
             
    # Ajouter le résultat du QCM avec la catégorie et la date
    add_qcm_result(user_id, score, chosen_category, qcm_result)

    # Afficher le score final
    print(f"\nVotre score final : {score}/{num_questions}")
     


def historique(user_id):
    for user in data["users"]:
        if user["id"] == user_id:
            if "qcm_results" in user:
                print(f"Results for user {user_id}:")
                for result in user["qcm_results"]:
                    print(f"Date: {result['date']}, Score: {result['score']}/5, Category: {result['category']}")
                
            else:
                print(f"No QCM results found for user {user_id}")
                



    return


def start():
    

    # Demander l'identifiant utilisateur
    

    while (True) : 
        user_id =  input(("Entrez votre id : ")) 
        if (represents_int(user_id)) :
            if (int(user_id)>0) :  
                if (exist(int(user_id))) :
                    print("il existe")
                else : 
                    addUser(int(user_id))   
                break
            else : 
                print("That's not a postive integer") 
        else : 
            print("That's is not an integer")

    user_id = int(user_id)

    

    while (True) : 
        choice = input(("veuiller saisir votre choix: \n 1.historique \n 2.nouveau qcm : ")) 
        if (represents_int(choice)) :
            if (int(choice)>0) :  
                if (int(choice) == 1) :
                    historique(user_id)
                    approve = input(("veuiller saisir 'y' si vous voulez passez un nouveau qcm : "))
                    if (approve == 'y') :
                        new_qcm(user_id)
                    break
                elif (int(choice) == 2)  :
                    new_qcm(user_id)
                    break
                else : 
                    print("veuillez choisir soit 1 ou 2 ")  
                
            else : 
                print("That's not a postive integer") 
        else : 
            print("That's is not an integer")
    
    

    

