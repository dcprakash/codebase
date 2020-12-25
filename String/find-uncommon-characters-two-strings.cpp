// C++ implementation to find the uncommon 
// characters of the two strings 
// https://www.geeksforgeeks.org/find-uncommon-characters-two-strings/

/*
str1 = "alphabets"
str2 = "characters"
str3=""
for i in str1:
    if i not in str2 and i not in str3:
        str3+=i
for i in str2:
    if i not in str1 and i not in str3:
        str3+=i
print(str3)
*/

#include <bits/stdc++.h> 
using namespace std; 

// size of the hash table 
const int MAX_CHAR = 26; 

// function to find the uncommon characters 
// of the two strings 
void findAndPrintUncommonChars(string str1, string str2) 
{ 
	// mark presence of each character as 0 
	// in the hash table 'present[]' 
	int present[MAX_CHAR]; 
	for (int i=0; i<MAX_CHAR; i++) 
		present[i] = 0; 

	int l1 = str1.size(); 
	int l2 = str2.size(); 

	// for each character of str1, mark its 
	// presence as 1 in 'present[]' 
	for (int i=0; i<l1; i++) 
		present[str1[i] - 'a'] = 1; 

	// for each character of str2 
	for (int i=0; i<l2; i++) 
	{ 
		// if a character of str2 is also present 
		// in str1, then mark its presence as -1 
		if (present[str2[i] - 'a'] == 1 
			|| present[str2[i] - 'a'] == -1) 
			present[str2[i] - 'a'] = -1; 

		// else mark its presence as 2 
		else
			present[str2[i] - 'a'] = 2; 
	} 

	// print all the uncommon characters 
	for (int i=0; i<MAX_CHAR; i++) 
		if (present[i] == 1 || present[i] == 2 ) 
			cout << (char(i + 'a')) << " "; 
} 

// Driver program to test above 
int main() 
{ 
	string str1 = "abc";
	string str2 = "cdc"; 
	findAndPrintUncommonChars(str1, str2); 
	return 0; 
} 
