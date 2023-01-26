import math

# Read in the input values
D = float(input("Enter a value for D(inch): "))
d = float(input("Enter a value for d(inch): "))
C = float(input("Enter a value for C(inch): "))

Pt = float(input("Enter a value for Pt(Hp): "))
Speed = float(input("Enter a value for Speed(rpm): "))

Running_time = float(input("Enter a value for Running time(hr/day): "))
Environment = int(input("Enter a value for Environment : "))




# Calculate SR
SR = D / d


# Calculate L
L = 2 * C + (math.pi / 2) * (D + d) + (D - d)**2 / (4 * C)


# Check if (D+d)/2 > C
if (D+d)/2 < C:
  # Output "Work" if the condition is true
  print("Work")
else:
  # Output "Not Work" if the condition is flase
  print("Not Work")

  # Round L up
L = round(L, 2)


# Output the result
print(f"The value of SR is: {SR}")



# Output the result
print(f"The value of L is: {L}")