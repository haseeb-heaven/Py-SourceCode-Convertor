# Py-SourceCode-Convertor
This project is a GUI based tool that allows users to convert source code written in C or C++ into assembly code and hexadecimal code. The tool is implemented using Python and Tkinter, and makes use of the GCC and objdump command-line tools for conversion.

## Features
- Open and view the contents of C/C++ source code files
- Convert source code to assembly code and view the output
- Convert source code to hexadecimal code and view the output
- Option to view assembly code with opcodes only or instructions only
- Option to group hexadecimal output by 2 bytes
- Filter to open only C/C++ files
- Tabbed interface for better organization of the different panes and buttons

# Getting Started
## Prerequisites
- Python 3.x
- GCC and objdump command-line tools (included with most Linux distributions and can be installed on Windows using MinGW or Cygwin)
- Tkinter library (usually included with Python)

## Running the tool
Clone or download the repository to your local machine
Open a terminal or command prompt and navigate to the project directory
Run the command python3 main.py
The tool's GUI should now be open and ready to use

## Using the tool
Click the "Open File" button to open a C/C++ source code file. </br>
The contents of the file will be displayed in the "Source" tab</br>
To view the assembly code, click the "Convert to Assembly" button. You can also select the "Opcodes only" or "Instructions only" checkbox to filter the output</br>
To view the hexadecimal code, click the "Convert to Hex" button. The output can also be grouped by 2 bytes</br>
The assembly code and hexadecimal code will be displayed in the "Assembly" and "Hex" tabs, respectively</br>

## Limitations
- Only C and C++ source code can be converted</br>
- The tool currently only supports x86 architecture</br>
- The tool can only open one file at a time</br>
- The tool may not work correctly with all source code files, as it relies on the GCC and objdump tools for conversion</br>

## Note
If you face any issues running the tool please make sure that you have GCC and objdump installed and are accessible from command line.
