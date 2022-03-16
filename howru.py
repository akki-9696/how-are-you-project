#this is our basic project for it hub
print("please enter your feedback in good/bad answer")
user_input = input("how are you==").lower()
print(user_input)
if user_input == "good":
     print("This is a good replay code")
     print("thanks!,nice to hear that!!")
     print("can u help me if you dont mind!")
elif user_input=="bad":
    print("this is the bad repay code")
    print("hey!!are you ok!!")
    print("do u want some help")
    print("i can help you to come outoff your problem")

else:
    print("please provide your outputin yes/no ")
    user_input = input("do u want to change your mood==")
    if user_input=="yes":
        print("lets play bgmi for mood change")
    elif user_input== "no":
        print("then sit like that only!!!")

    else: 
        print("wrong input")

   