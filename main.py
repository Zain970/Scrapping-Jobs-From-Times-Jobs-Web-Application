from bs4 import BeautifulSoup

with open("index.html", "r") as html_file:
    content = html_file.read()

    Soup = BeautifulSoup(content, "lxml")

    # Getting all the divs with the card class-name
    course_cards = Soup.find_all("div", class_="card")

    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split(" ")[-1]

        print("{} costs {}".format(course_name, course_price))

if __name__ == '__main__':
    pass
