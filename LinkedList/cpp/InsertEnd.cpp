#include <iostream>
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* head;

void insertEnd(int x)
{
	Node* t1 = new Node();
	t1->data = x;
	t1->next = NULL;
	Node* t2 = head;
	while (t2->next != NULL) {
		t2 = t2->next ;
	}
	t2->next = t1;
	
}

void print()
{
    struct Node* t1 = new Node;
    t1 = head;
    std::cout << "List is:";
    while (t1 != NULL) {
        std::cout << t1->data;
        t1 = t1->next;
    }
}

int main()
{
    std::cout << "Hello from AWS Cloud9!" << std::endl;
    head = NULL;
    std::cout<< std::endl;
    insertEnd(1);
    insertEnd(6);
    insertEnd(2);
    std::cout << "Insert at the End" << std::endl;
    print();
}