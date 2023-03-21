import typing

from .constants import SERVICES

def _poster_url(_type,_id):
    return f"https://img.rgstatic.com/content/{_type}/{_id}/poster-500.jpg"

def _extract_show_data(__data:typing.Dict,/) -> typing.Dict:
    d = __data
    trailer = d.get("trailer",{})
    trailer_site = trailer.get("site")
    trailer_url = None
    if trailer_site == "youtube":
        key = trailer.get("key")
        if key:
            trailer_url = f"www.youtube.com/watch?v={key}"
    
    sources = []
    for src in d.get("sources",[]):
        sources.append([src,SERVICES.get(src,src)])
    
    cast_crew = []
    for person in d.get("people",[]):
        cast_crew.append({
            "id": person["id"],
            "slug": person["slug"],
            "name": person["name"],
            "role": person["role"],
            "rank": person["rank"],
            "birthdate": person["birthdate"],
            "poster": _poster_url("person",person["id"])
        })
    
    all_episode_data: typing.Dict = d.get("episodes",{})
    seasons = {}
    for season in d.get("seasons",[]):
        season_sources = []
        for season_src in season.get("availability",[]):
            season_sources.append([season_src,SERVICES.get(season_src,season_src)])
        
        episode_data = {}
        for episode_id in season.get("episodes",[]):
            _episode_data = all_episode_data.get(episode_id)
            episode_data[_episode_data["number"]] = {
                "id": _episode_data["id"],
                "title": _episode_data["title"],
                "overview": _episode_data["overview"],
                "sequence_number": _episode_data.get("sequence_number"),
                "air_date": _episode_data.get("aired_at"),
            }
        
        seasons[season["number"]] = {
            "id": season["id"],
            "number": season["number"],
            "sources": season_sources,
            "episode_count": len(season.get("episodes",[])),
            "episodes": episode_data,
        }
    
    data = {
        "id": d["id"],
        "slug": d["slug"],
        "title": d["title"],
        "trailer": trailer_url,
        "cast_crew": cast_crew,
        "imdb_rating": d["imdb_rating"],
        "rt_critics": d["rt_critics_rating"],
        "rt_audience": d["rt_audience_rating"],
        "sources": sources,
        "season": seasons,
        "season_count": d["season_count"],
        "released_on": d["released_on"],
        "completed_on": d["completed_on"],
        "returning_on": d["returning_on"],
        "coming_on": d["coming_on"],
        "poster": _poster_url("show",d["id"]),
    }
    return data

def _extract_movie_data(__data:typing.Dict,/) -> typing.Dict:
    d = __data
    trailer = d.get("trailer",{})
    trailer_site = trailer.get("site")
    trailer_url = None
    if trailer_site == "youtube":
        key = trailer.get("key")
        if key:
            trailer_url = f"www.youtube.com/watch?v={key}"
    
    sources = []
    for src in d.get("sources",[]):
        sources.append([src,SERVICES.get(src,src)])
    
    sources_details = {}
    for src in d.get("availability",[]):
        src_id = src.get("source_name")
        sources_details[src_id] = {
            "rental_sd": src.get("rental_cost_sd"),
            "rental_hd": src.get("rental_cost_hd"),
            "purchase_sd": src.get("purchase_cost_sd"),
            "purchase_hd": src.get("purchase_cost_hd"),
        }
    
    cast_crew = []
    for person in d.get("people",[]):
        cast_crew.append({
            "id": person["id"],
            "slug": person["slug"],
            "name": person["name"],
            "role": person["role"],
            "rank": person["rank"],
            "birthdate": person["birthdate"],
            "poster": _poster_url("person",person["id"])
        })
    

    data = {
        "id": d["id"],
        "slug": d["slug"],
        "title": d["title"],
        "runtime": d["runtime"],
        "trailer": trailer_url,
        "cast_crew": cast_crew,
        "imdb_rating": d["imdb_rating"],
        "rt_critics": d["rt_critics_rating"],
        "rt_audience": d["rt_audience_rating"],
        "sources": sources,
        "source_details": sources_details,
        "released_on": d["released_on"],
        "poster": _poster_url("movie",d["id"])
    }
    return data
    