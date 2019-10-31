from app.models.videos import Video

from app.models.videos import db


class DBHandler:

    def __init__(self, items):
        self.items = items

    def persist_data(self):
        video_record = Video(
            video_url=self.items['video_url'],
            title=self.items['title'],
            duration=self.items['duration'],
            views=self.items['views'],
            img_path=self.items['img_path'],
            img_url=self.items['img_url']
            )
        db.session.add(video_record)
        db.session.commit()
        db.session.close()

    def get_video(self):
        result = db.session.query(Video).filter(Video.video_url == self.items).first()
        return result

    def update_video(self):
        result = db.session.query(Video).filter(Video.id is self.items['video_url']).update({
            Video.title: self.items['title'],
            Video.duration: self.items['duration'],
            Video.views: self.items['views'],
            Video.img_url: self.items['img_url'],
            Video.img_path: self.items['img_path'],
        }, synchronize_session=False)
        return result
