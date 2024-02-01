import helper

def tv_shows():
    return helper.shows[helper.shows['popularity'] > 5]['name'].values.tolist()

def get_info(tv_show):
    return helper.shows[helper.shows['name'] == tv_show]

def get_vote_info(df, vote_count=False):
    df = df.merge(helper.show_votes, on='show_id')
    if vote_count:
        return df['vote_count'].values[0]
    return df['vote_average'].values[0]

def get_genre(df):
    df = df.merge(helper.genres, on='show_id')
    df = df.merge(helper.genre_types, on='genre_type_id')
    return df[['genre_name']]

def get_language(df):
    df = df.merge(helper.spoken_languages, on='show_id')
    df = df.merge(helper.spoken_language_types, on='spoken_language_type_id')
    return df['spoken_language_name'].values[0]

def get_origin_country(df):
    df = df.merge(helper.production_countries, on='show_id')
    df = df.merge(helper.origin_country_types, on='origin_country_type_id')
    return df['origin_country_name'].values[0]

def get_status(df):
    df = df.merge(helper.status, on='status_id')
    return df['status_name'].values[0]

def get_type(df):
    df = df.merge(helper.types, on='type_id')
    return df['type_name'].values[0]

def get_network(df):
    df = df.merge(helper.networks, on='show_id')
    df = df.merge(helper.network_types, on='network_type_id')
    return df['network_name'].values[0]

def get_creators(df):
    df = df.merge(helper.created_by, on='show_id')
    df = df.merge(helper.created_by_types, on='created_by_type_id')
    return df[['created_by_name']].rename(columns={"created_by_name": "Creators"})

def get_prod_companies(df):
    df = df.merge(helper.production_companies, on='show_id')
    df = df.merge(helper.production_company_types, on='production_company_type_id')
    df.rename(columns={
        "production_company_name": "Production Companies"
    }, inplace=True)
    return df[['Production Companies']]

def get_prod_countries(df):
    df = df.merge(helper.production_countries, on='show_id')
    df = df.merge(helper.production_country_types, on='production_country_type_id')
    return df[['production_country_name']].rename(columns={
        "production_country_name": "Production Countries"
    })