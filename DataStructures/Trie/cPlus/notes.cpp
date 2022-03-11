class Trie {
    
    public class TrieNode {
        Dictionary<string, Trinode> child;
        bool eow;
        
        public TrieNode(){
            child = new Dictionary<>();
            eow=false;
            
        }
        
        TrieNode root = new TrieNode();
        
        public void insert(string word) {
            Trinode cur = root;
            
            for(int i=0;i<word.length();i++){
                char ch = word.charAt(i);
                TrieNode node = cur.child.TryGetValue(ch, out node)
                
                if node == null {
                    node = new TrieNode();
                    cur.child.Add(ch, node);
                }
                cur = node;
            }
            cur.eow=true;
        }
        
        public bool search(string word){
            TrieNode cur = root;
            for(int i=0;i<word.length();i++){
                char ch = word.charAt(i)
                TrieNode node = cur.child.TryGetValue(ch, out node)
                
                if node==NULL{
                    return false
                }
                cur=node
            }
            return cur.eow
        }
        
        public void del(string word){
            del(root, word, 0)
        }
        
        public bool del(TrieNode cur, string word, int ix){
            if ix==word.length(){
                if !cur.eow{ //don't delete as this is not eow=true, means there are children; and this was just substring. If we searched for "th", we dont want to delete this bcz this was only substring of "the"
                    return false
                }
                //https://www.geeksforgeeks.org/trie-insert-and-search/ delete word="a"
                cur.eow=false
                return cur.child.size==0 //returns false because "a" has child
            }
            
            char ch = word.charAt(ix);
            TrieNode node = cur.child.TryGetValue(ch, out node);
            if node==NULL
                return false
            bool shouldDelete = del(node, word, ix+1)
            
            if shouldDelete{
                cur.child.remove(ch); //if only "a" existed but not "answer"; we can delete
                return cur.child.size == 0; //if onlt "a" exist, this returns true
            }
            
            return false;
        }
    }
}