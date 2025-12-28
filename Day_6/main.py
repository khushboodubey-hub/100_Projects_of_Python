from question_model import Question
from  data import question_data
from quiz_brain import QuizBrain

Question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    Question_bank.append(new_question)

# print(Question_bank)
# QuizBrain(Question_bank)

quiz = QuizBrain(Question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("you've completed the quiz.")
print(f"your funal score was: {quiz.score}/{quiz.question_number}")