# Book Recommender

This repository contains the code and documentation for a book recommender system part of capstone project for BrainStation


## Overview

In today's world, with an ever-increasing number of books being published, discovering books that genuinely align with one's interests has become challenging. As an avid reader, I've personally grappled with this issue. The abundance of available books and vague categorizations often makes finding an enjoyable read a truly frustrating experience.

Therefore, this project aims to address this issue by creating an intelligent book recommendation system. Its primary goal is to seamlessly connect readers with books they are highly likely to relish, easing the burden of sifting through the overwhelming sea of available options.

A reliable book recommender has the potential to increase readers' consumption rate significantly. It can be a game-changer, reducing the time spent hunting for new books and ensuring they discover more engaging and enjoyable reads. Moreover, it's not just readers who stand to benefit from this innovation. Businesses have a vested interest in this as well, as it can enhance the shopping frequency of their customers, ultimately leading to higher sales and fostering customer loyalty.

To achieve this, the project leverages the power of machine learning. The book recommender system will employ a variety of approaches, including content-based, collaborative filtering, or hybrid methods. This includes exploring algorithms like K-Nearest Neighbors (K-NN) and Singular Value Decomposition, which will be instrumental in identifying similar users and predicting user ratings for book recommendations.

## Dataset

For this project will be working with the data [GoodBooks-10K](https://github.com/zygmuntz/goodbooks-10k) which contains four indidual files that will be utilized to build the book recommender system.

#### books.csv: A dataset with 10,000 unique books from Goodreads.

| Column     | Type    | Description    |
|-------------------|-------------------|-------------------|
| book_id   | int64  | Unique ID for each book  |
| authors	   | object  | the name of all authors of the book |
| original_publication_year   | float64  | the   |
| title   | object | Example Value 4  |
| work_ratings_count   | int64  | Example Value 4  |
| average_rating   | float64  | Example Value 4  |



#### ratings.csv: Contains 5.97 million user ratings for the books.

| Column     | Type    | Description    |
|-------------------|-------------------|-------------------|
| user_id   | int64  | Unique ID for each user  |
| book_id	   | int64  | Unique ID for each book |
| rating   | int64  | Rating from 1 to 5  |


#### book_tags.csv: Provides information on how often users have applied specific tags to books.

| Column     | Type    | Description    |
|-------------------|-------------------|-------------------|
| goodreads_book_id  | int64  | Unique ID for each book from the GoodReads Website |
| tag_id  | int64 | Unique ID for each tag  |
| count   | int64  | The number of users that have assigned the tag  |

#### tags.csv: Includes various user-generated tags that can be associated with books.

| Column     | Type    | Description    |
|-------------------|-------------------|-------------------|
| tag_id   | int64  | Unique ID for each tag   |
| tag_name  | object  | Name of the tag  |
