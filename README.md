## sudoku_solver
#### This project solves sudoku problems by just using its image 



## Technology Used 
 #### * Tensorflow 
 #### * Opencv 
 #### * Python  
 #### * Numpy 



## Working 
 #### First we will use Opencv to Detect the corner points of Sudoku Box from its Image 
 #### Then we will Transform its prespective using opencv so that further processing becomes easier
 #### Next we will filter the image to remove noise and get the contours of numbers from image
 #### These contours will be then converted into numbers using out tensorflow model trained on Mnist-digits data and some custom genarated images 
 #### Next the unsolved_sudoko will be solved using backtraking and projected on the original image



## Images 
 ### image no 1
 
 #### initial
 <img src = "output/raw1.jpeg" width = 400px style = "padding:20px;"></img>
 #### processed
 <img src = "output/processed1.jpeg" width = 400px style = "padding:20px;"></img>
 #### output 
 <img src = "output/output1.jpeg" width = 400px style = "padding:20px;"></img>
 
 ### image no 2
 
 #### initial
 <img src = "output/raw2.jpeg" width = 400px style = "padding:20px;"></img>
 #### processed
 <img src = "output/processed2.jpeg" width = 400px style = "padding:20px;"></img>
 #### output 
 <img src = "output/output2.jpeg" width = 400px style = "padding:20px;"></img>
