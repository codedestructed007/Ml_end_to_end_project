
from src.mlproject.pipeline.stage_01_data_ingestion import STAGE_NAME, DataIngestionTrainingPipeline
from src.mlproject import logger


try:
    logger.info(">>>>>Stage {} started".format(STAGE_NAME))
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(">>>> stage {} completed".format(STAGE_NAME))    
    
except Exception as e:    
    logger.exception(e)
    raise e