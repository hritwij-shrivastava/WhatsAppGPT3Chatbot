def read_conversation_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

# Cleaned conversation data with roles
file_path = 'output.txt'
conversation_lines = read_conversation_file(file_path)

# Convert lines to a list of dictionaries with roles
conversation = []
for line in conversation_lines:
    try:
        role, content = line.split(': ', 1)
    except:
        print(line)
        break