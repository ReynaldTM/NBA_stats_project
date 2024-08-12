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
    games = get(BASE_URL + scoreboard).json()["games"]  # accessing list

    for game in games:  # loop through and printiing individual list item
        home_team = game["hTeam"]
        away_team = game["vTeam"]
        clock = game["clock"]
        period = game["period"]

        print("------------------------------------------------------------------")
        print(f"{home_team["tricode"]} vs {away_team["tricode"]}, {clock}, {period}")
        print(f"{home_team["score"]} - {away_team["score"]}")
        print(f"{clock} - {period['current']}")


def get_stats():
    stats = get_links()["leagueTeamStatsLeaders"]
    teams = get(
        BASE_URL + stats).json()["league"]["standard"]["regularSeason"]["teams"]

    teams = list(filter(lambda x: x["team" != "Team"], teams))
    # runs anon function on every element to filter
    #  where team key doesn't equal team. returns object, not list
    teams.sort(key=lambda x: int(x["ppg"]["rank"]))  # ppg is dict containing ranks, sort desc after converting to int

    for i, team in enumerate(teams):
        name = team["name"]
        nickname = team["nickname"]
        ppg = team["ppg"]["avg"]
        print(f"{i + 1}. {name} - {nickname}, {ppg}")


get_scoreboard()
