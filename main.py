import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get('OPENAI_PROJECT_KEY')
)

print("Glycemic Load calculator. Please type 'exit' into any input to kill the process.")

while True:

    food = input("What food item? \n")

    if food.lower() == "exit":
        break

    amount = input("What amount (please denote in grams, ounces, cups, etc) \n")

    if amount.lower() == "exit":
        break

    user_input = f'{amount} of {food}'

    print("Calculating the Glycemic Load >>>>>>>>> ")

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an expert nutritionist with an understanding of calories, macros, bioavailability of calories, and glycemic load."},
        {"role": "user", "content": f"What is the glycemic load of {user_input}. If you have that information, respond with just the value. Nothing else. If you do not have that information, respond with UNKNOWN."}
    ]
    )

    print(f'The glycemic load of {user_input} is {completion.choices[0].message.content}.')
