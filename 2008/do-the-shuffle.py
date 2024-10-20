# Hemit Patel
# ICS3U0-4 
# MR VEERA 
# 781159
# 20 oct 2024 
songs = ["A", "B", "C", "D", "E"]

while True:

    button = int(input(""))
    amount_pressed = int(input(" "))

    if button == 1:
        # Shift the first song to the end
        for _ in range(amount_pressed):
            songs = songs[1:] + [songs[0]]
    elif button == 2:
        # Shift the last song to the start
        for _ in range(amount_pressed):
            songs = [songs[4]] + songs[0:4]
    
    elif button == 3:
        for _ in range(amount_pressed):
            songs = [songs[1]] + [songs[0]] + songs[2:]
    elif button == 4:
        songs_output = ""

        for song in songs:
            songs_output += song + " "
        
        print(songs_output)
        break;