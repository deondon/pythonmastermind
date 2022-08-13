#Rebulding Typeform Bet Generator in Python
#Why? because I cannot store variables or user profiles in Typeform

#https://pavlok.typeform.com/c/O6DUy5rc
#Long Term Goal is to execute via a sms to users phone
#Short Team Goal is to execute via a url

#print("Welcome to The Bet Generator")
#print("Press Go to Continue...")
#How to create "Go" button?

#print("""
#Rule Updates
#+100 For First Time Players Only.
#-10 Points if no Bet submitted by x time.
#-5 Points if No Screen Shot of Report submitted before Deadline.
#""")

print("How many Trust Points do you have Today?")
trustpoints = input("")
int(trustpoints)
print("You have " + trustpoints + " Trust Points\n\n")

print("What is your most important outcome for tomorrow?")
print("Complete this prompt: I must Spend at least 25 Minutes ______________.\n")
betstatement = input("")
print("I must Spend at least 25 Minutes " + betstatement + ".")
#How to Present a list of choices or prompts?

print("How many Points are you Betting You won't fail?")
betamount = input("")
print("I bet " + betamount + " Trust Points.\n\n")

print("Before what time will you get it done?\n")
print("If this is during a Supervised Pomodoro")
print("it must be within or very close to the end of the Pomodoro")
print("If it's after it must be before the end of your work day.\n")
deadlinetime = input("")
print("I will get it done before " + deadlinetime + ".\n\n\n")
#How to get time and store in variable?

print("Generating your Bet Statement...")
print("Copy or Screen Shot this into your Group Chat... \n")

print("I started with " + trustpoints + " Trust Points")
print("I Bet " + betamount + " Trust Points")
print("I must Spend at least 25 Minutes " + betstatement + " before " + deadlinetime + ".\n")
