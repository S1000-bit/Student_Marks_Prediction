from src.components.data_transformation import DataTransformation
import numpy as np

def test_data_transformmation():
    
    obj = DataTransformation()
    train_path = "artifact/train.csv"
    test_path = "artifact/test.csv"
    
    train_data,test_data,_ = obj.initiate_data_transformation(train_path,test_path)
    
    assert isinstance(train_data,np.ndarray)
    assert isinstance(test_data,np.ndarray)
    assert train_data.shape[1] == train_data.shape[1]