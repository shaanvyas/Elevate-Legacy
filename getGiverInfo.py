# import util as u
import ollamaModel as o
print("Please answer the following questions.")

model = o.OllamaEndpointLLM("llama3")
questions = ["What was a moment where you seriously considered giving up—and what made you keep going?", "What failure or setback hurt the most, and how did you recover from it emotionally and practically?", "Was there a time when everyone around you doubted you—or when you doubted yourself? How did you handle that?",  "What’s a sacrifice you had to make that you didn’t expect—and would you make it again?", "What’s something you wish someone had told you when you were starting, but no one did?"]
answers = []
for i, v in enumerate(questions):
    cur_answer = input("Question #" + str(i+1) + ": " + v + " ")
    answers.append(cur_answer)

# answers = ["When I crashed my car.", "Crashing my car and getting a new one.", "When I crashed my car I explained how I made this mistake.", "Having to leave my car after crashing it.", "Be careful when driving."]

linkedIn = "https://www.linkedin.com/in/amita-vyas/"
question = f"Based on this linkedIn: " + linkedIn + " and the following information " + str(answers) + ". Generate me a 5 sentence story that summarizes this person's story."
answer = model.generate(question)
print(answer)