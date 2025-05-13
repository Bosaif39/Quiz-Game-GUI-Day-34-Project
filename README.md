
# **Quiz Game**

## **Overview**

This is the Day 34 project from the course "100 Days of Code: The Complete Python Pro Bootcamp". It's a simple quiz game that asks the player a series of True/False questions based on general knowledge. The game provides immediate feedback for each answer and tracks the user's score.

The quiz is designed with a graphical user interface (GUI) using the `tkinter` library.

## **How It Works**

The game retrieves a set of True/False questions from the [Open Trivia Database](https://opentdb.com/). The user will be presented with one question at a time. After they select an answer, the game will provide feedback on whether their answer was correct or not. The game continues until all questions have been answered.

* The game shows the question along with True/False buttons.
* After each answer, the background changes color to show whether the answer was correct (green) or incorrect (red).
* The player’s score is displayed and updated after each question.
* When all questions are answered, the final score is displayed.

## **Example**

![Screenshot of Quiz Game]()

## **Features**

* True/False quiz questions based on general knowledge (video game-related).
* Real-time feedback after each question.
* Score tracking that updates after each question.
* A final score display after all questions have been answered.

## **Code Structure**

The project is organized into several Python files:

### **1. `data.py`**

* Contains the parameters and API request to retrieve quiz questions from the Open Trivia Database API.

### **2. `question_model.py`**

* Defines the `Question` class to represent each quiz question, including the question text and the correct answer.

### **3. `quiz_brain.py`**

* Handles the logic for the quiz game, including managing the flow of questions, checking answers, and tracking the score.

### **4. `ui.py`**

* The GUI implementation using the `tkinter` library. It creates the window, handles button clicks, and displays questions and feedback.

### **5. `main.py`**

* The entry point of the program. Initializes the quiz game and the GUI interface.

## **Requirements**

* Python 3.x
* `requests` library for API calls (`pip install requests`)
* `tkinter` for GUI (usually comes pre-installed with Python)

