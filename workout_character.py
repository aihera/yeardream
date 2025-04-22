import time

class WorkoutCharacter:
    def __init__(self, name):
        self.name = name
    
    def hear_song(self, song_name):
        if song_name.lower() == "roxanne":
            self.perform_burpees()
        else:
            print(f"{self.name} is waiting for 'Roxanne' to play!")

    def perform_burpees(self):
        print(f"{self.name} heard 'Roxanne' and starts the burpee workout!")
        
        # Simulate burpee performance (let's assume 5 burpees for this example)
        for i in range(1, 6):
            print(f"Burpee {i}...")
            time.sleep(1)  # Wait 1 second between each burpee
        
        print(f"{self.name} finished the burpee workout!")

# Create a character
character = WorkoutCharacter("Charlie")

# Simulate hearing the song "Roxanne"
character.hear_song("Roxanne")

# Simulate hearing another song
character.hear_song("Another Song")
