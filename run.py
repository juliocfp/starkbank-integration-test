import logging
import thread
import report

with open("setup.py") as f:
    exec(f.read())

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
data=thread.start_thread()
report.generate_report(data)
