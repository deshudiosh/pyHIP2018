from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import count_check
import logs_maker
from project import Project

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--headless")


def loop(project: Project):
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
    counted_successes = count_check.get_success_num(project.url)
    print(counted_successes, "/", project.times_to_vote)

    if counted_successes < project.times_to_vote:
        loop(project)
    else:
        print("Finished!")


# if __name__ == "__main__":
#     tapa1 = Project("Tapa", "https://idhipawards.secure-platform.com/a/gallery/rounds/15/vote/16489", 2500)
#     riverchair2 = Project("River chair 2 ", "https://idhipawards.secure-platform.com/a/gallery/rounds/15/vote/16482", 1800)
#     riverchair3 = Project("River chair 3 ", "https://idhipawards.secure-platform.com/a/gallery/rounds/15/vote/15076", 2500)
#     riverchair4 = Project("River chair 4", "https://idhipawards.secure-platform.com/a/gallery/rounds/15/vote/16448", 1600)
#
    # loop(tapa1)
