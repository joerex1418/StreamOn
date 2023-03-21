import typing
import datetime as dt

import rich
import httpx

from .utils import Urls
from .utils import Service
from .utils import ContentKind
from .utils import Availability
from .constants import BASE


def search(q:str,/,region:str="us",content_type:ContentKind=None):
    if isinstance(content_type,str):
        content_type = ContentKind(content_type.lower())
    
    if content_type:
        content_type = content_type.value.capitalize()
    
    with httpx.Client() as session:
        params = httpx.QueryParams({
            "terms": q,
            "region": region,
            "content_type": content_type
        })
        
        r = session.get(Urls.SEARCH,params=params)
        
        return r.json()

def content_search(q:str,/):
    url = BASE + "/v3.0/content/search/content"
    
    params = {
        "page": "1",
        "pageSize": "35",
        "region": "us",
        "take": "35",
        "terms": q
    }
    
    with httpx.Client() as session:
        r = session.get(url, params=params)
        return r.json()

def popular_movies(*,
                   region:str="us",
                   year_start:str=None,
                   year_end:str=None,
                   skip:int=None,
                   sort:int=None,
                   take:int=None
                   ):

    year_end = year_end or dt.date.today().year
    year_start = year_start or 1900

    params = {
        "availability": "onAnySource",
        # "content_kind": "movie",
        # "hide_seen": "false",
        # "hide_tracked": "false",
        # "hide_watchlisted": "false",
        # "imdb_end": "10",
        # "imdb_start": "0",
        "region": "us",
        "rg_end": "100",
        "rg_start": "0",
        "skip": "0",
        "sort": "0",
        "take": "35",
        "year_end": year_end,
        "year_start": year_start
    }
    
    with httpx.Client() as session:
        r = session.get(Urls.POPULAR_MOVIES, params=params)
        
        return r.json()

def browse(services:typing.Union[str,typing.List]=None,*,
                  content_kind:ContentKind=None,
                  free:bool=None,
                  region:str=None,
                  take:str=None,
                #   availability:str=None,
                  year_end:int=None,
                  year_start:int=None
                  ) -> typing.List[typing.Dict]:
    
    content_kind = content_kind or "both"
    if isinstance(content_kind,str):
        content_kind = ContentKind(content_kind.lower())
    
    services = services or Service.MOST_POPULAR
    if isinstance(services,list):
        services = ",".join(services)
    region = region or "us"
    take = take or 30
    year_end = year_end or dt.date.today().year
    year_start = year_start or 1900
    free = free or False
    
    url = BASE + f"/v3.0/content/browse/filtered"
    
    # url = BASE + f"/v3.0/content/browse/source/{service}"
    
    params = {
        "availability": "onSources",
        "content_kind": content_kind.value,
        "free": free,
        # "hide_seen": "false",
        # "hide_tracked": "false",
        # "hide_watchlisted": "false",
        # "imdb_end": "10",
        # "imdb_start": "0",
        # "override_user_sources": "true",
        # "overriding_free": "false",
        # "overriding_sources": "netflix",
        "region": "us",
        "rg_end": "100",
        "rg_start": "0",
        "skip": "0",
        "sort": "0",
        "sources": services,
        "take": take,
        "year_end": year_end,
        "year_start": year_start
    }
    
    with httpx.Client() as session:
        r = session.get(url,params=params)
        
        return r.json()
    
def movie(movie_id:str):
    url = Urls.MOVIE + f"/{movie_id}"
    
    with httpx.Client() as session:
        r = session.get(url)
        
        return r.json()

def show(show_id:str):
    url = Urls.SHOW + f"/{show_id}"
    
    with httpx.Client() as session:
        r = session.get(url)
        
        return r.json()
        
    