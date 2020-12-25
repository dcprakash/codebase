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
        void addLeaf(int key, node* ptr);
        void printInOrder(node* ptr);
}

bst::bst(){
    root=NULL;
}

node* bst::createLeaf(int kye){
    node* n = new node();
    n->key=key;
    n->left=NULL;
    n->right=NULL;
    return n;
}

void bst::addLeaf(int key, node* root){
    if root==NULL
        root=createLeaf(key)
    
    else if key<root->key {
        if root->left!=NULL{
            addLeaf(key, root->left)
        }
        else{
            root->left=createLeaf(key)
        }
    }
    
    else if key>root->key {
        if root->right!==NULL {
            addLeaf(key, root->right)
        }
        else {
            root->right=createLeaf(key)
        }
    }
    
    else
        cout<<"key has been already added"
}

//https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
//4,2,5,1,3
//1,2,4,5,3
//4,5,2,3,1
//1,2,3,4,5
void bst::printInOrder(node* ptr){
    if ptr!=NULL{
        if ptr->left!=NULL{
            printInOrder(ptr->left)
        }
        std::cout << ptr->key << std::endl;
        else if ptr->right!=NULL{
            printInOrder(ptr->right)
        }
    }
    else{
        std::cout << "Tree is empty" << std::endl;
    }
}

void bst::printPreOrder(node* ptr){
    if ptr!=NULL{
        std::cout << ptr->key << std::endl;
        if ptr->left!=NULL{
            printPreOrder(ptr->left)
        }
        else if ptr->right!=NULL{
            printPreOrder(ptr->right)
        }
    }
    else{
        std::cout << "Tree is empty" << std::endl;
    }
}

void bst::printPostOrder(node* ptr){
    if ptr!=NULL{
        if ptr->left!=NULL{
            printPostOrder(ptr->left)
        }
        else if ptr->right!=NULL{
            printPostOrder(ptr->right)
        }
        std::cout << ptr->key << std::endl;
    }
    else{
        std::cout << "Tree is empty" << std::endl;
    }
}

void bst::levelOrder(node* ptr){
    if ptr!=NULL{
        queue<Node *> q;
        q.push(ptr);
        while !q.empty(){
            node* cur = q.front();
            std::cout << cur->key << std::endl;
            if cur->left!=NULL{
                q.push(cur->left)
            }
            if cur->right!=NULL{
                q.push(cur->right)
            }
            q.pop()
        }
    }
    else{
        std::cout << "Tree is empty" << std::endl;
    }
}

node* bst::searchTree(int key, node* ptr){
    if ptr!=NULL{
        if key==ptr->key{
            return ptr
        }
        else if key<ptr->key{
            return searchTree(key, ptr->left)
        }
        else{
            return searchTree(key, ptr->right)
        }
    }
    else{
        return NULL;
    }
}

void bst::printChildren(int key){
    node* ptr = searchTree(key, root)
    if ptr!=NULL{
        std::cout << ptr->key << std::endl;
    }
    if ptr->left!=NULL{
        std::cout << ptr->left->key << std::endl;
    }
    if ptr->right!=NULL{
        std::cout << ptr->right << std::endl;
    }
}

void bst::removeNode(int key, node* root){
    if root!=NULL{
        if root->key==key{
            RemoveRootMatch();
        }
        else{
            if key<root->key && root->left!=NULL{
                root->left->key==key ? 
                    RemoveNodeMatch(key, root->left, true)
                    : removeNode(key, root->left)
                    
            }
            else if key>root->key && root->right!=NULL{
                root->right->key==key ?
                    RemoveNodeMatch(key, root->right, false)
                    : removeNode(key, root->right)
            }
        }
    }
    else{
        std::cout << "Tree is empty" << std::endl;
    }
}

int smllRightST(node* root){
    if root!=NULL{
        if root->left!=NULL{
            smllRightST(root->left)
        }
        else{
            return root->key
        }
    }
}

void bst::RemoveRootMatch(){
    if root!=NULL{
        node* delPtr = root;
        int rootKey = root->key;
        int smllRightST;
        
        if root->left==NULL && root->right==NULL {
            root = NULL
            delete delPtr
        }
        else if root->left==NULL && root->right!=NULL {
            root=root->right
            delPtr->right=NULL
            delete delPtr
        }
        else if root->left!=NULL && root->right==NULL {
            root=root->left
            delPtr->left=NULL
            delete delPtr
        }
        else {
            smllRightST = findSmallRST(root->right)
            RemoveNode(smllRightST, root)
            root->key=smllRightST;
        }
    }
    else{
        std::cout << "Tree is empty" << std::endl;
    }
}

void removeMatch(node* parent, node* match, bool left){
    node* delPtr = match;
    mkey=match->key;
    int smllRightST;
    
    if match->left==NULL && match-->right==NULL{
        left==true ? parent->left=NULL : parent->right=NULL
        delete delPtr
    }
    
    else if match->left==NULL && match->right!=NULL{
        left==true ? parent->left=match->right : parent->right=match->right
        delete delPtr
    }
    
    else if match->left!=NULL && match->right==NULL{
        left==true ? parent->left=match->left : parent->right = match->left
        delete delPtr
    }
    
    else{
        smllRightST = findSmallRST(match->right)
        removeNode(smllRightST, match)
        match->key=smllRightST;
    }
}