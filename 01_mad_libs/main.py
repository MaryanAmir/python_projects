def get(word:str):
    user_input=input(f'user{word}')
    return user_input

person = input("Enter a person's name: ")
job = input("Enter a job: ")
job_name2 = input("Enter an job2: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")


story= f"""
Today, {person} started a new job as a {job}.
Everything was going well until he knows about {job_name2}  !
Without thinking, {person} decided to {verb}.
Everyone was shocked because it was such a {adjective} thing to do.

In the end, {person} became {job_name2} like what he want.

The End!
"""

print(story)