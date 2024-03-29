def get_instruction(instruction):
    instruction = [int(i) for i in str(instruction)]
    while len(instruction) < 5:
        instruction.insert(0, 0)
    return instruction


class Computer:
    def __init__(self, code, input=[]):
        self.code = code + [0 for i in range(100)]
        self.inputs = input
        self.input_counter = len(self.inputs)
        self.outputs = []
        self.halt = False
        self.name = None

    def execute(self):
        i = 0
        if self.name is not None:
            print(f'Name: {self.name}')

        while True:
            instruction = get_instruction(self.code[i])

            opcode = int(str(instruction[3]) + str(instruction[4]))

            parameter_1 = instruction[2]
            parameter_2 = instruction[1]
            parameter_3 = instruction[0]

            if parameter_1 == 1:
                index_1 = i + 1
            else:
                index_1 = self.code[i + 1]

            if parameter_2 == 1:
                index_2 = i + 2
            else:
                index_2 = self.code[i + 2]

            if parameter_3 == 1:
                index_3 = i + 3
            else:
                index_3 = self.code[i + 3]

            if opcode == 1:
                self.code[self.code[i + 3]] = self.code[index_1] + self.code[index_2]
                i += 4

            elif opcode == 2:
                self.code[self.code[i + 3]] = self.code[index_1] * self.code[index_2]
                i += 4

            elif opcode == 3:
                inputs = self.get_input()
                print(f'input: {inputs}')
                self.code[self.code[i + 1]] = inputs
                i += 2

            elif opcode == 4:
                print(f'output: {self.code[index_1]}')
                self.add_output(self.code[index_1])
                i += 2

            elif opcode == 5:
                if self.code[index_1] != 0:
                    i = self.code[index_2]
                else:
                    i += 3

            elif opcode == 6:
                if self.code[index_1] == 0:
                    i = self.code[index_2]
                else:
                    i += 3

            elif opcode == 7:
                if self.code[index_1] < self.code[index_2]:
                    self.code[index_3] = 1
                else:
                    self.code[index_3] = 0
                i += 4

            elif opcode == 8:
                if self.code[index_1] == self.code[index_2]:
                    self.code[index_3] = 1
                else:
                    self.code[index_3] = 0
                i += 4

            elif opcode == 99:
                self.halt = True
                break

    def replace(self, positions: dict):
        for position, value in positions.items():
            self.code[position] = value

    def get_input(self):
        if len(self.inputs) == 0:
            return int(input('input: '))
        else:
            return self.inputs[self.input_counter - 1]

    def add_output(self, output):
        self.outputs.append(output)

    def add_input(self, input):
        self.inputs.append(input)
        self.input_counter += 1


def file_to_list(file):
    with open(file) as f:
        code = f.read().split(',')
        for i in range(len(code)):
            code[i] = int(code[i])
        return code
