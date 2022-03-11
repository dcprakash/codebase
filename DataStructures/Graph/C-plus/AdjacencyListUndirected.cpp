#include <iostream>
#include <stdio.h>
#include <stdlib.h>

struct AdjNode {
    int dest;
    AdjNode* next;
};

struct AdjList {
    struct AdjNode* head;
};

struct Graph {
  int v;
  struct AdjList* array;
};

struct AdjNode* AddNewNode(int destination) {
    struct AdjNode* nNode = new AdjNode();
    nNode->dest = destination;
    nNode->next = NULL;
    return nNode;
};

struct Graph* CreateGraph(int v){
    Graph* graph = new Graph();
    graph->v = v;
    graph->array = new AdjList();
    
    for(int i=0;i<v;i++){
        graph->array[i].head=NULL;
    }
    return graph;
}

void AddEdge(struct Graph* g, int src, int desti){
    struct AdjNode* newNode = AddNewNode(desti);
    newNode->next = g->array[src].head;
    std::cout<<"g->array[src].head" << g->array[src].head << std::endl;
    g->array[src].head = newNode;
    
    newNode = AddNewNode(src);
    newNode->next = g->array[desti].head;
    g->array[desti].head = newNode;
}    


void printGraph(struct Graph* graph)
{
    int v;
    for (v = 0; v < graph->v; ++v)
    {
        struct AdjNode* pCrawl = graph->array[v].head;
        printf("\n Adjacency list of vertex %d\n head ", v);
        while (pCrawl)
        {
            printf("-> %d", pCrawl->dest);
            pCrawl = pCrawl->next;
        }
        printf("\n");
    }
}

int main()
{
    int v = 5;
    struct Graph* graph = CreateGraph(v);
    AddEdge(graph, 0, 1);
    printGraph(graph);
    
    AddEdge(graph, 0, 4);
    printGraph(graph);
    
    AddEdge(graph, 1, 2);
    printGraph(graph);
    
    AddEdge(graph, 1, 3);
    printGraph(graph);
    
    AddEdge(graph, 1, 4);
    printGraph(graph);
    
    AddEdge(graph, 2, 3);
    printGraph(graph);
    
    AddEdge(graph, 3, 4);
    printGraph(graph);
	std::cout << "Hello from AWS Cloud9!" << std::endl;
}