import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from flask import jsonify
from pytube import YouTube

from app.db_configurations.db_connection import app
from app.models.videos import Video
from app.services.DBHandler import DBHandler
from app.services.YoutubHandlerService import request_data_from_youtube


@app.route('/')
def hello():
    return "Welcome to my youtube application :)"


@app.route('/channels')
def update_channel_data():
    url = 'https://www.youtube.com/user/AsapSCIENCE/videos'
    data = request_data_from_youtube(url)
    for i in range(len(data)):
        if DBHandler(data[i]['video_url']).get_video() is None:
            DBHandler(data[i]).persist_data()
        else:
            DBHandler(data[i]).update_video()

    return 'Videos saved/updated successfully !'


@app.route('/playlist')
def update_playlist_data():
    url = 'https://www.youtube.com/watch?v=ztiHRiFXtoc&list=PLvFsG9gYFxY_2tiOKgs7b2lSjMwR89ECb'
    data = request_data_from_youtube(url)
    for i in range(len(data)):
        if DBHandler(data[i]['video_url']).get_video() is None:
            DBHandler(data[i]).persist_data()
        else:
            DBHandler(data[i]).update_video()

    return 'Videos saved/updated successfully !'


@app.route('/get_videos')
def get_videos():
    data = Video.query.all()
    result = []
    for i in range(len(data)):
        result += [{
            'id': data[i].id,
            'title': data[i].title,
            'video_url': data[i].video_url,
            'duration': data[i].duration,
            'views': data[i].views,
            'img_url': data[i].img_url,
            'img_path': data[i].img_path
        }]
    return jsonify({'data': result})


# @app.route('/download')
# def download_video():
#     YouTube('https://www.youtube.com/watch?v=himEMfYQJ1w').streams.first().download()
#     return "download video"


scheduler = BackgroundScheduler()
scheduler.add_job(func=update_channel_data, trigger="interval", hours=1)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, use_reloader=False)
