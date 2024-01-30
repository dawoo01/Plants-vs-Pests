def loadLeaderboards(dictionary): #Function for loading the leaderboards
	readHandle = open("leaderboard.dat", "r")
	for line in readHandle:
		data = line.split(",")
		user, score, landSize, time = data #Sequence Unpacking
		holder = {
			"Player": user,
			"Score": int(score),
			"Farmsize": int(landSize),
			"Time": float(time)
			}
		dictionary[user] = holder #adds the holder to the leaderboards dictionary
	return dictionary


def saveLeaderboards(dictionary): #Function for saving the leaderboards
	fileHandle = open("leaderboard.dat", "a")
	for key1,key2 in dictionary.items(): #Sequence Unpacking
		fileHandle.write(f"{key1},{key2['Score']},{key2['Farmsize']},{key2['Time']}\n") #adds the details of the game run (including the player name, score, farmsize, and time elapsed) in the leaderboards dictionary to leaderboard.dat
	fileHandle.close()