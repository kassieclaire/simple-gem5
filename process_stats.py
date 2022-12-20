#Author: Kassie Povinelli
# Open the stats file in read mode

#function which reads the stats.txt file and returns a dictionary with the values of interest
def read_stats_file_simple():
    #open the file in read mode
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
    # Return the values of interest
    return simInsts, simOps, numCycles
#function which reads the stats file and returns a dictionary with the values of interest, which are specified by the user
#This version also can read from any area of interest, which is specified by the user
#The area of interest starts with 0. Area 0 is up to the first "End Simulation Statistics" line, 
#area 1 is up to the second "End Simulation Statistics" line, and so on
def read_stats_file(stats_of_interest, area_of_interest, filename = 'stats.txt'):
    #open the file in read mode
    with open(f'stats/{filename}', 'r') as file:
        # Initialize variables to store values
        simInsts = 0
        simOps = 0
        numCycles = 0
        #initialize the area counter
        area_counter = 0
        # Iterate over each line in the file
        for line in file:
            # Check if we have reached the "End Simulation Statistics" section
            if "End Simulation Statistics" in line:
                foundEnd = True
                #increment the area counter
                area_counter += 1
                continue
            #check if the area counter is less than the area of interest. If it is, skip this line
            if area_counter < area_of_interest:
                continue
            #check if the area counter is greater than the area of interest. If it is, stop reading the file
            if area_counter > area_of_interest:
                break
            # Split the line by spaces to get a list of words
            words = line.split()
            #check if the line is empty. If it is, skip it
            if len(words) == 0:
                continue
            # Check if the first word is one of the values of interest
            if words[0] in stats_of_interest:
                # The value of interest is the second word in the line, so we convert it to a float and store it in the stats_of_interest dictionary
                stats_of_interest[words[0]] = float(words[1])
    # Return the values of interest
    return stats_of_interest
#function which runs if this file is run as a script. It uses the default name of the stats file and the
#values of interest are simInsts, simOps, and numCycles (system.cpu.numCycles). It calls the read_stats_file function
#It then prints the values of interest
if __name__ == "__main__":
    #set up the dictionary of stats of interest
    stats_of_interest = {"simInsts": 0, "simOps": 0, "system.cpu.numCycles": 0}
    #call the read_stats_file function with the area of interest being 1
    stats_of_interest = read_stats_file(stats_of_interest, 1)
    #print the values of interest
    print("The values of interest are:")
    print(stats_of_interest)
    