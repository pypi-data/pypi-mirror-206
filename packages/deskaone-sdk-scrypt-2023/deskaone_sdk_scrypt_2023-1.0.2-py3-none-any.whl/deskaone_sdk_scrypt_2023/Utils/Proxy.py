from typing import Optional, Tuple
import requests, json, random, os
from requests.exceptions import ConnectionError, ConnectTimeout, SSLError, RequestException, HTTPError, ProxyError, Timeout, ReadTimeout, JSONDecodeError, TooManyRedirects, ChunkedEncodingError
from ..Typer import Typer, Color
from bs4 import BeautifulSoup

class WebShare:
    
    def __init__(self, Authorization: str) -> None:
        self.BASE_URL   = 'https://proxy.webshare.io/api/v2/'
        self.HEADERS    = dict(Authorization = Authorization)
        self.Session    = requests.Session()
    
    @property
    def __proxy__(self) -> list:
        URL     = self.BASE_URL + 'proxy/list/?mode=direct&page=1&page_size=100'
        return self.Session.get(URL, headers=self.HEADERS).json().get('results')
    
    def Main(self, New: bool) -> dict:
        if os.path.exists('MyProxy') is False:
            os.mkdir('MyProxy')
        if os.path.exists('MyProxy/__init__.json') is False or New is True:
            if os.path.exists('MyProxy/__init__.json') is True:Dict = dict(json.load(open('MyProxy/__init__.json')))
            else:Dict = dict()
            for Proxy in self.__proxy__:
                USERNAME        = Proxy.get('username')
                PASSWORD        = Proxy.get('password')
                IP              = Proxy.get('proxy_address')
                PORT            = Proxy.get('port')
                try:
                    Dict            = dict(**Dict, **{
                        f'{IP}:{PORT}'  : dict(
                        PROXY = dict(
                            http    = f'http://{USERNAME}:{PASSWORD}@{IP}:{PORT}',
                            https   = f'http://{USERNAME}:{PASSWORD}@{IP}:{PORT}',
                        ),
                        IpPort  = f'{IP}:{PORT}',
                    )})
                except TypeError:pass
            json.dump(Dict, open('MyProxy/__init__.json', 'w'))
        else:
            Dict = dict(json.load(open('MyProxy/__init__.json')))
        return Dict

class ProxyScrape:
    
    def __init__(self) -> None:
        self.Session    = requests.Session()
    
    def __proxy__(self, Dict: dict):
        URL     = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=5000&country=all&ssl=all&anonymity=all'
        Result  = self.Session.get(URL).text
        for Proxy in Result.replace(' ', '').replace('\r', '').split('\n'):
            try:
                Dict    = dict(**Dict, **{
                    f'{Proxy}'  : dict(
                    PROXY = dict(
                        http    = f'http://{Proxy}',
                        https   = f'http://{Proxy}',
                    ),
                    IpPort  = f'{Proxy}',
                )})
            except TypeError:pass
        
        URL     = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=5000&country=all&ssl=all&anonymity=all'
        Result  = self.Session.get(URL).text
        for Proxy in Result.replace(' ', '').replace('\r', '').split('\n'):
            try:
                Dict    = dict(**Dict, **{
                    f'{Proxy}'  : dict(
                    PROXY = dict(
                        http    = f'socks4://{Proxy}',
                        https   = f'socks4://{Proxy}',
                    ),
                    IpPort  = f'{Proxy}',
                )}) 
            except TypeError:pass
        
        URL     = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=5000&country=all&ssl=all&anonymity=all'
        Result  = self.Session.get(URL).text
        for Proxy in Result.replace(' ', '').replace('\r', '').split('\n'):
            try:
                Dict    = dict(**Dict, **{
                    f'{Proxy}'  : dict(
                    PROXY = dict(
                        http    = f'socks5://{Proxy}',
                        https   = f'socks5://{Proxy}',
                    ),
                    IpPort  = f'{Proxy}',
                )})
            except TypeError:pass
        return Dict
    
    def Main(self, New: bool) -> dict:
        if os.path.exists('MyProxy') is False:
            os.mkdir('MyProxy')
        if os.path.exists('MyProxy/__init__.json') is False or New is True:
            if os.path.exists('MyProxy/__init__.json') is True:
                Dict = self.__proxy__(dict(json.load(open('MyProxy/__init__.json'))))
            else:
                Dict = self.__proxy__(dict())
            json.dump(Dict, open('MyProxy/__init__.json', 'w'))
        else:
            Dict = dict(json.load(open('MyProxy/__init__.json')))
        return Dict
    
