import datetime
import logging
from jinja2 import Environment, FileSystemLoader

status_list=[]
combined_list=[]

def percentage_success_counter(list):
    for item in list:
        status_list.append(item.status)

    counter=status_list.count('success')
    percentage=(counter/len(status_list))*100

    return percentage

def average_time(list):
    created_list=[]
    updated_list=[]

    for item in list:
        created_list.append(item.created)
        updated_list.append(item.updated)

    for created, updated in zip(created_list, updated_list):
        combined_list.append(updated-created)

    average=sum(combined_list, datetime.timedelta())/len(combined_list)

    return average

def generate_report(data):
    environment=Environment(loader=FileSystemLoader("templates/"))
    filename="report_pix_transfers.html"
    template=environment.get_template("template.html")

    context={
        "percentage_success_counter": data[0],
        "average_time": data[1]
    }
    
    with open(filename, mode="w", encoding="utf-8") as results:
        results.write(template.render(context))
        logging.info(f"Generating report {filename}")
