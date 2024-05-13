def wordCounter(S):
  counts = {}
  for char in S:
    if char not in counts:
      counts[char] = 0
    counts[char] += 1
  return counts


# Example usage:

S = "upflairs pvt ltd"
counts = wordCounter(S)
print(counts)