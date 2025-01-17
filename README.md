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
 ![1](https://github.com/user-attachments/assets/9c9d02a3-c1fa-46c0-8642-818a383cd03a)
 
- If the user exists in the json file , we display " Utilisateur existe déjà! "
- We ask to choose between history and a new MCQ , in the example we choose "Historique"
- We display the results of the previous MCQs and we include the date , the score and the category ( from the json file ) 
- After that , we ask the user for a new MCQ ; in the example we choose 'n' to quit .  

## Example 2
![2](https://github.com/user-attachments/assets/19454428-74f8-4b1a-86ed-0eb327b56e5a)

- In this example , the id doesnt exist in the json file so the user is added automatically .
- if we choose history , we display " L'utilisateur avec ID 3 n'a pas encore fait de QCM! "

![image](https://github.com/user-attachments/assets/13d3f9c0-27da-4c91-b95e-97a0b9f3a0de)

- In this case we choose a new MCQ , the questions and categories are also stored in the json file.
- The user selects a category , in the example we choose python .
- Now the user answers the questions by typing the letter , if the response isnt correct we display the correct answer
- When the user completes , We display the score and the time .
- The score and the date and the category will be stored in the user json file to use them after if we wants to display his history . 
 
