from src.components.data_ingestion import  DataIngestion

def test_data_ingestion_creates_file(tmp_path):
    obj = DataIngestion()
    obj.DataIngestionConfig.train_data_path = os.path.join('tmp_path', "train.csv")
    obj.DataIngestionConfig.test_data_path = os.path.join('tmp_path', "test.csv")
    obj.DataIngestionConfig.raw_data_path = os.path.join('tmp_path', "raw.csv")
    
    train_path,test_path = obj.initiate_data_ingestion()
    assert os.path.exists(train_path)
    assert os.path.exists(test_path)