class Geonode:
    
    def __init__(self) -> None:
        self.Session    = requests.Session()
        self.BASE_URL   = 'https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc&speed=medium&protocols=http%2Chttps%2Csocks4%2Csocks5'
    
    def Main(self, New: bool) -> dict:
        if os.path.exists('MyProxy') is False:
            os.mkdir('MyProxy')
        if os.path.exists('MyProxy/__init__.json') is False or New is True:
            if os.path.exists('MyProxy/__init__.json') is True:
                Dict = self.__proxy__(dict(json.load(open('MyProxy/__init__.json'))))
            else:
                Dict = self.__proxy__(dict())
            json.dump(Dict, open('MyProxy/__init__.json', 'w'))
        else:
            Dict = dict(json.load(open('MyProxy/__init__.json')))
        return Dict
    
    def __proxy__(self, Dict: dict):
        Result  = self.Session.get(self.BASE_URL).json()
        data    = list(Result.get('data'))
        for List in data:
            IP      = List.get('ip')
            PORT    = List.get('port')
            SCHEMA  = List.get('protocols')[0]
            try:
                Dict    = dict(**Dict, **{
                    f'{IP}:{PORT}'  : dict(
                    PROXY = dict(
                        http    = f'{SCHEMA.lower()}://{IP}:{PORT}',
                        https   = f'{SCHEMA.lower()}://{IP}:{PORT}',
                    ),
                    IpPort  = f'{IP}:{PORT}',
                )})
            except TypeError:pass
        return Dict
    
class FreeProxyList:
    
    def __init__(self) -> None:
        self.Session    = requests.Session()
        self.BASE_URL   = 'https://free-proxy-list.net/'
    
    def __proxy__(self, Dict: dict):
        r  = self.Session.get(self.BASE_URL)
        Result = BeautifulSoup(r.content, 'html5lib')
        for row in Result.findAll('tbody')[0].findAll('tr'):
            SPLIT   = str(row).split('td>')
            IP      = SPLIT[1].split('</')[0]
            PORT    = SPLIT[3].split('</')[0]
            try:
                Dict    = dict(**Dict, **{
                    f'{IP}:{PORT}'  : dict(
                    PROXY = dict(
                        http    = f'http://{IP}:{PORT}',
                        https   = f'http://{IP}:{PORT}',
                    ),
                    IpPort  = f'{IP}:{PORT}',
                )})
            except TypeError:pass
        return Dict
    
    def Main(self, New: bool) -> dict:
        if os.path.exists('MyProxy') is False:
            os.mkdir('MyProxy')
        if os.path.exists('MyProxy/__init__.json') is False or New is True:
            if os.path.exists('MyProxy/__init__.json') is True:
                Dict = self.__proxy__(dict(json.load(open('MyProxy/__init__.json'))))
            else:
                Dict = self.__proxy__(dict())
            json.dump(Dict, open('MyProxy/__init__.json', 'w'))
        else:
            Dict = dict(json.load(open('MyProxy/__init__.json')))
        return Dict
    
