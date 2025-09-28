from Class import Question
question_prompts = [
    "What color are apples?\n(a) Red\n(b) Blue\n(c) Green",
    "What color are bananas?\n(a) Yellow\n(b) Blue\n(c) Green",
    "What color are grapes?\n(a) Red\n(b) Green\n(c) Purple"
]

question = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c")

]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt + "\n") # /n is to put in a new line
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")



run_test(question)