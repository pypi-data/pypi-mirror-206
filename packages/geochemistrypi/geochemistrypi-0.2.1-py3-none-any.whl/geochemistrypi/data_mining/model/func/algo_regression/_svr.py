# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from typing import Optional, List, Dict
from ....data.data_readiness import float_input, num_input, str_input
from ....global_variable import SECTION


def svr_manual_hyper_parameters() -> Dict:
    """Manually set hyperparameters.

    Returns
    -------
    hyper_parameters : dict
    """
    print("Kernel: This hyperparameter specifies the kernel function to be used for mapping the input data to a higher-dimensional feature space.")
    print("Please specify the kernel type to be used in the algorithm. It is generally recommended to leave it set to Radial basis function (RBF) kernel.")
    kernels = ['linear', 'poly', 'rbf', 'sigmoid']
    kernel = str_input(kernels, SECTION[2])
    degree = None
    if kernel == "poly":
        print("Degree: This hyperparameter is only used when the kernel is set to polynomial. It specifies the degree of the polynomial kernel function.")
        print("Please specify the degree of the polynomial kernel function. A good starting range could be between 2 and 5, such as 3.")
        degree = num_input(SECTION[2], "@Degree: ")
    gamma = None
    if kernel in ["poly", "rbf", "sigmoid"]:
        print("Gamma: This hyperparameter is only used when the kernel is set to Polynomial, RBF, or Sigmoid. It specifies the kernel coefficient for rbf, poly and sigmoid.")
        print("Please specify the kernel coefficient for rbf, poly and sigmoid. A good starting range could be between 0.0001 and 10, such as 0.1.")
        gamma = float_input(0.1, SECTION[2], "@Gamma: ")
    # coef0 = None
    # if kernel in ["poly", "sigmoid"]:
    #     print("Coef0: This hyperparameter is only used when the kernel is set to Polynomial or Sigmoid. It specifies the independent term in kernel function.")
    #     print("The coef0 parameter controls the influence of higher-order terms in the polynomial and sigmoid kernels, and it can help to adjust the balance between the linear and nonlinear parts of the decision boundary.")
    #     print("Please specify the independent term in kernel function. A good starting range could be between 0.0 and 1.0, such as 0.0.")
    #     coef0 = float_input(SECTION[2], "@Coef0: ")
    print("C: This hyperparameter specifies the penalty parameter C of the error term.")
    print("The C parameter controls the trade off between smooth decision boundary and classifying the training points correctly.")
    print("Please specify the penalty parameter C of the error term. A good starting range could be between 0.001 and 1000, such as 1.0.")
    C = float_input(1, SECTION[2], "@C: ")
    print("Shrinking: This hyperparameter specifies whether to use the shrinking heuristic.")
    print("The shrinking heuristic is a technique that speeds up the training process by only considering the support vectors in the decision function.")
    print("Please specify whether to use the shrinking heuristic. It is generally recommended to leave it set to True.")
    shrinkings = ["True", "False"]
    shrinking = bool(str_input(shrinkings, SECTION[2]))
    hyper_parameters = {"kernel": kernel, "C": C, "shrinking": shrinking}
    if degree:
        # Use the default value provided by sklearn.svm.SVR
        hyper_parameters["degree"] = 3
    if gamma:
        # Use the default value provided by sklearn.svm.SVR
        hyper_parameters["gamma"] = 'scale'
    # if coef0:
    #     # Use the default value provided by sklearn.svm.SVR
    #     hyper_parameters["coef0"] = 0.0
    return hyper_parameters


def plot_2d_decision_boundary(X: pd.DataFrame, X_test: pd.DataFrame, y_test: pd.DataFrame, trained_model: object,
                              image_config: dict, algorithm_name: str, contour_data: Optional[List[np.ndarray]] = None,
                              labels: Optional[np.ndarray] = None) -> None:
    """Plot the decision boundary of the trained model with the testing data set below.

    Parameters
    ----------
    X : pd.DataFrame (n_samples, n_components)
        The complete feature data.

    X_test : pd.DataFrame (n_samples, n_components)
        The testing feature data.

    y_test : pd.DataFrame (n_samples, n_components)
        The testing target values.

    trained_model : sklearn algorithm model
        The sklearn algorithm model trained with X_train data.

    algorithm_name : str
        The name of the algorithm model.
    """

    # Prepare the data for contour plot

    x0s = np.arange(X.iloc[:, 0].min(), X.iloc[:, 0].max(), (X.iloc[:, 0].max()-X.iloc[:, 0].min())/50)
    x1s = np.arange(X.iloc[:, 1].min(), X.iloc[:, 1].max(), (X.iloc[:, 1].max()-X.iloc[:, 1].min())/50)
    x0, x1 = np.meshgrid(x0s, x1s)
    input_array = np.c_[x0.ravel(), x1.ravel()]
    labels = trained_model.predict(input_array).reshape(x0.shape)

    # Use the code below when the dimensions of X are greater than 2

    # create drawing canvas
    fig, ax = plt.subplots(figsize=(image_config['width'], image_config['height']),dpi=image_config['dpi'])
    ax.patch.set_facecolor('cornsilk')

    # draw the main content
    ax.contourf(x0, x1, labels, cmap=image_config['cmap2'], alpha=image_config['alpha1'])
    ax.scatter(X_test.iloc[:, 0], X_test.iloc[:, 1],  alpha=image_config['alpha2'],
               marker=image_config['marker_angle'], cmap=image_config['cmap'])
    # automatically optimize picture layout structure
    fig.tight_layout()
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    x_adjustment = (xmax - xmin) * 0.01
    y_adjustment = (ymax - ymin) * 0.01
    ax.axis([xmin - x_adjustment, xmax + x_adjustment, ymin - y_adjustment, ymax + y_adjustment])

    # convert the font of the axes
    ax.set_xlabel(X.columns[0])
    ax.set_ylabel(X.columns[1])
    plt.tick_params(labelsize=image_config['labelsize'])  # adjust the font size of the axis label
    # plt.setp(ax.get_xticklabels(), rotation=image_config['xrotation'], ha=image_config['xha'],
    #          rotation_mode="anchor")  # axis label rotation Angle
    # plt.setp(ax.get_yticklabels(), rotation=image_config['rot'], ha=image_config['yha'],
    #          rotation_mode="anchor")  # axis label rotation Angle
    x1_label = ax.get_xticklabels()  # adjust the axis label font
    [x1_label_temp.set_fontname(image_config['axislabelfont']) for x1_label_temp in x1_label]
    y1_label = ax.get_yticklabels()
    [y1_label_temp.set_fontname(image_config['axislabelfont']) for y1_label_temp in y1_label]

    ax.set_title(label=image_config['title_label'],
                 fontdict={"size": image_config['title_size'], "color": image_config['title_color'],
                           "family": image_config['title_font']}, loc=image_config['title_location'],
                 pad=image_config['title_pad'])
