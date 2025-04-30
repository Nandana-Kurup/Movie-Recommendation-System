# %%
import numpy as np
import pandas as pd


# %%
movies=pd.read_csv("tmdb_5000_movies.csv")
credits=pd.read_csv("tmdb_5000_credits.csv")

# %%
movies.head()

# %%
credits.head(1)

# %%
movies.head(1)

# %%
movies=movies.merge(credits,on='title')

# %%
movies.head(1)

# %%
#genres
#id
#keywords
#title
#overview
#crew

movies = movies[['movie_id','title','overview','genres','cast','keywords','crew']]


# %%
movies['original_language'].value_counts()

# %%
movies.info()

# %%
movies.isnull().sum()

# %%
movies.dropna(inplace=True)

# %%
movies.duplicated().sum()

# %%
movies.iloc[0].genres

# %%
#[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"},{"id": 14, "name": "Fantasy"},{"id": 878, "name": "Science Fiction"}]'
#['Action','Adventure'.'Fantasy',SciFi']

# %%
def convert(obj):
    L=[]
    for i in ast.literal_eval(obj):
        L.append(i['name'])
        return L

# %%
import ast

# Correct usage of ast.literal_eval
result = ast.literal_eval('[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"},{"id": 14, "name": "Fantasy"},{"id": 878, "name": "Science Fiction"}]')
print(result)


# %%
movies['genres'].apply(convert)

# %%
movies.head()

# %%
movies['keywords']=movies['keywords'].apply(convert)

# %%
movies.head()

# %%
def convert3(obj):
    L=[]
    counter=0
    for i in ast.literal_eval(obj):
        if counter !=3:
            L.append(i['name'])
            counter+=1
        else:
            break
        return L
            
       

# %% [markdown]
# 

# %%
movies['cast']=movies['cast'].apply(convert3)

# %%
movies.head()

# %%
movies['genres']=movies['genres'].apply(convert3)

# %%
movies.head()

# %%
def convert(obj):
    L=[]
    for i in  ast.literal_eval(obj):
        L.append(i['name'])
    return L
    
    

# %%
movies['crew'][0]

# %%
def fetch_director(obj):
    L=[]
    for i in ast.literal_eval(obj):
        if i['job']=='Director':
            L.append(i['name'])
            break
    return L

# %%
movies['crew']=movies['crew'].apply(fetch_director)

# %%
movies.head()

# %%
movies['overview'][0]

# %%
movies['overview']=movies['overview'].apply(lambda x:x.split())

# %%
movies.head()

# %%
movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x] if x is not None else [])
movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x] if x is not None else [])
movies['cast'] = movies['cast'].apply(lambda x: [i.replace(" ", "") for i in x] if x is not None else [])
movies['crew'] = movies['crew'].apply(lambda x: [i.replace(" ", "") for i in x] if x is not None else [])


# %%
movies.head()

# %%
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']


# %%
new_df=movies[['movie_id','title','tags']]

# %%
new_df['tags']=new_df['tags'].apply(lambda x:" ".join(x))

# %%
new_df.head()

# %%
new_df['tags'][2]

# %%
new_df['tags']=new_df['tags'].apply(lambda x:x.lower())

# %%
new_df.head()

# %%
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=5000,stop_words='english')

# %%
vectors = cv.fit_transform(new_df['tags']).shape



# %%
 vectors

# %%
vectors[0]

# %%
cv.get_feature_names_out()



# %%
import nltk

# %%
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()

# %%
def stem(text):
    y=[]

    for i in text.split():
        y.append(ps.stem(i))

    return " ".join(y)
      

# %%
ps.stem('loved')

# %%
ps.stem('loving')

# %%
new_df['tags']=new_df['tags'].apply(stem)

# %%
from sklearn.metrics.pairwise import cosine_similarity

# %%
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_df['tags'])  # ← THIS is your 2D matrix (sparse matrix)


# %%
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vectors)  


# %%
similarity

# %%
new_df

# %%
def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    for i in movies_list:
        print(new_df.iloc[i[0]].title)
        
  

# %%
sorted(list(enumerate(similarity[0])), reverse=True, key=lambda x: x[1])[1:6]

# %%
recommend('Avatar')

# %%
new_df.iloc[1216].title

# %%
recommend('Batman Begins')

# %%
import pickle

# %%
pickle.dump(new_df.to_dict(), open('movies.pkl', 'wb'))


# %%
new_df


# %%
new_df['title'].values

# %%
new_df.to_dict()

# %%
pickle.dump(similarity,open('similarity.pkl','wb'))

# %%



