import json
import random
from qcmMang import *


def main():
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
    for i, question in enumerate(questions, start=1):
        display_question(question, i)
  
        user_choice=ask_for_valid_answer(question)
        if check_answer(user_choice, question["correct_option"]):
                 score += 1
             

    # Afficher le score final
    print(f"\nVotre score final : {score}/{num_questions}")


main()