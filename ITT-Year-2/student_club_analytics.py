details = [
    "Arun:AI,ML,Robotics", "Bala:ML,IoT", "Chitra:AI,CyberSecurity",
    "Divya:Robotics,IoT,AI", "Ezhil:ML,CyberSecurity", "Farah:AI,ML",
    "Ganesh:IoT,Robotics,AI", "Hari:ML"
]

def details_about(data):
    # Using .split() is more efficient than manual character loops
    name, clubs_raw = data.split(":")
    return name, set(clubs_raw.split(","))

# Building the map using a Dictionary Comprehension
student_club_map = {name: clubs for name, clubs in (details_about(d) for d in details)}
student_names = set(student_club_map.keys())
all_clubs = set().union(*student_club_map.values())

print(f"1. Student Names: {student_names}")
print(f"2. Unique Clubs: {all_clubs}")

# 3. AI and ML students (Using set subset logic)
ai_ml_students = [n for n, c in student_club_map.items() if {"AI", "ML"}.issubset(c)]
print(f"3. AI and ML students: {ai_ml_students}")

# 4. AI but not Robotics
ai_not_robotics = [n for n, c in student_club_map.items() if "AI" in c and "Robotics" not in c]
print(f"4. AI but not Robotics: {ai_not_robotics}")

# 5. Clubs excluding those belonging to "Solo Club" students
solo_clubs = {list(c)[0] for c in student_club_map.values() if len(c) == 1}
print(f"5. Clubs without solo-only members: {all_clubs - solo_clubs}")

# 6. Set operations for Vowels and Consonants
vowels = set("AEIOUaeiou")
v_clubs = [c for n, c in student_club_map.items() if n[0] in vowels]
c_clubs = [c for n, c in student_club_map.items() if n[-1] not in vowels]

print(f"6a. Intersection (Vowel Start): {set.intersection(*v_clubs) if v_clubs else set()}")
print(f"6b. Union (Consonant End): {set().union(*c_clubs) if c_clubs else set()}")

# 7 & 8. Character Analysis (Using .lower() for innovation)
all_chars = {char.lower() for name in student_names for char in name}
common_chars = set.intersection(*(set(name.lower()) for name in student_names))
print(f"7. All characters: {all_chars}")
print(f"8. Common characters: {common_chars}")

# 9. Students whose name characters are a subset of 'arun'
arun_set = set("arun")
arun_subsets = [n for n in student_names if set(n.lower()).issubset(arun_set)]
print(f"9. Name matches 'Arun' set: {arun_subsets}")

# 10. Duplicate club combinations
combinations = {}
for clubs in student_club_map.values():
    key = tuple(sorted(clubs))
    combinations[key] = combinations.get(key, 0) + 1
shared = [list(k) for k, count in combinations.items() if count > 1]
print(f"10. Duplicate club sets: {shared}")

# 11. Sorted list (Primary: Most clubs descending, Secondary: Alphabetical)
sorted_names = sorted(student_names, key=lambda n: (-len(student_club_map[n]), n))
print(f"11. Sorted list: {sorted_names}")

# 12. Final Prime Filter
def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

hari_clubs = student_club_map.get("Hari", set())
final_set = {
    n for n, c in student_club_map.items() 
    if is_prime(len(n)) and any(club[0] in vowels for club in c) and c.isdisjoint(hari_clubs)
}
print(f"12. Final filtered students: {final_set}")
