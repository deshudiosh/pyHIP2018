from multiprocessing import cpu_count
from subprocess import Popen


def gogogo():
    processes = []
    for i in range(cpu_count()-1):
        processes.append(Popen("python %s" % "pyHIP2018.py", shell=True))

    for process in processes:
        process.wait()


gogogo()
