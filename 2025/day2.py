# {name}
# {link}

def part1():
    ranges = []

    # Parse data from file
    with open("day2input.txt", "r") as file:
        # split by commas and store into an array
        ranges = file.read().strip().split(',')
    
    ranges = [list(map(int, r.split('-'))) for r in ranges]

    print(ranges)

    # for each range, check each number in the range and see if it has a repeated sequence of digits
    invalid_count = 0

    for r in ranges:
        print(r)
        for number in range(r[0], r[1] + 1):
            num_str = str(number)
            has_repeated = False

            # split it into half then compare the two halves
            mid = len(num_str) // 2
            first_half = num_str[:mid]
            second_half = num_str[mid:]

            if first_half == second_half:
                has_repeated = True
                invalid_count += int(number)
                print(f'Invalid number found: {number}')

    return invalid_count

def part2():
    pass

print('Part 1 solution:', part1())
print('Part 2 solution:', part2())
