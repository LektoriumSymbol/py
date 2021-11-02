print("* * * This is your first program * * *")
print("Hello! What is your name?")
name = input()
print("Hi " + name + "! How are you??")
my_shape = input()
print("Well, " + name + ", nice to hear that you are " + my_shape + "!")
print("Say.. %s, do you want to by an elephant??" % name)
my_best_answer = input()

if my_best_answer.lower() == "yes":
    print("Relax man, just a joke just a joke... chill")
else:
    print("No way bro, everyone says %(0)s, but you gonna try this, I'm telling ya %(1)s" % {"0": my_best_answer, "1": name})

my_best_answer = input()

if my_best_answer.lower() == "yes":
    print("Relax man, just a joke just a joke... chill, cheers!")
else:
    print("No way bro, everyone says %(0)s, but you gonna try this, I'm telling ya %(1)s" % {"0": my_best_answer, "1": name})
