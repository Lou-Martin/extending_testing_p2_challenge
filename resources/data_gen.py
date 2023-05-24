from faker import Faker
import os

# Initialize a Faker instance for UK locale
fake = Faker('en_UK')

# Define the directory path
dir_path = './testing_grounds/target_directory/originals'

# Check if the directory exists
if os.path.isdir(dir_path):

    # Generate 5 samples
    for _ in range(5):
        # Generate fake name and address
        name = f"{fake.prefix()} {fake.first_name()} {fake.last_name()}"
        address = fake.address().replace('\n', ', ')

        # Use the last name (split by space and get the last element) as the file name
        file_name = name.split()[-1]

        # Check if the file already exists, if so, generate a new one
        while os.path.isfile(os.path.join(dir_path, file_name)):
            name = f"{fake.prefix()} {fake.first_name()} {fake.last_name()}"
            file_name = name.split()[-1]

        # Write the data to a file
        with open(os.path.join(dir_path, file_name), 'w') as f:
            f.write(name + '\n' + address)
else:
    print(f"The directory {dir_path} does not exist.")