Title: Unexpected Entries in the "Finals" Directory

Severity: High

Component/Module: Allowlist Processing/Updates Directory

Environment: MacOS Ventura 13.3.1, Python 3.11, Ran from Terminal (ZSH)

Description:

In a test scenario involving an allowlist, originals, updates, and finals directories, the program exhibits unexpected behaviour when handling entries from the updates directory. Specifically, files from the updates directory appear in the finals directory even when their corresponding surnames are not included in the allowlist.

Steps to Reproduce:

1.Populate the originals and updates directories, the files in updates do not need to have the same surname as those in originals.
2.Create an allowlist file with one or more surname (to bypass the list index out of range error) from the originals directory (not those in updates).
3.Run the program.

Expected Result:

After running the program, only the files included in the allowlist should be present in finals.

Actual Result:

Regardless of whether a file is in the originals directory or on the allowlist, if a file is in the updates directory, it appears in the finals directory.

Additional Notes:

This issue needs further investigation to understand the underlying cause. It's not clear whether this behaviour is tied to specific surnames or specific conditions in the updates directory. The error handling for the allowlist, particularly with respect to how it handles the updates directory, may need to be reviewed.

Please note that the above details are based on observed application behaviour and could be subject to variations based on other untested conditions or configurations.

Please see test_plan.md for screenshots pertaining to the issue.
