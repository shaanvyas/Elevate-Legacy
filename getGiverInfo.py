# import util as u
import ollamaModel as o
# print("Please answer the following questions.")

model = o.OllamaEndpointLLM("llama3")
questions = ["What was a moment where you seriously considered giving up—and what made you keep going?", "What failure or setback hurt the most, and how did you recover from it emotionally and practically?", "Was there a time when everyone around you doubted you—or when you doubted yourself? How did you handle that?",  "What’s a sacrifice you had to make that you didn’t expect—and would you make it again?", "What’s something you wish someone had told you when you were starting, but no one did?"]
# answers = []
# for i, v in enumerate(questions):
#     cur_answer = input("Question #" + str(i+1) + ": " + v + " ")
#     answers.append(cur_answer)

car_crash_answers = ["When I crashed my car.", "Crashing my car and getting a new one.", "When I crashed my car I explained how I made this mistake.", "Having to leave my car after crashing it.", "Be careful when driving."]

good_answers = ["A moment that I considered giving up was when the federal government pulled my funding for a grant. I decided to keep going after i realized that I had a lot of important work to do and my students encouraged me to start a new project.", "not sure", "Trying to get my PhD I struggled often with coursework in my first few years and my advisor doubted me I decided to take some time off of studying to recollect my self before setting off on my studies once again.", "I had to sacrifice some work anmd work research excursions for my children. I would definitely do iut again if I could.", "I wish someonw would have told me the importance of networking in Academia when I first started."]
linkedIn = "https://www.linkedin.com/in/amita-vyas/"
question1 = f"Based on this linkedIn: " + linkedIn + " and the following information " + str(good_answers) + ". Generate me a 5 sentence story that summarizes this person's story."
answer1 = model.generate(question1)
print("The story: \n" + answer1)

question2 = f"Based on this story:" + answer1 + " Give me exactly and only 3 talking points for a 30-60 second video about the biggest hardship they faced and what they learned from it."
answer2 = model.generate(question2)
print(answer2)

talking_point = input("Type 1, 2, or, 3 for which talking point you want to use:")

question3 = f"Based on talking point number #" + talking_point + " from these talking points: " + answer2 + "Give me a script for the person making a 30-60 second video without a narrator focusing on the specifics utilizing the information in this LinkedIn as well: " + linkedIn + "Emphasize exactly what they want to get across to the people."
answer3 = model.generate(question3)
print(answer3)