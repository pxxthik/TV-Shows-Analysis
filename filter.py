import helper

def filter_df(element):
    genre = helper.genre_types
    language = helper.spoken_language_types
    date = helper.air_dates
    date['year'] = date['date'].dt.year
    types = helper.types

    if element['genre'] != "Overall":
        genre = genre[genre['genre_name'] == element['genre']]
    if element['language'] != "Overall":
        language = language[language['spoken_language_name'] == element['language']]
    if element['year'] != "Overall":
        date = date[date['year'] == element['year']]
    if element['type'] != "Overall":
        types = types[types['type_name'] == element['type']]
    
    temp_genre = genre.merge(helper.genres, on='genre_type_id')
    temp_lang = language.merge(helper.spoken_languages, on='spoken_language_type_id')

    temp_df = temp_genre.merge(temp_lang, on='show_id')
    temp_df = temp_df.merge(date, on='show_id')
    temp_df = temp_df.merge(helper.show_votes, on='show_id')

    df = temp_df.merge(helper.shows, on='show_id')
    df = df.merge(types, on='type_id')

    return df.rename(columns={
        "spoken_language_name": "Language",
        "genre_name": "Genre",
        "name": "Show name",
        "type_name": "Type"
    })