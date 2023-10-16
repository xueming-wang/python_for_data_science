from datetime import datetime


epoch_time = datetime(1970, 1, 1)

delta = (datetime.now() - epoch_time).total_seconds()

scientific_notation = "{:.2e}".format(16700000)

current_date = datetime.now().date().strftime("%b %d %Y")

print("Seconds since January 1, 1970:", delta, "or", scientific_notation, "in scientific notation\n" ,current_date)
