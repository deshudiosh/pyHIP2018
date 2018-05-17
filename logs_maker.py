import datetime
import os
import tempfile

from project import Project


def make_log_file(project: Project, success):
    dir = "./logs"
    if not os.path.exists(dir):
        os.makedirs(dir)
    file = tempfile.NamedTemporaryFile(dir=dir, delete=False, mode="w")
    file.write("\n".join([project.url, str(success), project.name]))
    file.close()

    t = datetime.datetime.now()
    print(" > ".join([":".join([str(t.hour), str(t.minute), str(t.second)]), project.name,
                      ("success" if success else "fail")]))


def success(project: Project):
    make_log_file(project, success=True)


def fail(project: Project):
    make_log_file(project, success=False)


