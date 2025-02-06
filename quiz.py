import random

class flashcard:
    def __init__(self):
        self.capital = {
            "America": "washington dc",
            "India": "new delhi",
            "China": "beijing",
            "Japan": "tokyo",
            "Korea": "seoul",
        }
        self.founder={
            "Apple": "Steve Jobs",
            "Google": "Larry Page",
            "Amazon": "Jeff Bezos",
            "Facebook": "Mark Zuckerberg",
            "Microsoft": "Bill Gates",
        }
        self.question={
            "capital" : self.capital,
            "founder": self.founder,
        }
    def  quiz(self):
        print("The quiz starts ----->")
        print("Rules ---> Enter capital of the country or founder of the company")
        print("According to the respective question")
        c= 0
        b= 0
        while(True):
            category= random.choice(list(self.question.keys()))
            data= self.question[category]
            key= random.choice(list(data.keys()))
            print(f"\nQuestion: Name the {category} of {key}?")
            user_answer = input("Enter your answer: ")
            correct_answer= data[key].lower()
            if user_answer.lower() == correct_answer:
                print("Correct ","\U0001F600")
                c+=1
                print("you answered",c)
                if c==5:
                    break
            else:
                b+=1
                print("wrong answer")
            if b==5:
                print("you looseeee")
                break

            del self.question[category][key]
            
        
            
            
fc = flashcard()
fc.quiz()

print("---------The quiz is over------ ")




        
