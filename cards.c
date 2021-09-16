#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

//OBJECTIVE:

//take in the unsorted stack of cards
//ask the amounts of each cards * 13 OR randomly generate it with size s 
//create cards 


//take int pointer(array) of struct where 0-12, each index marks the amount of cards //and type

//sort to min, then count to min of each type
//spit total amounts of decks

//if one index is all of one type or one index is 0, return incomplete




int** menu(){

  int select;
  int** stack = (int**) malloc(13 * sizeof(int*));

  

  printf("Card Stack Sort Finder!\n\n");

  printf("What would you like to do?\n\n");
  printf("1. Input your own stack of cards\n");
  printf("2. Generate random stack of cards\n\n");

  scanf("%d", &select);

  while (select != 1 && select != 2){

    printf("Pick a valid selection!\n\n");
    scanf("%d", &select);
  }

  

  if (select == 1){


    printf("\nCards will be oriented as 1-13 (denoted for aces, jacks, queens, and kings)\n");
    printf("Please enter the raw number of each type of card for cards 1 - 13\n");


    for (int i = 1; i <= 13; i++){
      
      stack[i] = malloc(4 * sizeof(int));

      //each card will have its own temp array for each of the four types
      //In order: hearts, clubs, spades, diamonds

      printf("Card %d:\n\n", i);

      printf("How many hearts? ");
      scanf("%d", &stack[i][0]);
     

      printf("How many clubs? ");
      scanf("%d", &stack[i][1]);
    

      printf("How many spades? ");
      scanf("%d", &stack[i][2]);


      printf("How many diamonds? ");
      scanf("%d", &stack[i][3]);
     
      
   

    }

  }

  else if (select == 2) generateStack(stack);
  
  return stack;
}

  int minimum(int* number){

    int min = __INT_MAX__;

    for (int i = 0; i < 4; i++){

      if (min > number[i]){

        min = number[i];

      }
      
    }

    return min;


  }


void generateStack(int** stack){

  // we must create a random generator of four types. Kept to 100 to reduce chance of overflow.

  srand(time(NULL));

  int r = rand() % 20;

  for (int i = 0; i < 14; i++){

    stack[i] = (int*) calloc (4,sizeof(int));

    r = rand()%50 + 1;
    stack[i][0] = r + 1;

    r = rand()%50;
    stack[i][1] = r + 1;

    r = rand()%50;
    stack[i][2] = r + 1;

    r = rand()%50;
    stack[i][3] = r + 1;


  }

  return stack;
    
}


int solveStack(int ** stack){
    int min = __INT_MAX__;

    for (int i = 0; i < 13; i++){

        if (min > minimum(stack[i])){
          min = minimum(stack[i]);
        }

    }
    return min;
}

void freeStack(int** stack){

  for (int i = 0; i < 14; i++){

      free(stack[i]);

  }

  free(stack);
}




void printStack(int** stack){

  printf("CURRENT STACK:\n\n\n");

  for (int i = 0; i < 13; i++){
    if (i == 0){
      printf("%d Ace of hearts\n", stack[i][0]);
      printf("%d Ace of clubs\n", stack[i][1]);
      printf("%d Ace of spades\n", stack[i][2]);
      printf("%d Ace of diamonds\n", stack[i][3]);
    }
    else if (i == 10){
      printf("%d Jack of hearts\n", stack[i][0]);
      printf("%d Jack of clubs\n", stack[i][1]);
      printf("%d Jack of spades\n", stack[i][2]);
      printf("%d Ace of diamonds\n", stack[i][3]);

    }
    else if (i == 11)
    {
      printf("%d Queen of hearts\n", stack[i][0]);
      printf("%d Queen of clubs\n", stack[i][1]);
      printf("%d Queen of spades\n", stack[i][2]);
      printf("%d Queen of diamonds\n", stack[i][3]);
      
    }
    else if (i == 12){

      printf("%d King of hearts\n", stack[i][0]);
      printf("%d King of clubs\n", stack[i][1]);
      printf("%d King of spades\n", stack[i][2]);
      printf("%d King of diamonds\n", stack[i][3]);
      
    }

    else {
      printf("(%d) %d of hearts\n", stack[i][0], (i+1));
      printf("(%d) %d of clubs\n", stack[i][1], (i+1));
      printf("(%d) %d of spades\n", stack[i][2], (i+1));
      printf("(%d) %d of diamonds\n", stack[i][3], (i+1));
    }
    
    printf("\n\n");
   
  }
}

int main(void) {
  int** stack = menu();
  printStack(stack);
  printf("MOST COMPLETE SETS IN STACK OF UNSORTED CARDS: %d", solveStack(stack));
  freeStack(stack);
}