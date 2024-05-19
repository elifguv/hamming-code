
# Hamming Code Calculator
This Python script provides a complete solution for generating Hamming codes and detecting errors in transmitted data. Hamming codes are used to detect and correct errors in data transmission, making them essential for reliable digital communication.

## Features
- Calculate Redundant Bits: Determine the number of redundant bits needed for a given length of data.
- Generate Hamming Code: Create the Hamming code by adding redundant bits to the original data.
- Error Detection: Check the received data for errors and identify the error position.
- Error Correction: Indicate whether the error is in the data bits or the check bits and show the corrected data.

## Prerequisites
Ensure you have Python and Flask installed on your system.

## Installation
1. Clone the repository or download the script files.
2. Navigate to the project directory.

## Setup
Install Flask using pip:
```
pip install flask
```

## Running the Application
1. Run the Flask application:
```
python app.py
```
2. Open your web browser and go to http://127.0.0.1:5000/ to access the Hamming Code Simulator.
