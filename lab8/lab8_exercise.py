# -----------------------------------
# Example 3 (Lab Exercise): working with external APIs (EPL)
# Complete points a, b, c, d, and e from ex 3
# -----------------------------------

# step 1, data collections
# a. download the csv file
import requests
import pandas as pd

original_url = "https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/en.1.csv"
working_url  = "https://raw.githubusercontent.com/footballcsv/england/master/2020s/2020-21/eng.1.csv"

file_name = "epl_matches.csv"

print(f"\nDownloading external file!...")
print("Attempting original URL first...")
response = requests.get(original_url)
print(f"Original URL status code: {response.status_code}")

if response.status_code != 200:
    print("Original URL failed (404). Switching to working mirror URL...")
    response = requests.get(working_url)
    print(f"Working URL status code: {response.status_code}")

if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
    print("Download complete!")
else:
    print("Download failed!")
    raise SystemExit("Stopping because the CSV file did not download.")


# step 2, create dataframe
# b. load dataframe from a csv file
matches = pd.read_csv(file_name, header=None)

# Most footballcsv EPL files follow this structure:
# Round, Date, HomeTeam, Score, AwayTeam
matches.columns = ["Round", "Date", "HomeTeam", "Score", "AwayTeam"]

print("\nMatches from csv file")
print(matches.head())


# step 3, working with the data in the dataframe
# c. filter Team vs Team (choose any two teams)
team_a = "Arsenal"
team_b = "Chelsea"

team_a_vs_team_b = matches[
    ((matches["HomeTeam"].str.contains(team_a, na=False)) & (matches["AwayTeam"].str.contains(team_b, na=False))) |
    ((matches["HomeTeam"].str.contains(team_b, na=False)) & (matches["AwayTeam"].str.contains(team_a, na=False)))
].copy()

print(f"\n{team_a} vs {team_b} games")
print(team_a_vs_team_b)

# split the Score column like "2-1" into numeric goals
score_split = team_a_vs_team_b["Score"].astype(str).str.split("–", expand=True)
team_a_vs_team_b["HomeGoals"] = pd.to_numeric(score_split[0], errors="coerce")
team_a_vs_team_b["AwayGoals"] = pd.to_numeric(score_split[1], errors="coerce")

team_a_home_games = team_a_vs_team_b[team_a_vs_team_b["HomeTeam"].str.contains(team_a, na=False)]
team_a_away_games = team_a_vs_team_b[team_a_vs_team_b["AwayTeam"].str.contains(team_a, na=False)]

print(f"\n{team_a} home games vs {team_b}")
print(team_a_home_games)

print(f"\n{team_a} away games @ {team_b}")
print(team_a_away_games)


# d. calculate averages of the home and away matches
home_avg_goals_for     = team_a_home_games["HomeGoals"].mean()
home_avg_goals_against = team_a_home_games["AwayGoals"].mean()
home_avg_goal_diff     = (team_a_home_games["HomeGoals"] - team_a_home_games["AwayGoals"]).mean()

away_avg_goals_for     = team_a_away_games["AwayGoals"].mean()
away_avg_goals_against = team_a_away_games["HomeGoals"].mean()
away_avg_goal_diff     = (team_a_away_games["AwayGoals"] - team_a_away_games["HomeGoals"]).mean()

print(f"\n{team_a} HOME avg goals for = {home_avg_goals_for}")
print(f"{team_a} HOME avg goals against = {home_avg_goals_against}")
print(f"{team_a} HOME avg goal diff = {home_avg_goal_diff}")

print(f"\n{team_a} AWAY avg goals for = {away_avg_goals_for}")
print(f"{team_a} AWAY avg goals against = {away_avg_goals_against}")
print(f"{team_a} AWAY avg goal diff = {away_avg_goal_diff}")


# e. visualization of data analysis
import matplotlib.pyplot as plt

metrics = ["Goals For", "Goals Against", "Goal Diff"]
home_values = [home_avg_goals_for, home_avg_goals_against, home_avg_goal_diff]
away_values = [away_avg_goals_for, away_avg_goals_against, away_avg_goal_diff]

x = range(len(metrics))
bar_width = 0.35

plt.figure(figsize=(9, 5))
plt.bar([i - bar_width/2 for i in x], home_values, width=bar_width, label='Home')
plt.bar([i + bar_width/2 for i in x], away_values, width=bar_width, label='Away')

plt.xticks(list(x), metrics)
plt.title(f"{team_a} vs {team_b} (2020–21) — Home vs Away Averages")
plt.ylabel("Average value")
plt.legend()
plt.savefig("epl_graph.png")
plt.show(block=True)

input("Press Enter to close...")

# graph not displayed in codespaces environment, saved locally using plt.savefig("epl_graph.png")