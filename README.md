# algo-visualiser

## Packages to be installed beforehand
1. Anaconda environment is preferred.
2. After [setting up Anaconda](https://docs.anaconda.com/anaconda/install/), run the following commands in order to install the required packages
   
   ```conda install graphviz```
   
   ```conda install pydot```
   
   ```conda install -c conda-forge tk``` (optional, required if not using web version)
   
   ```conda install pillow```
   
   ```sudo apt install php``` (optional, required if using web version)

### Note
If graphviz is not properly installed, try 

   ```sudo apt-get install graphviz```

## How to run?
<details>
   <summary>Hosting Dinic's Algorithm locally</summary>
   
1. Set the working directory in the terminal as ```Dinic's Visualisation/Web-support```.
2. Execute the command
   ```zsh
   php -S localhost:4000
   ```
3. Minimise the terminal, and visit http://localhost:4000/upload.php in your browser.
</details>
<details>
   <summary>Edmond's</summary>
   
1. Set the working directory in the terminal as ```Edmond-Karp-Visualisation```.
2. Execute the command
  ```zsh
  python3 start.py
  ```
3. Click on ```Choose input graph``` or press the Enter key and choose the text file having valid input in space-separated adjacency matrix format. Verify whether the label shows the path to the selected file.
4. Default valid index values of source and sink vertices will be automatically filled in the textbox. If it is to be modified, write two modified space-separated integers. 
5. Click on ```Proceed``` or press the Enter key on your keyboard.
6. Wait for algorithm to work in background. On completion, a new window will open.
7. Use "Next" and "Prev" buttons to move through the generated images. Right/Left arrow keys on keyboard is also supported.

The generated graph images will be stored in ```imgs``` folder. Also, for any integer $n$, ```imgs/flow/flowGraph{n}.png``` will be the flow graph image of the $n^{th}$ step. And, ```imgs/resi/residualGraph{n}.png``` will be the residual graph image of the $n^{th}$ step.

The input file should be adjacency matrix with entry at  i, j position is ```C[i][j]``` representing the capacity of the edge from i to j.
Nine sample inputs are given in the same folder.
</details>
<details>
   <summary>Dinic's</summary>
   
1. Set the working directory in the terminal as ```Dinic's Visualisation```.
2. Execute the command
  ```zsh
  python3 start.py
  ```
3. Click on ```Choose input graph``` or press the Enter key and choose the text file having valid input in space-separated adjacency matrix format. Verify whether the label shows the path to the selected file.
4. Default valid index values of source and sink vertices will be automatically filled in the textbox. If it is to be modified, write two modified space-separated integers. 
5. Click on ```Proceed``` or press the Enter key on your keyboard.
6. Wait for algorithm to work in background. On completion, a new window will open.
7. Use "Next" and "Prev" buttons to move through the generated images. Right/Left arrow keys on keyboard is also supported.

The generated graph images will be stored in ```imgs``` folder. Also, for any integer $n$, ```imgs/flow/{n}.png``` will be the flow graph image of the $n^{th}$ step. And, ```imgs/level/{n}.png``` will be the level graph image of the $n^{th}$ step.

The input file should be adjacency matrix with entry at  i, j position is ```C[i][j]``` representing the capacity of the edge from i to j.
Nine sample inputs are given in the same folder.
</details>
