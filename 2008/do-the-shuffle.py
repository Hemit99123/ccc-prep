# Hemit Patel
# ICS3U0-4 
# MR VEERA 
# 781159
# 20 oct 2024 
# ccc 2008 j2

# we initalize the default values for song before the true loop because inside the loop it would be reset each time a new sequence is ran
# meaning the shifted songs would not remain the same but be replaced with the default songs value again

songs = ["A", "B", "C", "D", "E"]


# running this logic repeately until btn 4 is pressed
while True:

    button = int(input("Enter the button:"))
    amount_pressed = int(input("How many times is this button pressed:"))

    if button == 1:
        # Shift the first song to the end
        for _ in range(amount_pressed):
            # here we are taking all values from the second place and onwards 
            # we are shifting that before the initial value which means that the first value is now the last value with others is untouched
            songs = songs[1:] + [songs[0]]
    elif button == 2:
        # Shift the last song to the start
        for _ in range(amount_pressed):
            # opposite logic here
            # we are taking all values from first onwards
            # we then shift the last song to the first place by adding it first and then the rest of the list
            # for songs[0:4] we need to spiecify the limit as 4 so it doesn't include 4 as the upper-limit is non-inclusive
            # so it is from 0 to 3 which is what we want as the idx 4 is being put forward of the other songs

            songs = [songs[4]] + songs[0:4]
    
    elif button == 3:
        for _ in range(amount_pressed):
            # here we swap the first 2 digits, hence why idx 1 is being added first before 0
            # then the remaning songs are added aferwards the swap is made
            songs = [songs[1]] + [songs[0]] + songs[2:]
    elif button == 4:
        songs_output = ""
        # these songs are in a list so we are putting them into a string for the proper output by iterating over them
        for song in songs:
            # here is where we add to the string itself
            songs_output += song + " "
        # now print the final songs output before breaking out of the loop to end this computer program (application)
        print(songs_output)
        break;
