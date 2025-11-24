This project contains two parts:

1. A Python program that collects assignment grades, calculates the final weighted score, determines pass/fail status, and exports the results to a CSV file.

2. A Bash shell script that automatically archives CSV files by renaming them with timestamps and logging all actions.



## Features
- Interactive input: User enters assignment name, category (FA/SA), grade, and weight
- Input validation: make sure grades are between 0-100, weights are positive, and category is correct
- Calculates weighted scores for each category
- Determines final grade and pass/fail status
- Calculates GPA based on final grade
- Automatically saves all data to a CSV file
- Bash script archives CSV files with timestamps and logs actions

## How to Run

1. Make sure Python 3 is installed on your system
2. Open the project folder in your terminal
3. Run the Python program:
   ```bash
   python3 grade_generator.py
   ```

To archive CSV files, run the Bash script:
```bash
bash organizer.sh
```


