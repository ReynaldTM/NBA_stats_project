from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"  # base site
ALL_JSON = "/prod/v1/today.json"  # specific data point

printer = PrettyPrinter()


def get_links():  # request to ALL_JSON to access scoreboard
    data = get(BASE_URL + ALL_JSON).json()  # like python dict
    links = data["links"]
    return links


def get_scoreboard():  # send request for currentscoreboard, then print
    scoreboard = get_links()["currentscoreboard"]
    games = get(BASE_URL + scoreboard).json()["games"] # accessing list

    for game in games: # printiing individual list item
        home_team = game["hTeam"]
        away_team = game["vTeam"]
        clock = game["clock"]
        period = game["period"]

        print("------------------------------------------------------------------")
        print(f"{home_team["tricode"]} vs {away_team["tricode"]}, {clock}, {period}")
        print(f"{home_team["score"]} - {away_team["score"]}")
        print(f"{clock} - {period['current']}")


get_scoreboard()
