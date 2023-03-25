# main.py script
import pathlib

import file_operations

current_directory = pathlib.Path(__file__).parent.resolve()
file_name = current_directory / "./sample.txt"
content = file_operations.read_file(file_name)
print(f"The content of {file_name} is: '{content}'")
