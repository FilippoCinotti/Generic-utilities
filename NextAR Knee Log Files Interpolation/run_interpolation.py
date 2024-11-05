import numpy as np
import pandas as pd
import PySimpleGUI as sg
import os

def polynomial_interpolation(x_points, y_points, degree):
    """
    Fit a polynomial of the specified degree to the given x and y points,
    enforcing that the polynomial passes through (0, y(0)).

    Parameters:
    x_points (array-like): x-values of the data points.
    y_points (array-like): y-values of the data points.
    degree (int): Degree of the polynomial to fit.

    Returns:
    polynomial (np.poly1d): Polynomial function.
    """
    if degree >= len(x_points):
        raise ValueError("Degree of the polynomial should be less than the number of points.")

    # Ensure polynomial passes through (0, y(0)) exactly
    y_zero = y_points[0]  # The actual y-value at x = 0
    adjusted_y_points = y_points - y_zero  # Shift y-values by y(0)
    coefficients = np.polyfit(x_points, adjusted_y_points, degree)
    coefficients[-1] += y_zero  # Adjust constant term to satisfy y(0)

    polynomial = np.poly1d(coefficients)
    return polynomial

def find_y_for_missing_x(polynomial, x_values):
    """
    Compute the y-values for missing x-values using the polynomial.

    Parameters:
    polynomial (np.poly1d): Polynomial function.
    x_values (array-like): Array of x-values where y-values are to be estimated.

    Returns:
    np.ndarray: Estimated y-values for missing x-values.
    """
    return polynomial(x_values)

def calculate_squared_error(polynomial, x_points, y_points):
    """
    Calculate the squared error between actual and predicted y-values.

    Parameters:
    polynomial (np.poly1d): Polynomial function.
    x_points (array-like): Original x-values.
    y_points (array-like): Original y-values.

    Returns:
    float: Sum of squared errors.
    """
    y_predicted = polynomial(x_points)
    squared_error = np.sum((y_points - y_predicted) ** 2)
    return squared_error

def process_csv(file_path, degree, missing_x_values):
    """
    Process CSV data by fitting a polynomial to each series and calculating missing y-values.

    Parameters:
    file_path (str): Path to the input CSV file.
    degree (int): Degree of the polynomial.
    missing_x_values (array-like): x-values for which y-values are to be estimated.

    Returns:
    dict: Results containing polynomial, missing y-values, and squared error for each y-series.
    """
    data = pd.read_csv(file_path, skiprows=1)
    x_points = data.iloc[:, 0].values  # First column as x_points
    y_series = data.iloc[:, 1:].values  # Remaining columns as y_points series

    results = {}
    
    for i, y_points in enumerate(y_series.T):
        polynomial = polynomial_interpolation(x_points, y_points, degree)
        missing_y_values = find_y_for_missing_x(polynomial, missing_x_values)
        squared_error = calculate_squared_error(polynomial, x_points, y_points)
        
        results[f'y_series_{i+1}'] = {
            'polynomial': polynomial,
            'missing_y_values': missing_y_values,
            'squared_error': squared_error
        }
        
    return results

def save_results_to_csv_and_txt(results, missing_x_values, input_file_path):
    """
    Save missing y-values to a CSV and details for each series to a text file.

    Parameters:
    results (dict): Dictionary containing results for each series.
    missing_x_values (array-like): x-values for which y-values were estimated.
    input_file_path (str): Original path of the input file for saving output.
    """
    # Prepare output file paths
    base, ext = os.path.splitext(input_file_path)
    output_csv_path = f"{base}_output{ext}"
    output_txt_path = f"{base}_output.txt"
    
    # Load original CSV header and create output DataFrame
    original_header = pd.read_csv(input_file_path, nrows=0).columns.tolist()
    output_df = pd.DataFrame({'Missing X Values': missing_x_values})
    
    for series, result in results.items():
        output_df[series] = result['missing_y_values']
    
    output_df.to_csv(output_csv_path, index=False, header=[*original_header])
    
    # Save detailed results to a text file
    with open(output_txt_path, 'w') as txt_file:
        for series, result in results.items():
            txt_file.write(f"Results for {series}:\n")
            txt_file.write(f"Polynomial function: {result['polynomial']}\n")
            txt_file.write(f"Missing y-values for x = {missing_x_values}: {result['missing_y_values']}\n")
            txt_file.write(f"Interpolation squared error: {result['squared_error']}\n\n")

def run_interpolation():
    """
    Run the interpolation process by selecting a CSV file and performing interpolation.
    """
    # Set dark theme for the GUI
    sg.theme("DarkBlue")

    layout = [
        [sg.Text("Polynomial Interpolation", font=("Helvetica", 14))],
        [sg.Text("Select CSV file:"), sg.Input(), sg.FileBrowse(key="file_path")],
        [sg.Text("Degree of polynomial:"), sg.InputText("5", key="degree", size=(5, 1))],
        [sg.Button("Run"), sg.Button("Exit")],
        [sg.Output(size=(80, 20))]
    ]

    window = sg.Window("Polynomial Interpolation Tool", layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break

        if event == "Run":
            try:
                file_path = values["file_path"]
                degree = int(values["degree"])
                missing_x_values = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

                if not file_path:
                    print("Please select a file.")
                    continue

                print("Processing file:", file_path)
                results = process_csv(file_path, degree, missing_x_values)
                save_results_to_csv_and_txt(results, missing_x_values, file_path)

                print("Process completed. Results saved to CSV and TXT files.")
            
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    window.close()

# Run the PySimpleGUI-based interpolation tool
if __name__ == "__main__":
    run_interpolation()
