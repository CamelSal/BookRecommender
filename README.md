# Book Recommender

This repository contains the code and documentation for a book recommender system part of capstone project for BrainStation


## Overview

### Problem Statement:

In today's world, with an ever-increasing number of books being published, discovering books that genuinely align with one's interests has become challenging. The abundance of available books and vague categorizations often makes finding an enjoyable read a truly frustrating experience.

### Those Affected:
As an avid reader, I've personally grappled with this issue. Readers, both casual and dedicated, encounter this problem. The moment you finish a book you enjoyed, you're left searching for something similar, often with no clear starting point, leaving readers in a state of ambiguity. This is an issue that resonates with anyone who's ever embarked on the quest for their next great read.


### Business Values:

A reliable book recommender has the potential to increase readers' consumption rate significantly. It can be a game-changer, reducing the time spent hunting for new books and ensuring they discover more engaging and enjoyable reads. Moreover, it's not just readers who stand to benefit from this innovation. Businesses have a vested interest in this as well, as it can enhance the shopping frequency of their customers, ultimately leading to higher sales and fostering customer loyalty.

### Proposed Data Science Solution:

This project addresses the issue by developing an intelligent book recommendation system. The primary aim is to seamlessly connect readers with books that align with their tastes, simplifying the process of finding enjoyable reads amidst the vast sea of available options.

To achieve this, the project harnesses the power of machine learning. The book recommender system will employ various techniques, including both content-based and collaborative filtering, resulting in a hybrid recommender. The implementation will involve exploring algorithms such as Singular Value Decomposition (SVD) and Cosine Similarity. These algorithms are instrumental in identifying similar users and making predictions about user ratings for book recommendations. This combination ensures a robust and effective recommendation system for book enthusiasts.

![alt text](https://github.com/CamelSal/BookRecommender/blob/main/images/image1.png?raw=true)

## Dataset

For this project will be working with the data [GoodBooks-10K](https://github.com/zygmuntz/goodbooks-10k) which contains four indidual files that will be utilized to build the book recommender system.

#### books.csv: A dataset with 10,000 unique books from Goodreads.

| Column     | Type    | Description    |
|-------------------|-------------------|-------------------|
| book_id   | int64  | Unique ID for each book  |
| goodreads_book_id	   | object  | Unique ID for the most popular edition of each book from the Goodreads Website |
| work_id	   | object  | Unique ID for the aggereagtion of all edition of each book from the Goodreads Website |
| authors	   | object  | The name of all the authors |
| original_publication_year   | float64  | The year the original boook was publish   |
| title   | object | The title of the book  |
| work_ratings_count   | int64  | The number of users rating |
| average_rating   | float64  | The average rating  |
| language_code  | object | Abbreviated language tag  |


#### ratings.csv: Contains 5.97 million user ratings for the books.

| Column     | Type    | Description    |
|-------------------|-------------------|-------------------|
| user_id   | int64  | Unique ID for each user  |
| book_id	   | int64  | Unique ID for each book |
| rating   | int64  | Rating from 1 to 5  |


#### book_tags.csv: the tags Assigned by users to books and their counts

| Column     | Type    | Description    |
|-------------------|-------------------|-------------------|
| goodreads_book_id  | int64  | Unique ID for each book from the GoodReads Website |
| tag_id  | int64 | Unique ID for each tag  |
| count   | int64  | The number of users that have assigned the tag  |

#### tags.csv: All user-generated tags id and their names

| Column     | Type    | Description    |
|-------------------|-------------------|-------------------|
| tag_id   | int64  | Unique ID for each tag   |
| tag_name  | object  | Name of the tag  |



## Project Organization

### Data Collection and Preprocessing
1. **Gather Data**: Collect data from GoodBooks-10K. 

2. **Clean Data**: Addressed missing values by filling in the gaps for the publication year and language code and eliminated redundant columns such as ISBN and Original Title. In addition, six duplicated rows were removed from the Book Tags dataset.


### Exploratory Data Analysis

3. **Data Visualization**: Create visualizations to explore the dataset, examining the distribution of publication years, the distribution of the number of tags per book, and the distribution of the number of books rated by each user.

![alt text](https://github.com/CamelSal/BookRecommender/blob/main/images/ratings_dis.png?raw=true)

4. **Identify Data Patterns**: Identified that the ratings exhibited a good amount of spread between users and books, making them ready for modelling. In contrast, the tags required some feature engineering, as over half of the tags were present in only one book.

![alt text](https://github.com/CamelSal/BookRecommender/blob/main/images/books_dis.png?raw=true)

### Feature Engineering

5. **Refine Data** Refine the book tag data by eliminating tags that appeared in fewer than 10 books or were present in more than 66% of the books, resulting in approximately 5,000 tags. Most books now have around 60-80 tags each

![alt text](https://github.com/CamelSal/BookRecommender/blob/main/images/num_tags.png?raw=true)

###  Collaborative Filtering Model Building

6. **Baseline Model**: The Funk Singular Value Decomposition (SVD) model for collaborative filtering was implemented. Using the ratings dataset, a sample of 200k ratings was taken, and RMSE, MAE, and FCP metrics were used to evaluate its performance.

7. **Tune Hyperparameters** Using the small sampled data, the hyperparameters, including n_factors, epochs, and learning rate, were tuned. This was accomplished using a five-fold cross-validation approach to evaluate the performance of different parameter combinations.

8. **Integrate Large Dataset** Incorporated the larger dataset, representing 80% of the original data, to further fine-tune the hyperparameters, particularly focusing on optimizing 'n_factors' for the Funk SVD model.

9. **Latent Book Factors** Ran the Funk SVD model with the hyper-tuned parameters (best parameters: n_factors 20, epochs 20, learning rate 0.0075 and biased False) and extracted the latent factors of the books to perform a cosine similarity comparison for each book.

10. **First Recommender** Made a function to generate the initial book recommendations by utilizing the latent factors to identify the top 10 similar books for a given book.


### Future Steps
- Content-Based Filtering Model Building
- Hybrid Filtering Model Combining

