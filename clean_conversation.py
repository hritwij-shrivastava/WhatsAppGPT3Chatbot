input_file_path = 'conversation.txt'
output_file_path = 'output.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()

cleaned_lines = []

current_line = ""
for line in lines:
    line = line.strip()  # Remove leading/trailing whitespace
    if line.startswith(tuple( str(f"{str(i).zfill(2)}/") for i in range(1, 32))):
        if current_line:
            cleaned_lines.append(current_line)
        current_line = line
    else:
        current_line += " " + line

# Append the last line if it's not empty
if current_line:
    cleaned_lines.append(current_line)

# Now, you can write the cleaned lines to a new file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in cleaned_lines:
        role, content = line.split(': ', 1)
        role = role.split("- ")[-1]
        if role=='Jeevitha(ITC)':
            role = 'Jeevitha'
        else:
            role = 'Hritwij'
        line = f"{role}: {content}"
        output_file.write(line + '\n')
