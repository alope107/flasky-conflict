"""new stuff

Revision ID: 02999f32f1a4
Revises: 4acae02715b9
Create Date: 2022-10-31 12:50:35.679688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02999f32f1a4'
down_revision = '4acae02715b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bike', sa.Column('new_stuff', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bike', 'new_stuff')
    # ### end Alembic commands ###
