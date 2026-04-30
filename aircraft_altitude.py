from aircraft import Aircraft

model = input("Enter aircraft model:\n")
plane = Aircraft(model)

while True:
    command = input("Enter command (A for ascent, D for descent, X to exit):\n")
    parts = command.split()

    if parts[0] == "X":
        break
    elif parts[0] == "A":
        plane.climb(int(parts[1]))    
    elif parts[0] == "D":
        plane.descend(int(parts[1]))

print(f"Final altitude: {plane.altitude} feet")