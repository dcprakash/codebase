#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using std::string;

class hashTable {
    private:
        static const int tableSize = 10;
        struct item {
            string name;
            string drink;
            item* next;
        };
        item* hashingTable[tableSize];
    
    public:
        hashTable();
        int hash(string key);
        void addItems(string names, string drinks);
        void findDrink(string names);
        void print();
        int numberOfItems(int ix);
};

hashTable::hashTable() {
    for(int i=0;i<tableSize;i++){
        hashingTable[i] = new item;
        hashingTable[i]->name = "empty";
        hashingTable[i]->drink = "empty";
        hashingTable[i]->next = NULL;
    }
}

int hashTable::hash(string key) {
    int hash=0, index;
    for(int i=0;i<key.length();i++){
        hash=hash+(int)key[i];
    }
    index = hash % tableSize;
    std::cout << "Calculated Hash is ";
    std::cout << index << std::endl;
    return index;
}

void hashTable::addItems(string names, string drinks){
    int ix = hash(names);
    if(hashingTable[ix]->name=="empty"){
        std::cout << "inserting for an emptry table" << std::endl;
        hashingTable[ix]->name=names;
        hashingTable[ix]->drink=drinks;
    }
    else{
        item* ptr = hashingTable[ix];

        item* temp = new item();
        temp->name=names;
        temp->drink=drinks;

        while (ptr->next!=NULL){
            ptr=ptr->next;
        }
        
        ptr->next=temp;

    }

}

void hashTable::findDrink(string names){
    int ix = hash(names);
    if (hashingTable[ix]->name=="empty"){
        std::cout << "Cannot find record for this name" << std::endl;
    }
    item* ptr = hashingTable[ix];
    while(ptr->name!=names){ //also check for null, if item does not exist, handle it.
        ptr=ptr->next;
    }
    std::cout << names <<" drnks " << ptr->drink << std::endl;
}

int hashTable::numberOfItems(int ix){
    int cnt=0;
    if (hashingTable[ix]->name=="empty"){
        return cnt;
    }
    else{
        item* ptr = hashingTable[ix];
        cnt++;
        while(ptr->next != NULL){
            cnt++;
            ptr=ptr->next;
        }
        return cnt;
    }

}

void hashTable::print(){
    int ix;
    for(int i=0;i<tableSize;i++){
        ix = numberOfItems(i);
        if(ix!=0){
            for(int j=0;j<ix;j++){
                std::cout << "----------" << std::endl;
                std::cout << "Row " << i <<" has " << ix<< " items"<<std::endl;
                std::cout<<hashingTable[5]->name << std::endl;
                std::cout<<hashingTable[5]->drink << std::endl;
                std::cout << "----------" << std::endl;
            }
        }
    }
}



int main()
{
	std::cout << "This is Hash Table" << std::endl;
	hashTable h;
	h.hash("Darsh");
	h.addItems("Darshan", "Wine");
	h.print();
	int noi = h.numberOfItems(5);
	std::cout<<noi << " items" << std::endl;
	h.findDrink("Darshan");
}