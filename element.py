import numpy as np
import helper

def get_genre_names():
    genre_names = helper.genre_types['genre_name'].values.tolist()
    genre_names.insert(0, "Overall")
    return genre_names

def get_top_languages():
    popular_languages = helper.spoken_languages['spoken_language_type_id'].value_counts().head(50).reset_index()
    languages = popular_languages.merge(helper.spoken_language_types, on='spoken_language_type_id')['spoken_language_name'].values.tolist()
    languages.insert(0, "Overall")
    return languages

def get_top_networks():
    popular_networks = helper.networks['network_type_id'].value_counts().head(7).reset_index()
    networks = popular_networks.merge(helper.network_types, on='network_type_id')['network_name'].values.tolist()
    networks.insert(0, "Overall")
    return networks

def get_top_prod_companies():
    temp = helper.production_companies['production_company_type_id'].value_counts().head(50).reset_index()
    temp = temp.merge(helper.production_company_types, on='production_company_type_id')
    companies = temp['production_company_name'].values.tolist()
    companies.insert(0, "Overall")
    return companies

def get_years():
    years = np.unique(helper.air_dates['date'].dt.year.values)
    years = years[~np.isnan(years)].astype(int).tolist()
    years = years[::-1]
    years.insert(0, "Overall")
    return years

def get_types():
    types = helper.types['type_name'].values.tolist()
    types.insert(0, "Overall")
    return types

def get_metrics(df):
    count = df.drop_duplicates('show_id')['show_id'].count()
    popularity = round(df.drop_duplicates('show_id')['popularity'].mean(), 2)
    vote_count = df.drop_duplicates('show_id')['vote_count'].sum()
    vote_average = round(df.drop_duplicates('show_id')['vote_average'].mean(), 2)
    metrics = {"count": count, "popularity": popularity, "vote_count": vote_count, "vote_average": vote_average}
    return metrics

def popular(df):
    df = df.drop_duplicates('show_id')
    return df

def get_top_creators(df):
    top_creators_id = helper.created_by['created_by_type_id'].value_counts().head(7).index
    top_creators = helper.created_by[helper.created_by['created_by_type_id'].isin(top_creators_id)]

    temp = top_creators.merge(df, on='show_id').groupby(['genre_type_id', 'created_by_type_id'])['show_id'].count().unstack()
    temp = temp.reset_index().melt(id_vars=['genre_type_id'], value_name='count')
    temp = temp.merge(helper.genre_types, on='genre_type_id').merge(helper.created_by_types, on='created_by_type_id')
    return temp

def air_date_trends(df):
    temp = df.groupby(['date', 'Genre', 'is_first'])['show_id'].count()
    temp = temp.unstack().reset_index()
    temp['year'] = temp['date'].dt.year
    return temp

def top_networks(df):
    temp_networks = df[['show_id']].merge(helper.networks, on='show_id').drop_duplicates('show_id')

    popular_networks = temp_networks['network_type_id'].value_counts().head(7).reset_index()
    return popular_networks.merge(helper.network_types, on='network_type_id')

def origin_country_analysis(df):
    top_origin_countries_index = helper.production_countries['origin_country_type_id'].value_counts().head(5).index
    top_origin_countries = helper.production_countries[helper.production_countries['origin_country_type_id'].isin(top_origin_countries_index)]

    temp = top_origin_countries.merge(helper.origin_country_types, on='origin_country_type_id')
    temp = temp.merge(df, on='show_id')
    temp = temp.groupby(['date', 'origin_country_name'])['show_id'].count().unstack()
    temp = temp.reset_index()
    temp = temp.melt(id_vars=['date'], value_name='count')
    temp['year'] = temp['date'].dt.year
    return temp

def production_company_insights(df):
    temp = df[['show_id', 'popularity']].merge(helper.production_companies, on='show_id').drop_duplicates('show_id')
    temp2 = temp['production_company_type_id'].value_counts().head(10).reset_index()
    temp = temp.merge(temp2, on='production_company_type_id')
    temp = temp.merge(helper.production_company_types, on='production_company_type_id')
    return temp[['popularity', 'count', 'production_company_name']]

def status_analysis(df):
    temp = df.merge(helper.status, on='status_id')
    temp1 = temp.groupby("status_name")['show_id'].count().reset_index()
    temp2 = temp.groupby("status_name")['popularity'].mean().reset_index()
    return temp1.merge(temp2, on='status_name').rename(columns={"show_id": "count"})