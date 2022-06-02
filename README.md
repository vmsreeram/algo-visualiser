# algo-visualiser

## How to run?
1. Set the ```pwd``` in the terminal as ```Edmond-Karp-Visualisation```.
2. Execute the command
  ```zsh
  python3 start.py
  ```
3. Click on ```Browse``` and choose the text file having valid input in space-separated adjacency matrix format. Verify whether the label shows the path to the selected file.
4. If zero capacity edges with non-zero flow is to be shown in the visualisation, uncheck the checkbox.
5. Default valid index values of source and sink vertices will be automatically filled in the textbox. If it is to be modified, write two modified space-separated integers. 
6. Wait for algorithm to work in background. On completion, a new window will open.
7. Use "Next" and "Prev" buttons to move through the generated images.

The generated graph images will be stored in ```imgs``` folder. Also, for any integer $n$, ```imgs/flow/flowGraph{n}.png``` will be the flow graph image of the $n^{th}$ step. And, ```imgs/resi/residualGraph{n}.png``` will be the residual graph image of the $n^{th}$ step.

To change the input graph, edit the adjacency matrix in the file ```input.txt```. ```C[i][j]``` is the capacity of edge from i to j.
