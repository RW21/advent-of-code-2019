def get_fuel_for_fuel(fuel_mass)
  fuel_for_fuel = 0

  while true
    fuel_mass = get_fuel(fuel_mass)
    if fuel_mass <= 0
      break
    end
    fuel_for_fuel += fuel_mass
  end

  fuel_for_fuel
end

def get_fuel(mass)
  mass = (mass / 3).floor - 2
end

sum_a = 0
sum_b = 0

File.readlines("inputs/day_1.txt").each do |line|
  mass = line.delete("\n").to_i
  fuel = get_fuel(mass)

  sum_a += fuel
  sum_b += fuel + get_fuel_for_fuel(fuel)
end

p sum_a
p sum_b



