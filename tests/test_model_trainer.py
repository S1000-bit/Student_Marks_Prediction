from src.components.model_trainer import ModelTrainer
import numpy as np

def mock_test_train_samples():
    X_train = np.random.randint(0,100, size=(100,7))
    y_train = np.random.randint(0, 100, size=(100,))
    X_test = np.random.randint(0,100, size=(20,7))
    y_test = np.random.randint(0,100, size=(20,))
    
    return X_train,X_test,y_train,y_test

def test_model_trainer():
    X_train,X_test,y_train,y_test = mock_test_train_samples()
    train_arr = np.column_stack((X_train,y_train))
    test_arr = np.column_stack((X_test,y_test))
    
    trainer = ModelTrainer()
    score = trainer.initiate_model_trainer(train_arr,test_arr)
    
    assert isinstance(score,float)
    