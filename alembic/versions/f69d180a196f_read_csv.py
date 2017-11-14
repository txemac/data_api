"""Read CSV

Revision ID: f69d180a196f
Revises: c2e5e95cf811
Create Date: 2017-11-14 21:29:28.302742

"""
import os

from alembic import op

# revision identifiers, used by Alembic.

revision = 'f69d180a196f'
down_revision = 'c2e5e95cf811'
branch_labels = None
depends_on = None


def upgrade():
    path = os.path.join(os.path.abspath(os.getcwd()), 'products.csv')

    op.execute("COPY product FROM '{path}' WITH CSV HEADER;".format(path=path), execution_options=None,)


def downgrade():
    pg_connection = op.get_bind()
    pg_connection.execute("""DELETE FROM product CASCADE;""")
