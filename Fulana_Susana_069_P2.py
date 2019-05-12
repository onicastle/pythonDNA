"""This program reads DNA sequences from an input file and finds the
consensus sequence.  An output file is also created to store the
counts per column, so as to validate the consensus.
Add the corresponding code to accomplish the requested tasks
"""
##### ADD YOUR NAME, Student ID, and Section number #######
# NAME: 
# STUDENT ID:
# CLASS:
# SECTION: 
###########################################################



#Read DNA sequences from file and return them in a list.
# Assuming the target file exist's

def load_data(fileName):
    
    dataList = list()
    
    target=open(fileName,'r')
    
    for line in target:
        if line.startswith('>'): #skips description 
            continue
        strip=line.strip() #removes whitespaces & newlines 
        dataList.append(strip) #adds sequences to dataList
    target.close()
    return dataList



    # Usew dataList to save the the all data to the target file
    # If file opens successfully, loop over the contents and store sequences in list.
    # Skip description lines 
def count_nucl_freq(dataList):
    countStruct = []
    colCount=0
    while colCount < len(dataList[0]):
        dataDict={} #Through each column it creates a dict for that column
        for rowIndex in dataList:
            letter= rowIndex[colCount] #tells the iterator where to go
            dataDict[letter]=dataDict.get(letter,0)+1 #counts the ocurrences
            if letter != 'A':
                dataDict['A'] = dataDict.get('A', 0)
            if letter != 'T':
                dataDict['T'] = dataDict.get('T', 0)
            if letter != 'C':
                dataDict['C'] = dataDict.get('C', 0)
            if letter != 'G':
                dataDict['G'] = dataDict.get('G', 0)
        countStruct.append(dataDict) #adds each columns dict to the list 
        colCount = colCount+1 #column traveler
    return countStruct




    # Indexed by columns (List of what? countStruct is a List of dictionaries)
    # Loop over the sequences in dataList to count the nucleotides
    # We'll need a nested loop to process every character in every sequence.
    # Recommend: Use outer loop for columns (characters) and inner loop for
    # rows (sequences), since countStruct only cares about the characters (not the seqs).
def find_consensus(countData):
    """Return the consensus sequence according to highest-occuring nucleotides"""
    largest = 0
    
    consensusString = ""
    
    for columnDicts in countData:
        largest= 1
        for letter, frequency in columnDicts.items(): #this loop filters the largest frequency in the column dictionaries to construct the consensus sequence
            if frequency > largest:
                largest = frequency
        consensusString = consensusString + letter
    return consensusString


    # Loop here to find highest-occuring nucleotide in each column / concatenate them into consensusString
    # creates a new .txt file called DNAOutput and prints the consensus string in the output file
def process_results(countData, outFilename):
    """Print consensus to screen and store results in output file."""
    consensus = find_consensus(countData)
    index= 1
    fhandle= open(outFilename, 'w') 
    fhandle.write('Consensus: ' + consensus + '\n' + '\n') 
    for colDict in countData: 
        tupsList=[]
        for nucleotide,frequency in colDict.items():
            tupsList.append((frequency,nucleotide)) #Appends the coverted dictionaries to the list of tuples
        sortedTups= sorted(tupsList, reverse=True) #sorts the tuple lists
        fhandle.write('Pos ' + str(index) + ":" + '\t' + '\t') # Prints position index 
        index=index+1 #Counter for columns for positions
        for tuple in sortedTups:
            fhandle.write(tuple[1] + ':' + str(tuple[0])+'\t') #Prints the frequencies 
        fhandle.write('\n')
    print('The Consensus is:' , consensus + '\n' + 'see "DNAOutput.txt" int the directory' + '\n')
    fhandle.close()

    
    # Now open the output file, and write the consensus string.
    # Then loop, to print nucleotide count in non-increasing order.
    # Each row in the output file (except the first one) should
    # have the count data for a column, in order of columns.
def main():

    # File name "constants". Assume the names of the files don't change.
    INPUTFILE  = "DNAInput.fasta"
    OUTPUTFILE = "DNAOutput.txt"

    seqList = load_data(INPUTFILE)

    countData = count_nucl_freq(seqList)

    process_results(countData, OUTPUTFILE)

# The code below makes Python start from the main function
# whenever our program is invoked as a "standalone program"
# (as opposed to being imported as a module).
if __name__ == "__main__":
    main()
