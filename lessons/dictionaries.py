"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()
# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary
# by its key
schools.pop("Duke")

# Update / Reassign a key-value pair
schools["UNC"] = 2000
schools["NCSU"] += 200

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")
if "Duke" in schools:
    print("Found the key in 'Duke' in schools.")
else:
    print("No key 'Duke' in schools")

print(schools)

# Demonstraation of dictionary literals

# Empty dictionary literal
schools = {} # Same as dict()
print(schools)

# Alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

# What happens when a key does not exist
#print(schools["UNCC"])

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
    print(type(school))
# Lesson Questions
courses: dict[int, str] = dict()
courses[110] = "Intro to Programming"
courses[210] = "Data Structures"
print(courses[110])

# Lesson Questions 2
points: dict[str, int] = {"Kris": 0, "Kaki": 10}
points["Kaki"] += 100
print(points["Kaki"])
