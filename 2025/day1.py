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
    pass

print('Part 1 solution:', part1())
print('Part 2 solution:', part2())
