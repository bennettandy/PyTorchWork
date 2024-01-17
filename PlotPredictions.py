import matplotlib.pyplot as plt # visualisation
import numpy as np

# Visualise
def plot_predictions(train_data,
                     train_labels,
                     test_data,
                     test_labels,
                     predictions=None):
    """
    Plots training data, test data and compares predictions
    """
    plt.figure(figsize=(10,7))
    
    # plot training data in blue
    plt.scatter(train_data, train_labels, c="b", s=4, label="Training data")
    
    # plot testing data in green
    plt.scatter(test_data, test_labels, c="g", s=4, label="Testing data")
    
    # Are there predictions?
    if predictions is not None:
        # plot predictions
        plt.scatter(test_data, predictions, c="r", s=4, label="Predictions")
    
    # Show legend
    plt.legend(prop={"size": 14})