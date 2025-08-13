# Importing necessary libraries
from sklearn.model_selection import KFold, cross_val_score, GridSearchCV
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.tree import DecisionTreeClassifier

class Hyper():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def logistic_hyper_parameter(self):
        """
        This function performs hyperparameter tuning for logistic regression.
        
        Args:
          None (uses self.x and self.y)
          
        Returns:
          The best model after hyperparameter tuning
        """
        folds = KFold(n_splits=5, shuffle=True, random_state=4)
        
        # Specify params
        params = {"C": [0.01, 0.1, 1, 10, 100, 1000]}
        
        # Specifing score as roc-auc
        model_cv = GridSearchCV(estimator=LogisticRegression(),
                                param_grid=params,
                                scoring='roc_auc',
                                cv=folds,
                                verbose=1,
                                return_train_score=True)
        
        # Fit the model
        return model_cv.fit(self.x, self.y)
    
    def xgboost_hyper_parameter(self):
        """
        This function performs hyperparameter tuning for XGBoost.
        
        Args:
          None (uses self.x and self.y)
          
        Returns:
          The best model after hyperparameter tuning
        """
        folds = 3
        
        # Specify range of hyperparameters
        param_grid = {'learning_rate': [0.2, 0.6],
                      'subsample': [0.3, 0.6, 0.9]}
        
        # Specify model
        xgb_model = XGBClassifier(max_depth=2, n_estimators=200)
        
        # Set up GridSearchCV()
        model_cv = GridSearchCV(estimator=xgb_model,
                                param_grid=param_grid,
                                scoring='roc_auc',
                                cv=folds,
                                verbose=1,
                                return_train_score=True)
        
        # Fit the model
        return model_cv.fit(self.x, self.y)
    
    def decision_tree_parameter(self):
        """
        This function performs hyperparameter tuning for decision tree.
        
        Args:
          None (uses self.x and self.y)
          
        Returns:
          The best model after hyperparameter tuning
        """
        param_grid = {
            'max_depth': range(5, 15, 5),
            'min_samples_leaf': range(50, 150, 50),
            'min_samples_split': range(50, 150, 50),
        }
        
        # Instantiate the grid search model
        dtree = DecisionTreeClassifier()
        
        grid_search = GridSearchCV(estimator=dtree,
                                   param_grid=param_grid,
                                   scoring='roc_auc',
                                   cv=3,
                                   verbose=1)
        
        # Fit the grid search to the data
        return grid_search.fit(self.x, self.y)
