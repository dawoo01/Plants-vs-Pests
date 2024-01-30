"""
@author: Myko Jefferson M. Javier
@date: December 3, 2023
@section: CMSC 12 T1L
@code-description: CMSC 12 Project - Plants vs Pests
"""
import random
import time
import datetime
import saver_and_loader

#Functions

def renderFarm(num, dict): #Function for rendering the farm. Takes a number (will be used to know how many lands are opened) and a dictionary. 
    for key in dict:
        if key <= num: #Opens the number of farmland the user will input.
            dict[key] = 'O'
        else:
            dict[key] = 'Y'
    #Renders the Farm showing which lands are open and reserved 
    print("\n:::::::::: Your Farm ::::::::::")
    print(f"[: {dict[1]} :]	[: {dict[2]} :]	[: {dict[3]} :]	[: {dict[4]} :]")
    print(f"[: {dict[5]} :]	[: {dict[6]} :]	[: {dict[7]} :]	[: {dict[8]} :]")
    print(f"[: {dict[9]} :]	[: {dict[10]} :]	[: {dict[11]} :]	[: {dict[12]} :]")
    print(f"[: {dict[13]} :]	[: {dict[14]} :]	[: {dict[15]} :]	[: {dict[16]} :]")
    print(":::::::::: Your Farm ::::::::::")
    print("\nMap Legend: [: O :] Open [: Y :] Reserved")
    print("\nFarmer Decisions: [0] Kill [1] Grow [2] Transform\n")

def gameProper(dict): #Function for the main game. Also has some function calles in it.
    organism = ["Plants", "Pest"] #List for the organism that will show. (Will be randomized using indexes)
    factor = ["Warm", "Humid", "Stormy"] #List for the varying factors. (Will be randomized as well using indexes)
    timeStart = time.time() #Starting the timer, as the game will officially start at this point
    score = 0 #set the initial score to be 0
    for key in dict: #Iterates through the dictionary
        if dict[key] == 'O': #If the farmland is open, then the user can decide what to do with his land.
            randomOrganism = organism[random.randint(0,100)%2] #Randomizer, used modulo to make it a bit complex, same with the one below
            weatherCondition = factor[random.randint(0,100)%3] #Used this implementation, as it is easier to randomize the scenarios using the indexes of the lists. 
            print(f"\nDay {key-1}: {randomOrganism}") 
            print(f"Factor: {weatherCondition}")
            while True: #Used while loop, to make sure we get a valid input. (Will continue to ask if the user doesn't provide a valid one.)
                decision = input("Farmer's decision: ")
                if decision.isdigit(): #Checks if the user input is a number, if true then proceed to the next set of conditional statements. 
                    decision = int(decision) #Converts the user input to an integer
                    if decision < 0 or decision > 2: #If the user inputs a value less than 0 or greater than 2 (not within the scope of valid input) 
                        print("Please enter a valid input [0-2]")  #Then the program will ask the user to input a valid number
                    else: #Else the program will accept it
                        break 
                else:
                    print("Please enter a valid input [0-2]") #Prints this whenever the user enter a non-number input
            dict[key] = gameScoring(randomOrganism,weatherCondition,decision,crop,season) #Calls the function gameScoring, as this function returns the validated score, then the farm will be updated, with the value being the score for that specific day
            score += dict[key] #Will update the user's accumulated score.
    timeEnd = time.time() #Takes the time when the user ends the game. 
    timeElapsed =  timeEnd - timeStart #Formula for finding the time elapsed
    gameResult(dict,score,timeElapsed) #Calls the function gameResult
    saver_and_loader.saveLeaderboards(leaderboards) #Saves the user's score to the leaderboards.dat

    showLeaderboards(saver_and_loader.loadLeaderboards(leaderboards)) #Calls the function showLeaderboards with the parameter loadLeaderboards



