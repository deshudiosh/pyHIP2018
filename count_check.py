def get_success_num(url):
    file = open("log.txt")
    lines = file.readlines()
    file.close()

    for line in lines:
        found = line[:len(url)] == url

        if found:
            return int(line.split(">")[1].split("/")[0])

    return 0
