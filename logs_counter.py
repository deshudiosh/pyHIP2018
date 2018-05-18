import datetime
import os
from time import sleep


def write_to_logtxt(url, success=0, fail=0):
    log = open("log.txt", "r")
    lines = log.readlines()
    log.close()

    add_new_line = True

    newlines = []

    for line in lines:
        line = line.strip("\n")
        found = line[:len(url)] == url

        if found:
            values = [int(val) for val in line.split(">")[1].split("/")]
            values = [values[0] + success, values[1] + fail]
            newline = url + " > " + str(values[0]) + " / " + str(values[1])
            newlines.append(newline)
            add_new_line = False
        else:
            newlines.append(line)

    if add_new_line:
        newline = url + " > " + str(success) + " / " + str(fail)
        newlines.append(newline)

    log = open("log.txt", "w")
    for line in newlines:
        log.write(line + "\n")
    log.close()


def count_logs_and_move_to_used():
    logs_dir = "./logs/"
    logs_used = "./logs_used/"

    files = os.listdir(logs_dir)

    for filename in files:
        file = open(logs_dir + filename)
        url = file.readline().strip("\n")
        success = file.readline().strip("\n") == "True"
        file.close()

        if success:
            write_to_logtxt(url, success=1)
        else:
            write_to_logtxt(url, fail=1)

        new_path = logs_used + os.path.basename(filename)
        os.rename(logs_dir + filename, new_path)

    return len(files)


while(True):
    interval = 5  # interval in seconds
    count = count_logs_and_move_to_used()
    t = datetime.datetime.now()
    # print(":".join([str(t.hour), str(t.minute), str(t.second)]), count, "logs counted!")
    print(t.strftime("%H:%M:%S"), count, "logs counted. Logs per sec:", count//interval)
    sleep(interval)

