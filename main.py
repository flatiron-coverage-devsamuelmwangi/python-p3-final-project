import click
from db.models import User, Product, Review
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from algorithms.algorithm import calculate_average_rating

engine = create_engine('sqlite:///db/reviews.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Enter your user name')
def add_user(name):

    user = User(name=name)
    session.add(user)
    session.commit()

    session.close()
    click.echo(f'Hi "{name}", welcome. Create a product for sale!')
    

@cli.command()
@click.option('--name', prompt='Enter the product name')
@click.option('--price', type=int, prompt='Enter the product price')
def add_product(name, price):

    product = Product(name=name, price=price)
    session.add(product)
    session.commit()

    session.close()
    click.echo(f'Product "{name}" added successfully!')


@cli.command()
@click.option('--rating', type=int, prompt='Enter the star rating')
@click.option('--comment', prompt='Enter the review comment')
def add_review(rating, comment):


    user = session.query(User).order_by(desc(User.id)).first()
    product = session.query(Product).order_by(desc(Product.id)).first()

    if not user or not product:
        session.close()
        click.echo('User or product does not exist.')
        return

    review = Review(star_rating=rating, comment=comment)
    user.reviews.append(review)
    product.reviews.append(review)

    session.add(review)
    session.commit()

    session.close()
    click.echo('Review added successfully!')


@cli.command()
def get_user_reviews():

    user = session.query(User).order_by(desc(User.id)).first()
    product = session.query(Product).order_by(desc(Product.id)).first()

    if not user:
        session.close()
        click.echo('User not found.')
        return

    reviews = user.reviews

    session.close()
    click.echo(f'Thanks for the review {user.name}:')
    for review in reviews:
        click.echo(f'Product: {product.name}, Star Rating: {review.star_rating}, Comment: {review.comment}')


@cli.command()
def average_rating():
    average = calculate_average_rating()
    click.echo(f'Average Products Rating: {average}')


if __name__ == '__main__':
    cli()