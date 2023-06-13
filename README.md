# Project Description 
Website Link (https://bodyfatprediction.azurewebsites.net/)

This project aimed to develop a machine learning framework using algorithms like Random Forest, Decision Tree, XGBoost, Extra Trees, and KNN to predict obesity levels, bodyweight, and fat percentage. We employed hyperparameter optimization (HPO) algorithms such as Genetic Algorithm, Random Search, Grid Search, and Optuna to improve model accuracy. We implemented continuous integration and continuous deployment (CI/CD) to deploy a user-friendly web app using Python Flask. The app allows users to easily access body fat percentage predictions. Model performance was tracked using DVC and MLflow, while the app was hosted on Azure. In summary, our project provides an accessible framework for predicting body metrics using machine learning, with optimized models and a deployed web app for user convenience

# Important Steps

Step 1. Install all the libraries : 
```bash 
    pip install -r requirements.txt 
```
Step 2. Setup the git (for git and dvc (data version control)) :
```bash 
    git init
```

```bash 
    dvc init
```

Step 3. Mlflow server command (Must be runnig in background incase testing and deploying new model) 
```bash 
mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root ./artifacts \
    --host 0.0.0.0 -p 1234
```

Steps 4. Run this if changes are made to the model or the data
```bash 
    dvc repro
```

