class FlightMatch:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

class FlightMatchTable:
    def __init__(self):
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def list_matches_by_team(self, team_name):
        team_matches = [match for match in self.matches if team_name in (match.team1, match.team2)]
        return team_matches

    def list_matches_by_location(self, location):
        location_matches = [match for match in self.matches if location == match.location]
        return location_matches

    def list_matches_by_timing(self, timing):
        timing_matches = [match for match in self.matches if timing == match.timing]
        return timing_matches

def main():
    flight_match_table = FlightMatchTable()

    flight_match_table.add_match(FlightMatch("Mumbai", "India", "Sri Lanka", "DAY"))
    flight_match_table.add_match(FlightMatch("Delhi", "England", "Australia", "DAY-NIGHT"))
    flight_match_table.add_match(FlightMatch("Chennai", "India", "South Africa", "DAY"))
    flight_match_table.add_match(FlightMatch("Indore", "England", "Sri Lanka", "DAY-NIGHT"))
    flight_match_table.add_match(FlightMatch("Mohali", "Australia", "South Africa", "DAY-NIGHT"))
    flight_match_table.add_match(FlightMatch("Delhi", "India", "Australia", "DAY"))

    while True:
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            team_name = input("Enter the team name: ")
            team_matches = flight_match_table.list_matches_by_team(team_name)
            for match in team_matches:
                print(f"{match.team1} vs {match.team2} at {match.location}, {match.timing}")
        elif choice == 2:
            location = input("Enter the location: ")
            location_matches = flight_match_table.list_matches_by_location(location)
            for match in location_matches:
                print(f"{match.team1} vs {match.team2} at {match.location}, {match.timing}")
        elif choice == 3:
            timing = input("Enter the timing: ")
            timing_matches = flight_match_table.list_matches_by_timing(timing)
            for match in timing_matches:
                print(f"{match.team1} vs {match.team2} at {match.location}, {match.timing}")
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
