# Flow of Image Classifier

## 1. Install dependencies

Use pip to install required libraries.

---

## 2. Clean up dirty files

Create a list of permissible file extensions (jpeg, png etc) and loop through each file in directory to identify and remove all files which do not match extension type.

Using `filetype` to identify file, solely based off of file name. Removal happens if file is unknown or does not match the file type from the list.

Also check if file is readable by OpenCV, if not ID as corrupted and delete the image as well.

---

## 3. Loading the data

The function:

```python
tf.keras.utils.image_dataset_from_directory()
```

a. recursively scans the directory for supported files, and returns a file count and divides them into classes.

b. it automatically creates and sorts into labels, based on the folder structure given to it. it assigns them as 0 or 1 (in-case of binary database).

c. it reads each image file and decodes it into numerical pixel data, dividing each image into 3 arrays (assuming RGB bands) and based on pixel intensity, maps the image into values ranging from 0 to 255.

d. it resizes the images to `255 x 255 x 3` (size in pixels and 3 bands), to make it consistent throughout the dataset.

e. it creates batches, so instead of giving the neural network each individual picture, it gives it in batches. In this case, batch size is `32`. So, the dataset actually contains batches of images, and not individual images.

We then create an iterator that helps in retrieving the batches as numpy arrays which can be looped through.

---

## 4. Normalization/Scaling of pixel values

```python
data = data.map(lambda x, y: (x/255, y))
```

a lambda function (one-line, short duration anonymous function) is used to divide the pixel values and get to the range of 0 to 1 (inclusive).

only `x` is divided as `y` is the class of the image.

---

## 5. Splitting of dataset

Once entire dataset is prepped and ready, it is divided for multiple functions.

* `70%` is used for training
* `20%` for validation
* `10%` for testing

`take()` and `skip()` are built-in functions that help in doing this relatively easily.

---

## 6. Building the model

Here we build the actual model.

`Sequential` is essentially all layers in one sequence, each layer receives the output of the previous layer. This is appropriate because we don't need branching or multiple inputs and outputs.

### Convolutional layer

First, we use a convolutional layer, which acts as a feature detector.

Input is:

```text
256 x 256 x 3
```

`16` is 16 different filters.

Characteristics such as edges, corners, color transitions, simple shapes and textures is what it picks up on.

Each filter acts a `3x3` window, which looks at local regions of the `256x256` image.

`1` is the stride.

The activation function used is `ReLU`, which is mathematically equivalent to:

$$
f(x) = \max(0, x)
$$

### Max pooling layer

A max pooling layer comes immediately after to reduce spatial size of the feature maps.

Keras uses a `2x2` window with stride of `2`.

It takes the maximum value from each region, which is essentially keeping the minimum data that is required to keep the feature while reducing the amount of computation.

This helps in building tolerance.

### Additional convolutional layers

The third layer, another convo layer, is made up of `32` instead of `16` filters.

This is used to combine the simple features learned by the first convo layer into more complex ones, say transitioning from edges and patterns to shape, texture and parts.

It is again followed by a pooling layer.

Another convo layer is followed, same idea.

### Flatten layer

Then there is a flatten layer.

It is used to convert the 3D feature map into a vector.

### Dense layers

Lastly we have two dense layers.

The first one is used to send the data from flatten into all the neurons. This layer combines all the features extracted by the CNN.

The final dense layer is the output.

It contains only one neuron because we have two classes.

This neuron's value can vary from `0` to `1`, which can be used to interpret the score.

We use a sigmoid function, which is used to make sure the value lies between `0` and `1`.

### Compile

We then use `compile()` and give instructions on how to run it.

The optimizer determines how the model's weights are changed using tuning.

The optimizer used is **Adam**, which essentially predicts, calculates error, figures out which weights to be adjusted, adjusts them, and tries again.

`BinaryCrossEntropy` is us telling the model how to measure error.

We are also asking Keras to report how many predictions were correct.

---

## 7. Training the model

First, we store the training information in logs.

We then use a callback, which is something Keras can automatically execute while training is happening.

The callback records things like:

* training loss
* validation loss
* training accuracy
* validation accuracy

primarily for monitoring reasons.

Then, `model.fit()` is used to train the model.

The dataset is shown `20` times (`epoch = one pass through the dataset`), the model's weights are adjusted to reduce its errors, and evaluate it on the validation data along the way.

This happens by Adam and by the concept of backpropagation.

While training, the callback also executes to record the metrics.

We then use plots and various graphs to see how accuracy and loss varies throughout each training run.

---

## 8. Evaluation, testing and saving

We print the precision, accuracy and recall obtained from the model testing.

Then, we pick random images and test our trained model.

In this case, since we have used one neuron, if the value is above `0.5`, it belongs to **"Sad"**, else it belongs to **"Happy"**.

We then save our model, like a version which can be imported and used later.
