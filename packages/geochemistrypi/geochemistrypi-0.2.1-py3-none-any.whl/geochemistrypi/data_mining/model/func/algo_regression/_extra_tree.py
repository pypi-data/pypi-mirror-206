# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict
from ....data.data_readiness import float_input, num_input, str_input
from ....global_variable import SECTION


def extra_trees_manual_hyper_parameters() -> Dict:
    """Manually set hyperparameters.

    Returns
    -------
    hyper_parameters : dict
    """
    print("N Estimators: The number of trees in the forest.")
    print("Please specify the number of trees in the forest. A good starting range could be between 50 and 500, such as 100.")
    print("For small datasets, a range of 50 to 200 trees may be sufficient, while for larger datasets, a range of 200 to 500 trees may be appropriate.")
    n_estimators = num_input(SECTION[2], "@N Estimators: ")
    print("Max Depth: The maximum depth of a tree. Increasing this value will make the model more complex and more likely to overfit.")
    print("Please specify the maximum depth of a tree. A good starting range could be between 5 and 10, such as 4.")
    max_depth = num_input(SECTION[2], "@Max Depth: ")
    print("Min Samples Split: The minimum number of samples required to split an internal node.")
    print("Please specify the minimum number of samples required to split an internal node. A good starting range could be between 2 and 10, such as 2.")
    min_samples_split = num_input(SECTION[2], "@Min Samples Split: ")
    print("Min Samples Leaf: The minimum number of samples required to be at a leaf node.")
    print("Please specify the minimum number of samples required to be at a leaf node. A good starting range could be between 1 and 10, such as 1.")
    min_samples_leaf = num_input(SECTION[2], "@Min Samples Leaf: ")
    print("Max Features: The number of features to consider when looking for the best split.")
    print("Please specify the number of features to consider when looking for the best split. A good starting range could be between 1 and the total number of features in the dataset.")
    print("It's recommended to start with a value of sqrt(n_features) or log2(n_features). Make sure to use integer values.")
    max_features = num_input(SECTION[2], "@Max Features: ")
    print("Bootstrap: Whether bootstrap samples are used when building trees. Bootstrapping is a technique where a random subset of the data is sampled with replacement to create a new dataset of the same size as the original. This new dataset is then used to construct a decision tree in the ensemble. If False, the whole dataset is used to build each tree.")
    print("Please specify whether bootstrap samples are used when building trees. It is generally recommended to leave it set to True.")
    bootstraps = ["True", "Flase"]
    bootstrap = bool(str_input(bootstraps, SECTION[2]))
    print("oob_score: Whether to use out-of-bag samples to estimate the generalization accuracy. When the oob_score hyperparameter is set to True, Extra Trees will use a random subset of the data to train each decision tree in the ensemble, and the remaining data that was not used for training (the out-of-bag samples) will be used to calculate the OOB score. ")
    print("Please specify whether to use out-of-bag samples to estimate the generalization accuracy. It is generally recommended to leave it set to True.")
    oob_scores = ["True", "Flase"]
    oob_score = bool(str_input(oob_scores, SECTION[2]))
    hyper_parameters = {"n_estimators": n_estimators, "max_depth": max_depth, "min_samples_split": min_samples_split, "min_samples_leaf": min_samples_leaf, "max_features": max_features, "bootstrap": bootstrap, "oob_score": oob_score}
    return hyper_parameters


def feature_importances(X_train: pd.DataFrame, trained_model: object, image_config: dict) -> None:
    """Draw the feature importance bar diagram.

    Parameters
    ----------
    X_train : pd.DataFrame (n_samples, n_components)
        The training feature data.

    trained_model : sklearn algorithm model
        The sklearn algorithm model trained with X_train data.
    """
    # create drawing canvas
    fig, ax = plt.subplots(figsize=(image_config['width'], image_config['height']), dpi=image_config['dpi'])

    # draw the main content
    importances_values = trained_model.feature_importances_
    importances = pd.DataFrame(importances_values, columns=["importance"])
    feature_data = pd.DataFrame(X_train.columns, columns=["feature"])
    importance = pd.concat([feature_data, importances], axis=1)
    importance = importance.sort_values(["importance"], ascending=True)
    importance["importance"] = (importance["importance"]).astype(float)
    importance = importance.sort_values(["importance"])
    importance.set_index('feature', inplace=True)
    importance.plot.barh(alpha=image_config['alpha2'], rot=0)

    # automatically optimize picture layout structure
    fig.tight_layout()
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    x_adjustment = (xmax - xmin) * 0.01
    y_adjustment = (ymax - ymin) * 0.01
    ax.axis([xmin - x_adjustment, xmax + x_adjustment, ymin - y_adjustment, ymax + y_adjustment])

    # convert the font of the axes
    x1_label = ax.get_xticklabels()  # adjust the axis label font
    [x1_label_temp.set_fontname(image_config['axislabelfont']) for x1_label_temp in x1_label]
    y1_label = ax.get_yticklabels()
    [y1_label_temp.set_fontname(image_config['axislabelfont']) for y1_label_temp in y1_label]

    ax.set_title(label=image_config['title_label'],
                 fontdict={"size": image_config['title_size'], "color": image_config['title_color'],
                           "family": image_config['title_font']}, loc=image_config['title_location'],
                 pad=image_config['title_pad'])


