
# robot cheerleaders

an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

for w in word:
    if w in an_letters:
        #print(f'Give me an {c}: {c}') # with f-strings
        print("Give me an " + w + ": " + w)
    else:
        #print(f'Give me a {c}: {c}') # with f-strings
        print("Give me a " + w + ": " + w)
print("What does that spell?")
for i in range(times):
    print(word, "!!!")