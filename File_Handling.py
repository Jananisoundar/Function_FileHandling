from datetime import datetime

def create_timestamped_file():
    # Capture the current timestamp
    current_timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = "current_timestamp_02.txt"

    # Write the current timestamp to the file
    with open(file_name, 'w') as file:
        file.write(current_timestamp)

    print(f'File {file_name} created with content: {current_timestamp}')

def read_file(file_name):

        with open(file_name, 'r') as file:
              content = file.read()
              print(f'Content of {file_name}:')
              print(content)


# Call the function to create the file
create_timestamped_file()

# Call the function to read the file
read_file('current_timestamp_02.txt')
