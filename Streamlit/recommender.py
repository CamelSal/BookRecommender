import streamlit as st
import pandas as pd
import numpy as np

#loading all dataframes
#book_df = pd.read_csv('../data_clean/books.csv',index_col=[0])
book_df = pd.read_csv('books.csv',index_col=[0])
book_demo_df = pd.read_csv('book_demo_noauth.csv',index_col=[0])
book_demo_au_df = pd.read_csv('book_demo_auth.csv',index_col=[0])

image_df = book_df[['book_id','title','image_url']]

# Function to retrieve book recommendations based on given book IDs
def recommend_res(ls_id):
    """
    Retrievs book recommendations based on book IDs.

    Parameters:
    ls_id (DataFrame): DataFrame containing book IDs.

    Returns:
    DataFrame: Book recommendations with additional information.
    """
    results = pd.merge(ls_id,book_df[['book_id','title','authors','original_publication_year','average_rating']],
                        on ='book_id', how = 'left').set_index('book_id')

    return results

# Function to display book image based on the title
def sh_image(titl):
    
    """
    Get the image URL for a given book title.

    Parameters:
    titl (str): Book title.

    Returns:
    str: Image URL.
    """
    result = image_df[image_df['title'] == titl]['image_url'].values[0]
    return result


# Page Title
st.title(r"$\textsf{\huge GoodRecs 10K}$")
st.title('**Hybrid Based Book Recommendation System**')
# Header
#st.header('Welcome to My Book Recommender Made By Camilo Salazar')
# Text
st.write('This Streamlit app provides a user-friendly interface for generating \
          book recommendations. By choosing a book title from a curated list of \
          **10,000** titles, the app employs a sophisticated recommendation system to \
          present a carefully selected list of titles and book covers for the top \
          10 books that share similarities with the chosen book.\
          \n\nThe recommendations are generated using a hybrid approach \
         that combines collaborative filtering and content-based filtering. \
         This ensures a well-rounded selection based on both user ratings and \
         book content. Enjoy a seamless and personalized book discovery experience \
         with this interactive showcase.')

# Sidebar Input with all titles available in dataframe 
options = book_df['title'].values
selected_title = st.selectbox('**Select Book Title**', options)


# Display Book Image
st.image(sh_image(selected_title))

# Checkbox to exclude works by the same author
sm_auth = st.checkbox('Exclude Works by the Same Author')

# Button to trigger book recommendations
if st.button('Recomend Me Some Books'):
    # Data Display
    st.write('Top 10 Recomendations')
    # DataFrame based on user selection and author exclusion preference
    if sm_auth:
        rec_id = pd.DataFrame(book_demo_df.loc[selected_title].values, columns = ['book_id'])
    else:
        rec_id = pd.DataFrame(book_demo_au_df.loc[selected_title].values, columns = ['book_id'])

    # Display top 10 recommended books with images
    for i in range(10):
        top_1 = rec_id.loc[i].values[0] 
        top_gid = book_df[book_df['book_id'] == top_1]['goodreads_book_id'].values[0]
        top_title = book_df[book_df['book_id'] == top_1]['title'].values[0]

        st.markdown(f'{i+1}. [{top_title}](https://www.goodreads.com/book/show/{top_gid})')
        st.image(sh_image(top_title))
    
    # Display full information of recommended books in a DataFrame
    st.markdown(' ')
    st.markdown(' ')
    st.markdown('Full Info')
    st.dataframe(recommend_res(rec_id))
