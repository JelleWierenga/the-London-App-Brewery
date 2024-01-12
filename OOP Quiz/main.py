from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(Text=question_text, Answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


# quiz.next_question()

while quiz.still_has_question():
    quiz.next_question()
print(quiz.score)
print("You have completed the quiz")
print(f"Your final score was: {quiz.score} out of {quiz.question_number}")
print("Do i have to say congrats or your bad at this?")