def gameScoring(organism,weather,decision,crop,season): #Function for validating the user's score for the specific day
    score = 0 #Sets the variable score
    #Scoring based on the game's CheatSheet (includes the seasonal and crop effects)
    if organism == 'Pest': 
        if weather == 'Humid':
            if decision == 2:
                score = random.randint(0,1)
            else: 
                score = 0
        elif weather == 'Warm':
            if decision == 0:
                score = 1
            else:
                score = 0
        elif weather == 'Stormy':
            if decision == 0:
                score = 1
            else:
                score = 0
    elif organism == 'Plants':
        if season == 'Rainy' and crop == 'Palay':
            if weather == 'Humid':
                if decision == 1 or decision == 2:
                    score = 1
                else:
                    score = 0       
            elif weather == 'Stormy':
                if decision == 2:
                    score = 1
                else:
                    score = 0
        elif season == 'RainyBer' and (crop == 'Palay' or crop =='Strawberry'):
            if weather == 'Humid':
                if decision == 1 or decision == 2:
                    score = 1
                else:
                    score = 0 
            elif weather == 'Stormy':
                if decision == 2:
                    score = 1
                else:
                    score = 0
        elif season == 'DryBer' and (crop == 'Starfruit' or crop =='Strawberry'):
            if weather == 'Warm':
                if decision == 1 or decision == 2:
                    score = 1
                else:
                    score = 0 
            elif weather == 'Stormy':
                if decision == 2:
                    score = 1
                else:
                    score = 0
        elif season == 'Dry' and crop == 'Starfruit':
            if weather == 'Warm':
                if decision == 1 or decision == 2:
                    score = 1
                else:
                    score = 0 
            elif weather == 'Stormy':
                if decision == 2:
                    score = 1
                else:
                    score = 0
        else:
            if weather == 'Humid' or weather =='Warm':
                if decision == 1:
                    score = 1
                else:
                    score = 0
            elif weather == 'Stormy':
                if decision == 2:
                    score = random.randint(0,1)
                else:
                    score = 0
    return score 

def gameResult(dict, score, time): #Function for showing the user the result of the game. 
    #Prints the updated farm, with the value being the score  
    print("\n:::::::::: Your Farm ::::::::::")
    print(f"[: {dict[1]} :]	[: {dict[2]} :]	[: {dict[3]} :]	[: {dict[4]} :]")
    print(f"[: {dict[5]} :]	[: {dict[6]} :]	[: {dict[7]} :]	[: {dict[8]} :]")
    print(f"[: {dict[9]} :]	[: {dict[10]} :]	[: {dict[11]} :]	[: {dict[12]} :]")
    print(f"[: {dict[13]} :]	[: {dict[14]} :]	[: {dict[15]} :]	[: {dict[16]} :]")
    print(":::::::::: Your Farm ::::::::::")
    print("\n:::::::::::::: Game Over :::::::::::::")
    print("Name\t     Score\t      Time") 
    print(f"{user}\t     {score}/{landSize}\t   {round(time,2)} secs") #Prints the user's name, score, and the time it took him/her/other to finish the game. 
    loader = { #Temporary Dictionary Holder
        "Player": user,
		"Score": int(score),
		"Farmsize": int(landSize),
		"Time": float(round(time,2))
         }
    leaderboards[user] = loader #Adds the user's result to the leaderbards dictionary

def showLeaderboards(dictionary): # Function for showing the global leaderboards
    print("\n:::::::::::: Global Score ::::::::::::")
    print("Name\t     Score\t      Time")
    for key, value in dictionary.items(): #Iterates through the dictionary, which will come from the loadLeaderboard function. 
        print(f"{key}\t     {value['Score']}/{value['Farmsize']}\t   {value['Time']} secs")
    
         

def isCrop(): #Function for validating the user input for crop
    while True:
        crop = input("Pick your crop: ")
        if crop.isdigit(): #Checks if the user inputs a number, Will base the value to assigned number to the crops
            if int(crop) == 1:
                crop ="Palay" # 1 for Palay
                break
            elif int(crop) == 2:
                crop = "Strawberry" #2 for Strawberry
                break
            elif int(crop) == 3:
                crop = "Starfruit" #3 for Starfruit
                break
            else:
                print("Please enter a valid crop")
        else: #If the user didn't input a number, then he/she/they must have input a string
            if (crop.replace(" ","")).upper() == "PALAY": #Will remove the spaces, so the program will not display error messages when the user accidentally enters a space. Also formats the string to all caps, to make the input case insensitive.
                crop = "Palay"
                break
            elif (crop.replace(" ","")).upper() == "STRAWBERRY":
                crop == "Strawberry"
                break
            elif (crop.replace(" ","")).upper() == "STARFRUIT":
                crop == "Starfruit"
                break
            else:
                print("Please enter a valid crop")
    return crop

