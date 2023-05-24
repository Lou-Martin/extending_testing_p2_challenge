Test Script 1: Happy Path with Allowlist

Precondition: Populate the originals directory with the generated files.
Action: Create an allowlist file containing all the surnames used in the originals directory.
Expected Result: After running the program, all files from the originals directory should be copied to the finals directory.
Actual Result:


Test Script 2: Happy Path with Droplist

Precondition: Populate the originals directory with the generated files.
Action: Create a droplist file with none of the surnames used in the originals directory.
Expected Result: After running the program, all files from the originals directory should be copied to the finals directory.
Actual Result:


Test Script 3: Droplist Supersedes Originals

Precondition: Populate the originals directory with the generated files.
Action: Create a droplist file with some of the surnames used in the originals directory.
Expected Result: After running the program, only files with surnames not included in the droplist should be copied to the finals directory.
Actual Result:


Test Script 4: Updates Supersedes Originals

Precondition: Populate the originals and updates directories with files. Some files in updates have the same surname as those in originals.
Action: Create an allowlist file with all the surnames used in the originals directory.
Expected Result: After running the program, the finals directory should contain all files from updates and only files from originals that do not have a corresponding file in updates.
Actual Result:


Test Script 5: Both Allowlist and Droplist Present

Precondition: Populate the originals directory with the generated files.
Action: Create both an allowlist and droplist file in the root directory.
Expected Result: After running the program, an error message should be displayed stating that both an allowlist and droplist are present.
Actual Result:
