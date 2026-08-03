# Binary image classification using TensorFlow CNN

This project implements a Convolutional Neural Network (CNN) using TensorFLow/Keras for binary image classification. 
The dataset used for the project is made up of faces of happy and sad people, and was scraped from Google Images (using a browser extension) and consists of 100+ images across the two classes.

The repository also contains a simple script to use a Python script `collect_dataset.py` to collect a manual dataset using a Raspberry Pi Camera system.

## Evaluation metrics:
- `Accuracy : 0.8000`
- `Precision: 0.6667`
- `Recall   : 1.0000`

## Pipeline implemented
1. Dataset cleaning 
2. Data loading
3. Image preprocessing
4. Dataset splitting
5. CNN model construction
6. Model training
7. Performance evaluation
8. Prediction on unseen images
9. Saving the trained model

## Output
The model outputs a single probability between **0 and 1** using a sigmoid activation function.

- Values closer to **0** indicate the image is predicted as **Happy**.
- Values closer to **1** indicate the image is predicted as **Sad**.

## Tech used
- Python
- TensorFlow/Keras
- OpenCV
- NumPy
- Matplotlib
  
## Model architecture
<p align="left">
  <img src="https://github.com/user-attachments/assets/bd0379fa-472a-44cd-842c-6e2ca4015fd0" width="50%">
</p>

## Confusion matrix
<p align="left">
  <img src="https://github.com/user-attachments/assets/a526828a-25f5-43ed-a2ad-06e28ea175e3" width="50%">
</p>

## Loss chart
<p align="left">
  <img src="https://github.com/user-attachments/assets/47fbbe61-b452-4597-9363-9f2b20c0270c" width="50%">
</p>

## Accuracy chart
<p align="left">
  <img src="https://github.com/user-attachments/assets/379acbaf-d80b-4541-b4fb-35e895ae76ae" width="50%">
</p>


## Installation
```bash
git clone https://github.com/TricksterC/Image-classifier.git
cd image-classifier
pip install -r requirements.txt
``` 

## Usage
1. Clone the repository
2. Install dependencies
3. Open `main.ipynb`
4. Run all cells
5. The trained model is saved in `/models`
