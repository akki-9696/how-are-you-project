#this is our basic project for it hub
print("please enter your feedback in good/bad answer")
user_input = input("how are you==").lower()
print(user_input)
if user_input == "good":
     print("thanks!,nice to hear that!!")
elif user_input=="bad":
    print("hey!!are you ok!!")
    print("do u want some help")

else:
    print("please provide your outputin yes/no ")
    user_input = input("do u want to change your mood==")
    if user_input=="yes":
        print("lets play bgmi for mood change")
    elif user_input== "no":
        print("then sit like that only!!!")

    else: 
        print("wrong input")

   