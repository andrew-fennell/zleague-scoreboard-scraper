import sys
import time
from selenium import webdriver
import warnings

# A few deprecated libraries/functions used
warnings.filterwarnings("ignore", category=DeprecationWarning)


class ZLeague:
    def __init__(self, team_name, scoreboard_url):
        # Initialize variables
        self.team_name = team_name
        self.scoreboard_url = scoreboard_url

        # Session variables
        self.s = None

        self.scoreboard = []

        # Scoreboard information
        self.team_data = {
            "team_name": None,
            "place": None,
            "division": None,
            "total_games": None,
            "best_2_wins": None,
            "best_2_kills": None,
            "placement_points": None,
            "total_points": None,
            "points_behind_leader": None,
        }

    def connect(self):
        # Setup session variables for Chrome webdriver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.s = webdriver.Chrome(
            executable_path="./chromedriver.exe", options=chrome_options
        )

    def get_scoreboard_data(self):
        """Scrape scoreboard data."""

        # Get ZLeague scoreboard
        self.s.get(self.scoreboard_url)
        print("Getting scoreboard...")
        time.sleep(1)

        # Get scoreboard data
        table = self.s.find_element_by_tag_name("tbody")

        # Parse data
        rows = table.text.split("\n")

        for i in range(0, len(rows), 3):
            rows_team_data = {
                "team_name": None,
                "place": None,
                "division": None,
                "total_games": None,
                "best_2_wins": None,
                "best_2_kills": None,
                "placement_points": None,
                "total_points": None,
                "points_behind_leader": None,
            }

            rows_team_data["place"] = rows[i]
            rows_team_data["team_name"] = rows[i + 1]
            (
                rows_team_data["division"],
                rows_team_data["total_games"],
                rows_team_data["best_2_wins"],
                rows_team_data["best_2_kills"],
                rows_team_data["placement_points"],
                rows_team_data["total_points"],
                rows_team_data["points_behind_leader"],
            ) = rows[i + 2].split(" ")

            self.scoreboard.append(rows_team_data)

            if self.team_name == rows[i + 1]:
                self.team_data = rows_team_data

        self.s.close()

        return self.scoreboard

    def get_scoreboard(self):
        """Returns the entire scoreboard."""
        return self.scoreboard

    def get_team_score(self):
        """Returns your team's score."""
        return self.team_data

    def print_scoreboard(self):
        for x in self.scoreboard:
            print("-------------------------------------------")
            for key in x.keys():
                print(f"{key}: {x[key]}")

        print("-------------------------------------------")

    def print_team_score(self):
        print("-------------------------------------------")
        for key in self.team_data.keys():
            print(f"{key}: {self.team_data[key]}")
        print("-------------------------------------------")


if __name__ == "__main__":
    team_name = input("Enter your team name: ")
    scoreboard_url = input("Enter your scoreboard url: ")

    # Initialize ZLeague object
    z = ZLeague(team_name, scoreboard_url)

    # Initiate session that will connect to ZLeague.gg
    z.connect()

    # Get scoreboard data from ZLeague
    data = z.get_scoreboard_data()

    # Print team's scoreboard data
    z.print_team_score()
