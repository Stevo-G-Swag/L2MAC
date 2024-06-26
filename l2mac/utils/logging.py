import logging
import multiprocessing


def generate_log_file_path(file, log_folder="logs", config={}):
    import time

    # file_name = os.path.basename(os.path.realpath(file)).split('.py')[0]
    from pathlib import Path

    Path(f"./{log_folder}").mkdir(parents=True, exist_ok=True)
    path_run_name = "{}".format(time.strftime("%Y%m%d-%H%M%S"))
    return f"{log_folder}/{path_run_name}_log.txt"


def create_logger_in_process(log_file_path):
    logger = multiprocessing.get_logger()
    if not logger.hasHandlers():
        formatter = logging.Formatter("%(processName)s| %(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s")
        stream_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(log_file_path)
        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
    return logger
