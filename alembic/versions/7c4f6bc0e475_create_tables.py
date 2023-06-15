"""Create tables

Revision ID: 7c4f6bc0e475
Revises: 
Create Date: 2023-06-15 08:18:10.816098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c4f6bc0e475'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Upgrade function to create tables

    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String)
    )

    op.create_table(
        'products',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('price', sa.Integer)
    )

    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('star_rating', sa.Integer),
        sa.Column('comment', sa.String),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('product_id', sa.Integer, sa.ForeignKey('products.id'))
    )


def downgrade():
    # Downgrade function to drop tables

    op.drop_table('reviews')
    op.drop_table('products')
    op.drop_table('users')
