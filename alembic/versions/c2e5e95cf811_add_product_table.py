"""Add product table

Revision ID: c2e5e95cf811
Revises: 2dbdaa71bedb
Create Date: 2017-11-14 19:32:47.678640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2e5e95cf811'
down_revision = '2dbdaa71bedb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'product',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('gender_names', sa.Text()),
        sa.Column('category_names', sa.Text()),
        sa.Column('currency', sa.Text()),
        sa.Column('size_infos', sa.Text()),
        sa.Column('country_code', sa.Text()),
        sa.Column('title', sa.Text()),
        sa.Column('base_sku', sa.Text()),
        sa.Column('current_price_value', sa.Float(), nullable=False),
        sa.Column('timestamp', sa.DateTime(timezone=True), nullable=False, server_default=sa.text(u'now()')),
        sa.Column('brand', sa.Text()),
        sa.Column('image_urls', sa.Text()),
        sa.Column('description_text', sa.Text()),
        sa.Column('original_price_value', sa.Float(), nullable=False),
        sa.Column('url', sa.Text(), nullable=False),
        sa.Column('color_name', sa.Text()),
        sa.Column('identifier', sa.Text()),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('product')
