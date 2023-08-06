from typing import Optional
import requests, json, random, os
from requests.exceptions import ConnectionError, ConnectTimeout, SSLError, RequestException, HTTPError, ProxyError, Timeout, ReadTimeout, JSONDecodeError, TooManyRedirects, ChunkedEncodingError
from deskaone_sdk import Typer, Color

class WebShare:
    
    def __init__(self, Authorization: str) -> None:
        self.BASE_URL   = 'https://proxy.webshare.io/api/v2/'
        self.HEADERS    = dict(Authorization = Authorization)
        self.Session    = requests.Session()
    
    @property
    def __proxy__(self) -> list:
        URL     = self.BASE_URL + 'proxy/list/?mode=direct&page=1&page_size=100'
        return self.Session.get(URL, headers=self.HEADERS).json().get('results')
    
    def __save__(self, New: bool) -> dict:
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

    
    def Random(self, TIMEOUT: int, NEW: bool, IP_OLD_SAME: Optional[str] = None):
        if os.path.exists('MyProxy/__init__.json') is True:os.unlink('MyProxy/__init__.json')
        Proxys = self.__save__(NEW)
        List = [v for k, v in zip(Proxys.keys(), Proxys.values())]
        if len(List) != 0:
            while True:
                PROXY   = List[random.randint(0, len(List) - 1)]
                if PROXY.get('IpPort') != IP_OLD_SAME or IP_OLD_SAME is None:
                    try:
                        API     = dict(requests.get("http://ip-api.com/json/%1s" % (PROXY.get('IpPort').split(":")[0])).json())
                        Typer.Print(f'{Color.RED}=> {Color.WHITE}Mencoba Koneksi Proxy {Color.GREEN}{PROXY.get("IpPort")} {Color.WHITE}Country {Color.GREEN}{API.get("country")}', Refresh=True) 
                        MYIP    = dict(requests.get("https://kin4u.com/test").json())
                        S1 = requests.Session()
                        CHECK   = dict(S1.get("https://kin4u.com/test", proxies=PROXY.get('PROXY'), timeout=TIMEOUT).json())
                        if MYIP.get('HTTP_X_FORWARDED_FOR') != CHECK.get('HTTP_X_FORWARDED_FOR'):
                            S1.close()
                            return dict(
                                PROXY   = PROXY.get('PROXY'),
                                DATA    = API
                            )
                    except ProxyError as e:pass
                    except ConnectTimeout as e:pass
                    except ConnectionError as e:pass
                    except ReadTimeout as e:pass
                    except JSONDecodeError:pass
                    except TooManyRedirects as e:pass
                    except Exception as e:pass
        return None

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
    
    def __save__(self, New: bool) -> dict:
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
        
    
    def Random(self, TIMEOUT: int, NEW: bool, IP_OLD_SAME: Optional[str] = None):
        if os.path.exists('MyProxy/__init__.json') is True:os.unlink('MyProxy/__init__.json')
        Proxys = self.__save__(NEW)
        List = [v for k, v in zip(Proxys.keys(), Proxys.values())]
        if len(List) != 0:
            while True:
                PROXY   = List[random.randint(0, len(List) - 1)]
                if PROXY.get('IpPort') != IP_OLD_SAME or IP_OLD_SAME is None:
                    try:
                        API     = dict(requests.get("http://ip-api.com/json/%1s" % (PROXY.get('IpPort').split(":")[0])).json())
                        Typer.Print(f'{Color.RED}=> {Color.WHITE}Mencoba Koneksi Proxy {Color.GREEN}{PROXY.get("IpPort")} {Color.WHITE}Country {Color.GREEN}{API.get("country")}', Refresh=True) 
                        MYIP    = dict(requests.get("https://kin4u.com/test").json())
                        S1 = requests.Session()
                        CHECK   = dict(S1.get("https://kin4u.com/test", proxies=PROXY.get('PROXY'), timeout=TIMEOUT).json())
                        if MYIP.get('HTTP_X_FORWARDED_FOR') != CHECK.get('HTTP_X_FORWARDED_FOR'):
                            S1.close()
                            return dict(
                                PROXY   = PROXY.get('PROXY'),
                                DATA    = API
                            )
                    except ProxyError as e:pass
                    except ConnectTimeout as e:pass
                    except ConnectionError as e:pass
                    except ReadTimeout as e:pass
                    except JSONDecodeError:pass
                    except TooManyRedirects as e:pass
                    except Exception as e:pass
        return None

class MyProxy:
    
    def __init__(self, TIMEOUT: int, NEW: bool, IP_OLD_SAME: Optional[str] = None, Authorization: Optional[str] = None) -> None:
        RANDOM, WebShares = random.randint(0, 1), False
        if RANDOM == 0:
            if Authorization is not None:
                Proxy = WebShare(Authorization=Authorization).Random(TIMEOUT, NEW, IP_OLD_SAME)
                if Proxy is None:WebShares = False
                else:self.Proxy, WebShares = Proxy, True
        if WebShares is False: self.Proxy = ProxyScrape().Random(TIMEOUT, NEW, IP_OLD_SAME)
    
    def __repr__(self) -> str:
        return json.dumps(self.Proxy, indent=4)
    
    
        
            