"""
Fitbod Exercise Finder
Utility to extract unique exercise names from Fitbod exports.
Maintained by: Scaling Better LLC
"""
import csv
import os

def find_unique_exercises():
    print("==========================================")
    print(" Scaling Better LLC: Exercise Finder      ")
    print("==========================================\n")
    
    file_name = input("Enter your Fitbod CSV filename: ").strip()

    if not os.path.exists(file_name):
        print(f"Error: {file_name} not found.")
        return

    exercises = set()
    try:
        with open(file_name, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row.get('exercise_name', '').strip()
                if name:
                    exercises.add(name)
        
        print(f"\nFound {len(exercises)} unique exercises:\n")
        for ex in sorted(exercises):
            print(f"- {ex}")
            
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    find_unique_exercises()