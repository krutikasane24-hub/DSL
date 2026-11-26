#include <iostream>
using namespace std;

class Graph
{
    int adj[20][20];
    int vertices;

public:

    Graph(int v)
    {
        vertices = v;

        for (int i = 0; i < vertices; i++)
        {
            for (int j = 0; j < vertices; j++)
            {
                adj[i][j] = 0;
            }
        }
    }

    void addEdge(int u, int v)
    {
        adj[u][v] = 1;
        adj[v][u] = 1;
    }

    void display()
    {
        cout << "\nAdjacency Matrix:\n";

        for (int i = 0; i < vertices; i++)
        {
            for (int j = 0; j < vertices; j++)
            {
                cout << adj[i][j] << " ";
            }

            cout << endl;
        }
    }

    void DFS(int vertex, bool visited[])
    {
        cout << vertex << " ";

        visited[vertex] = true;

        for (int i = 0; i < vertices; i++)
        {
            if (adj[vertex][i] == 1 && !visited[i])
            {
                DFS(i, visited);
            }
        }
    }
};

int main()
{
    int vertices, edges;
    int u, v, start;

    cout << "Enter number of vertices: ";
    cin >> vertices;

    Graph g(vertices);

    cout << "Enter number of edges: ";
    cin >> edges;

    cout << "Enter edges:\n";

    for (int i = 0; i < edges; i++)
    {
        cin >> u >> v;
        g.addEdge(u, v);
    }

    g.display();

    bool visited[20] = {false};

    cout << "\nEnter starting vertex: ";
    cin >> start;

    cout << "DFS Traversal: ";
    g.DFS(start, visited);

    return 0;
}