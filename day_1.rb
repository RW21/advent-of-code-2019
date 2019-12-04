sum = 0

File.readlines("inputs/day_1.txt").each do |line|
  mass = line.delete("\n").to_i
  sum += (mass / 3).floor - 2
end

p sum

