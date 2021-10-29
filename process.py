log_file = open("um-server-01.txt")


def sales_reports(log_file):
    # loop used to iterate through log_files
    for line in log_file:
        # changes the status of line.rstrip()
        line = line.rstrip()
        # changes the status of day
        day = line[0:3]
        # calling to get all info with Monday
        if day == "Mon":
            print(line)


sales_reports(log_file)
