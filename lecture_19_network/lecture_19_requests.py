import requests

params = {"param": "KhAI"}
r = requests.get("https://httpbin.org/get", params=params)
print(type(r))
print(r)
print(r.status_code)

if r:
    print("Success!")
else:
    print("Failed!")

print(r.text)
print(r.headers)
print(r.cookies)
print(r.url)
print(r.content)
print(r.encoding)
print(r.headers['Content-Type'])


def google_search(title, num):
    res = requests.get("https://www.google.com/search",
                       params={"q": title, "num": num})
    return res.url


print(google_search("python", 1))

r = requests.get("https://httpbin.org/image/jpeg")
print(r.content)

with open("image.jpeg", "wb") as file:
    file.write(r.content)
