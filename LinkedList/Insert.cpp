#include <iostream>
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* head;

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
    std::cout << "Hello from AWS Cloud9!" << std::endl;
    head = NULL;
    insertBegining(1);
    insertBegining(6);
    insertBegining(2);
    std::cout << "Inser at Begining" << std::endl;
    print();

}