class ProxyList:
    
    def __init__(self) -> None:
        self.Session    = requests.Session()
        
    def __http__(self, Dict: dict):
        r  = self.Session.get('https://www.proxy-list.download/HTTP')
        Result = BeautifulSoup(r.content, 'html5lib')
        for row in Result.findAll('tbody', attrs={'id': 'tabli'})[0].findAll('tr'):
            SPLIT   = str(row).split('td>')
            IP      = SPLIT[1].replace(' ', '').replace('\n', '').replace('\r', '').split('</')[0]
            PORT    = SPLIT[3].replace(' ', '').replace('\n', '').replace('\r', '').split('</')[0]
            try:
                Dict    = dict(**Dict, **{
                    f'{IP}:{PORT}'  : dict(
                    PROXY = dict(
                        http    = f'http://{IP}:{PORT}',
                        https   = f'http://{IP}:{PORT}',
                    ),
                    IpPort  = f'{IP}:{PORT}',
                )})
            except TypeError:pass
        return Dict
        
    def __https__(self, Dict: dict):
        r  = self.Session.get('https://www.proxy-list.download/HTTPS')
        Result = BeautifulSoup(r.content, 'html5lib')
        for row in Result.findAll('tbody', attrs={'id': 'tabli'})[0].findAll('tr'):
            SPLIT   = str(row).split('td>')
            IP      = SPLIT[1].replace(' ', '').replace('\n', '').replace('\r', '').split('</')[0]
            PORT    = SPLIT[3].replace(' ', '').replace('\n', '').replace('\r', '').split('</')[0]
            try:
                Dict    = dict(**Dict, **{
                    f'{IP}:{PORT}'  : dict(
                    PROXY = dict(
                        http    = f'http://{IP}:{PORT}',
                        https   = f'http://{IP}:{PORT}',
                    ),
                    IpPort  = f'{IP}:{PORT}',
                )})
            except TypeError:pass
        return Dict
        
    def __socks4__(self, Dict: dict):
        r  = self.Session.get('https://www.proxy-list.download/SOCKS4')
        Result = BeautifulSoup(r.content, 'html5lib')
        for row in Result.findAll('tbody', attrs={'id': 'tabli'})[0].findAll('tr'):
            SPLIT   = str(row).split('td>')
            IP      = SPLIT[1].replace(' ', '').replace('\n', '').replace('\r', '').split('</')[0]
            PORT    = SPLIT[3].replace(' ', '').replace('\n', '').replace('\r', '').split('</')[0]
            try:
                Dict    = dict(**Dict, **{
                    f'{IP}:{PORT}'  : dict(
                    PROXY = dict(
                        http    = f'socks4://{IP}:{PORT}',
                        https   = f'socks4://{IP}:{PORT}',
                    ),
                    IpPort  = f'{IP}:{PORT}',
                )})
            except TypeError:pass
        return Dict
        
    def __socks5__(self, Dict: dict):
        r  = self.Session.get('https://www.proxy-list.download/SOCKS5')
        Result = BeautifulSoup(r.content, 'html5lib')
        for row in Result.findAll('tbody', attrs={'id': 'tabli'})[0].findAll('tr'):
            SPLIT   = str(row).split('td>')
            IP      = SPLIT[1].replace(' ', '').replace('\n', '').replace('\r', '').split('</')[0]
            PORT    = SPLIT[3].replace(' ', '').replace('\n', '').replace('\r', '').split('</')[0]
            try:
                Dict    = dict(**Dict, **{
                    f'{IP}:{PORT}'  : dict(
                    PROXY = dict(
                        http    = f'socks5://{IP}:{PORT}',
                        https   = f'socks5://{IP}:{PORT}',
                    ),
                    IpPort  = f'{IP}:{PORT}',
                )})
            except TypeError:pass
        return Dict
    
    def __proxy__(self, Dict: dict):
        Dict = self.__http__(Dict)
        Dict = self.__https__(Dict)
        Dict = self.__socks4__(Dict)
        Dict = self.__socks5__(Dict)
        return Dict
    
    def Main(self, New: bool) -> dict:
        if os.path.exists('MyProxy') is False:
            os.mkdir('MyProxy')
        if os.path.exists('MyProxy/__init__.json') is False or New is True:
            if os.path.exists('MyProxy/__init__.json') is True:
                Dict = self.__proxy__(dict(json.load(open('MyProxy/__init__.json'))))
            else:
                Dict = self.__proxy__(dict())
            json.dump(Dict, open('MyProxy/__init__.json', 'w'))
        else:
            Dict = dict(json.load(open('MyProxy/__init__.json')))
        return Dict

