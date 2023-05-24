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



IDEAS FOR FURTHER TESTING

The below feature a list of ideas I may want to test in loose priority order

target_directory is not present.
originals directory is not present.
updates directory is not present.
allowlist file is not present.
droplist file is not present.
allowlist is empty.
droplist is empty.
originals directory is empty.
updates directory is empty.
allowlist contains all entries present in originals and updates.
droplist contains all entries present in originals and updates.
allowlist contains items that aren't in originals/updates.
droplist contains items that aren't in originals/updates.
Both allowlist and droplist are present and contain entries.
Both allowlist and droplist are present and empty.
Files in updates directory have the same names as in originals directory.
Files in updates directory have different names than in originals directory.
Files in originals and updates have the same content.
Files in originals and updates have different content.
Handling of files with special characters in the name.
Handling of files with very long names.
Handling of large files.
Handling of files with non-standard text encodings.
Handling of subdirectories in originals and updates directories.
