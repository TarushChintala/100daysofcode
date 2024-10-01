from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question_bank.append(Question(i["question"],i["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()

print("You have completed the Quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")