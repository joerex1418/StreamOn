import typing
from enum import Enum

from .constants import BASE

class ContentKind(Enum):
    MOVIE = "movie"
    SHOW = "show"
    BOTH = "both"

class Availability(Enum):
    SOURCES = "onSources"
    ANY_SOURCE = "onAnySource"

class _Urls(typing.NamedTuple):
    SEARCH  = BASE + "/v3.0/content/search/typeahead"
    SHOW = BASE + "/v3.0/content/show"
    MOVIE = BASE + "/v3.0/content/movie"
    POPULAR_SHOWS = BASE + "/v3.0/content/browse/generated/popular-shows"
    POPULAR_MOVIES = BASE + "/v3.0/content/browse/generated/popular-movies"

class Service:
    ANY: str = "#any#"
    FREE: str = "#free#"
    PHILO: str = "philo"
    MOST_POPULAR: str = "amazon_prime,disney_plus,netflix,hulu_plus,hbo_max,peacock_free,apple_tv_plus,discovery_plus,directv,tubi_tv,crackle,plutotv,showtime,paramount_plus,starz,philo,fubo_tv"
    NETFLIX: str = "netflix"
    PEACOCK: str = "peacock"
    HBO_MAX: str = "hbo_max"
    APPLE_TV_PLUS: str = "apple_tv_plus"
    DISNEY_PLUS: str = "disney_plus"
    AMAZON_PRIME: str = "amazon_prime"
    HBO: str = "hbo"
    HULU_PLUS: str = "hulu_plus"
    PARAMOUNT_PLUS: str = "paramount_plus"
    FUBO_TV: str = "fubo_tv"
    TUBI_TV: str = "tubi_tv"
    PLUTO_TV: str = "plutotv"
    PLEX_FREE: str = "plex_free"
    VUDU_FREE: str = "vudu_free"
    CRACKLE: str = "crackle"
    IMDB_TV: str = "imdb_tv"
    PEACOCK_FREE: str = "peacock_free"
    BET_PLUS: str = "bet_plus"
    DIRECTV: str = "directv"
    KANOPY: str = "kanopy"
    FANDOR: str = "fandor"
    FX_TVEVERYWHERE: str = "fx_tveverywhere"
    EPIX: str = "epix"
    POPCORNFLIX: str = "popcornflix"
    STARZ: str = "starz"
    MUBI: str = "mubi"
    HOOPLA: str = "hoopla"
    SHUDDER: str = "shudder"
    CRITERION_CHANNEL: str = "criterion_channel"
    TBS: str = "tbs"
    TNT: str = "tnt"
    TRUTV_TVEVERYWHERE: str = "trutv_tveverywhere"
    TVISION: str = "tvision"
    AMC: str = "amc"
    HALLMARK_MOVIES_NOW: str = "hallmark_movies_now"
    SHOWTIME: str = "showtime"
    DISCOVERY_PLUS: str = "discovery_plus"
    NBC_TVEVERYWHERE: str = "nbc_tveverywhere"
    HALLMARK_EVERYWHERE: str = "hallmark_everywhere"
    CINEMAX: str = "cinemax"
    YOUTUBE_PREMIUM: str = "youtube_premium"
    LIFETIME_TVEVERYWHERE: str = "lifetime_tveverywhere"
    SYFY_TVEVERYWHERE: str = "syfy_tveverywhere"
    VH1_TVEVERYWHERE: str = "vh1_tveverywhere"
    NATGEO_TVEVERYWHERE: str = "natgeo_tveverywhere"
    CRUNCHYROLL_PREMIUM: str = "crunchyroll_premium"
    CRUNCHYROLL_FREE: str = "crunchyroll_free"
    BRITBOX: str = "britbox"
    WATCH_TCM: str = "watch_tcm"
    FUNIMATION: str = "funimation"
    CARTOON_NETWORK: str = "cartoon_network"
    COMEDYCENTRAL_TVEVERYWHERE: str = "comedycentral_tveverywhere"
    DISNEYNOW: str = "disneynow"
    AMC_PREMIERE: str = "amc_premiere"
    ABC_TVEVERYWHERE: str = "abc_tveverywhere"
    AE_TVEVERYWHERE: str = "ae_tveverywhere"
    ACORNTV: str = "acorntv"
    SUNDANCE_TVEVERYWHERE: str = "sundance_tveverywhere"
    BET_TVEVERYWHERE: str = "bet_tveverywhere"
    BBC_AMERICA_TVE: str = "bbc_america_tve"
    DC_UNIVERSE: str = "dc_universe"
    INDIEFLIX: str = "indieflix"
    IFC: str = "ifc"
    
    def __getitem__(self,k):
        return getattr(self,k)

Urls = _Urls()


