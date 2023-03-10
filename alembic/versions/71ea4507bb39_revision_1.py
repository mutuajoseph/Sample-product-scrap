"""revision 1

Revision ID: 71ea4507bb39
Revises: 
Create Date: 2023-01-26 08:22:45.030731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71ea4507bb39'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('public_id', sa.String(length=256), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=False),
    sa.Column('brand', sa.String(length=256), nullable=False),
    sa.Column('images_link', sa.String(length=256), nullable=False),
    sa.Column('upc', sa.String(length=256), nullable=False),
    sa.Column('department', sa.String(length=256), nullable=False),
    sa.Column('premium_brand', sa.Boolean(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('ratings_total', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('update', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_products_id'), table_name='products')
    op.drop_table('products')
    # ### end Alembic commands ###
