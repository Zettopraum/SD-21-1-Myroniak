import logging
import time

def logger_function():
    logging.basicConfig(filename='files.logs', filemode='w', level=logging.INFO)
    logger = logging.getLogger()
    start_time = time.time()
    while True:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        elapsed_time = round(time.time() - start_time, 2)
        logger.info(f"Program has been running for {elapsed_time} seconds. Current time: {current_time}")
        time.sleep(5)
        if elapsed_time >= 60:
            break
    logger.error("Task completed")