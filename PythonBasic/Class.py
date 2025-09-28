class student: # Class representing a student
    def __init__(self, name, age, major, gpa):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
        
    
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer