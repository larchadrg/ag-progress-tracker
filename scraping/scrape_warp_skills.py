import os 

# Set up the path to the data directory
DIR = r'C:\Users\larac\Documents\ag-progress-tracker\app\static\images\warp_skills'
files = os.listdir(DIR)
ws_names = [
    "Power UP: Melee",
    "Precision Hub",
    "Telekinesis Vector I",
    "Evolution Particle IV",
    "Flashback Core IV",
    "The Executioner",
    "Brownian Motion",
    "Life-sustaining",
    "Power UP: Ranged",
    "Evolution Particle I",
    "Flashback Core I",
    "Telekinesis Vector IV",
    "The Judge",
    "Curveaway",
    "Insulating Armor",
    "Critical Support"
]

# Create a dictionary to store the data
data = {}
for i in range(len(files)): 
    data[ws_names[i]] = files[i]

for key, value in data.items():
    print(key, value)