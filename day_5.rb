INPUT = 1

def is_OP?(number)

end

def get_instruction(number)
  instruction = number.digits
  instruction.append(0) while instruction.length != 5
  instruction
end

def get_value(code, index, immediate)
  if immediate
    code[index]
  else
    code[code[index]]
  end
end


def run(code)
  # process input
  code[code[1]] = INPUT

  code.each_with_index do |n, i|
    next unless (i % 4) == 2
    instruction = get_instruction(n)

    num_1 = if instruction[2].zero?
              code[code[i + 1]]
            else
              code[i + 1]
            end

    num_2 = if instruction[3].zero?
              code[code[i + 2]]
            else
              code[i + 2]
            end

    case instruction[0]
    when 1
      code[code[i + 3]] = num_1 + num_2

    when 2
      code[code[i + 3]] = num_1 * num_2
    when 3
      
    when 4
      p code[code[i + 1]]
    end

  end
  code
end

code = File.read('inputs/day_5.txt').split(',').map(&:to_i)

run(code)