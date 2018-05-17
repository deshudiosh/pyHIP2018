from collections import namedtuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import count_check
import logs_maker

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--headless")


def loop(project):
    driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=chrome_options)
    driver.get(project.url)

    try:
        driver.find_element_by_class_name("confirmVote").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "voteComplete")))
        logs_maker.success(project)
    except:
        logs_maker.fail(project)

    driver.close()

    #TODO: count successes on file copy (so write acces wont fail in logs_counter)
    counted_successes = count_check.get_success_num(project["url"])
    print(counted_successes, "/", project["times_to_vote"])

    if counted_successes < project["times_to_vote"]:
        loop(project)
    else:
        print("Finished!")


Project = namedtuple("Project", "name url times_to_vote")

if __name__ == "__main__":
    # for project in vote_for_list.get_project_list():
    #     loop(project)

    riverchair = Project(name="River chair",
                         url="https://idhipawards.secure-platform.com/a/gallery/rounds/15/vote/15076",
                         times_to_vote=2500)

    loop(riverchair)
