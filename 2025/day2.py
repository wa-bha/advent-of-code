# Day 2: Gift Shop
# https://adventofcode.com/2025/day/2

def part1():
    ranges = []

    # Parse data from file
    with open("day2input.txt", "r") as file:
        # split by commas and store into an array
        ranges = file.read().strip().split(',')
    
    invalid_count = 0

    for r in ranges:
        start, end = map(int, r.split('-'))

        for number in range(start, end + 1):
            num_str = str(number)

            num_length = len(num_str)

            # we can skip all numbers with odd digit lengths
            if num_length % 2 != 0:
                continue

            # split it into half then compare the two halves
            mid = num_length // 2
            first_half = num_str[:mid]
            second_half = num_str[mid:]

            if first_half == second_half:
                invalid_count += int(number)

    return invalid_count

def part2():
    pass

print('Part 1 solution:', part1())
print('Part 2 solution:', part2())
