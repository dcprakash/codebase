//https://practice.geeksforgeeks.org/problems/count-bst-nodes-that-lie-in-a-given-range/1

//Code by 1shubhamjoshi1
#include<bits/stdc++.h>
using namespace std;
struct Node {
int data;
struct Node * right, * left;
};
void insert(Node ** tree, int val)
{
    Node *temp = NULL;
    if(!(*tree))
    {
        temp = (Node *)malloc(sizeof(Node));
        temp->left = temp->right = NULL;
        temp->data = val;
        *tree = temp;
        return;
    }
    if(val < (*tree)->data)
    {
        insert(&(*tree)->left, val);
    }
    else if(val > (*tree)->data)
    {
        insert(&(*tree)->right, val);
    }
}
int getCountOfNode(Node *root, int l, int h);
int main()
{
    int T;
    cin>>T;
    while(T--)
    {
        Node *root;
        Node *tmp;
        //int i;
        root = NULL;
        int N;
        cin>>N;
        for(int i=0;i<N;i++)
        {
            int k;
            cin>>k;
            insert(&root, k);
        }
        int l,r;
        cin>>l>>r;
        cout<<getCountOfNode(root,l,r)<<endl;
    }
}


/*Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above.*/

/*
The structure of a BST node is as follows:
struct Node {
int data;
Node * right, * left;
};
*/
int getCountOfNode(Node *root, int l, int h)
{
  // your code goes here
  if(root==NULL)
  return 0;
  if(root->data<l)
  return getCountOfNode(root->right,l,h);
  else if(root->data>h)
  return getCountOfNode(root->left,l,h);
  else if((root->data>=l) && (root->data<=h))
  return 1+getCountOfNode(root->left,l,h) + getCountOfNode(root->right,l,h);
}