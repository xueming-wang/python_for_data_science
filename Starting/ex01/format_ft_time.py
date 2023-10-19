from datetime import datetime
import time

my_time = time.time()
current_date = datetime.now().date().strftime("%b %d %Y")
# ,4f:4 decimal places with comma separator, .2e:Exponent notation
print("Seconds since January 1, 1970: {:,.4f} or".format(my_time), "{:.2e}".format(my_time), "in scientific notation")
print(current_date)
