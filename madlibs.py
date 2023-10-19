#Load story as a string, parse through the string and grab each of the blank words. Story in read mode using "with" syntax so I can perform file operations on the f variable in the indented text block, and Python will clean it up after the block is closed. To prevent repeated words, use a set instead of a list.
with open("story.txt", "r") as f:
    story = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i +1]
        words.add(word)
        start_of_word = -1

#Get value for each of words from user. Set up a dictionary to do this. Loop through the unique words and ask for a value for each. Use plus signs instead of commas because I'm using the input statement - not the print statement, so I need to concatenate.
answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

#Replace the word prompts with the words provided by the user. Loop through.

for word in words:
    story = story.replace(word, answers[word])

print(story)