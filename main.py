from zleague import ZLeague

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

# Team data
team_data = z.get_team_score()

# Scoreboard data
scoreboard_data = z.get_scoreboard()

