# Open the stats file in read mode
with open('stats/stats.txt', 'r') as file:
    # Initialize variables to store values
    simInsts = 0
    simOps = 0
    numCycles = 0
    # Flag to track whether we have reached the "End Simulation Statistics" section
    foundEnd = False

    # Iterate over each line in the file
    for line in file:
        # Check if we have reached the "End Simulation Statistics" section
        if "End Simulation Statistics" in line:
            foundEnd = True
            continue

        # If we have not reached the "End Simulation Statistics" section, skip this line
        if not foundEnd:
            continue
        # Split the line by spaces to get a list of words
        words = line.split()
        #check if the line is empty. If it is, skip it
        if len(words) == 0:
            continue
        # Check if the first word is one of the values of interest
        if words[0] == "simInsts":
            # The value we want is the second word in the line, so we convert it to an integer and store it in the simInsts variable
            simInsts = int(words[1])
        elif words[0] == "simOps":
            simOps = int(words[1])
        elif words[0] == "system.cpu.numCycles":
            numCycles = int(words[1])

# Print the values to check that they were extracted correctly
print("simInsts:", simInsts)
print("simOps:", simOps)
print("numCycles:", numCycles)
