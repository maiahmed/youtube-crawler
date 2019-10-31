from flask_sqlalchemy import SQLAlchemy
from app.db_configurations.db_connection import app

db = SQLAlchemy(app)


class Video(db.Model):

    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True)
    video_url = db.Column(db.String(64))
    title = db.Column(db.String(64))
    duration = db.Column(db.String(64))
    views = db.Column(db.String(64))
    img_path = db.Column(db.Text)
    img_url = db.Column(db.Text)

    def __init__(self, video_url, title, duration, views, img_path, img_url):
        self.video_url = video_url
        self.title = title
        self.duration = duration
        self.views = views
        self.img_path = img_path
        self.img_url = img_url
