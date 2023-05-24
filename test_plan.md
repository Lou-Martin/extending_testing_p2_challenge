Test Script 1: Happy Path with Allowlist

Precondition: Populate the originals directory with the generated files.
Action: Create an allowlist file containing all the surnames used in the originals directory.
Expected Result: After running the program, all files from the originals directory should be copied to the finals directory.
Actual Result: Upon running the program with Ali Archer Ball Coach Myers Winter in the allowlist only Coach made it into finals. The names on the allowlist were separated by newlines. Re-running test with items on allowlist seperated by commas. Same result, only Coach made it onto the finals.  PROCEED TO TEST SCRIPT 4.


~~Test Script 2: Happy Path with Droplist~~ Removed due to timeconstraints

Precondition: Populate the originals directory with the generated files.
Action: Create a droplist file with none of the surnames used in the originals directory.
Expected Result: After running the program, all files from the originals directory should be copied to the finals directory.
Actual Result:


~~Test Script 3: Droplist Supersedes Originals~~ Removed due to timeconstraints

Precondition: Populate the originals directory with the generated files.
Action: Create a droplist file with some of the surnames used in the originals directory.
Expected Result: After running the program, only files with surnames not included in the droplist should be copied to the finals directory.
Actual Result:


~~Test Script 4: Updates Supersedes Originals~~ Removed due to timeconstraints

Precondition: Populate the originals and updates directories with files. Some files in updates have the same surname as those in originals.
Action: Create an allowlist file with all the surnames used in the originals directory.
Expected Result: After running the program, the finals directory should contain all files from updates and only files from originals that do not have a corresponding file in updates.
Actual Result: Regardless of if a file is in originals, if a file is in updates then it will proceed to finals. It must however be on the allowlist(?) this is true if the allowlist is empty but further testing required to determine if there is *anything* on the allowlist then it may still allow other items to populate finals.
![Screenshot 2023-05-24 at 16 14 43](https://github.com/Lou-Martin/extending_testing_p2_challenge/assets/106453870/b71b6ff0-8d67-4e5c-a55b-ad255166769f)

PART TWO:
Testing the interactions of the update/allowlist/originals list continues and shows that if the allowlist is not empty (in this case it held the name "Dickinson") then there is the potential for further names to be populated in finals. See below screenshot.

Allowlist: Dickinson

Originals: Brown Coach Dickinson Goddard Parsons Williams

Updates: Coach

Finals: Coach Dickinson (note: Coach (from updates) and Dickinson (from originals)

![Screenshot 2023-05-24 at 16 21 04](https://github.com/Lou-Martin/extending_testing_p2_challenge/assets/106453870/e2228085-49e1-4d7f-a1c0-448344a9a7ad)

PART THREE:
Precondition:Since the only result not as expected in part two was the appearance of "Coach" in the finals directory, an attempt will be made to replicate and narrow down that bug. Note: Coach was not on the allowlist but was on the originals and updates. In this scenario lets change *one* further variable. We will keep 1 entry on the allowlist (any but Coach) but also remove Coach from the originals.
Action: Create an allowlist with a surname that isn't Coach, delete Coach from originals
Expected Result: Coach appears in finals along with the surname on the allowlist
Actual Result: As expected, even if an entry is not on the allowlist and if the allowlist is populated to prevent an index error being thrown then anything in the update directory *will* be populated into finals

![Screenshot 2023-05-24 at 17 10 30](https://github.com/Lou-Martin/extending_testing_p2_challenge/assets/106453870/5059c65d-9f94-4624-925a-2504610903f4)

~~Test Script 5: Both Allowlist and Droplist Present~~ Removed due to timeconstraints

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
