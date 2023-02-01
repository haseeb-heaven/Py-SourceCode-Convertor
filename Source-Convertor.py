#Py-Source Convertor is tool to convert any source file to Assembly/Hex (Binary) using Python and GCC tools.
# This tool uses the following tools:
# 1. GCC - GNU Compiler Collection
# 2. objdump - GNU object file disassembler
# 3. xxd - make a hexdump or do the reverse
# 4. tkinter - Python GUI library
# Written by Haseeb Mir @ 2023.

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess
import os
from tkinter import ttk

# Clear all the panes
def clear_panes():
    source_pane.delete("1.0", tk.END)
    hex_pane.delete("1.0", tk.END)
    assembly_pane.delete("1.0", tk.END)

# Function to open a file dialog and display the contents of the selected file
def open_file():
    clear_panes()
    global filepath
    filepath = filedialog.askopenfilename(defaultextension=".c", filetypes=[("C files", "*.c"), ("C++ files", "*.cpp")])
    if filepath:
        with open(filepath, 'r') as file:
            contents = file.read()
            source_pane.insert('1.0', contents)

# Function to convert the source code to hexadecimal code and display the output
def convert_to_hex():
    hex_pane.delete("1.0", tk.END) # Clear the pane before inserting data.
    global filepath
    extension = os.path.splitext(filepath)[1]
    if extension == ".c":
        subprocess.run(["gcc", "-c", "-o", "output.o", filepath])
    elif extension == ".cpp":
        subprocess.run(["g++", "-c", "-o", "output.o", filepath])
    hex_code = subprocess.run(["xxd", "-g", "1", "output.o"], capture_output=True, universal_newlines=True).stdout
    hex_pane.insert('1.0', hex_code)

# Function to convert the source code to assembly code and display the output
def convert_to_assembly():
    assembly_pane.delete("1.0", tk.END) # Clear the pane before inserting data.
    global filepath
    extension = os.path.splitext(filepath)[1]
    if extension == ".c":
        subprocess.run(["gcc", "-c", "-o", "output.o", filepath])
    elif extension == ".cpp":
        subprocess.run(["g++", "-c", "-o", "output.o", filepath])
    if opcode_var.get() == 1:
        output = subprocess.run(["objdump", "-d","--no-show-raw-insn", "output.o"], capture_output=True)
    elif instruction_var.get() == 1:
        output = subprocess.run(["objdump", "-d", "-M", "intel", "output.o"], capture_output=True)
    else:
        output = subprocess.run(["objdump", "-d", "-M", "intel", "output.o"], capture_output=True)
    if output.returncode != 0:
        assembly_pane.insert('1.0', output.stderr.decode())
    else:
        assembly_code = output.stdout.decode()
        assembly_pane.insert('1.0', assembly_code)

# Function to display the help message
def show_help():
    messagebox.showinfo("Help", "GUI based tool that allows users to convert source code written in C or C++ into assembly code and hexadecimal code.\nWritten by Haseeb Mir @2023")

## GUI - Section.
root = tk.Tk()
root.title("Source Code Converter")
root.geometry("600x400") # sets the size of the window to 600x400 pixels
root.resizable(False, False) # disables the maximize button, the first argument controls width, the second height.
root.minsize(600, 480)
root.maxsize(600, 500)

# Create a tab control to hold the source, assembly, and hex tabs
tab_control = ttk.Notebook(root)

# Create a source tab and add it to the tab control
source_tab = ttk.Frame(tab_control)
tab_control.add(source_tab, text='Source')
source_pane = tk.Text(source_tab)
source_pane.pack()

open_file_button = tk.Button(source_tab, text="Open File", command=open_file)
open_file_button.pack()

# Create an assembly tab and add it to the tab control
assembly_tab = ttk.Frame(tab_control)
tab_control.add(assembly_tab, text='Assembly')
assembly_pane = tk.Text(assembly_tab)
assembly_pane.pack()

# Create checkboxes to control the assembly output
opcode_var = tk.IntVar()
instruction_var = tk.IntVar()

opcode_checkbox = tk.Checkbutton(assembly_tab, text="Opcodes only", variable=opcode_var)
opcode_checkbox.pack()

instruction_checkbox = tk.Checkbutton(assembly_tab, text="Instructions only", variable=instruction_var)
instruction_checkbox.pack()

convert_to_assembly_button = tk.Button(assembly_tab, text="Convert to Assembly", command=convert_to_assembly)
convert_to_assembly_button.pack()

# Create a hex tab and add it to the tab control
hex_tab = ttk.Frame(tab_control)
tab_control.add(hex_tab, text='Hex')
hex_pane = tk.Text(hex_tab)
hex_pane.pack()

convert_to_hex_button = tk.Button(hex_tab, text="Convert to Hex", command=convert_to_hex)
convert_to_hex_button.pack()

# Create a help button
help_button = tk.Button(root, text="Help", command=show_help)
help_button.pack()

# Pack the tab control and start the GUI event loop
tab_control.pack(expand=1, fill='both')
root.mainloop()

