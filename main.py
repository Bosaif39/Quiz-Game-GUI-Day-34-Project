from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Create a list to hold question objects created from question_data
question_bank = []

# Loop through each dictionary in question_data to extract text and answer
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # Create a new Question object and append it to the question_var list
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create an instance of the QuizBrain class with the list of questions
quiz = QuizBrain(question_bank)
# Pass the quiz logic to the UI
quiz_ui = QuizInterface(quiz)
