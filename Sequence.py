import asyncio
import os.path
from os import path


async def main():
    print("\nMain Interface\n\n")
    print("1. Record new sequence\n2. Modify existing sequence\n3. Compare sequences\n4. Exit (Closes program)\n") 

    select = input()
    select = int(select)    

    if (select < 1 | select > 4):
        print("\nInvalid option!")
        print (await main())

    else:
      print(await mainOptions(select))

    return select


async def writeToNew():

    print("\nEnter new name for sequence: ")
    
    name = input()
    filename = 'A:/Code/DNA/Data Entries/' + name + '.txt'
    entry = open(filename, "w")

    print("Using no spaces, type or paste your data sequence in text.")
    
    sequence = input()

    entry.write(sequence)


async def uploadCheck():

    print("\nPlease drop your file in folder containing the sequence in text.\n\nType 'done' to proceed.\n")

    firstEntry = input()

    if (firstEntry == "done"):
        print("\nPlease type name of sequence file name to check if it has been recieved: ")

        name = input()
        filename = 'A:/Code/DNA/Data Entries/' + name + '.txt'

        if (os.path.exists(filename) == True):
            print("\nFile successfully stored!")
            exit
            
        else:
            print("\nFile not found. Let's try again...\n")
            print(await uploadCheck())

    else:
        print("\nSorry, would you like to go back? (Y/N)")
        
        goback = input()
        
        if ((input == 'Y') or (input == 'y')):
          print(await main())
    
        else:
            print(await uploadCheck())

async def mainOptions(select):

    if (select == 1):
        print("\nRecording new sequence:\n1. Drop File\n2. Record manually\n")
        firstInput = input()

        if (int(firstInput) == 1):
           await uploadCheck()

        elif (int(firstInput) == 2):
           await writeToNew()

        else:
            print(mainOptions(select))



asyncio.run(main())