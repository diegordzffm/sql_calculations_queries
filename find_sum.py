'''def find_numbers_sum(numbers):
  """
  Finds pairs of numbers in the given list that sum to 1000.

  Args:
    numbers: A list of numbers.

  Returns:
    A list of tuples, where each tuple contains two numbers that sum to 1000.
  """

  count = 0
  for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
      if numbers[i] + numbers[j] == 245650.27:
        count += 1
  return count

# Example usage:
numbers = [0.00,	18560.11,	426.36,	64552.14,	77244.43,	44456.58,	2271.53, 5663.72,	63210.24,	3901.56, 105531.55,	2629.81, 516.50]
result = find_numbers_sum(numbers)
print("Numbers suming that:", result) '''




def find_numbers_summing_to_X(numbers):
  import itertools

  combinations = []
  for i in range(2, len(numbers) + 1):
    for subset in itertools.combinations(numbers, i):
      if sum(subset) == 245650.27:
        combinations.append(subset)

  return combinations

# Example usage:
numbers = [0.00,	18560.11,	426.36,	64552.14,	77244.43,	44456.58,	2271.53, 5663.72,	63210.24,	3901.56, 105531.55,	2629.81, 516.50]
result = find_numbers_summing_to_X(numbers)

if result:
  print("Combinations summing to X:")
  for combination in result:
    print(combination)
else:
  print("No combinations found that sum up to X.")
