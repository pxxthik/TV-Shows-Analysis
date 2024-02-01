import helper

def popular_tv_shows():
    popular_votes = helper.show_votes[helper.show_votes['vote_count'] > 10000]
    temp = helper.shows.merge(popular_votes, on='show_id').sort_values('popularity', ascending=False).head(12)
    return temp.rename(columns={'number_of_seasons': "seasons"})

def genre_popularity():
    temp = helper.shows.merge(helper.genres, on='show_id')
    temp = temp.groupby('genre_type_id')['popularity'].mean().reset_index()
    temp = temp.merge(helper.genre_types, on='genre_type_id')
    return temp

def language_distribution():
    popular_languages = helper.spoken_languages['spoken_language_type_id'].value_counts().head(12).reset_index()
    temp = popular_languages.merge(helper.spoken_language_types, on='spoken_language_type_id')

    x = helper.spoken_languages.merge(helper.shows, on='show_id')[['show_id', 'popularity', 'spoken_language_type_id']]
    x = x.groupby('spoken_language_type_id')['popularity'].mean().reset_index()

    return x.merge(temp, on='spoken_language_type_id')

def status_analysis():
    temp1 = helper.shows.merge(helper.status, on='status_id')
    temp1 = temp1.groupby("status_name")['show_id'].count().reset_index()

    temp2 = helper.shows.merge(helper.status, on='status_id')
    temp2 = temp2.groupby("status_name")['popularity'].mean().reset_index()

    temp = temp1.merge(temp2, on='status_name')
    return temp.rename(columns={"show_id": "count"})

def type_distribution():
    temp1 = helper.shows.merge(helper.types, on='type_id')
    temp1 = temp1.groupby("type_name")['show_id'].count().reset_index()

    temp2 = helper.shows.merge(helper.types, on='type_id')
    temp2 = temp2.groupby("type_name")['popularity'].mean().reset_index()

    temp = temp1.merge(temp2, on='type_name')
    return temp.rename(columns={"show_id": "count"})

def network_analysis():
    popular_networks = helper.networks['network_type_id'].value_counts().head(7).reset_index()
    return popular_networks.merge(helper.network_types, on='network_type_id')

def production_company_insights():
    temp = helper.production_companies['production_company_type_id'].value_counts().head(10).reset_index()
    temp = temp.merge(helper.production_company_types, on='production_company_type_id')

    x = helper.production_companies.merge(helper.shows, on='show_id').groupby('production_company_type_id')['popularity'].mean().reset_index()
    return x.merge(temp, on='production_company_type_id')

def origin_country_analysis():
    top_origin_countries_index = helper.production_countries['origin_country_type_id'].value_counts().head(5).index
    top_origin_countries = helper.production_countries[helper.production_countries['origin_country_type_id'].isin(top_origin_countries_index)]

    temp = top_origin_countries.merge(helper.origin_country_types, on='origin_country_type_id')
    temp = temp.merge(helper.shows, on='show_id')
    temp = helper.air_dates.merge(temp, on='show_id')
    temp = temp.groupby(['date', 'origin_country_name'])['show_id'].count().unstack()
    temp = temp.reset_index()
    temp = temp.melt(id_vars=['date'], value_name='count')
    temp['year'] = temp['date'].dt.year
    return temp

def air_date_trends():
    temp = helper.air_dates.merge(helper.shows, on='show_id').merge(helper.genres, on='show_id').merge(helper.genre_types, on='genre_type_id')
    temp = temp.groupby(['date', 'genre_name', 'is_first'])['show_id'].count()
    temp = temp.unstack().reset_index()
    temp['year'] = temp['date'].dt.year
    return temp

def top_creators():
    top_creators_id = helper.created_by['created_by_type_id'].value_counts().head(7).index
    top_creators = helper.created_by[helper.created_by['created_by_type_id'].isin(top_creators_id)]

    temp = top_creators.merge(helper.genres, on='show_id').groupby(['genre_type_id', 'created_by_type_id'])['show_id'].count().unstack()
    temp = temp.reset_index().melt(id_vars=['genre_type_id'], value_name='count')
    temp = temp.merge(helper.genre_types, on='genre_type_id').merge(helper.created_by_types, on='created_by_type_id')
    return temp