require 'set'


class Wire
  attr_accessor :points, :current

  def initialize(x, y)
    @x = x
    @y = y
    @points = Set.new
    @current = [0, 0]
    @count = {}
  end

  def add(distance)
    case distance[0]
    when 'U'
      distance[1..distance.length].to_i.times do
        @current[1] += 1
        @points.add(current.dup)
      end


    when 'R'
      distance[1..distance.length].to_i.times do
        @current[0] += 1
        points.add(current.dup)
      end


    when 'D'
      distance[1..distance.length].to_i.times do
        @current[1] -= 1
        @points.add(@current.dup)
      end


    when 'L'
      distance[1..distance.length].to_i.times do
        @current[0] -= 1
        @points.add(@current.dup)
      end
    end
  end
end


wire_a = Wire.new(0, 0)
wire_b = Wire.new(0, 0)

File.readlines('inputs/day_3.txt').each_with_index do |line, i|
  line.split(',').each do |distance|
    if i.zero?
      wire_a.add(distance)

    else
      wire_b.add(distance)
    end
  end
end


intersection = wire_b.points.intersection(wire_a.points)
minimum = intersection.first[0].abs + intersection.first[1].abs

intersection.each do |i|
  distance = i[0].abs + i[1].abs
  minimum = distance if minimum > distance
end

p minimum
