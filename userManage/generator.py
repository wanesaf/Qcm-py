import os
import json
import time
from datetime import datetime
from Question_management.qcmMang import *
from userManage.user import *
from displayFunc import print_with_frame

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
        if 'qcm_results' in user:
         user["qcm_results"].append(qcm_entry)
        else :
         user["qcm_results"] = []
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
    start_time = time.time()  # Start the timer

    # Charger les questions par catégories
    questions_file = "Question_management/questions.json"
    categories = load_questions_by_category(questions_file)

    if not categories:
        print_with_frame(["Aucune question disponible dans cette categorie"])
        return

    # Sélectionner une catégorie
    chosen_category = select_category(categories)
    print(f"\nVous avez choisi la categorie : {chosen_category}")

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

    # Stop the timer and calculate elapsed time
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Save the QCM result and display the score
    add_qcm_result(user_id, score, chosen_category, qcm_result)
    print_with_frame([f"Votre score final : {score}/{num_questions}"])
    print_with_frame([f"Temps écoulé : {elapsed_time:.2f} secondes"])


def historique(user_id):
    for user in data["users"]:
        if user["id"] == user_id:
            if "qcm_results" in user and user["qcm_results"]:
                results_lines = [
                    f"Les résultats des QCMs que l'utilisateur avec ID {user_id} a fait:",
                    "-" * (os.get_terminal_size().columns - 4) 
                ]
                for result in user["qcm_results"]:
                    results_lines.append(
                        f"Date: {result['date']}, Score: {result['score']}/10, Category: {result['category']}"
                    )
                results_lines.append("-" * (os.get_terminal_size().columns - 4))
                
                # Afficher les résultats encadrés
                print_with_frame(results_lines)
            else:
                # Message si aucun résultat trouvé
                print_with_frame([f"L'utilisateur avec ID {user_id} n'a pas encore fait de QCM!"])
    return



def start():
    while True:
        user_id = input("Entrez votre ID : ")
        if represents_int(user_id):
            if int(user_id) > 0:
                if exist(int(user_id)):
                    print_with_frame(["Utilisateur existe déjà!"])
                    addedNow = False
                else:
                    print_with_frame(["Ajouté dans la liste des utilisateurs!"])
                    addUser(int(user_id))
                    addedNow = True
                break
            else:
                print("C'est pas un entier naturel")
        else:
            print("C'est pas un entier")

    user_id = int(user_id)

    while True:
        print_with_frame(["Veuillez saisir votre choix:", "1. Historique", "2. Nouveau QCM  "])
        choice = input("Votre choix : ")
        if represents_int(choice):
            if int(choice) > 0:
                if int(choice) == 1:
                    historique(user_id)
                    if(addedNow) :
                        print_with_frame([f"L'utilisateur avec ID {user_id} n'a pas encore fait de QCM!"])    
                    approve = input("Veuillez saisir 'y' si vous voulez passer un nouveau QCM : ")
                    if approve == 'y':
                        new_qcm(user_id)
                    else:
                        print_with_frame(["Bonne chance pour la prochaine fois!"])
                    break
                elif int(choice) == 2:
                    new_qcm(user_id)
                    break
                else:
                    print_with_frame(["Veuillez choisir soit 1 ou 2"])
            else:
                print("C'est pas un entier naturel")
        else:
            print("C'est pas un entier")


