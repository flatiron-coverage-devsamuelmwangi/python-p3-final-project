from db.models import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db/reviews.sqlite')
Session = sessionmaker(bind=engine)

def calculate_average_rating():
    session = Session()

    reviews = session.query(Review).all()
    total_rating = sum(review.star_rating for review in reviews)
    average_rating = total_rating / len(reviews)

    session.close()
    return average_rating