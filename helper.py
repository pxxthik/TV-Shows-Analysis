import numpy as np
import pandas as pd

shows1 = pd.read_csv("artifacts/shows1.csv")
shows2 = pd.read_csv("artifacts/shows2.csv")
shows = pd.concat([shows1, shows2], axis=0, ignore_index=True)

show_votes = pd.read_csv("data/show_votes.csv")
air_dates = pd.read_csv("data/air_dates.csv")
air_dates['date'] = pd.to_datetime(air_dates['date'])
genres = pd.read_csv("data/genres.csv")
genre_types = pd.read_csv("data/genre_types.csv")
spoken_languages = pd.read_csv("data/spoken_languages.csv")
spoken_language_types = pd.read_csv("data/spoken_language_types.csv")
status = pd.read_csv("data/status.csv")
types = pd.read_csv("data/types.csv")
networks = pd.read_csv("data/networks.csv")
network_types = pd.read_csv("data/network_types.csv")
production_companies = pd.read_csv("data/production_companies.csv")
production_company_types = pd.read_csv("data/production_company_types.csv")
production_countries = pd.read_csv("data/production_countries.csv")
production_country_types = pd.read_csv('data/production_country_types.csv')
origin_country_types = pd.read_csv("data/origin_country_types.csv")
created_by = pd.read_csv("data/created_by.csv")
created_by_types = pd.read_csv("data/created_by_types.csv")
links = pd.read_csv("data/links.csv")

def get_posters(df):
    return links[links['link_type_id'] == 3].merge(df, on='show_id')['link'].values.tolist()