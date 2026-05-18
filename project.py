import random

# --- Features ---
def shuffle_song(playlist, moods):
    if not moods:
        print("No moods available yet!")
        return
    mood = random.choice(list(moods))
    if playlist[mood]:
        song = random.choice(playlist[mood])
        print("\n Random Pick:")
        print(f"Mood: {mood}")
        print(f"Song: {song}")
    else:
        print(f"\nMood: {mood} has no songs yet!")

def study_booster(playlist):
    booster_songs = ["Lo-Fi Beats", "Piano Focus", "Coding Chill"]
    if "Study" in playlist:
        if not playlist["Study"]:
            playlist["Study"].extend(booster_songs)
            print("\n Study Booster activated!")
            print("Added default focus tracks:", ", ".join(booster_songs))
        else:
            print("\n Study mood already has songs!")
    else:
        print("No Study mood found yet.")

def mood_suggestions(playlist):
    suggestions = {
        "Sad": "Happy",
        "Happy": "Chill",
        "Study": "Chill",
        "Workout": "Relax"
    }
    for mood, songs in playlist.items():
        if len(songs) >= 3:  # threshold
            if mood in suggestions:
                print(f"\n You’ve added many songs to {mood} mood.")
                print(f"Try adding something to {suggestions[mood]} mood for balance!")

def show_playlists(playlist):
    print("\n🎶 All Moods and Playlists:")
    for mood, songs in playlist.items():
        print(f"\nMood: {mood}")
        if songs:
            print("Songs:", ", ".join(songs))
        else:
            print("Songs: No songs yet")
        print("-" * 30)

# --- Main Program ---
moods = set()
playlist = {}

while True:
    print("\n--- Playlist Menu ---")
    print("1. Add Mood")
    print("2. Add Song")
    print("3. Show Playlists")
    print("4. Shuffle Song")
    print("5. Study Booster")
    print("6. Mood Suggestions")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        mood_name = input("Enter mood name: ")
        if mood_name not in moods:
            moods.add(mood_name)
            playlist[mood_name] = []
            print(f"Mood '{mood_name}' added!")
        else:
            print("Mood already exists!")

    elif choice == "2":
        mood_name = input("Enter mood name: ")
        if mood_name not in moods:
            moods.add(mood_name)
            playlist[mood_name] = []
        song_name = input(f"Enter a song for {mood_name}: ")
        playlist[mood_name].append(song_name)
        print(f"Song '{song_name}' added to {mood_name} mood!")

    elif choice == "3":
        show_playlists(playlist)

    elif choice == "4":
        shuffle_song(playlist, moods)

    elif choice == "5":
        study_booster(playlist)

    elif choice == "6":
        mood_suggestions(playlist)

    elif choice == "7":
        print("Exiting... Goodbye! ")
        break

    else:
        print("Invalid choice, try again!")
