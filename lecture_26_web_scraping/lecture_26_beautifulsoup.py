import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
# print(page.text)

res = soup.find_all("div", class_="card")
for item in res:
    # print(item, end="\n" * 3)
    title = item.find("h2", class_="title")
    print(title.text)
    company = item.find("h3", class_="company")
    print(company.text)
    locations = item.find("p", class_="location")
    print(locations.text.strip(), end="\n" * 2)

python_jobs = soup.find_all("h2", string="Python Programmer (Entry-Level)")
print(python_jobs)

python_jobs = soup.find_all("h2", string=lambda text: "python" in text.lower())
print(python_jobs)

python_jobs_elements = [el.parent.parent.parent for el in python_jobs]
print(python_jobs_elements)

for job in python_jobs_elements:
    links = job.find_all("a")
    for link in links:
        print(link.text.strip(), link["href"])

big_el = soup.find(id="ResultsContainer")
print(big_el.prettify())
