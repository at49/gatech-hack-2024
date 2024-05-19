"""Credit to Chat GPT 3.5 for generating the main logic for this file"""

import pandas as pd
import random


def sampleData1():

    # Sample data

    # Sample authors
    authors = [
        "John Doe",
        "Jane Smith",
        "Alice Johnson",
        "Michael Brown",
        "Emily Davis",
    ]

    # Generating sample data
    data = {
        "name": [],
        "affiliation": [],
        "interests": [],
        "description": [],
    }

    for author in authors:
        for i in range(5):
            data["name"].append(author)
            data["description"].append(f"{i} Sample paper by {author}")
            data["affiliation"].append("GaTech")
            data["interests"].append(["ML", "LLMs"])

    # Creating dataframe
    df = pd.DataFrame(data)

    # print(df)

    return df


# Reference: https://scholar.google.com/citations?hl=en&user=JicYPdAAAAAJ
def geoffSamplePapers():
    description1 = "We trained a large, deep convolutional neural network to classify the 1.3 million high-resolution images in the LSVRC-2010 ImageNet training set into the 1000 different classes. On the test data, we achieved top-1 and top-5 error rates of 39.7\% and 18.9\% which is considerably better than the previous state-of-the-art results. The neural network, which has 60 million parameters and 500,000 neurons, consists of five convolutional layers, some of which are followed by max-pooling layers, and two globally connected layers with a final 1000-way softmax. To make training faster, we used non-saturating neurons and a very efficient GPU implementation of convolutional nets. To reduce overfitting in the globally connected layers we employed a new regularization method that proved to be very effective."
    description2 = "Deep learning allows computational models that are composed of multiple processing layers to learn representations of data with multiple levels of abstraction. These methods have dramatically improved the state-of-the-art in speech recognition, visual object recognition, object detection and many other domains such as drug discovery and genomics. Deep learning discovers intricate structure in large data sets by using the backpropagation algorithm to indicate how a machine should change its internal parameters that are used to compute the representation in each layer from the representation in the previous layer. Deep convolutional nets have brought about breakthroughs in processing images, video, speech and audio, whereas recurrent nets have shone light on sequential data such as text and speech."
    description3 = "Deep neural nets with a large number of parameters are very powerful machine learning systems. However, overfitting is a serious problem in such networks. Large networks are also slow to use, making it difficult to deal with overfitting by combining the predictions of many different large neural nets at test time. Dropout is a technique for addressing this problem. The key idea is to randomly drop units (along with their connections) from the neural network during training. This prevents units from co-adapting too much. During training, dropout samples from an exponential number of different “thinned” networks. At test time, it is easy to approximate the effect of averaging the predictions of all these thinned networks by simply using a single unthinned network that has smaller weights. This significantly reduces overfitting and gives major improvements over other regularization methods. We show that dropout improves the performance of neural networks on supervised learning tasks in vision, speech recognition, document classification and computational biology, obtaining state-of-the-art results on many benchmark data sets."

    allDesc = f"{description1} \n {description2} \n {description3}"
    return allDesc, [description1, description2, description3]
