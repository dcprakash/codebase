//https://practice.geeksforgeeks.org/problems/lru-cache/1

#include<bits/stdc++.h>
using namespace std;
class LRUCache
{
    public:
    LRUCache(int );
 
    int get(int );
 
    void set(int , int );
};

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
    int n;
    cin>>n;
    LRUCache *l  = new LRUCache(n);
    int q;
    cin>>q;
    for(int i=0;i<q;i++)
    {
        string a;
        cin>>a;
        if(a=="SET")
        {
            int aa,bb;
            cin>>aa>>bb;
            l->set(aa,bb);
        }else if(a=="GET")
        {
            int aa;
            cin>>aa;
            cout<<l->get(aa)<<" ";
        }
    }
    cout<<endl;
    }
}


/*Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above.*/

/*The structure of the class is as follows 
class LRUCache
{
public:
    LRUCache(int );
    int get(int );
    void set(int , int );
};*/
/*You are required to complete below methods */
/*Inititalize an LRU cache with size N */
list<int> dq;

unordered_map<int,int> ma;
int csize;
LRUCache::LRUCache(int N)
{
    csize=N;
    dq.clear();
    ma.clear();
     
     
}
/*Sets the key x with value y in the LRU cache */
void LRUCache::set(int x, int y) 
{
    list<int>::iterator i = find(dq.begin(),dq.end(),x);
    if(ma.find(x)==ma.end()){
        if(dq.size()==csize){
            int last=dq.back();
            dq.pop_back();
            ma.erase(last);
        }
    }
    else dq.erase(i);
    dq.push_front(x);
    ma[x]=y;
    
}
/*Returns the value of the key x if 
present else returns -1 */
int LRUCache::get(int x)
{
   list<int>::iterator i = find(dq.begin(),dq.end(),x);
   
    if(ma.find(x)==ma.end()) return -1;
    else {
        dq.erase(i);
        dq.push_front(*i);
        
        return ma[x];        
        
        
    }
}