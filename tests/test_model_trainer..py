from src.components.model_trainer import ModelTrainer
import numpy as np

def mock_test_train_samples():
    X_train = np.random.rand(100, 5)
    y_train = np.random.randint(0, 2, size=(100,))
    X_test = np.random.rand(20, 5)
    y_test = np.random.randint(0, 2, size=(20,))
    
    return X_train_X_test,y_train,y_test

def test_model_trainer():
    X_train_X_test,y_train,y_test = mock_test_train_samples()
    train_arr = np.column.stack((X_train,y_train))
    test_arr = np.column.stack((X_test,y_test))
    
    trainer = ModelTrainer()
    score = trainer.initiate_model_trainer(train_arr,test_arr)
    
    assert isinstance(score,float)
    