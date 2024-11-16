import pywhatkit as kit
import random

def play_music():
    # List of song titles or genres
    songs = [
        "Shape of You by Ed Sheeran",
        "Blinding Lights by The Weeknd",
        "Levitating by Dua Lipa",
        "Imagine Dragons hits",
        "Pop music hits",
        "Bollywood top songs",
        "Classical music playlist",
        "Jazz classics",
        "Top hits 2024",
        "Rock legends playlist"
    ]
    
    # Choose a random song or genre
    song_to_play = random.choice(songs)
    
    # Play it on YouTube
    kit.playonyt(song_to_play)
    print(f"Playing: {song_to_play}")
