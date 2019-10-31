This is my first python app which is crowel youtube data

DB will be in the 'db/scripts', 'db/rollback' files, I used MySQL DB, and SQLALCHEMY for ORM

To getting videos data I used Beautifulsoap to fetch data with commen identifiers (I tried another sol but it doesn't work fine with me)

To update data periodically I needed to save data by anyway to not hit db a lot of times, so the way I know and it was easy to me is to save it in file system
but there is a bug while fetching data from file and I can't solve it, so because the deadline I worked with db to check data every time.

To periodically update data, I used schedulers to run every 1 hour (I tried a lot to apply cron, but the used way was the only that worked fine with me) 

Image thumbnail saved in images/ path 

note:
I don't know why Beautifulsoap doesn't fetch all videos on the page, I investigated and searched a lot of time to know why and how to solve it and I tried another ways 
but all thy way I tried give me the same result, and I can't fix it !!

 I didn't understand your point that the crawler should support two formats: (one for channel) and (another for playlist)
 I see that the two formats are the same, So I'm sorry if it's not right as you want
 
 