lower_range = 248345
upper_range = 746315

def verify(number)
  adjacency = false

  number = number.digits.reverse
  previous_num = number.first

  number.each_with_index do |n, i|
    return false if n < previous_num

    adjacency = true if previous_num == n && !i.zero?
    previous_num = n

  end
  adjacency
end

def verify_b(number)
  number = number.digits.reverse

  (0..4).each do |i|
    return false if number[i] > number[i + 1]
  end

  count = number.each_with_object({}) do |n, memo|
    d = memo[n] || 0
    d += 1
    memo[n] = d
  end
  count.values.member?(2)
end

count = 0

(lower_range..upper_range).each do |n|
  count += 1 if verify(n)
end

p count

count = 0

(lower_range..upper_range).each do |n|
  count += 1 if verify_b(n)
end

p count


