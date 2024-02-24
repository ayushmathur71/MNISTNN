**README File For Building Image Recognition Neural Network (MNIST DIGITS DATA)**
    
    *Image recognition neural network to identify digits from MNIST Dataset*
    
    There are 3 files for this project:
    
    1. **model.py** --> This file defines the neural network layers with a class called **NET**
        **Forward** function defines the actual implementation with activation function & returns the output with predicted labels.
    
    2. **utils.py** --> This file contains following function definitions:
        a. **GetCorrectPredCount** --> Compares the predicted & test datasets, Returns correctly predicted image count
        
        b. **Train** --> Intakes the training dataset from train loader ; predicts image labels & optimizes losses. Also changes gradient values with optimizer function (Stochastic Gradient Descend)
        c. **Test** --> Intakes test dataset ; Without initiating any gradeints (preventing leakage), predicts image class. Calculates loss & accuracy, updates correctly tagged image count and prints accuracy for each batch

    3. **S5.ipynb** --> Main file containing the overall implementation of the neural network. We call the defined training & test functions from this file & analyse the data as well as output of our network.
