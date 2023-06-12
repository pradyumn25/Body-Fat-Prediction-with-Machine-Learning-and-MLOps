This project aimed to develop a machine learning framework using algorithms like Random Forest, Decision Tree, XGBoost, Extra Trees, and KNN to predict obesity levels, bodyweight, and fat percentage. We employed hyperparameter optimization (HPO) algorithms such as Genetic Algorithm, Random Search, Grid Search, and Optuna to improve model accuracy. We implemented continuous integration and continuous deployment (CI/CD) to deploy a user-friendly web app using Python Flask. The app allows users to easily access body fat percentage predictions. Model performance was tracked using DVC and MLflow, while the app was hosted on Azure. In summary, our project provides an accessible framework for predicting body metrics using machine learning, with optimized models and a deployed web app for user convenience.


1. create the environment and activated the environment => "conda create -n new_main python=3.11.3 -y"
2. created the requirements.txt
3. installed the requirements "pip install -r requirements.txt"
4. Mlflow server command 

mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root ./artifacts \
    --host 0.0.0.0 -p 1234

