from src import logger
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
#from src.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
#from src.pipeline.stage_03_training import ModelTrainingPipeline
#from src.pipeline.stage_04_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



#logger.info("Welcome to our custom logging")