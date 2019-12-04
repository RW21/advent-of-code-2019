def run(code)
  code.each_with_index do |n, i|
    next unless (i % 4).zero?

    code[code[i + 3]] = code[code[i + 1]] + code[code[i + 2]] if n == 1
    code[code[i + 3]] = code[code[i + 1]] * code[code[i + 2]] if n == 2
    break if n == 99
  end
  code
end

code = File.read('inputs/day_2.txt').split(',').map(&:to_i)

code_copy = code.dup
code_copy[1] = 12
code_copy[2] = 2
p run(code_copy)

done = false

(0..99).each do |noun|

  (0..99).each do |verb|

    code_copy_1 = code.dup
    code_copy_1[1] = noun
    code_copy_1[2] = verb

    next unless run(code_copy_1)[0] == 19_690_720
    
    p noun, verb
    done = true
    break

  end

  break if done

end
