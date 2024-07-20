from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(item["question"], item["correct_answer"]) for item in question_data]
game = QuizBrain(question_bank)

while game.still_has_questions():
    game.next_question()
print(f"You've completed the quiz!")
print(f"Your final score was: {game.score}/{game.question_number}")
