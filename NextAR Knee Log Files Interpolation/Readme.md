# Polynomial Interpolation Tool

This Python project performs polynomial interpolation on data series from a CSV file. Using this tool, you can estimate missing `y` values for specified `x` values based on polynomial fits of selected degrees. The GUI interface allows you to select an input CSV file and specify the polynomial degree easily.

## Features
- Supports polynomial interpolation of multiple data series from a CSV file.
- Allows user-specified degree of polynomial interpolation.
- Calculates estimated `y` values for specified `x` values and outputs these to a CSV file.
- Saves detailed results (polynomial equation and squared error) in a text file.
- Provides a dark-themed GUI interface built with PySimpleGUI for ease of use.

## Requirements
- Python 3.x
- `numpy` for numerical operations
- `pandas` for data handling
- `PySimpleGUI` for the graphical interface

You can install the necessary packages with:
```bash
pip install numpy pandas PySimpleGUI
Usage
Run the run_interpolation.py script.
Use the GUI to select your input CSV file and specify the desired polynomial degree.
Click "Run" to perform the interpolation. Results are saved automatically to the same directory as the input file, with _output appended to the filename.
Input CSV Format
The input CSV file should have:
The first row as the header row, which will be preserved in the output CSV file.
The first column as x values.
Remaining columns as y data series for which interpolation will be performed.
Output Files
An output CSV file containing the missing y values for the specified x values.
A text file with detailed results for each y series, including the polynomial function and interpolation error.
Example
To run the application:

bash
Copia codice
python run_interpolation.py
License
This project is licensed under the MIT License.

yaml
Copia codice

---

### User Guide

#### Step 1: Install Dependencies
Before using the application, install the required dependencies:
```bash
pip install numpy pandas PySimpleGUI
Step 2: Prepare Your CSV File
Ensure your CSV file is formatted with:

A header row (which will be preserved in the output).
The first column containing the x values.
Remaining columns as y series for interpolation.
Step 3: Launch the Application
Run the following command to open the application:

bash
Copia codice
python run_interpolation.py
Step 4: Use the GUI to Select Parameters
Select CSV File: Use the "Browse" button to navigate to and select your input CSV file.
Specify Polynomial Degree: Enter the degree for the polynomial interpolation in the input field. The default is 5.
Click the Run button to begin interpolation.
Step 5: View Results
The program will output:

A CSV file with missing y values estimated for specified x values. The file is saved in the same directory as the input file, with _output added to its name.
A text file with details for each y series, including the polynomial function and squared error, saved in the same directory as the CSV output.
Example Run
Select example.csv as the input file.
Enter 5 as the polynomial degree.
Click Run. You will see a confirmation in the output window and find both output files in the input file’s directory.