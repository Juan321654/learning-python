from os import name
from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
  contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
  print(tag.get("href"))
# https://www.appbrewery.co/
# https://angelabauer.github.io/cv/hobbies.html
# https://angelabauer.github.io/cv/contact-me.html

heading = soup.find(name="h1", id="name")
print(heading) # <h1 id="name">Angela Yu</h1>

section_heading = soup.find(name="h3", class_="heading")
print(section_heading) # <h3 class="heading">Books and Teaching</h3>

company_url = soup.select_one(selector="p a") # same as css selection >  p a {color: red}
print(company_url) # <a href="https://www.appbrewery.co/">The App Brewery</a>

name = soup.select_one(selector="#name")
print(name) # <h1 id="name">Angela Yu</h1>

heading_class = soup.select_one(selector=".heading")
print(heading_class) # <h3 class="heading">Books and Teaching</h3>