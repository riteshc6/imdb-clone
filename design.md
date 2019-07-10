# Design Document for IMDB App

#### User Story
1) As a User <br>
    I want to be able to <br>
    * Register and login
    * Add Movies with image and other details
    * Edit Movies Uploaded by me
    * see a list of all Movies and there ratings on IMDB when I login
    * Add review and rate a Movie

2) As an Administrator <br>
    I want to be able to<br>
    * Delete Spam posts by users
    * delete a movie uploaded by users

#### MVP
1) User Registration/ Login
2) Administrator can add and delete movies 
3) User can review and rate movies
4) User can edit reviews
5) User can delete his review

#### URL Design
    * `/` or `/index` : Home Page(Displays list of movies)
    * `/login` : Login page(Displayed when user is not looged in)
    * `/register` : Resgistration Page
    * `/movies/upload/` : Upload Movie form
    * `/movies/<movie_id>` : Movie Detail Page and a form to review movie or edit if already reviewed
    * `/movies/<movie_id>/edit` : Edit movie details of the movies added by user     
    * `/movies/<movie_id>/review` : Post Url for submitting review


#### Forms
    * Movie Upload form : {
            "title" : "Title to be provided by the creator"
            "Stars" : "Actor/Actress of movie"
            "Director" : "Movie Director"
            "description" : "Description of video in 140 words"
            "image" : "Upload movie poster"
        }
        After upload redirect to cerator's profile page
    *  Register Form : {
            "Username" : "",
            "E-mail" : "",
            "password" : "",
            "confirm password" : ""
        }
    * Login Form : {
            "Username" : "",
            "Password" : ""
        }    

####    Authentication
    * Any registered user can see reviews of Movies
    * Any registered user can upload Movies and review other movies

#### Database Schema Design
    * User : { "id" : primary key, integer, autoincrement;
                "Username" : String;
                "email_id": string;
                "password": string;
                "comments" : db.realationship('Comment', backref="user", lazy="dynamic")
        }
    * Movie : { "id" : primary key, integer, autoincrement;
                 "title" : String;
                 "stars" : String;
                 "director" : String;
                 "movie_description" : String;
                 "image_path": <directory/image_id>;  # No need of path video will be saved using id value
                 "timestamp": "timestamp"
                 "user_id": integer, ForeignKey(user.id)
            }
    * Review : {"id" : primary key, integer, autoincrement;
                "body": String;
                "rating": integer(1-10)
                "timestamp":timestamp;
                "user_id" : integer, ForeignKey(user.id)
                "movie_id" : integer, ForeignKey(movie.id)
        }        





