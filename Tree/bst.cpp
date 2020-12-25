#include <iostream>
#include <stdio.h>
#include <stdlib.h>

class bst {
    public:
        struct node {
          int key;
          node* left;
          node* right;
        };
        node* root;
        bst();
        node* createLeaf(int key);
        void addLeaf(int key);
        void printInOrder(node* ptr);
        node* searchTree(int key, node* ptr);
};

bst::bst(){
    root=NULL;
}

node* bst::createLeaf(int key){
    node* ptr = new node();
    ptr->key=key;
    ptr->left=NULL;
    ptr->right=NULL;
    return ptr;
}

void bst::addLeaf(int key){
    node* ptr = root;
    if(ptr!=NULL){
        ptr=createLeaf(key);
    }
    else if(key<ptr->key){
        if (ptr->left!=NULL){
            addLeaf(key);
        }
        else{
            ptr->left=createLeaf(key);
        }
    }
    else if(key>ptr->key){
        if(ptr->right!=NULL){
            addLeaf(key);
        }
        else{
            ptr->right=createLeaf(key);
        }
    }
    else{
        cout<<"Key has already added to the tree"<<endl;
    }
}

void bst::printInOrder(node* ptr){
    if (ptr!=NULL){
        if(ptr->left!=NULL)printInOrder(ptr->left);
        cout<<ptr->key<<" ";
        if(ptr->right!=NULL)printInOrder(ptr->right);
    }
    else{
        cout<<"Tree is empty"<<" ";
    }
}

node* bst::searchTree(int key, node* ptr){
    if(ptr->key==key){
        cout<<"Match found at the level "<< ptr << endl;
        return ptr;
    }
    else if(key<ptr->key){
        searchTree(key, ptr->left);
    }
    else if(key>ptr->key){
        searchTree(key, ptr->right);
    }
    else{
        cout<<"key not found in tree";
        return NULL;
    }
}

/*
RemoveNode(key, ptr)
    if root!=null
      if root->key==key
        RemoveRootMatch();
    else
      if key<ptr->key && ptr->left!=NULL
        ptr->left->key==key? RemoveMatch(ptr, ptr->left, true): RemoveNode(key, ptr->left);
      else if key>ptr->key && ptr->right!=NULL
        ptr->right->key==key? RemoveMatch(ptr, ptr->right, false): RemoveNode(key, ptr->right);
      else
        cout<<"key not found"
*/

RemoveRootMatch(){
    if root!=NULL {
        node* delPtr=root;
        int rootKey = root->key;
        int smllRightST;
        
        if(root->left==NULL && root->right==NULL){
            root=NULL;
            delete delPtr;
        }
        else if(root->left==NULL && root->right!=NULL){
            root=root->right;
            delPtr->right=NULL;
            delete delPtr;
        }
        else if(root->right==NULL && root->left!=NULL){
            root=root->left;
            delPtr->left=NULL;
            delete delPtr;
        }
        else {
            smllRightST = FindSmallRightSubTree(root->right);
            RemoveMatch(smllRightST, root);
            root->smllRightST;
        }
    }
}

RemoveMatch(int key, node* ptr){
    
}

int main()
{
	std::cout << "Hello from AWS Cloud9!" << std::endl;
}