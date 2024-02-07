import requests

question_data = []

api_link = f"https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean"

response = requests.get(api_link)

data = response.json()

for i in range(10):
    first_question = data['results'][i]['question']
    correct_answer = data['results'][i]['correct_answer']
    question_dict = {"text": first_question, "answer": correct_answer}
    question_data.append(question_dict)

