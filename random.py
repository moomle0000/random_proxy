from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random

ua = UserAgent()
proxies = [] # Will contain proxies [ip, port]

# Main function

# Retrieve latest proxies
proxies_req = Request('https://www.sslproxies.org/')
proxies_req.add_header('User-Agent', ua.random)
proxies_doc = urlopen(proxies_req).read().decode('utf8')

soup = BeautifulSoup(proxies_doc, 'html.parser')
proxies_table = soup.find(id='proxylisttable')

# Save proxies in the array
for row in proxies_table.tbody.find_all('tr'):
    proxies.append({
    'ip':   row.find_all('td')[0].string,
    'port': row.find_all('td')[1].string
    })

# Choose a random proxy
proxy_index = random.randint(0, len(proxies) - 1)
proxy = proxies[proxy_index]


PROXY = proxy['ip'] + ':' + proxy['port']
print(PROXY)
# Retrieve a random index proxy (we need the index to delete it if not working)

