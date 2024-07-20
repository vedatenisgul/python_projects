class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_input, answer):
        if user_input == answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        true_or_false = input(f"Q.{self.question_number}: {current_question.text}. (True/False)? ").lower()
        self.check_answer(true_or_false, current_question.answer)
