# algo-visualiser

## How to run?
1. Set the ```pwd``` in the terminal as ```Edmond-Karp-Visualisation```.
2. Execute the command
  ```zsh
  python3 Edmond_Karp.py
  ```
3. If zero capacity edges with non-zero flow be shown in the visualisation, Enter ```n```. Otherwise all zero capacity edges will be hidden.
4. Use "Next" and "Prev" buttons to move through the generated images, to understand the algorithm.

The generated graph images will be stored in ```imgs``` folder. Also, ```imgs/flow/flowGraph{n}.png``` will be the flow graph image of the $n^{th}$ step. And, ```imgs/resi/residualGraph{n}.png``` will be the residual graph image of the $n^{th}$ step.

To change the input graph (for running Edmond-Karp algorithm), edit the adjacency matrix C in the file Edmond_Karp.py. ```C[[i][j]]``` is the capacity of edge from i to j.
