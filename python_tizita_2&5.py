# 2)	Write a program that:
# •	Has a predefined dictionary of groceries with prices.
# •	Lets the user "add" items by typing their names.
# •	For each valid item, asks for the quantity.
# •	Keeps adding to the cart until the user types "checkout".
# •	Displays a final bill: each item, quantity, subtotal, and total.


groceries = {
     "milk":3.5,
     "eggs":6,
     "bread":7,
     "butter":10,
     "apple":8,
     "tomato":6

}

total=0
#item_total = 0

for key,value in groceries.items():
       print(f"{key}:${value}")

while True:
   grocery = (input("enter items you want to buy(checkout to quit):"))
   
   if grocery == "checkout":
        break
   
   if grocery in groceries:   
        quantity = int(input("how many:"))   
        price=groceries.get(grocery)
        item_total=price*quantity
        total += item_total
        print(f"you selected {quantity} {grocery}")
   else:
        print("you entered invalid item")
print()
print(f"your total is {total}$")

#question 5
# Create a basic quiz game that:
# •	Contains a list of 5–10 questions stored in a dictionary (or list of dictionaries [{}, {}] ).
# •	Ask the user each question and records their answers.
# •	At the end, displays:
# o	 The user's score (e.g., 7/10)
# o	Correct answers for any questions they got wrong


correct_answer={}
score=0
questions=[
    {"question":"what is the capital city of ethiopia", "answer":"addis ababa"},
    {"question":"what is the capital city of turkey", "answer":"ankara"},
    {"question":"what is the capital city of eriteria", "answer":"asmara"},
    {"question":"what is the capital city of kenya", "answer":"nairobi"},
    {"question":"what is the capital city of Gana", "answer":"akra"},
]

for i in questions:
    user_answer = input(i["question"])
    if user_answer==i["answer"]:
        print("correct")
        score=score+1

    else:
        print("wrong")
        correct_answer=i["answer"]
        print(f" the correct answer for this question is {correct_answer}")
y=(len(questions))
print(f"your score is {score}/{y}")
