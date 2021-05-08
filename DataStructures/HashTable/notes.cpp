class hashTable {
    private:
        static const int tableSize = 10;
        struct item {
            string name;
            string drink;
            item *next;
        }
        item *hashingTable[tableSize];
    
    public:
        hashTable();
        int hash(string key);
        void addItems(string name, string drinks);
        void findDrink(string name);
        int numberOfItems(int index);
        void print();
}

hashTable::hashTable() {
    for(int i=0;i<tableSize;i++){
        hashingTable[i]->name="empty";
        hashingTable[i]->drink="empty";
        hashingTable[i]->next=null;
    }
}

int hashTable::hash(string key) {
    int hash=0, index;
    for(int i=0;i<key.length();i++){
        hash=hash+key[i];
    }
    index=hash%tableSize;
    return index;
}

void hashTable::addItems(string name, string drink) {
    index=hash(name);
    
    if hashingTable[index]->name=="empty" {
        hashingTable[index]-->name=name;
        hashingTable[index]->drink=drink;
        hashingTable[index->next=null;
    }
    else {
        struct item* ptr = hashingTable[index];
        
        item* t2 = new item();
        t2->name=name;
        t2->drink=drink;
        t2->next=null;
        
        while(ptr->next!=null){
            ptr=ptr->next;
            ptr->next=t2;
        }
        
    }
}

void hashTable::findDrink(string name){
    index=hash(name);
    if hashingTable[index]->name=="empty"{
        print("item not found");
    }
    else{
        item* ptr=hashingTable[ix];
        while(ptr->next!=NULL){
            if ptr->name==name;
                print(ptr->drink)
                exit
            else
                ptr=ptr->next
        }
        print("cannot find the person")

    }
}

int hashingTable::numberOfItems(int index){
    int count = 0;
    if hashingTable[index]-->name=="empty"
        return count
    else
        item* ptr = hashingTable[index];
        while ptr->next!=NULL
            ptr=ptr->next;
            count++;
    return count;
}

void hashTable::print() {
    int items;
    for(int i=0; i<tableSize; i++){
        items = numberOfItems(i);
        for(int j=0; j<items;i++){
            print(hashingTable[j]->name)
            print(hashingTable[j]->drink)
        }
    }
}

class hashTable {
    private:
        int tableSize=10;
        struct item {
            string name;
            string drink;
            item* next;
        }
        item* hashingTable[tableSize];
    public:
        hashTable();
}

hashTable::hashTable(){
    for(int i=0;i<tableSize;i++){
        hashingTable[i] = new item();
        hashingTable[i]->name="empty";
        hashingTable[i]->drink="empty";
        hashingTable[i]->next=NULL;
    }
}

hashTable::getHash(string name){
    int h=0, ix;
    for(int i=0;i<name.length();i++){
        h=h+int(name[i])
    }
    ix=h%tableSize;
    return ix;
}

hashTable::addItems(string name, string drink){
    index=getHash(name);
    if hashingTable[ix]-->name=="empty"
        hashingTable-->name=name;
        hashingTable-->drink=drink;
        hashingTable-->next=NULL;
        
    else
        item* ptr = hashingTable[ix];
        
        item* t = new item();
        t->name=name;
        t->drink=drink;
        t->next=NULL;
        
        while ptr->next != NULL
            ptr=ptr->next;
        
        ptr->next=t;
}

hashTable::findDrink(string name){
    index = getHash(name);
    if hashingTable[index]-->name=="empty"
        print("item does not exist")
    else
        item* ptr = hashingTable[index];
        while ptr->name!=name
            ptr=ptr->next
        
}

