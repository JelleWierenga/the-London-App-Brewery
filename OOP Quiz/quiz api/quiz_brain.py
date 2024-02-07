class QuizBrain:
    def __init__(self, q_list):
        self.category = None
        self.amount = None
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

    def selections(self):
        from data import data

        while True:
            try:
                self.amount = int(input("How many questions do you want: "))
                break
            except ValueError:
                print("Invalid input")
        while True:
            try:
                self.category = int(input("What category do you want? (enter the corresponding number)\n"
                                          "general knowledge = 9\n"
                                          "Books = 10\n"
                                          "Film = 11\n"
                                          "Music = 12\n"
                                          "Musical = 13\n"
                                          "television = 14\n"
                                          "video games = 15\n"
                                          "Board games = 16\n"
                                          "Science and Nature = 17\n"
                                          "Computers = 18\n"
                                          "Mathematics = 19\n"
                                          "Mythology = 20\n"
                                          "Sports = 21\n"
                                          "Geography = 22\n"
                                          "History = 23\n"
                                          "Politics = 24\n"
                                          "Art = 25\n"
                                          "Celebrities = 26\n"
                                          "Animals = 27\n"
                                          "Vehicles = 28\n"
                                          "Comics = 29\n"
                                          "Gadgets = 30\n"
                                          "Japanese Anime & Mange = 31\n"
                                          "Cartoon & Animations = 32\n"
                                          "\n"
                                          "Your desired category: "))
                break
            except ValueError:
                print("Invalid input")
            data(amount, category)
