class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list


    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number = self.question_number + 1
        ans = input(f"Q.{self.question_number}: {curr_question.text} (True or False): ")
        self.check_answer(ans, curr_question.answer)

    def check_answer(self, ans, curr_ans):
        if ans.lower() == curr_ans.lower():
            self.score = self.score + 1
            print(f"Good job your score is {self.score} out of {self.question_number}")
        else:
            print(f"You are bad at this :) your score is {self.score} out of {self.question_number}")
            print(f"The correct answer was {curr_ans}")
        print("\n")

