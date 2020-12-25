#include <iostream>
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* head;

void reverseList(){
    struct Node *prv, *cur, *nxt;
    cur = head;
    prv = NULL;
    while(cur != NULL){
        nxt = cur->next;
        cur->next = prv;
        prv = cur;
        cur = nxt;
    }
    head = prv; 
}

void print()
{
    struct Node* t1 = new Node;
    t1 = head;
    std::cout << "List is: ";
    while (t1 != NULL) {
        std::cout << t1->data;
        t1 = t1->next;
    }
}

void insertBegining(int x)
{
    Node* t1 = new Node();
    t1->data = x;
    t1->next = head;
    head = t1;
}

int main()
{
	std::cout << "This is linked list reverse code" << std::endl<< std::endl;
    head = NULL;
    insertBegining(1);
    insertBegining(6);
    insertBegining(2);
    std::cout << "Insert at Begining" << std::endl;
    print();
    std::cout << std::endl;
    std::cout << std::endl;
    std::cout << "After Reversal" << std::endl;
    reverseList();
    print();
}