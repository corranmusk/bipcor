"""Log table

Revision ID: e4abb9581242
Revises: f21a3cc46a1e
Create Date: 2019-12-04 14:09:44.843958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4abb9581242'
down_revision = 'f21a3cc46a1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('log_entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('logtime', sa.DateTime(), nullable=True),
    sa.Column('loglevel', sa.String(length=8), nullable=True),
    sa.Column('detail', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('log_entry')
    # ### end Alembic commands ###