# Qcm-py
MCQ app using python. 

## Features 
- Allows users to answer MCQs.
- Evaluates their answers and displays a score.
- Provides a user-friendly console interface.
- Manages user data, tracking their history of MCQs and previous scores.

## How to use 
- You must have python installed
- Clone the repo using
  ```bash
  https://github.com/wanesaf/Qcm-py.git
- run the main.py using
    ```bash
    python main.py

 ## Example 1
 ![1](https://github.com/user-attachments/assets/c7dc4d09-11bc-48a7-bf76-6d2634c4986d)

 
- If the user exists in the json file , we display " Utilisateur existe déjà! "
- We ask to choose between history and a new MCQ , in the example we choose "Historique"
- We display the results of the previous MCQs and we include the date , the score and the category ( from the json file ) 
- After that , we ask the user for a new MCQ ; in the example we choose 'n' to quit .  

## Example 2
![2](https://github.com/user-attachments/assets/19454428-74f8-4b1a-86ed-0eb327b56e5a)

- In this example , the id doesnt exist in the json file so the user is added automatically .
- if we choose history , we display " L'utilisateur avec ID 3 n'a pas encore fait de QCM! "

![2](https://github.com/user-attachments/assets/946cfb5c-978c-442e-ba38-8fd9e1e6f40f)

![3](https://github.com/user-attachments/assets/ffa1859d-7df5-4e0e-bc78-147630f19f25)



- In this case we choose a new MCQ , the questions and categories are also stored in the json file.
- The user selects a category , in the example we choose "Devloppement Web" .
- Now the user answers the questions by typing the letter , if the response isnt correct we display the correct answer
- When the user completes , We display the score and the time .
- The score and the date and the category will be stored in the user json file to use them after if we wants to display his history . 
 
