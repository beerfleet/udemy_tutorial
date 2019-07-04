from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
    <ol>
      <li class="regular">This list item is regular.</li>
      <li class="special">But this one is special.</li>
    </ol>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
specials = soup.select(".special")

# print element name + attributes
for el in specials:
  print(el.name)
  print(el.attrs)

# css selectors => returns a list
d = soup.select("[data-example]")
e = soup.select("body div")

# element resultset
f = soup.find_all("li")
g = soup.find_all(class_='special')
h = soup.find_all(attrs={"data-example":"yes"})

print(type(h))
print(soup.find("h3")['data-example']) # print h3 data-example attribute
print(soup.find("div")['id']) # print div id attribute
print(soup.select("body > div > ol > li.regular")) # print selector
