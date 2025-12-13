# Day 1: Secret Entrance
# https://adventofcode.com/2025/day/1

def part1():
    dial = 50  # Starting position of the dial
    number_of_times_turned = 0

    # Parse data from file
    with open("day1input.txt", "r") as file:
        for line in file:
            direction = -1 if line[:1] == 'L' else 1 # Left or Right
            distance = int(line[1:])

            # Turn the dial in the specified direction
            dial += (direction * distance)
        
            # Wrap around the dial (to ensure it's always between 0 and 99)
            dial = dial % 100
            
            # Check if we've returned to 0
            if dial == 0:
                number_of_times_turned += 1

    return number_of_times_turned
    
def part2():
    dial = 50  # Starting position of the dial
    number_of_times_turned = 0

    # Parse data from file
    with open("day1input.txt", "r") as file:
        for line in file:
            direction = 1 if line[:1] == 'R' else -1 # Left or Right
            distance = int(line[1:])

            # Turn the dial in the specified direction
            dial += (direction * distance)

            print("The dial is rotated", line.strip("\n"), "to position", dial % 100)

            rotations = (abs(dial) // 100)

            # Check if we crossed 0 during the turn
            if (dial > -100 and dial < 0 and direction == -1):
                rotations += 1

            if (rotations > 0):
                number_of_times_turned += rotations
                print("[TOTAL]:", number_of_times_turned, "The dial rotated past 0", rotations, "times")

            # Wrap around the dial (to ensure it's always between 0 and 99)
            dial = dial % 100

            if (dial == 0):
                number_of_times_turned += 1
                print("[TOTAL]:", number_of_times_turned, "The dial was equal to 0")
                

    return number_of_times_turned

print('Part 1 solution:', part1())
print('Part 2 solution:', part2())
