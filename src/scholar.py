import pandas as pd
import json

from config import google_api_key, google_profiles_engine, google_author_engine
from serpapi import GoogleSearch

# general pattern for author param:
# mauthors=label%3Amachine_learning
# mauthors=label%3Anlp&hl=en


def get_search_keyword(keyword):
    if " " in keyword:
        keyword = keyword.replace(" ", "_")
    return "label:" + keyword


def set_search_params(search_type, search_term=None, author_id=None, citation_id=None):
    # google_search_label = "label:machine_learning"
    # set params for API call
    if search_type == "profile":
        params = {
            "engine": google_profiles_engine,
            "mauthors": search_term,
            "api_key": google_api_key,
        }
    elif search_type == "pubs":
        params = {
            "engine": google_author_engine,
            "author_id": author_id,
            "num": 5,
            "api_key": google_api_key,
        }
    else:
        params = {
            "engine": google_author_engine,
            "view_op": "view_citation",
            "citation_id": citation_id,
            "api_key": google_api_key,
        }
    return params


def get_top_authors(keyword):
    params = set_search_params(search_type="profile", search_term=keyword)
    search = GoogleSearch(params)
    results = search.get_dict()
    profiles = results["profiles"]
    df = pd.DataFrame(profiles)
    return df


def get_article_desc(citation_id):
    params = set_search_params(search_type="article", citation_id=citation_id)
    search = GoogleSearch(params)
    results = search.get_dict()
    citation = results["citation"]
    desc = citation.get("description")
    return desc


def json_cleanup(interest_list):
    interests = [item["title"] for item in interest_list]
    return interests


def get_top_pubs(user_input):
    # clean search term
    keyword = get_search_keyword(user_input)

    # grab top authors for keyword
    top_authors = get_top_authors(keyword)
    top_authors = top_authors.head(3)

    top_authors.to_csv("output/top_authors.csv")

    # grab list of author ids
    author_ids = top_authors["author_id"].unique()

    article_list = []

    # only get top 3 author's papers
    for id in author_ids:
        # for each author, run query
        params = set_search_params(search_type="pubs", author_id=id)
        search = GoogleSearch(params)
        results = search.get_dict()
        articles = results["articles"]

        # append to main list
        for a in articles[0:5]:
            desc = get_article_desc(a.get("citation_id"))
            article_list.append(
                {
                    "author_id": id,
                    "article_id": a.get("citation_id"),
                    "title": a.get("title"),
                    "description": desc,
                }
            )

    results_temp = pd.DataFrame(article_list)
    results_final = results_temp.merge(top_authors, how="left", on="author_id")
    results_final = results_final[
        ["name", "interests", "affiliations", "title", "description"]
    ]

    # clean up interests mess-up... should've done this at the start smh
    results_final["interests_clean"] = results_final["interests"].apply(
        lambda x: json_cleanup(x)
    )
    results_final.drop("interests", axis=1, inplace=True)
    results_final.rename(columns={"interests_clean": "interests"}, inplace=True)

    results_final.to_csv("output/test_results.csv")
    return results_final
