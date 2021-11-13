# youtube_api

## Steps to work on this repo:-
 1. Clone this repoistory 
 2. Install python 3 in ur system 
 3. pip3 install Django 
 4. create a virtualenv 
    1.  by using the command virtualenv {name}
    2.  source {name}/bin/activate
 5. pip3 install requirement.txt
 6. Now move the setting.py file inside the youtube directory and change the api keys 
 7. You have to get your api keys from the google youtube api keys v3 api
 8. python3 manage.py makemigrations
 9. python3 manage.py migrate
 10. python3 manage.py crontab add
 11. Now start the server
    1. python3 manage.py runserver
 
## How to use the api
1. visit the url => http://127.0.0.1:8000/
2. Now the call to the api will be taking place after every minute in the background 
3. So we can refresh the url or visit the url => http://127.0.0.1:8000/get/ after minute to see the new feteched videos.
4. We can also call the api by our selves by visting the url=> http://127.0.0.1:8000/refresh and then we can go back to the url=>  http://127.0.0.1:8000/ to see the latest fetched videos. 
5. Also we can switch between the different pages by clicking on the respective page no.
6. There is one filter button available on the top and after clicking that we have fews options available like we can enter the channel title and can filter out all the content according to that.
7. Also we can search the videos by their title and description search.


## How can we change the code 
1. We can customize the video feed list by changing the query inside the get_feed.py file that is present inside the api folder and there we can change the q={string} 
