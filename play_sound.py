import winsound

def play_note(frequency, duration):
    winsound.Beep(frequency, duration)

# Here you can rearange the notes so that the songs can play (Frequency, Duration)
theme_song = [
    (392, 500),  # G4
    (440, 500),  # A4
    (587, 500),  # D5
    (523, 500),  # C5
    (587, 500),  # D5
    (659, 1000), # E5
]
