
# User Activity Tracker and Analysis

This project consists of two Python scripts to track and analyze user activity. The first script tracks activity and logs it into a CSV file, and the second script provides analytical insights from the logged data. The project is designed for users who wish to monitor their screen time and understand how they spend their time on different applications and websites.

---

## Features

1. **Activity Tracker** (`activity_tracker.py`):
   - Logs active window titles and browser URLs.
   - Tracks activity duration and stores the data in a CSV file (`UserActivityLog.csv`).
   - Supports automatic file setup and appends new data to the existing log.

2. **Analysis Tool** (`analysis_tool.py`):
   - Provides insights into screen time for a selected date.
   - Generates visual reports as a PDF, including:
     - Time spent on various activities.
     - Time spent on websites (when using a browser).
   - Allows future expansion for weekly, monthly, and yearly analyses.

---

## Installation

### Requirements

- **Python**: Version 3.7 or higher.
- **Pip Packages**:
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `uiautomation`
  - `pywin32`

### Setup

1. Clone the repository or download the files.
2. Ensure Python is installed on your device. Install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
3. Place both scripts (`activity_tracker.py` and `analysis_tool.py`) in the same directory.

---

## Usage

### 1. **Activity Tracker**
Run the tracker script to start logging activity:
```bash
python activity_tracker.py
```

- The script will create a file named `UserActivityLog.csv` in the directory.
- It runs continuously and tracks user activity until manually stopped (Ctrl+C).
- Activity is categorized as browser or non-browser activity.

### 2. **Analysis Tool**
Run the analysis script to generate reports:
```bash
python analysis_tool.py
```

- Select from the available options:
  1. Daily Analysis
  2. Weekly Analysis (future feature)
  3. Monthly Analysis (future feature)
  4. Yearly Analysis (future feature)
  5. Exit
- For daily analysis, enter the desired date in `YYYY-MM-DD` format.
- The analysis generates a PDF report saved in the same directory.

---

## File Structure

- **`activity_tracker.py`**: Logs user activity and saves it to `UserActivityLog.csv`.
- **`analysis_tool.py`**: Analyzes and visualizes data from `UserActivityLog.csv`.
- **`UserActivityLog.csv`**: Log file containing tracked activity.

---

## Notes

1. The `activity_tracker.py` script uses `uiautomation` and `win32gui`, so it only works on Windows systems.
2. The `analysis_tool.py` relies on the CSV file created by the tracker. Ensure the file exists before running the analysis.
3. The analysis tool is currently implemented for daily analysis. Weekly, monthly, and yearly analyses are placeholders for future updates.

---

## Troubleshooting

1. **Missing Dependencies**: Install missing Python packages using `pip install <package_name>`.
2. **Permission Issues**: Ensure the script has permission to write to the current directory.
3. **No Data Found**: Make sure `UserActivityLog.csv` is in the same directory and contains data.

---

## Contributions

Feel free to fork the repository and contribute to the project. Suggestions and improvements are welcome!

---

## License

This project is licensed under the MIT License.

--- 

Enjoy tracking and analyzing your activity! 😊
