#include <iostream>  // This is the standard header file for input/output in C++.

//extra library
#include <string>

using namespace std; // This line is used to include the standard namespace in the program.


int Count (int list[], int iterator) {

    //declare and initialize the iterator that will increment 
    //each time an even number is found
    int evens = 0;

    //loop through the array
    for (int i = 0; i < iterator; i++) {

        //check if current element is even (i.e. i % 2 == 0) 
        if (list[i] % 2 == 0) {
            //iterate
            evens++;
        }
    }

    //return the total count
    return evens;
}

int main()
{

    //declare array
    int num_List[100];

    //declare integer variable that will be the total count of even numbers
    //and iterator to count the total amount
    int iterator = 0;
    int num_Even;

    //string variable to confirm user choice
    string choice;

    //Loop until the user quits
    while (choice != "yes") {

        cout << "Enter a number: " << endl;
        cin >> num_List[iterator];

        cout << "Are you finished? Type \"yes\" if so." << endl;
        cin >> choice;

        if (choice != "yes") {
            iterator++;
        }
    }

    //assign num_Even to the result of the Count function
    num_Even = Count(num_List, iterator);

    cout << "Total number of evens: " << num_Even << endl;
    

    return 0; // Ignore this line (do not delete it)
}