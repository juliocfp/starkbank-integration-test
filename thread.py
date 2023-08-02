import logging
import time
import request
import report

def start_thread():
    logging.info(f"Starting thread.")
    logging.info(f"It will take 24 hours to complete.")
    for i in range(8):
        for _ in range(10):
            request.do_transfer()
            time.sleep(1)
        time.sleep(2*60*60)
        logging.info(f"Collecting data {i+1}/8...")
        percentage_success_counter=report.percentage_success_counter(request.do_search())
        average_time=report.average_time(request.do_search())
        logging.info(f"Done!")
        time.sleep(1*60*60)
    
    logging.info(f"Ending thread.")
    
    return [percentage_success_counter, average_time]
