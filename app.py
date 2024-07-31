import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=34273115e9829da6e03549a2f125d9fe'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

movies_list=pickle.load(open('movies_dict.pkl','rb'))
similarity=pickle.load(open('sim.pkl','rb'))
movies=pd.DataFrame(movies_list)
print(movies_list)
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_l=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_mov=[]
    recommended_mov_poster=[]
    for i in movies_l:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_mov.append(movies.iloc[i[0]].title)
        recommended_mov_poster.append(fetch_poster(movie_id))
    return recommended_mov,recommended_mov_poster
st.title('Movie Recommender System')
selected_movie_name=st.selectbox(
    'Enter the name of preferred movie',
    (movies['title'].values)
)
if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])


