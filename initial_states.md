#States:

-Initial State: A directory exists (target directory) containing two subdirectories (originals and updates) and either an allowlist or a droplist file, but not both *to be confirmed*.
  -originals directory: Contains versions of document content that may or may not be kept and considered for use as the final version.
  -updates directory: Contains versions of document content that must be used as the final version.
  -allowlist file: Lists documents that, if present in originals, are kept from the originals directory and may be used as the final version if not superseded by a document in updates.
  -droplist file: Lists documents that, if present in originals, are ignored from the originals directory and hence not kept at all.
Final State: Directory inside target directory created called finals which contains documents kept or not dropped from originals (depending on the allowlist/droplist file presence and content) which were not superseded by documents from updates, along with all the files from updates.
