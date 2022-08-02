import asyncio

#This class is needed to establish a connection with the target website and handle HTTP requests
from http.client import HTTPConnection

#This class will help to parse target URLs
from urllib.parse import urlparse

import aiohttp

def site_is_online(url, timeout=2):
    """
    Return True if the target URL is online. 
    Otherwise, raise an exception.
    """
    error = Exception("Unknown Error")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout = timeout)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception as e:
            error = e
        finally:
            connection.close()
    raise error

async def site_is_online_async(url, timeout=2):
    """
    Return True if the target URL is online.
    Raise an exception otherwise.
    """
    error = Exception("unknown error")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for scheme in ("http", "https"):
        target_url = scheme + "://" + host
        async with aiohttp.ClientSession() as session:
            try:
                await session.head(target_url, timeout=timeout)
                return True
            except asyncio.exceptions.TimeoutError:
                error = Exception("timed out")
            except Exception as e:
                error = e
    raise error