from question_model import Question


class QuizBrain:
    def __init__(self,question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_have_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self,user_answer,true_answer):
        if user_answer.lower() == true_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answer is {true_answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n")

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)? ")
        self.check_answer(user_answer,question.answer)