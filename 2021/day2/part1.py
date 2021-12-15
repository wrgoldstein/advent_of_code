sample_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2""".split("\n")

position = 0
depth = 0
for line in sample_input:
    direction, val = line.split()
    if direction == "forward":
        position += int(val)
    elif direction == "down":
        depth += int(val)
    elif direction == "up":
        depth -= int(val)

print(position * depth)
