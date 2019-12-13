from __future__ import annotations

import itertools
from intcode import Computer, file_to_list

code = file_to_list('inputs/test.txt')


def part_a():
    combinations = itertools.permutations([0, 1, 2, 3, 4], 5)

    result = 0

    for combination in combinations:
        a = Computer(code, input=[combination[0], 0])
        a.execute()
        b = Computer(code, input=[combination[1], a.outputs[-1]])
        b.execute()
        c = Computer(code, input=[combination[2], b.outputs[-1]])
        c.execute()
        d = Computer(code, input=[combination[3], c.outputs[-1]])
        d.execute()
        e = Computer(code, input=[combination[4], d.outputs[-1]])
        e.execute()

        if e.outputs[-1] > result:
            result = e.outputs[-1]

    print(result)



def part_b():
    combinations = itertools.permutations([5, 6, 7, 8, 9], 5)

    result = 0

    combination = (9, 8, 7, 6, 5)

    a = Computer(code, input=[combination[0]])
    a.name = 'a'
    b = Computer(code, input=[combination[1]])
    b.name = 'b'
    c = Computer(code, input=[combination[2]])
    c.name = 'c'
    d = Computer(code, input=[combination[3]])
    d.name = 'd'
    e = Computer(code, input=[combination[4]])
    e.name = 'e'

    amplifiers = [a, b, c, d, e]

    a.add_input(0)

    def execute_all():
        for amplifier in amplifiers:
            amplifier.execute()

    execute_all()

    while a.halt:
        a.add_input(e.outputs[-1])
        b.add_input(a.outputs[-1])
        c.add_input(b.outputs[-1])
        d.add_input(c.outputs[-1])
        e.add_input(d.outputs[-1])

        execute_all()





part_b()
