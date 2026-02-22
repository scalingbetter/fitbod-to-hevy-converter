"""
Fitbod to Hevy Converter
Standardizes Fitbod CSV exports for import into Hevy/Strong.

Maintained by: Scaling Better LLC
License: MIT
Version: 1.0.0
"""
import csv
import os
from collections import defaultdict
from datetime import datetime

# Maps Fitbod names to Hevy library names
EXERCISE_MAPPING = {
    "Ab Crunch Machine": "Crunch (Machine)",
    "Air Squats": "Squat (Bodyweight)",
    "Alternating Heel Touch": "Heel Taps",
    "Bicycle Crunch": "Bicycle Crunch",
    "Calf Press": "Calf Press (Machine)",
    "Crunches": "Crunch",
    "Cycling - Stationary": "Cycling",
    "Dumbbell Bench Press": "Bench Press (Dumbbell)",
    "Dumbbell Bicep Curl": "Bicep Curl (Dumbbell)",
    "Dumbbell Kickbacks": "Triceps Kickback (Dumbbell)",
    "Dumbbell Row": "Dumbbell Row",
    "Glute Kickback Machine": "Rear Kick (Machine)",
    "Hack Squat": "Hack Squat (Machine)",
    "Lat Pulldown": "Lat Pulldown (Machine)",
    "Leg Extension": "Leg Extension (Machine)",
    "Lying Hamstrings Curl": "Lying Leg Curl (Machine)",
    "Machine Bench Press": "Chest Press (Machine)",
    "Machine Bicep Curl": "Bicep Curl (Machine)",
    "Machine Fly": "Chest Fly (Machine)",
    "Machine Hip Abductor": "Hip Abduction (Machine)",
    "Machine Hip Adductor": "Hip Adduction (Machine)",
    "Machine Lateral Raise": "Lateral Raise (Machine)",
    "Machine Leg Press": "Leg Press Horizontal (Machine)",
    "Machine Preacher Curl": "Preacher Curl (Machine)",
    "Machine Rear Delt Fly": "Rear Delt Reverse Fly (Machine)",
    "Machine Row": "Seated Row (Machine)",
    "Machine Shoulder Press": "Shoulder Press (Machine)",
    "Machine Squat": "Squat (Machine)",
    "Machine Tricep Dip": "Seated Dip Machine",
    "Machine Tricep Extension": "Triceps Extension (Machine)",
    "Plank": "Plank",
    "Rowing": "Rowing Machine",
    "Russian Twist": "Russian Twist",
    "Seated Back Extension": "Back Extension (Machine)",
    "Seated Leg Curl": "Seated Leg Curl (Machine)",
    "Seated Machine Calf Press": "Calf Press (Machine)",
    "Single Leg Leg Extension": "Single Leg Extensions",
    "Sit Up": "Sit Up",
    "Smith Machine Glute Bridge": "Hip Thrust (Machine)",
    "Standing Dumbbell Shoulder Press": "Shoulder Press (Dumbbell)",
    "Walking - Treadmill": "Walking"
}

def convert_fitbod_to_hevy():
    print("==========================================")
    print(" Scaling Better LLC: Fitbod to Hevy Tool ")
    print("==========================================\n")
    
    input_file = input("Enter Fitbod CSV filename: ").strip()
    
    if not os.path.exists(input_file):
        print(f"Error: '{input_file}' not found.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"Hevy_Import_{timestamp}.csv"

    daily_data = defaultdict(list)
    try:
        with open(input_file, mode='r', encoding='utf-8-sig') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                date_key = row.get("date", "")[:10]
                if date_key:
                    daily_data[date_key].append(row)
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    with open(output_file, mode='w', newline='', encoding='utf-8-sig') as outfile:
        fieldnames = [
            "Date", "Workout Name", "Exercise Name", "Set Order", 
            "Weight", "Weight Unit", "Reps", "RPE", "Distance", 
            "Distance Unit", "Seconds", "Notes", "Workout Notes", "Workout Duration"
        ]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for date_val in sorted(daily_data.keys()):
            unified_timestamp = f"{date_val} 09:00:00"
            workout_name = f"Fitbod Workout {date_val}"
            sorted_rows = sorted(daily_data[date_val], key=lambda x: x['exercise_name'])
            exercise_set_tracker = defaultdict(int)

            for row in sorted_rows:
                raw_name = row.get("exercise_name", "").strip()
                hevy_name = EXERCISE_MAPPING.get(raw_name, raw_name).strip()
                exercise_set_tracker[hevy_name] += 1
                
                writer.writerow({
                    "Date": unified_timestamp,
                    "Workout Name": workout_name,
                    "Exercise Name": hevy_name,
                    "Set Order": exercise_set_tracker[hevy_name],
                    "Weight": row.get("weight_kg", ""),
                    "Weight Unit": "kg",
                    "Reps": row.get("Reps", ""),
                    "RPE": "",
                    "Distance": row.get("distance_meters", ""),
                    "Distance Unit": "m",
                    "Seconds": row.get("duration_seconds", "").strip() or "0",
                    "Notes": "Warmup" if row.get("isWarmup", "").lower() in ["true", "1"] else "",
                    "Workout Notes": "",
                    "Workout Duration": "60m"
                })

    print(f"\nSuccess! Created: {output_file}")

if __name__ == "__main__":
    convert_fitbod_to_hevy()