import requests, json
from os import environ as env

class Query:
    def __init__(self):
        pass

    def fetch_movie(self):
        apiKey = env['OMDB_API_KEY']
        continueProgram = True
        while continueProgram:
            validInput = False
            while validInput == False:
                movieTitle = input("Enter the name of the film: ")
                if len(movieTitle) < 1:
                    print("Invalid film title")
                else:
                    validInput = True

            data_URL = 'http://www.omdbapi.com/?apikey=' + apiKey
            params = {
                't': movieTitle
            }
            response = requests.get(data_URL, params=params)
            response_values = json.loads(response.text)

            if response_values['Response'] == 'False':
                print("Movie does not exist")
            else:
                ratings = response_values['Ratings']
                rotten = ""
                for r in ratings:
                    if r['Source'] == 'Rotten Tomatoes':
                        rotten = r['Value']
                if rotten == "":
                    print("This movie has no Rotten Tomatoes rating")
                else:
                    print("Rotten Tomatoes Rating: ", rotten)

            inp = input("Press q to exit or \'Enter\' to continue")
            if inp == "q":
                continueProgram = False
