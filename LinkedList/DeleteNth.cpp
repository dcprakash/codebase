#include <iostream>
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    Node* next;
};

Node* head;

void deleteNode(int n) {
    struct Node* t1 = head;
    if (n == 1){
        head = t1->next;
        free(t1);
        return;
    }
    for(int i=0;i<n-2;i++){
        t1 = t1->next;
    }
    struct Node* t2 = t1->next;
    t1->next = t2->next;
    free(t2);
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
    std::cout << "Delete Node" << std::endl;
    head = NULL;
    insertBegining(1);
    insertBegining(6);
    insertBegining(2);
    std::cout << "Insert at Begining" << std::endl;
    print();
    deleteNode(1);
    std::cout << std::endl << std::endl << "After deleting first element" << std::endl;
    print();
    deleteNode(2);
    std::cout << std::endl << std::endl << "After deleting second element" << std::endl;
    print();
    
}