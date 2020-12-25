/*
Might have to remove:
-parsing right nodes on method leftp
-parsing left nodes on method rightp

https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1

Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.*/


/* A binary tree Node
struct Node
{
    int data;
    Node* left, * right;
}; */
void leftp(Node *root){
     if(root){
    if(root->left){
         cout << root->data << " ";
         leftp(root->left);
    }
    else if(root->right){
        cout << root->data << " ";
         leftp(root->right);
    }
     }
}
void leaf(Node *root){
    if(root){
        leaf(root->left);
        leaf(root->right);
        if(root->left==NULL && root->right==NULL )
        cout << root->data << " ";
    }
}
void rightp(Node *root){
    if(root){
    if(root->right){
        rightp(root->right);
        cout << root->data << " "; 
    }
    else if(root->left){
        rightp(root->left);
     cout << root->data << " ";   
    }
    }
}
void printBoundary(Node *root)
{    
    cout << root->data << " ";
    leftp(root->left);
    leaf(root);
    rightp(root->right);
         
     
}