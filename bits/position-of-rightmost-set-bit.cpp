// C++ implementation of above approach 
// https://www.geeksforgeeks.org/position-of-rightmost-set-bit/
#include <iostream> 
using namespace std; 
#define INT_SIZE 32 

int Right_most_setbit(int num) 
{ 
	int pos = 1; 
	// counting the position of first set bit 
	for (int i = 0; i < INT_SIZE; i++) { 
		cout<<(1 << i)<<endl;
		cout<<(num & (1 << i)) <<endl;
		cout<< (!(num & (1 << i))) << endl;
		cout <<"--------"<<endl;
		if (!(num & (1 << i))) 
			pos++; 
		else
			break; 
	} 
	return pos; 
} 
int main() 
{ 
	int num = 2; 
	int pos = Right_most_setbit(num); 
	cout << pos << endl; 
	return 0; 
} 
// This approach has been contributed by @vivek kumar9 
