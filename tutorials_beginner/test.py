import os

text = '../report/income_summarization.txt'

# Print the current working directory
print("Current working directory:", os.getcwd())

# Construct the full path
full_path = os.path.abspath(text)
print("Full path:", full_path)

try:
    with open(text, "r") as f:
        instruction = f.read() + "\n\nReply TERMINATE at the end of your response."
        print(instruction)
except FileNotFoundError:
    print("File not found. Please verify the file path.")