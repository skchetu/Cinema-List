from app import db

class FilmInfo(db.Model):

    __tablename__ = 'filminfo'

    film_id = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    director = db.Column(db.String, nullable=False)
    shanRating = db.Column(db.String, nullable=False)
    cheRating = db.Column(db.String, nullable=False)
    andhiRating = db.Column(db.String, nullable=False)
    avgRating = db.Column(db.String, nullable=False)

    def __init__(self, week, title, director, shanRating, cheRating, andhiRating, avgRating):
        self.week = week
        self.title = title
        self.director = director
        self.shanRating = shanRating
        self.cheRating = cheRating
        self.andhiRating = andhiRating
        self.avgRating = avgRating

    def __repr__(self):
        return f'\n{{' \
        '"week": "{self.week}"\n' \
        '}}'