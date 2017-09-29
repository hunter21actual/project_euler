#include <stdio.h>
#include <limits.h>
#define V 40

int minKey(int key[], bool mstSet[])
{
   int MIN = INT_MAX, min_index;

   for (int v = 0; v < V; v++)
     if (mstSet[v] == false && key[v] < MIN)
         MIN = key[v], min_index = v;

   return min_index;
}

int getMST(int parent[], int n, int graph[V][V])
{
   int updated_wt_sum = 0;
   for (int i = 1; i < V; i++){
        updated_wt_sum += graph[i][parent[i]];
   }
    return updated_wt_sum;
}

int primMST(int graph[V][V])
{
     int parent[V];
     int key[V];
     bool mstSet[V];

     for (int i = 0; i < V; i++)
        key[i] = INT_MAX, mstSet[i] = false;

     key[0] = 0;
     parent[0] = -1;

     for (int cnt = 0; cnt < V-1; cnt++){
        int u = minKey(key, mstSet);
        mstSet[u] = true;

        for (int v = 0; v < V; v++)
          if (graph[u][v] && mstSet[v] == false && graph[u][v] <  key[v])
             parent[v]  = u, key[v] = graph[u][v];
     }

     getMST(parent, V, graph);
}

int main()
{
    int graph[V][V] = {{0}};
    FILE* fp;
    fp = fopen("C:\\Users\\hp lap\\Desktop\\College\\pep_107 data.txt", "r");

    int x;
    for(int i = 0; i < 40; ++i){
        for(int j = 0; j < 40; ++j){
            fscanf(fp,"%d,", &x);
            graph[i][j] = x;
        }
    }

    fclose(fp);

    int total_wt = 0;
    for(int i = 0; i < 40; ++i){
        for(int j = 0; j < 40; ++j){
            total_wt += graph[i][j];
        }
    }
    total_wt = total_wt/2;

    int save = total_wt - primMST(graph);
    printf("%d", save);

    return 0;
}
