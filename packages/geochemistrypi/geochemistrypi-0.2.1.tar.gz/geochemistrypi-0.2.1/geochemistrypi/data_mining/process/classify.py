# -*- coding: utf-8 -*-
import pandas as pd
from multipledispatch import dispatch
from ..global_variable import DATASET_OUTPUT_PATH
from ..model.classification import ClassificationWorkflowBase, SVMClassification, DecisionTreeClassification,\
    RandomForestClassification, XgboostClassification, LogisticRegressionClassification, DNNClassification, ExtraTreesClassification
from ..data.data_readiness import num_input, float_input, str_input, limit_num_input
from ..global_variable import SECTION


class ClassificationModelSelection(object):
    """Simulate the normal way of training classification algorithms."""

    def __init__(self, model):
        self.model = model
        self.clf_workflow = ClassificationWorkflowBase()

    @dispatch(object, object, object, object, object, object)
    def activate(self, X: pd.DataFrame, y: pd.DataFrame, X_train: pd.DataFrame,
                 X_test: pd.DataFrame, y_train: pd.DataFrame, y_test: pd.DataFrame) -> None:
        """Train by Scikit-learn framework."""

        self.clf_workflow.data_upload(X=X, y=y, X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)

        # model option
        if self.model == "Support Vector Machine":
            hyper_parameters = SVMClassification.manual_hyper_parameters()
            if hyper_parameters["kernel"] == "linear":
                self.clf_workflow = SVMClassification(kernel=hyper_parameters["kernel"], C=hyper_parameters["C"], shrinking=hyper_parameters["shrinking"])
            elif hyper_parameters["kernel"] == "poly":
                self.clf_workflow = SVMClassification(kernel=hyper_parameters["kernel"], degree=hyper_parameters["degree"], gamma=hyper_parameters["gamma"], C=hyper_parameters["C"], shrinking=hyper_parameters["shrinking"])
            elif hyper_parameters["kernel"] == "rbf":
                self.clf_workflow = SVMClassification(kernel=hyper_parameters["kernel"], gamma=hyper_parameters["gamma"], C=hyper_parameters["C"], shrinking=hyper_parameters["shrinking"])
            elif hyper_parameters["kernel"] == "sigmoid":
                self.clf_workflow = SVMClassification(kernel=hyper_parameters["kernel"], gamma=hyper_parameters["gamma"], C=hyper_parameters["C"], shrinking=hyper_parameters["shrinking"])
        elif self.model == "Decision Tree":
            hyper_parameters = DecisionTreeClassification.manual_hyper_parameters()
            self.clf_workflow = DecisionTreeClassification(criterion=hyper_parameters['criterion'], max_depth=hyper_parameters['max_depth'], min_samples_split=hyper_parameters['min_samples_split'], min_samples_leaf=hyper_parameters['min_samples_leaf'], max_features=hyper_parameters['max_features'])
        elif self.model == "Random Forest":
            hyper_parameters = RandomForestClassification.manual_hyper_parameters()
            self.clf_workflow = RandomForestClassification(n_estimators=hyper_parameters['n_estimators'], max_depth=hyper_parameters['max_depth'], min_samples_split=hyper_parameters['min_samples_split'], min_samples_leaf=hyper_parameters['min_samples_leaf'], max_features=hyper_parameters['max_features'], bootstrap=hyper_parameters['bootstrap'], oob_score=hyper_parameters['oob_score'])
        elif self.model == "Xgboost":
            hyper_parameters = XgboostClassification.manual_hyper_parameters()
            self.clf_workflow = XgboostClassification(n_estimators=hyper_parameters['n_estimators'], learning_rate=hyper_parameters['learning_rate'], max_depth=hyper_parameters['max_depth'], subsample=hyper_parameters['subsample'], colsample_bytree=hyper_parameters['colsample_bytree'], alpha=hyper_parameters['alpha'], lambd=hyper_parameters['lambd'])
        elif self.model == "Logistic Regression":
            hyper_parameters = LogisticRegressionClassification.manual_hyper_parameters()
            self.clf_workflow = LogisticRegressionClassification(penalty=hyper_parameters['penalty'], C=hyper_parameters['C'], solver=hyper_parameters["solver"], max_iter=hyper_parameters['max_iter'], class_weight=hyper_parameters['class_weight'], l1_ratio=hyper_parameters['l1_ratio'])
        elif self.model == "Deep Neural Network":
            hyper_parameters = DNNClassification.manual_hyper_parameters()
            self.clf_workflow = DNNClassification(hidden_layer_sizes=hyper_parameters['hidden_layer_sizes'], activation=hyper_parameters['activation'], solver=hyper_parameters['solver'], alpha=hyper_parameters['alpha'], learning_rate=hyper_parameters['learning_rate'], max_iter=hyper_parameters['max_iter'])
        elif self.model == "Extra-Trees":
            hyper_parameters = ExtraTreesClassification.manual_hyper_parameters()
            self.clf_workflow = ExtraTreesClassification(n_estimators=hyper_parameters['n_estimators'], max_depth=hyper_parameters['max_depth'], min_samples_split=hyper_parameters['min_samples_split'], min_samples_leaf=hyper_parameters['min_samples_leaf'], max_features=hyper_parameters['max_features'], bootstrap=hyper_parameters['bootstrap'], oob_score=hyper_parameters['oob_score'])

        self.clf_workflow.show_info()

        # Use Scikit-learn style API to process input data
        self.clf_workflow.fit(X_train, y_train)
        y_test_predict = self.clf_workflow.predict(X_test)
        y_test_predict = self.clf_workflow.np2pd(y_test_predict, y_test.columns)
        self.clf_workflow.data_upload(X=X, y=y, X_train=X_train, X_test=X_test,
                                      y_train=y_train, y_test=y_test, y_test_predict=y_test_predict)

        # Common components for every classification algorithm
        self.clf_workflow.common_components()

        # Special components of different algorithms
        self.clf_workflow.special_components()

        # Save the prediction result
        self.clf_workflow.data_save(y_test_predict, "Y Test Predict", DATASET_OUTPUT_PATH, "Model Prediction")

        # Save the trained model
        self.clf_workflow.save_model()

    @dispatch(object, object, object, object, object, object, bool)
    def activate(self, X: pd.DataFrame, y: pd.DataFrame, X_train: pd.DataFrame, X_test: pd.DataFrame,
                 y_train: pd.DataFrame, y_test: pd.DataFrame, is_automl: bool) -> None:
        """Train by FLAML framework + RAY framework."""

        self.clf_workflow.data_upload(X=X, y=y, X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)

        # Model option
        if self.model == "Support Vector Machine":
            self.clf_workflow = SVMClassification()
        elif self.model == "Decision Tree":
            self.clf_workflow = DecisionTreeClassification()
        elif self.model == "Random Forest":
            self.clf_workflow = RandomForestClassification()
        elif self.model == "Xgboost":
            self.clf_workflow = XgboostClassification()
        elif self.model == "Logistic Regression":
            self.clf_workflow = LogisticRegressionClassification()
        elif self.model == "Deep Neural Network":
            self.clf_workflow = DNNClassification()
        elif self.model == "Extra-Trees":
            self.clf_workflow = ExtraTreesClassification()

        self.clf_workflow.show_info()

        # Use Scikit-learn style API to process input data
        self.clf_workflow.fit(X_train, y_train, is_automl)
        y_test_predict = self.clf_workflow.predict(X_test, is_automl)
        y_test_predict = self.clf_workflow.np2pd(y_test_predict, y_test.columns)
        self.clf_workflow.data_upload(X=X, y=y, X_train=X_train, X_test=X_test,
                                      y_train=y_train, y_test=y_test, y_test_predict=y_test_predict)

        # Common components for every classification algorithm
        self.clf_workflow.common_components(is_automl)

        # Special components of different algorithms
        self.clf_workflow.special_components(is_automl)

        # Save the prediction result
        self.clf_workflow.data_save(y_test_predict, "y test predict", DATASET_OUTPUT_PATH, "Model Prediction")

        # Save the trained model
        self.clf_workflow.save_model(is_automl)