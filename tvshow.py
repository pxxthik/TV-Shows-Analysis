import helper

def tv_shows():
    return helper.shows[helper.shows['popularity'] > 70]['name'].values.tolist()

def get_info(tv_show):
    x = helper.shows[helper.shows['name'] == tv_show]
    x = x.merge(helper.genres, on='show_id').merge(helper.genre_types, on='genre_type_id')
    x = x.merge(helper.spoken_languages, on='show_id').merge(helper.spoken_language_types, on='spoken_language_type_id')
    x = x.merge(helper.status, on='status_id').merge(helper.types, on='type_id')
    x = x.merge(helper.created_by, on='show_id').merge(helper.created_by_types, on='created_by_type_id')
    x = x.merge(helper.networks, on='show_id').merge(helper.network_types, on='network_type_id')
    x = x.merge(helper.show_votes, on='show_id')
    x = x.merge(helper.production_companies, on='show_id').merge(helper.production_company_types, on='production_company_type_id')
    x = x.merge(helper.air_dates, on='show_id')
    x = x.merge(helper.production_countries, on='show_id')
    x = x.merge(helper.production_country_types, on='production_country_type_id').merge(helper.origin_country_types, on='origin_country_type_id')
    return x