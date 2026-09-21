class HostelPremierLeague:

    class Player:
        def __init__(self, id, name, hostel, team, runs=0, wickets=0):
            self.id = id
            self.name = name
            self.hostel = hostel
            self.team = team
            self.runs = runs
            self.wickets = wickets

        def player_info(self):
            return f"ID: {self.id} | Name: {self.name} | Hostel: {self.hostel} | Team: {self.team} | Runs: {self.runs} | Wickets: {self.wickets}"

    def __init__(self):
        self.players = []

    def add_player(self):
        id = int(input("Enter Player ID: "))
        name = input("Enter Player Name: ")
        hostel = input("Enter Hostel Name: ")
        team = input("Enter Team Name: ")

        p = self.Player(id, name, hostel, team)
        self.players.append(p)

        print("Player added successfully.")

    def show_players(self):
        if len(self.players) == 0:
            print("No players registered yet.")
        else:
            print("Players List ")
            for p in self.players:
                print(p.player_info())
            print()

    def update_score(self):
        id = int(input("Enter Player ID: "))

        for p in self.players:
            if p.id == id:
                runs = int(input("Enter Runs: "))
                wickets = int(input("Enter Wickets: "))

                p.runs = p.runs + runs
                p.wickets = p.wickets + wickets

                print("Score updated successfully.")
                return

        print("Player ID not found.")

    def search_player(self):
        id = int(input("Enter Player ID: "))

        for p in self.players:
            if p.id == id:
                print(p.player_info())
                return

        print("Player ID not found.")


hpl = HostelPremierLeague()

while True:
    print("HOSTEL PREMIER LEAGUE ")
    print("a. Add Player")
    print("b. View Players")
    print("c. Update Score")
    print("d. Search Player")
    print("e. Exit")

    ch = input("Enter choice: ")

    if ch == "a":
        hpl.add_player()

    elif ch == "b":
        hpl.show_players()

    elif ch == "c":
        hpl.update_score()

    elif ch == "d":
        hpl.search_player()

    elif ch == "e":
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")