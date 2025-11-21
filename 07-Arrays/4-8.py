computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]
counter = 1
computer_games = sorted(computer_games)
while counter <= len(computer_games):
    for game in computer_games:
        print(f'{counter}. {game}')
        counter += 1