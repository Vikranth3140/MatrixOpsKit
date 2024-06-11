# Matrix Operations and Parametric Form Finder

## Introduction

This Python script is designed to perform various matrix operations and find the parametric form of a matrix. It utilizes the SymPy library for matrix operations and provides functionality for the following:

1. Reading a matrix from a file.
2. Finding the Reduced Row Echelon Form (RREF) of the matrix.
3. Extracting column vectors from the RREF matrix.
4. Generating an identity matrix of appropriate size.
5. Determining the parametric form of the matrix.

## Usage

### Prerequisites

Before using this script, make sure you have Python installed on your system. Additionally, you need to install the SymPy library, which can be done using the following command:

```bash
pip install sympy
```

### Running the Script

1. Place your matrix data in a file named "matrix.txt" in the same directory as the script.
2. Run the script using the following command:

```bash
python main.py
```

The script will perform the matrix operations and display the results in the console.

## Results

### Reduced Row Echelon Form (RREF)

The RREF of the input matrix is displayed in the console.

### Column Matrix

The column vectors extracted from the RREF matrix are displayed.

### Parametric Form

The parametric form of the matrix is displayed as a linear combination of variables.

## Customization

You can customize the script by modifying the code to read matrices from different file locations or make any other desired changes.

## Acknowledgments

- [SymPy](https://www.sympy.org/) - The library used for symbolic mathematics in Python.

## License

This project is licensed under the [MIT License](LICENSE.md).
