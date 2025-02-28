import random as r

song_playlist = ["Tears in her Fanta by Black Kray", "Diamonds by ThaiBoy Digital", "Poppin my Collar by Three Six Mafia", "News or Something by Future", "October by Girl in Red", "Back 2 the Basics by Summrs", "Entombed by Deftones", "Guardian by Tigers Jaw", "Never Meant by American Football", "Drunk Punx by Lil Tracy"]
shuffle_playlist = []

playlist_length = int(input("How many songs would you like to listen to?: "))

shuffle_playlist = r.sample(song_playlist, playlist_length)

print("Your shuffled playlist:")
for song in shuffle_playlist:
    print(song)