class HideMy:
    
    def First(self):
        URL = 'https://hidemy.name/en/proxy-list/'
        r = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'})
        return BeautifulSoup(r.content, 'html5lib')

    def ParseTable(self, Dict: dict):
        SOUP = self.First()
        for row in SOUP.findAll('tbody')[0].findAll('tr'):
            #print(row.td.text)
            TD = str(row).split('td>')
            IP = TD[1].split('</')[0]
            PORT = TD[3].split('</')[0]
            TYPE = 'http' if TD[9].split('</')[0].lower() == 'https' else TD[9].split('</')[0].lower()
            try:
                Dict    = dict(**Dict, **{
                    f'{IP}:{PORT}'  : dict(
                        PROXY = dict(
                            http    = f'{TYPE}://{IP}:{PORT}',
                            https   = f'{TYPE}://{IP}:{PORT}',
                        ),
                        IpPort  = f'{IP}:{PORT}',
                    )})
            except:pass
        return Dict
    
    def NextPage(self, Dict: dict, SOUP: BeautifulSoup):
        for X in range(10):
            try:
                paginator   = SOUP.find('div', attrs = {'class':'pagination'})
                for page in paginator:
                    URL = 'https://hidemy.name/en/proxy-list/?' + page.find('li', attrs = {'class':'next_array'}).a['href'].split('?')[1]
                    r = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'})
                    SOUP = BeautifulSoup(r.content, 'html5lib')
                    Dict    = self.ParseTable(Dict)
            except:pass
        return Dict
    
    def Main(self, New: bool) -> dict:
        if os.path.exists('MyProxy') is False:
            os.mkdir('MyProxy')
        if os.path.exists('MyProxy/__init__.json') is False or New is True:
            if os.path.exists('MyProxy/__init__.json') is True:
                Dict = self.ParseTable(dict(json.load(open('MyProxy/__init__.json'))))
            else:
                Dict = self.ParseTable(dict())
            json.dump(Dict, open('MyProxy/__init__.json', 'w'))
        else:
            Dict = dict(json.load(open('MyProxy/__init__.json')))
        return Dict

class Proxy:
    
    def __init__(self, Authorization: Optional[str] = None, *args, **kwargs) -> None:
        self.__get__(Authorization, True, **kwargs)
    
    def __get__(self, Authorization: Optional[str] = None, New = True, *args, **kwargs):
        self.List   = list()
        if Authorization is not None:
            A1 = WebShare(Authorization).Main(New)
            for k, v in zip(A1.keys(), A1.values()):self.List.append(v)
        if kwargs.get('ProxyScrape') is True or kwargs.get('ProxyScrape') is None:
            A2  = ProxyScrape().Main(New)
            for k, v in zip(A2.keys(), A2.values()):self.List.append(v)
        if kwargs.get('Geonode') is True or kwargs.get('Geonode') is None:
            A3  = Geonode().Main(New)
            for k, v in zip(A3.keys(), A3.values()):self.List.append(v)
        if kwargs.get('FreeProxyList') is True or kwargs.get('FreeProxyList') is None:
            A4  = FreeProxyList().Main(New)
            for k, v in zip(A4.keys(), A4.values()):self.List.append(v)
        if kwargs.get('ProxyList') is True or kwargs.get('ProxyList') is None:
            A5  = ProxyList().Main(New)
            for k, v in zip(A5.keys(), A5.values()):self.List.append(v)
        if kwargs.get('HideMy') is True or kwargs.get('HideMy') is None:
            A6  = HideMy().Main(New)
            for k, v in zip(A6.keys(), A6.values()):self.List.append(v)
    
    def __check__(self):
        while True:
            try:
                PROXY   = self.List[random.randint(0, len(self.List) - 1)]
                API     = dict(requests.get("http://ip-api.com/json/%1s" % (PROXY.get('IpPort').split(":")[0])).json())
                Typer.Print(f'{Color.RED}=> {Color.WHITE}Check New Proxy {Color.GREEN}{PROXY.get("IpPort")} {Color.WHITE}Country {Color.GREEN}{API.get("country")}', Refresh=True) 
                MYIP    = dict(requests.get("https://kin4u.com/test").json())
                S1 = requests.Session()
                CHECK   = dict(S1.get("https://kin4u.com/test", proxies=PROXY.get('PROXY'), timeout=15).json())
                if MYIP.get('HTTP_X_FORWARDED_FOR') != CHECK.get('HTTP_X_FORWARDED_FOR'):
                    S1.close()
                    return dict(
                        PROXY   = PROXY.get('PROXY'),
                        DATA    = API,
                        IpPort  = PROXY.get('IpPort')
                    )
            except ProxyError as e:pass
            except ConnectTimeout as e:pass
            except ConnectionError as e:pass
            except ReadTimeout as e:pass
            except JSONDecodeError:pass
            except TooManyRedirects as e:pass
            except Exception as e:pass
    
    def Generate(self) -> Tuple[bool, dict]:
        if len(self.List) != 0:return True,  self.__check__()
        return False, dict()
                