import streamlit as st
import plotly.express as px 
import overall, element

st.set_page_config(
    page_title="TV Shows Analysis",
    page_icon="📺"
)

st.sidebar.title("TV Show Analysis")
st.sidebar.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8SXO99LnAGaUD-g7avPMokXrFhpl2YQVdGA&usqp=CAU')

user_menu = st.sidebar.radio(
    'Select an Option',
    ('Overall Analysis', 'Element-wise Analysis', 'Show-wise Analysis')
)

if user_menu == "Overall Analysis":
    st.title("📺 Overall TV Show Analysis")

    st.header("🔥 Most Popular TV Shows")
    st.dataframe(overall.popular_tv_shows())

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
    fig=px.bar(df,x='count',y='spoken_language_name', orientation='h')
    st.plotly_chart(fig)

    st.header("🌐 Top Network Analysis")
    df = overall.network_analysis()
    fig = px.pie(df, values='count', names='network_name', hole=0.4)
    st.plotly_chart(fig)

    st.header("📅🔥 Air Date Popularity Trends")
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
    fig = px.bar(df, x='production_company_name', y='count')
    st.plotly_chart(fig)

    st.header("Status Analysis")
    df = overall.status_analysis()
    fig = px.bar(df, x='status_name', y='count')
    st.plotly_chart(fig)
    
    st.header("Type Distribution")
    df = overall.type_distribution()
    fig = px.bar(df, x='type_name', y='count')
    st.plotly_chart(fig)
    
elif user_menu == "Element-wise Analysis":
    st.title(f"🛠️ {user_menu}")

    selected_genre = st.sidebar.selectbox("Select Genre", element.get_genre_names())
    selected_language = st.sidebar.selectbox("Select Language", element.get_top_languages())
    selected_year = st.sidebar.selectbox("Select Year", element.get_years())
    selected_type = st.sidebar.selectbox("Select Type", element.get_types())

    elements = {"genre": selected_genre, "language": selected_language, "year": selected_year, "type": selected_type}
    metrics = element.get_metrics(elements)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("No of Shows", metrics['count'])
    with col2:
        st.metric("Popularity", metrics['popularity'])
    with col3:
        st.metric("No of Votes", metrics['vote_count'])
    with col4:
        st.metric("Avg Votes", metrics['vote_average'])

    st.header("🔥 Most Popular TV Shows")
    st.dataframe(element.popular(elements)[['Show name','Genre' , 'popularity', 'year', 'vote_average', 'Language', 'Type']])

    st.header("✍️ Top Creators")
    df = element.get_top_creators(elements)
    fig = px.bar(df, x="created_by_name", y="count", color="genre_name")
    st.plotly_chart(fig)

    st.header("🌐 Top Network Analysis")
    df = element.top_networks(elements)
    fig = px.pie(df, values='count', names='network_name', hole=0.4)
    st.plotly_chart(fig)

    st.header("📅🔥 Air Date Popularity Trends")
    df = element.air_date_trends(elements, pop=True)
    try:
        fig = px.line(df, x="date", y=1, color="Genre")
        st.plotly_chart(fig)
    except:
        st.write("No Data")

    st.header("📅 Air Date Trends")
    df = element.air_date_trends(elements)
    try:
        fig = px.line(df, x="date", y=1, color="Genre")
        st.plotly_chart(fig)
    except:
        st.write("No Data")
    
    st.header("🎌 Top Origin Country Analysis")
    df = element.origin_country_analysis(elements)
    fig = px.line(df, x="date", y="count", color="origin_country_name")
    st.plotly_chart(fig)

    st.header("🏢 Production Company Insights")
    df = element.production_company_insights(elements)
    fig = px.bar(df, x='production_company_name', y='count', text_auto='.2s', color='popularity')
    st.plotly_chart(fig)

    st.header("Status Analysis")
    df = element.status_analysis(elements)
    fig = px.bar(df, x='status_name', y='count', color='popularity')
    st.plotly_chart(fig)

    
elif user_menu == "Show-wise Analysis":
    st.title(f"🎭 {user_menu}")