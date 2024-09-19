#include <iostream>   // This is the standard header file for input/output in C++.
using namespace std;  // This line is used to include the standard namespace in the program.

int main()
{
    string yourName;
    
    cout << "enter your name : ";
    cin >> yourName;

    cout << "Hello " + yourName << endl;

    return 0; //Ignore this line (do not delete it)
}