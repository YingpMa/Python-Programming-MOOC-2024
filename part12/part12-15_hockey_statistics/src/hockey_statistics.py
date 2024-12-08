# Write your solution here
import json

class ExamineHockeyApplication:
    def __init__(self):
        self.file = []

    def open_file(self):
        while True:
            filename = input("file name: ")
            try:
                with open(filename) as my_file:
                    data = my_file.read()
                    self.file = json.loads(data)
                    return
            except:
                pass

    def help(self):
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def search_for_player(self):
        player = input("name: ")
        for item in self.file:
            if player == item["name"]:
                print(f"{item['name']:<20} {item['team']:<4} {item['goals']:>2} + {item['assists']:>2} = {item['goals'] + item['assists']:>3}")

    def teams(self):
        teams = sorted(list(set(map(lambda t: t["team"], self.file))))
        for team in teams:
            print(team)

    def countries(self):
        countries = sorted(list(set(map(lambda t: t["nationality"], self.file))))
        for country in countries:
            print(country)

    def players_in_team(self):
        team = input("team: ")
        players = [item for item in self.file if item["team"] == team]
        players.sort(key=lambda item: item["assists"] + item["goals"], reverse=True)
        for item in players:
            print(f"{item['name']:<20} {item['team']:<4} {item['goals']:>2} + {item['assists']:>2} = {item['goals'] + item['assists']:>3}")        

    def players_from_country(self):
        country = input("country: ")
        players = [item for item in self.file if item["nationality"] == country]
        players.sort(key=lambda item: item["assists"] + item["goals"], reverse=True)
        for item in players:
            print(f"{item['name']:<20} {item['team']:<4} {item['goals']:>2} + {item['assists']:>2} = {item['goals'] + item['assists']:>3}")     

    def most_points(self):
        number = int(input("how many: "))
        players = sorted(self.file, key=lambda item: (item["assists"]+ item["goals"], item["goals"]), reverse=True)
        players = players[:number]
        for item in players:
            print(f"{item['name']:<20} {item['team']:<4} {item['goals']:>2} + {item['assists']:>2} = {item['goals'] + item['assists']:>3}")           

    def most_goals(self):
        number = int(input("how many: "))
        players = sorted(self.file, key=lambda item: (item["goals"], -item["games"]), reverse=True)
        players = players[:number]
        for item in players:
            print(f"{item['name']:<20} {item['team']:<4} {item['goals']:>2} + {item['assists']:>2} = {item['goals'] + item['assists']:>3}")  

    def execute(self):
        self.open_file()
        print(f"read the data of {len(self.file)} players")
        self.help()
        while True:
            print()
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.search_for_player()
            elif command == "2":
                self.teams()
            elif command == "3":
                self.countries()
            elif command == "4":
                self.players_in_team()
            elif command == "5":
                self.players_from_country()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.most_goals()
            else:
                self.help()

app = ExamineHockeyApplication()
app.execute()