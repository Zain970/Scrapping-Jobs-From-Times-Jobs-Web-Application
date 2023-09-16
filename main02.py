import requests
from bs4 import BeautifulSoup
import time


def find_jobs():
    print("Put some skill that you are not familiar with : ")
    unfimiliar_skill = input("> ")
    print(f"Filtering out {unfimiliar_skill} ... ")

    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
    html_text = requests.get(url)
    Soup = BeautifulSoup(html_text.text, "lxml")

    Jobs = Soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    for index, job in enumerate(Jobs):
        # When the job was posted
        published_date = job.find("span", class_="sim-posted").span.text

        if "few" in published_date:
            # Name of the company
            company_name = job.find("h3", class_="joblist-comp-name").text.strip()

            # Position for which job is open
            position = job.find("h2").find("a").text

            # Skills for the job
            skills = job.find("span", class_="srp-skills").text.replace(" ", "").replace(" ", "")

            # Link for applying
            apply_link = job.find("header").find("h2").a["href"]

            if unfimiliar_skill not in skills:
                with open(f"posts/{index}.txt", "w") as f:
                    # print(f"Company Name : {company_name.strip()}")
                    # print(f"Required Skills : {skills.strip()}")
                    # print(f"Apply link : {apply_link} ")
                    #

                    f.write(f"Company Name : {company_name.strip()} \n")
                    f.write(f"Required Skills : {skills.strip()} \n ")
                    f.write(f"Apply link : {apply_link} \n ")

                print("File saved : ", index)


if __name__ == "__main__":
    while True:
        # Running the function to extract the jobs
        find_jobs()

        # Wait time to fetch data after 10 minutes
        time_wait = 10

        print("Waiting ", time_wait, " minutes ... ")

        # Waiting for 10 minutes
        time.sleep(time_wait * 60)
