import pandas as pd

matches =pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")


#basic explore
print("matches shape: ", matches.shape)
print("deliveries shape: ", deliveries.shape)
print("\nmatches columns: ")
print(matches.columns.tolist())



# Pehli 5 rows 
print(matches.head())

# Kitne seasons hain
print("\nSeasons:", matches["season"].unique())

# Kaun kitni baar jeeta
print("\nTop Teams:")
print(matches["winner"].value_counts().head(10))



import matplotlib.pyplot as plt

# Top 10 teams ka bar chart
top_teams = matches["winner"].value_counts().head(10)

plt.figure(figsize=(12,6))
plt.bar(top_teams.index, top_teams.values, color="blue")
plt.title("IPL - Top 10 Winning Teams")
plt.xlabel("Teams")
plt.ylabel("Wins")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# Toss Analysis
toss_match = matches[matches["toss_winner"] == matches["winner"]]
percentage = round(len(toss_match) / len(matches) * 100, 2)
print(" %  Toss winning team wins the match:", percentage, "%")



# Season wise matches
season_matches = matches.groupby("season").size()
print(season_matches)

plt.figure(figsize=(12,6))
plt.plot(season_matches.index, season_matches.values, marker="o", color="green")
plt.title("IPL - Matches Per Season")
plt.xlabel("Season")
plt.ylabel("Matches")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# Top 10 Players
top_players = matches["player_of_match"].value_counts().head(10).sort_values()
print(top_players)
plt.figure(figsize=(12,6))
plt.barh(top_players.index, top_players.values, color="orange")
plt.title("IPL - Top 10 Player of the Match")
plt.xlabel("Times Won")
plt.ylabel("Players")
plt.tight_layout()
plt.show()