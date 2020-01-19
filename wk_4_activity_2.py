"""
The Order Of Operations Demonstration Program

This program demonstrates how the Python follows order of operations. It also
demonstrates how numerical comparisons are made.
To use it, run 'python wk_4_activity_2.py'
"""

# Prints the statement "I will now count my chickens:"
print("I will now count my chickens:")

# Calculates 30 divided by 6 = 5 then adds 25. The result is 30.
print("Hens", (25 + 30 / 6))

# Calculates 25 multipled by 3 = 75 then determines the modulus(the amount
# remaining when 75 divided 4). The modulus is 3. Then performes 100 subtract 3.
# The result is 97.
print("Roosters", (100 - 25 * 3 % 4))

# Prints the statement "Now I will count the eggs:"
print("Now I will count the eggs:")

# Calculates 4 modulus 2 = 0 and 1 divided by 4 = 0.25. By following order of
# operations the math statement turns into 3 + 2 + 1 - 5 + 0 - 0.25 + 6
# The result is 6.75
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

# Prints the statement "Is it true that 3 + 2 < 5 - 7?"
print("Is it true that 3 + 2 < 5 - 7?")

# Calculates 3 + 2 and 5 - 7, then determines if 3 + 2 is less than 5 - 7.
# 3 + 2 = 5 and 5 - 7 = -2. Since 5 is not less than -2, the result is false.
print(3 + 2 < 5 - 7)

# Calculates 3 + 2. The result is 5
print("What is 3 + 2?", (3 + 2))

# Calculates 5 - 7. The result is -2
print("What is 5 - 7?", (5 - 7))

# Prints the statement "Oh, that's why it's false."
print("Oh, that's why it's false.")

# Prints the statement "How about some more."
print("How about some more.")

# Compares if 5 greater than -2. The result is true.
print("Is it greater?", (-2 < 5))

# Compares if 5 is greater than or equal to -2. The result is true.
print("Is it greater or equal?", (-2 <= 5))

# Compares if 5 is less than or equal to -2. The result is false.
print("Is it less or equal?", (-2 >= 5))
