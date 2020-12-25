#include <iostream>
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    Node* next;
};

Node* head;

void insertNode(int n, int x) {
    Node * t1 = new Node();
    t1->data=x;
    t1->next=NULL;
    
    if (n==1){
        t1->next=head;
        head=t1;
        return;
    }
    Node* t2 = head;    
    for (int i=0;i<n-2;i++){
        t2 = t2->next;
    }
    t1->next = t2->next;
    t2->next = t1;
}

void insertBegining(int x)
{
    Node* t1 = new Node();
    t1->data = x;
    t1->next = head;
    head = t1;
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
    std::cout << "Insert Nth Node" << std::endl;
    head = NULL;
    insertBegining(1);
    insertBegining(6);
    insertBegining(2);
    std::cout << "Insert at Begining" << std::endl;
    print();
    insertNode(1, 3);
    std::cout << std::endl << std::endl << "After Insert 3 at first element" << std::endl;
    print();
    insertNode(2, 5);
    std::cout << std::endl << std::endl << "After Insert 5 at second element" << std::endl;
    print();
    
}