from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_Bank = []

for question in question_data:
    Q_text = question["text"]
    Q_answer = question["answer"]
    new_question = Question(Q_text, Q_answer)
    Question_Bank.append(new_question)

quiz = QuizBrain(Question_Bank)

while quiz.still_has_questions():
    quiz.next_question()

if quiz.score == len(Question_Bank):
    print("Congratulations!,You got all questions right")
else:
    print("You have completed the quiz")
    print(f"Your final score is {quiz.score}/{len(Question_Bank)}")
