{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d3ee6b67",
   "metadata": {},
   "source": [
    "**README File For Building First Neural Network**\n",
    "\n",
    "*Image recognition neural network to identify digits from MNIST Dataset*\n",
    "\n",
    "There are 3 files for this project:\n",
    "\n",
    "1. **model.py** --> This file defines the neural network layers with a class called **NET** \n",
    "    **Forward** function defines the actual implementation with activation function & returns the output with predicted labels.\n",
    "    \n",
    "    \n",
    "    \n",
    "2. **utils.py** --> This file contains following function definitions:\n",
    "    a. **GetCorrectPredCount** --> Compares the predicted & test datasets, Returns correctly predicted image count\n",
    "    \n",
    "    b. **Train** --> Intakes the training dataset from train loader ; predicts image labels & optimizes losses. Also changes gradient values with optimizer function (Stochastic Gradient Descend)\n",
    "                 \n",
    "    c. **Test** --> Intakes test dataset ; Without initiating any gradeints (preventing leakage), predicts image class. Calculates loss & accuracy, updates correctly tagged image count and prints accuracy for each batch"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5d2e3350",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
