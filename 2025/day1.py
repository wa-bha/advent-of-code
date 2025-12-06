# Day 1: Secret Entrance
# https://adventofcode.com/2025/day/1

def part1():
    dial = 50
    direction = []
    distance = []

    number_of_times_turned = 0

    # Parse data from file
    with open("day1input.txt", "r") as file:
        for line in file:
            direction.append(line[:1])
            distance.append(int(line[1:]))

    for i in range(len(direction)):
        # Turn the dial
        if direction[i] == 'L':
            dial -= distance[i]
        elif direction[i] == 'R':
            dial += distance[i]
        
        # Wrap around the dial
        if dial < 0 or dial > 99:
            dial = dial % 100
        
        # Check if we've returned to 0
        if dial == 0:
            number_of_times_turned += 1

    return number_of_times_turned
    
def part2():
    pass

print('Part 1 solution:', part1())
print('Part 2 solution:', part2())
