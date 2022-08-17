#Rebuilding Typeform Bet Generator in Python
#Why? because I cannot store variables or user profiles in Typeform

#https://pavlok.typeform.com/c/O6DUy5rc
#Long Term Goal is to execute via a sms to users phone
#Short Team Goal is to execute via a url


#MVP BET GEN FUNCTION TODO LIST

#How to make available via url on mobile? #Django?
#How to get before time (deadline) and store in variable?
#How to Present a list of choices or prompts?
#How to make User Profiles via gmail? #Django?
#How to make available via sms? #Twilio?

#DONE
#Connect VSCode to Github - Passed
#Download VSCode
#Pause Spyder Usage - Connect github to Spyder - Failed
#Connect github to VSCode
#Upload code to github
#Download Spyder

#print("Welcome to The Bet Generator")
#print("Press Go to Continue...")
#How to create "Go" button?

#print("""
#Rule Updates
#+100 For First Time Players Only.
#-10 Points if no Bet submitted by x time.
#-5 Points if No Screen Shot of Report submitted before Deadline.
#""")


def load_data()
  f = open("../.DS_Store", 'r')
  trustpoints=f.readline()
  if trustpoints is None:
    trustpoints=100
  f.close()
  
def save_data()
  f = open("../.DS_Store", 'w')
  f.writeline(trustpoints)
  f.close()
  

if __name__ == '__main__':
print("How many Trust Points do you have Today?")
#trustpoints = input("")
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
beforetime = input("")
print("I will get it done before " + beforetime + ".\n\n\n")
#How to get time and store in variable?

print("Generating your Bet Statement...")
print("Copy or Screen Shot this into your Group Chat... \n")

print("I started with " + trustpoints + " Trust Points")
print("I Bet " + betamount + " Trust Points")
print("I must Spend at least 25 Minutes " + betstatement + " before " + beforetime + ".\n")