def seasonChecker(): #Function for checking the season, based on the current date. (Will adapt to when you play the game). (Ex. Playing in March, will set the season to Dry/Summer)
    month = (datetime.datetime.now()).month #Takes the current month in form of an int (Ex. December = 12)
    #Conditions for setting the season to either Rainy, Dry, Bermonths, or some intersections. (Was based on PAG-ASA's data on Philippine Climate Timeline, with an added twist of the Filipino Culture of Bermonths)
    if 6 <= month <= 8:
        season = "Rainy"
        print("It's the Rainy Season 💦. This 'tag-ulan' time, Palays get an extra buff!!!")
    elif 9 <= month <= 11:
        season = "RainyBer"
        print("It's the Rainy💦 and Bermonths🎅🏼 Season . This 'tag-ulan/lamig' time, Palays and Strawberries get an extra buff !!!")
    elif month == 12:
        season = "DryBer"
        print("It's the Dry☀️ and Bermonths🎅🏼 Season . This 'tag-tuyot/lamig' time, Starfruits and Strawberries get an extra buff !!!")
    else:
        season = "Dry"
        print("It's the Dry Season ☀️. This 'tag-tuyot' time, Starfruits get an extra buff!!!")

    return season


#Main Program
#The Farm the will hold the score of the users, as well as the open or reserved farmlands at the start of the game. (PS: Got this idea from Aliyah Guoc, Thanks Gab! <3)
farm = {1:'O',2:'O',3:'O',4:'O',5:'O',6:'O',7:'O',8:'O',
        9:'O',10:'O',11:'O',12:'O',13:'O',14:'O',15:'O',16:'O'}

leaderboards = {} #Sets the initial leaderboard to an empty dictionary

#Got this from a pixel text generator online. I just addded to this to give it more of an actual game feel.
print("\nP    H     I     L       I      P       P      I     N     E           E      D      I      T      I     O    N   \n")
print("██████╗░██╗░░░░░░█████╗░███╗░░██╗████████╗░██████╗  ██╗░░░██╗░██████╗  ██████╗░███████╗░██████╗████████╗░██████╗")
print("██╔══██╗██║░░░░░██╔══██╗████╗░██║╚══██╔══╝██╔════╝  ██║░░░██║██╔════╝  ██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔════╝")
print("██████╔╝██║░░░░░███████║██╔██╗██║░░░██║░░░╚█████╗░  ╚██╗░██╔╝╚█████╗░  ██████╔╝█████╗░░╚█████╗░░░░██║░░░╚█████╗░")
print("██╔═══╝░██║░░░░░██╔══██║██║╚████║░░░██║░░░░╚═══██╗  ░╚████╔╝░░╚═══██╗  ██╔═══╝░██╔══╝░░░╚═══██╗░░░██║░░░░╚═══██╗")
print("██║░░░░░███████╗██║░░██║██║░╚███║░░░██║░░░██████╔╝  ░░╚██╔╝░░██████╔╝  ██║░░░░░███████╗██████╔╝░░░██║░░░██████╔╝")
print("╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═════╝░  ░░░╚═╝░░░╚═════╝░  ╚═╝░░░░░╚══════╝╚═════╝░░░░╚═╝░░░╚═════╝░")

#Just added this username validator, so we can make sure that the player name will not be empty, as it can get me in trouble in the saving and loading process of the leaderboards.
while True:
    user = input("\nEnter the name of the player: ")
    if user == "":
        print("Please enter the player's name")
    else:
        break

print(f"Welcome to the game, {user}\n")
season = seasonChecker() #Tells the user the Season first, so the user can know which crops are best to be played in the session.
print("\nHere are your crop list:")
print("1) Palay")
print("2) Strawberry")
print("3) Starfruit")

crop = isCrop() #Calles the crop function, which returns the user input for crop. Did this to make it look a bit more organize in the actual program. 

#Validates if the user inputs a valid Farmland size
while True:
    landSize = input("Create farmland [5 to 16]: ")
    if landSize.isdigit(): #Checks if the user input is a number, if it is, then proceed to the next conditional statements
        if int(landSize) < 5 or int(landSize) > 16: #Converts the input to an integer, and checks if it is less than 5 or greater than 16 (the invalid inputs)
            print("Please enter a valid farm size [5 to 16]") 
        else: #If it is within the valid score, then sets the landsize equal the user input. 
            landSize = int(landSize)
            break
    else:
         print("You can only enter a number [5 to 16]")

renderFarm(landSize,farm) #Calls the function render Farm 

gameProper(farm)






