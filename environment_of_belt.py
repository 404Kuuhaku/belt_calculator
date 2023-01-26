options = {
    1: "Frequent start and stop of machine",
    2: "Hard to conduct maintenance checkup",
    3: "Dusty environment",
    4: "High temperature",
    5: "Oil or water splashing",
}

values = {
    1: 0.1,
    2: 0.2,
    3: 0.3,
    4: 0.4,
    5: 0.5,
}

print("Select an option:")
for key, value in options.items():
    print(f"{key}. {value}")

choice = int(input())

if choice in options:
    value = values[choice]
    print(f"Value for {options[choice]} is {value}")
else:
    print("Invalid choice.")