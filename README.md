# Fitbod to Hevy Converter Suite

A professional utility suite designed to standardize Fitbod CSV exports for seamless import into the Hevy or Strong workout apps. Developed and maintained by **Scaling Better LLC**.

## Why this exists?
Directly importing Fitbod data into Hevy often results in "split sets," where every set of an exercise appears as a separate entry. This suite ensures your data is cleaned, mapped, and sorted so that workouts group correctly into single sessions.

## Tools Included
1. **fitbod_to_hevy.py**: The main conversion engine.
2. **exercise_finder.py**: A utility to identify unique exercise names in your Fitbod data for custom mapping.

## How to Use

### Step 1: Identify your Exercises (Optional)
If you have custom exercises or want to verify names for mapping, run the finder script:
`python exercise_finder.py`

### Step 2: Convert your Data
1. Place fitbod_to_hevy.py in the same folder as your Fitbod CSV export.
2. Run the converter: `python fitbod_to_hevy.py`
3. Enter the filename when prompted (e.g., workout_data.csv).
4. A new file named Hevy_Import_Ready_[TIMESTAMP].csv will be generated.

### Step 3: Import to Hevy
Upload the generated file to Hevy (Web or App) using the **Strong** CSV import option.

## Disclaimer
This script is provided by Scaling Better LLC for educational and utility purposes. It is not affiliated with, maintained by, or supported by Fitbod or Hevy. Use this script at your own risk. Scaling Better LLC is not responsible for any data loss, corruption, or incorrect workout information resulting from the use of this tool. Always back up your original CSV data before processing.

## License
Distributed under the MIT License. See LICENSE for more information.