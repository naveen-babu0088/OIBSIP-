# Advanced BMI Calculator

## Project Overview

The Advanced BMI Calculator is a Python-based desktop application developed using Tkinter. It allows users to calculate their Body Mass Index (BMI), view health categories, store historical BMI records, and analyze BMI trends over time.

The project combines GUI development, database management, data validation, and data visualization to provide a complete health-monitoring application.

---

## Features

### BMI Calculation

* Calculate BMI using weight and height.
* Instant BMI result display.
* Accurate BMI calculation based on standard formula.

### BMI Categories

The application automatically categorizes users into:

* Underweight
* Normal Weight
* Overweight
* Obese

### User-Friendly GUI

* Built using Tkinter.
* Simple and intuitive interface.
* Easy data entry and result viewing.

### Data Storage

* Stores user BMI records in SQLite database.
* Automatically saves calculation history.
* Supports multiple users.

### Historical Data

* View previously calculated BMI records.
* Displays:

  * User Name
  * BMI Value
  * Health Category
  * Date and Time

### BMI Trend Analysis

* Visualize BMI changes over time.
* Generate BMI trend graphs using Matplotlib.

### Input Validation

* Prevents invalid weight and height entries.
* Displays helpful error messages.
* Handles unexpected user input safely.

---

## Technologies Used

| Technology | Purpose              |
| ---------- | -------------------- |
| Python     | Programming Language |
| Tkinter    | GUI Development      |
| SQLite3    | Database Storage     |
| Matplotlib | Graph Visualization  |
| Datetime   | Timestamp Management |

---

## Project Structure

```text
BMI_Calculator/
│
├── bmi_calculator.py
├── bmi_data.db
├── requirements.txt
└── README.md
```

---

## Installation

### Prerequisites

* Python 3.10 or later

Verify installation:

```bash
python --version
```

---

## Install Dependencies

Install required packages:

```bash
pip install matplotlib
```

If matplotlib is not required, the application can still run without the graph functionality.

---

## Running the Application

Open Command Prompt and navigate to the project folder:

```bash
cd BMI_Calculator
```

Run the application:

```bash
python bmi_calculator.py
```

---

## How to Use

### Step 1

Enter your name.

### Step 2

Enter your weight in kilograms.

Example:

```text
70
```

### Step 3

Enter your height in centimeters.

Example:

```text
175
```

### Step 4

Click **Calculate BMI**.

### Step 5

View:

* BMI Value
* Health Category

### Step 6

Click **Show Trend Graph** to view BMI history visualization.

---

## BMI Formula

BMI is calculated using:

BMI = Weight (kg) / Height² (m²)

Example:

Weight = 70 kg

Height = 1.75 m

BMI = 70 / (1.75 × 1.75)

BMI = 22.86

---

## BMI Classification Table

| BMI Range      | Category      |
| -------------- | ------------- |
| Less than 18.5 | Underweight   |
| 18.5 - 24.9    | Normal Weight |
| 25.0 - 29.9    | Overweight    |
| 30.0 and Above | Obese         |

---

## Database Schema

```sql
CREATE TABLE bmi_records(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    weight REAL,
    height REAL,
    bmi REAL,
    category TEXT,
    date TEXT
);
```

---

## Learning Outcomes

This project helps in understanding:

* Python Programming
* GUI Development with Tkinter
* SQLite Database Operations
* Data Validation Techniques
* Event-Driven Programming
* Health Analytics
* Data Visualization
* Error Handling

---

## Future Enhancements

* User Login System
* Dark Mode Interface
* PDF Report Generation
* Excel Export
* Cloud Database Integration
* Mobile App Version
* Diet Recommendations
* Ideal Weight Suggestions
* Email Notifications

---

## Sample Output

```text
Name: Naveen
Weight: 70 kg
Height: 175 cm

BMI: 22.86
Category: Normal Weight
```

---

## Author

Naveen

Advanced BMI Calculator

Developed using Python, Tkinter, SQLite, and Matplotlib for educational and health-monitoring purposes.

---

## License

This project is open-source and intended for educational and personal use.
