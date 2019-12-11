def get_indirect_orbits(orbits, target):
    count = 0
    while target in orbits:
        target = orbits[target]
        count += 1

    return count - 1


def get_total_orbits(orbits, target):
    count = 0
    while target in orbits:
        target = orbits[target]
        count += 1

    return count


with open('inputs/day_6.txt') as f:
    lines = f.readlines()

orbits = {}

for line in lines:
    line = line.split(')')

    child = line[1][:3].replace('\n', '')
    parent = line[0]

    orbits[child] = parent

# part A

count = 0
for orbit in orbits.keys():
    count += get_total_orbits(orbits, orbit)

print(count)

