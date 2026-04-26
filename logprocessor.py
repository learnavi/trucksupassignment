from collections import Counter
import re
import matplotlib.pyplot as plt   #  enhancement by me  for graph

# Counters
total_logs            = 0
error_count           = 0
info_count            = 0
warning_count         = 0
booking_failure_count = 0
no_return_load_count  = 0

error_messages = Counter()

#  enhancements
failed_orders = set()        # store unique orderIds
route_count   = Counter()    # store route frequency

# Read the file
with open("log.txt", "r") as log_file:
    for line in log_file:

        # Count every line
        total_logs += 1

        # Check log
        if "ERROR" in line:
            error_count += 1

            message = line.split("ERROR")[1].strip()


            if "Booking failed" in message:
                message = "Booking failed due to driver unavailable"

            error_messages[message] += 1

        elif "INFO" in line:
            info_count += 1

        elif "WARNING" in line:
            warning_count += 1

        # Booking failures
        if "driver unavailable" in line:
            booking_failure_count += 1

            # NEW: extract orderId
            match = re.search(r'orderId=(\w+)', line)
            if match:
                failed_orders.add(match.group(1))

        # No return load
        if "No return load" in line:
            no_return_load_count += 1

        # NEW: extract route
        route_match = re.search(r'route ([A-Za-z\-]+)', line)
        if route_match:
            route = route_match.group(1)
            route_count[route] += 1


# - OUTPUT - 1

print("\n= LOG ANALYSIS REPORT =\n")

print("Total Logs:", total_logs)
print("ERROR:", error_count)
print("INFO:", info_count)
print("WARNING:", warning_count)

print("\nBooking Failures:", booking_failure_count)
print("No Return Load Cases:", no_return_load_count)

print("\nTop 3 ERROR messages:")
for msg, count in error_messages.most_common(3):
    print(f"{msg} -> {count}")

# OUTPUT 2
print("\nUnique Failed Order IDs:")
print(failed_orders)

print("\nTop Problematic Routes:")
for route, count in route_count.most_common(3):
    print(f"{route} -> {count}")
     # enhancement by me for graph

    labels = ['ERROR', 'INFO', 'WARNING']
    values = [error_count, info_count, warning_count]

    plt.bar(labels, values)
    plt.title("Log Level Distribution")
    plt.show()