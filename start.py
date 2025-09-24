from bs4 import BeautifulSoup
import re

with open(r"FastAPI\templates\adddata.html", "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

# print(soup.prettify())

# print(soup.title)

# print(soup.title.name)

# print(soup.title.string)

# print(soup.p)

# print(soup.find_all('a'))

# for link in soup.find_all('a'):
#     print(link.get('href'))

# print(soup.form["class"])

# for tag in soup.find_all(True):
#     print(tag.name)

# print(soup.find_all("meta"))

# for form in soup.find_all('form'):
#     print(form.attrs.keys())

# print(soup.input)

# soup.input['placeholder'] = 'ammar'

# print(soup.input)

# for input in soup.find_all("input"):
#     print(input["class"])
#     print(input.get("id"))

# print(type(soup.a.string))

# print(soup.a)
# soup.a.string.replace_with("Ammar Dashboard")
# print(soup.a)

# print(len(soup.a.contents[0]))
# print(soup.a.contents[0])

# print(len("soup.children"))
# print(len("soup.descendants"))

# doc = BeautifulSoup("<document><content/>INSERT FOOTER HERE</document", "html.parser")
# footer = BeautifulSoup("<footer>Here's the footer</footer>", "html.parser")
# doc.find(string="INSERT FOOTER HERE").replace_with(footer)
# print(doc.prettify())

# soup = BeautifulSoup(html_content, 'html.parser')
# # print(soup.a.next_sibling.next_sibling.next_sibling.next_sibling)
# print(soup.a.next_element.next_element.next_element.next_element.next_element)

# print(soup.find_all(id=True))
# for script in soup.find_all("script"):
#     script.decompose()
# Str = soup.find_all(string=True)

# clean = [s.strip() for s in Str if s.strip() != ""]

# print(clean)
# print(soup.find(string=re.compile("Dashboard")).find_parents())

# print(soup.a.find_all_next(string=True))
# print(soup.form.find_all_next(string=True))

print(soup.css.select("html form"))
print(soup.css.select("form html"))