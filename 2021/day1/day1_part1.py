import requests

sample_data = map(int, """
199
200
208
210
200
207
240
269
260
263
""".strip().split("\n"))


headers = {
    'cookie': '_ga=GA1.2.648359719.1638387579; _gid=GA1.2.1442344881.1638387579; session=53616c7465645f5f633f6407b041e04200a5218c6b15131c81e15c83e805325e22b436ec4d4b735352e7c4c4c096ee3f',
}
res = requests.get("https://adventofcode.com/2021/day/1/input", headers=headers)
data = map(int, res.text.strip().split("\n"))
val = None
count = 0
for line in data:
    i = int(line)
    if val is None:
        val = i
        continue

    if i > val:
        count += 1
    
    val = i

print(count)
