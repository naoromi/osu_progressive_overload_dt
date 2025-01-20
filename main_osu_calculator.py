from beatmap_class import Beatmap

total_time = 0
playlist = []

def display_menu():
    
    print("1. Add beatmap")
    print("2. Remove beatmap")
    print("3. Display beatmaps")
    print("4. Exit")
    print("5. Calculate total time")



    if display_menu() == 1:

        playlist.append(Beatmap("beatmap_name"))


playlist.append(Beatmap("beatmap_name"))