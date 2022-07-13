# Rules

Any live cell with two or three live neighbours survives.
Any dead cell with three live neighbours becomes a live cell.
All other live cells die in the next generation. Similarly, all other dead cells stay dead.


# Example

* printed out is the state of the board
* edge pixels use mirrored values (first line's upper neighbors is last line, last column's right neighbor is first column)

```
Input                                Output
[[1, 1, 0, 1, 0, 0, 0, 0, 0],        [[1, 1, 0, 0, 1, 0, 1, 0, 0],  
 [0, 0, 1, 1, 1, 0, 0, 1, 1],         [0, 0, 0, 0, 0, 1, 0, 1, 0],  
 [1, 0, 1, 0, 1, 1, 0, 0, 1],         [0, 0, 0, 0, 0, 1, 1, 0, 0],  
 [0, 1, 0, 1, 0, 0, 1, 0, 1],         [0, 1, 1, 1, 0, 0, 0, 0, 0],  
 [0, 0, 0, 0, 0, 1, 1, 1, 1],         [0, 0, 0, 0, 0, 1, 0, 0, 0],  
 [1, 0, 0, 0, 0, 0, 0, 1, 1],         [0, 0, 0, 0, 0, 0, 0, 0, 0],  
 [1, 0, 0, 0, 0, 1, 1, 0, 1],         [0, 0, 0, 0, 0, 1, 0, 0, 0],  
 [0, 1, 1, 0, 0, 0, 1, 1, 1],         [0, 1, 1, 0, 0, 0, 0, 0, 0],  
 [0, 0, 1, 0, 0, 0, 1, 1, 1]]         [0, 0, 0, 1, 0, 0, 1, 0, 0]]  
                                                                    
``` 

## corresponding logs
 
``` 
Cell 0,0 (1) with 3 live neighbors survives
Cell 0,1 (1) with 3 live neighbors survives
Dead cell 0,4 (0) with 3 live neighbors revived
Dead cell 0,6 (0) with 3 live neighbors revived
Dead cell 1,5 (0) with 3 live neighbors revived
Cell 1,7 (1) with 2 live neighbors survives
Cell 2,5 (1) with 3 live neighbors survives
Dead cell 2,6 (0) with 3 live neighbors revived
Cell 3,1 (1) with 2 live neighbors survives
Dead cell 3,2 (0) with 3 live neighbors revived
Cell 3,3 (1) with 2 live neighbors survives
Cell 4,5 (1) with 2 live neighbors survives
Cell 6,5 (1) with 2 live neighbors survives
Cell 7,1 (1) with 3 live neighbors survives
Cell 7,2 (1) with 2 live neighbors survives
Dead cell 8,3 (0) with 3 live neighbors revived
Cell 8,6 (1) with 3 live neighbors survives
```