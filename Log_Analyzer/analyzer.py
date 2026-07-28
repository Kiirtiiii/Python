def print_results(count, info_count, warning_count, error_count, error_logs):
    print ("INFO entries :", info_count)
    print ("WARNING entries :", warning_count)
    print ("ERROR entries :", error_count)
    print(f"Total Log Entries : {count}") 

    print ("\nError Logs:")
    if error_logs :
     for error in error_logs:
        print(error)
    else :
        print("No ERROR logs found.")


# creating a simple report
def save_report(count, info_count, warning_count, error_count, error_logs) :
 with open("report.txt", "w") as report: 
  report.write(f"Total Log Entries: {count}\n")
  report.write(f"INFO Entries: {info_count}\n")
  report.write(f"WARNING Entries: {warning_count}\n")
  report.write(f"Error Logs: {error_count}\n\n") # 2 \n means move down 2 lines (leave one blank)
# write the error logs
  for error in error_logs:
        report.write(error + "\n")


def analyze_logs():
# count every entry and storing it in a variable.
 count = 0
 info_count = 0
 warning_count = 0
 error_count = 0
# store error logs
 error_logs = []
# open the log files
 with open("logs/sample.log", "r") as file : 
    # read one line at a time
    for line in file :
        count += 1
        # checking for info
        if "INFO" in line : 
            info_count += 1
        # checking for warning 
        elif "WARNING" in line :
            warning_count += 1
        # checking for error
        elif "ERROR" in line :
            error_count += 1
            error_logs.append(line.strip())
    print_results(count, info_count, warning_count, error_count, error_logs)
    save_report(count, info_count, warning_count, error_count, error_logs)


analyze_logs()