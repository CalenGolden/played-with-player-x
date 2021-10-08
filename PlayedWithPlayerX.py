#Thanks to Farzain for his YouTube tutorial on how to work with Riot's API.
import requests

#JSON request for the summoner data of the entered player to get the playerID
def requestSummonerData(region, summonerName, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    print(URL)
    response = requests.get(URL)
    return response.json()

#Uses the above playerID to access the player's match history
def requestMatchHistory(region, ID, APIKey):
    URL = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/" + ID + "/ids?start=0&count=50&api_key=" + APIKey
    print(URL)
    response = requests.get(URL)
    return response.json()

#Retrieves the data of a specific match from the match history
def requestMatch(region, gameId, APIKey):
    URL = "https://americas.api.riotgames.com/lol/match/v5/matches/" + gameId + "?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()

def main():

    x = 0
    i = 0
    count = 0
    print("Type in one of the following regions\n")
    print("na1 or EUW\n")

    #Prompting the user to enter their region, summoner name, and APIKey for accessing the JSON files
    region = (str)(input('Type in one of the regions above: '))
    summonerName = (str)(input('Type your Summoner Name here and DO NOT INCLUDE ANY SPACES: '))
    checkName = ((str)(input('Type the Summoner Name you wish to check for: '))).replace(" ", "%")
    APIKey = (str)(input('Copy and paste your API Key here: '))
    summonerDataInfo  = requestSummonerData(region, summonerName, APIKey)

    #JSON request for player match history
    playerID = summonerDataInfo['puuid']
    playerID = str(playerID)
    matchHistoryInfo = requestMatchHistory(region, playerID, APIKey)

    checkerResponse  = requestSummonerData(region, checkName, APIKey)
    checkerID = checkerResponse['puuid']
    checkerID = str(checkerID)



    #Iteratively loop through the match history to check for the specified summoner name
    for x in range(20):
        gameId = matchHistoryInfo[x]
        gameId = str(gameId)
        matchInfo = requestMatch(region, gameId, APIKey)
        i = 0

        for i in range(10):
            if matchInfo['metadata']['participants'][i] == checkerID:
                count += 1
                break

    count = str(count)
    print("In the last 20 games you have played with " + checkName + " " + count + " time(s)!")


if __name__ == "__main__":
    main()

