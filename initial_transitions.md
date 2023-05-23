#Transitions:

1.From Initial State to Allowlist Check or Droplist Check: The program starts and checks for the presence of either the allowlist or droplist file. If neither is present throw error/exception.
2.From Allowlist Check to Originals Check: If an allowlist file is present, the program proceeds to check the originals directory.
3.From Droplist Check to Originals Check: If a droplist file is present, the program proceeds to check the originals directory.
4.From Originals Check to Updates Check: After processing the originals directory, the program checks the updates directory.
5.From Updates Check to Document Update: After checking the updates directory, the program updates the finals directory according to the rules.
6.From Document Update to Program End: Once all necessary documents have been updated, the program finishes running.





