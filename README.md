# Personal Projects

Personal Projects I have been working on outside of school.

**- Cipher Auxiliary Scripts:**

Java program used to demonstrate the encryption and decryption methods of the famous Vigenère cipher. 

This program is currently being worked on right now to test a bulk of keys based off a dictionary to test ciphertext with a key length of 4 or below. 
    
**- Card Counter:**

Inspired by one of my CS2 questions, and effectively putting it into code:
   
"A friend of yours has a large pile of playing cards from several identical decks. They know that they have at least several complete decks, but also that some of the decks are incomplete.They want to get as many possible complete, sorted decks of cards out of the pile as they can. Devise a straightforward method for your friend to do so. Explain why you chose it, and what sorting algorithm – or combination of sorting algorithms – it most resembles. (Length limit: Two paragraphs.)"
   
   
Every card in the stack goes from A to 10, Jack, Queen, And King (or in this case, 1-13), and needs one of each four types per sorted stack to be considered a full deck. The first thing that must be done in order to pre determine the maximum number of decks in the stack is to use a Bucket sort to essentially sort by number. With bucket sort, we’ll be able to have 13 bins, A - 10, Jack, Queen, and King. (In this c file we used a predetermined array of arrays using dynamically allocated pointers). We will now assume that the MINIMUM amount of cards in any of the buckets will be our D, or number of predetermined decks. Now we examine the bucket of values with the least amount of cards, since it has to be the maximum amount of full decks within the stack. Since there are four of each type of a card in a stack, we must examine any groupings that exist from within this bucket. Each type (heart,spades, clubs, and diamonds) must now be sorted by grouping, since there could exist duplicates. Finally, we count the amounts of each of the four types. The minimum amount ofcards x of a certain type are guaranteed to match with x cards of each type and of bucket. With them all added up, there will now be a use of another sort (since there’s only 4 types of sums tocompare with each other, so the run time will be fairly quick) to determine the amount of full decks in the stack.

**- Logisim Clock Logic Gate Simulator**:

Used Logisim to effectively create a clock that counts seconds, hours, days, months, and years. Also has a leap year detection function, all done with logic gates.

**- Turing Machine Replication in Python**:

Simulated a turing machine in Python complete with "tape", initial and final states, transitions, and individual head positions. Given states are defined within the program, and the machine completes its readthrough of the tape and returns an accept or reject state.  

