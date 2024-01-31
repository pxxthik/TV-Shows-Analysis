import streamlit as st
import plotly.express as px 
import overall, element, helper, filter

st.set_page_config(
    page_title="TV Shows Analysis",
    page_icon="📺"
)

st.sidebar.title("TV Show Analysis")
st.sidebar.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8SXO99LnAGaUD-g7avPMokXrFhpl2YQVdGA&usqp=CAU')

def add_posters(df):
    poster_images = helper.get_posters(df)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        try:
            st.image(f"https://image.tmdb.org/t/p/w500/{poster_images[0]}")
        except:
            st.error("Image Not Found")
    with col2:
        try:
            st.image(f"https://image.tmdb.org/t/p/w500/{poster_images[1]}")
        except:
            st.error("Image Not Found")
    with col3:
        try:
            st.image(f"https://image.tmdb.org/t/p/w500/{poster_images[2]}")
        except:
            st.error("Image Not Found")
    with col4:
        try:
            st.image(f"https://image.tmdb.org/t/p/w500/{poster_images[3]}")
        except:
            st.error("Image Not Found")
    with col5:
        try:
            st.image(f"https://image.tmdb.org/t/p/w500/{poster_images[4]}")
        except:
            st.error("Image Not Found")


user_menu = st.sidebar.radio(
    'Select an Option',
    ('Overall Analysis', 'Element-wise Analysis', 'Show-wise Analysis')
)

if user_menu == "Overall Analysis":
    st.title("📺 Overall TV Show Analysis")

    df = overall.popular_tv_shows()
    add_posters(df.head())
    st.header("🔥 Most Popular TV Shows")
    st.dataframe(df[['name','seasons', 'original_name', 'popularity' , 'vote_count', 'vote_average']])

    st.header("🎭 Genres Popularity")
    df = overall.genre_popularity()
    fig = px.pie(df, values='popularity', names='genre_name')
    st.plotly_chart(fig)

    st.header("✍️ Top Creators")
    df = overall.top_creators()
    fig = px.bar(df, x="created_by_name", y="count", color="genre_name")
    st.plotly_chart(fig)

    st.header("💁👌 Top Language Distribution")
    df = overall.language_distribution()
    fig=px.bar(df,x='count',y='spoken_language_name', orientation='h', color='popularity')
    st.plotly_chart(fig)

    st.header("🌐 Top Network Analysis")
    df = overall.network_analysis()
    fig = px.pie(df, values='count', names='network_name', hole=0.4)
    st.plotly_chart(fig)

    st.header("📅🔥 Air Date Popularity")
    df = overall.air_date_trends(pop=True)
    fig = px.line(df, x="date", y=1, color="genre_name")
    st.plotly_chart(fig)

    st.header("📅 Air Date Trends")
    df = overall.air_date_trends()
    fig = px.line(df, x="date", y=1, color="genre_name")
    st.plotly_chart(fig)

    st.header("🎌 Top Origin Country Analysis")
    df = overall.origin_country_analysis()
    fig = px.line(df, x="date", y="count", color="origin_country_name")
    st.plotly_chart(fig)

    st.header("🏢 Production Company Insights")
    df = overall.production_company_insights()
    fig = px.bar(df, x='production_company_name', y='count', color='popularity')
    st.plotly_chart(fig)

    st.header("Status Analysis")
    df = overall.status_analysis()
    fig = px.bar(df, x='status_name', y='count', color='popularity')
    st.plotly_chart(fig)
    
    st.header("Type Distribution")
    df = overall.type_distribution()
    fig = px.bar(df, x='type_name', y='count', color='popularity')
    st.plotly_chart(fig)
    
elif user_menu == "Element-wise Analysis":
    st.title(f"🛠️ {user_menu}")

    selected_genre = st.sidebar.selectbox("Select Genre", element.get_genre_names())
    selected_language = st.sidebar.selectbox("Select Language", element.get_top_languages())
    selected_year = st.sidebar.selectbox("Select Year", element.get_years())
    selected_type = st.sidebar.selectbox("Select Type", element.get_types())

    elements = {"genre": selected_genre, "language": selected_language, "year": selected_year, "type": selected_type}

    filtered_df = filter.filter_df(elements)

    metrics = element.get_metrics(filtered_df)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("No of Shows", metrics['count'])
    with col2:
        st.metric("Popularity", metrics['popularity'])
    with col3:
        st.metric("No of Votes", metrics['vote_count'])
    with col4:
        st.metric("Avg Votes", metrics['vote_average'])

    df = element.popular(filtered_df)
    add_posters(df.head(10))

    st.header("🔥 Most Popular TV Shows")
    st.dataframe(df[['Show name','Genre' , 'popularity', 'year', 'vote_average', 'Language', 'Type']].head(50))

    if st.button("Load more"):
        st.header("✍️ Top Creators")
        df = element.get_top_creators(filtered_df)
        fig = px.bar(df, x="created_by_name", y="count", color="genre_name")
        st.plotly_chart(fig)

        st.header("🌐 Top Network Analysis")
        df = element.top_networks(filtered_df)
        fig = px.pie(df, values='count', names='network_name', hole=0.4)
        st.plotly_chart(fig)

        st.header("📅🔥 Air Date Popularity")
        df = element.air_date_trends(filtered_df, pop=True)
        try:
            fig = px.line(df, x="date", y=1, color="Genre")
            st.plotly_chart(fig)
        except:
            st.write("No Data")

        st.header("📅 Air Date Trends")
        df = element.air_date_trends(filtered_df)
        try:
            fig = px.line(df, x="date", y=1, color="Genre")
            st.plotly_chart(fig)
        except:
            st.write("No Data")
        
        st.header("🎌 Top Origin Country Analysis")
        df = element.origin_country_analysis(filtered_df)
        fig = px.line(df, x="date", y="count", color="origin_country_name")
        st.plotly_chart(fig)

        st.header("🏢 Production Company Insights")
        df = element.production_company_insights(filtered_df)
        fig = px.bar(df, x='production_company_name', y='count', text_auto='.2s', color='popularity')
        st.plotly_chart(fig)

        st.header("Status Analysis")
        df = element.status_analysis(filtered_df)
        fig = px.bar(df, x='status_name', y='count', color='popularity')
        st.plotly_chart(fig)

    
elif user_menu == "Show-wise Analysis":
    st.title(f"🎭 {user_menu}")