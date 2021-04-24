#include <iostream>

struct node {
    int data;
    struct node* next;
}


void insertAtBegin(int x){
    struct node* t = new node();
    t->data=x;
    t->next=head;
    head = t;
}


void insertAtEnd(int x){
    struct node* t = new node();
    t->data=x
    t->next=null;
    struct node* t2 = head;
    while (t2->next!=null){
        t2=t2->next;
    }
    t2->next=t1;
    
}


void inserAtNth(int x, int n){
    struct node* t1 = new node();
    t1->data=x
    t1->next=null;
    
    if n==1 {
        t1->next=head;
        head=t1;
        return;
    }
    
    struct node* t2 = head;
    for(int i=0;i<2;i++){
        t2=t2->next;
    }
    t1->next=t2->next;
    t2->next=t1;
}


void print(){
    struct node* t = head;
    while (t->next!=null){
        print(t->data);
        t=t->next;
    }
}


void reverseList(){
    struct node* prv, cur, nxt;
    cur=head;
    prv=null;
    while(cur->next!=null){
        nxt=cur->nxt;
        cur->nxt=prv;
        prv=cur;
        cur=nxt;
    }
    head=prv;
}


void deleteNth(int n){
    struct node* t1 = head;
    
    if(n==1){
        head = t1->next;
        free(t1)
        return;
    }
    
    for(int i=0;i<n-2;i++){
        t1=t1->next;
    }
    
    struct node* t2 = t1->next;
    t1->next=t2->next;
    free(t2);
}

int main()
{
    head = null;
    int n, i, x;
    scanf("%d", &n);
    //1, 4, 7, 8
    for(i=0;i<n;i++){
        scanf("%d", &x);
        insertAtBegin(x)
    }
}





// double linked list
struct node {
    int data;
    struct node* next;
    struct node* prv;
}

void getNewNode(int x){
    struct node* t = new node();
    node->data=x;
    node->next=null;
    node->prv=null;
    return t;
}

void insertAtBeginDouble(int x){
    struct node* newnode = getNewNode(x);
    
    if(head==null){
        head=newnode;
        return;
    }
    
    head->prv=newnode;
    newnode->next=head;
    head=newnode;
}
    
void printReverse(){
    struct node* t = head;
    while (t->next!=null){
        t=t->next;
    }
    while(t->prv!=null){
        print(t->data);
        t=t->prv;
    }
}





//Circular
struct node{
    int data;
    struct node *next;
}

struct node *addEmpty(struct node *lst, int x){
    if lst!=null{
        return lst;
    }
    
    struct node *lst = new node();
    lst->data=x;
    lst->next=lst;
    
    return lst;
}

struct node *addAtBegin(struct node *lst, int x){
    if lst==null{
        addEmpty(lst, x)
    }
    
    struct node *t = new node();
    t->data=x;
    t->next=lst->next;
    lst->next=t;
    
    return lst;
}

struct node *addAtEnd(struct node *lst, int x){
    if lst==null{
        addEmpty(lst, x);
    }
    
    struct node *t = new node();
    t->data=x;
    t->next=last->next;
    last->next=t;
    last=t;
    
    return lst;
}

struct node *addAtNth(struct node *lst, int x, int n){
    if lst==null {
        addEmpty(lst, x)
    }
    
    struct node *t1 = new node();
    t1->data=x;
    
    struct node *t2 = lst;
    for(int i=0; i<n-2; i++){
        t2=t2->next;
    }
    
    t1->next=t2->next;
    t2->next=t1;
    
    if t2==lst{
        lst=t1;
    }
    
    return lst;
}

void traverse(struct node *lst){
    struct node* t = lst->next;
    
    if lst == null {
        print("list if empty");
        return;
    }
    
    do{
        std::cout << t->data << std::endl;
        t = t->next;
    }while(t!=lst->next);
}

void hasCycle(struct node head){
    if head == null {
        std::cout << "empty" << std::endl;
    }
    
    node fast = head->next;
    node slow = head;
    
    while (fast!=null && fast->next!=null && slow!=null){
        if fast == slow {
            std::cout << "Cycle detected" << std::endl;
        }
        fast=fast->next->next;
        slow=slow->next;
    }
    std::cout << "no cycle detected" << std::endl;
}

int main(){
    struct node* lst = null;
}



