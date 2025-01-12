import json
import random
from displayFunc import print_with_frame
#Charger les questions depuis JSON.
def load_questions_by_category(file_path):
    with open(file_path, "r") as file:
            categories = json.load(file)
            return categories.get("categories", {})

#Affiche les catégories disponibles.
def Afficher_categories(categories):
    print("\nCategories disponibles :")
    for idx, category in enumerate(categories.keys(), start=1):
        print(f"{idx}) {category}")



def select_category(categories):
    Afficher_categories(categories)
    while True:
        try:
            choice = int(input("Choisissez une categorie (entrez le numero) : "))
            category_list = list(categories.keys())
            if 1 <= choice <= len(category_list):
                return category_list[choice - 1]
            else:
                print("Numero invalide. Veuillez reessayer.")
        except ValueError:
            print("Entree invalide. Veuillez entrer un numero.")


# ===== Gestion des Questions =====
def display_question(question, question_number):
    #Affiche une question et ses options.
    print(f"\nQuestion {question_number}: {question['question']}")
    for key, value in question["options"].items():
        print(f"{key}) {value}")


#Vérifie si la reponse est correct
def check_answer(user_choice, correct_option):
    if user_choice == correct_option:
        print("Bonne reponse !")
        return True
    else:
        print(f"Mauvaise reponse ! La bonne reponse etait : {correct_option}")
        return False
    
#Demande à l'utilisateur de répondre avic une reponse valid.
def ask_for_valid_answer(question):
    while True:
        user_choice = input("Votre reponse : ").strip().lower()
        if user_choice in question["options"]:
            return user_choice  # Retourne la réponse valide de l'utilisateur
        else:
            print("Reponse invalide. Veuillez entrer une option valide.")

#Mélange les questions pour chaque session.
def shuffle_questions(questions):
    random.shuffle(questions)
    return questions

  #Limite le nombre de questions 
def limit_questions(questions, limit):
    return questions[:limit]

