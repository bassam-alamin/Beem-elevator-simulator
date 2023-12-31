"""add description field

Revision ID: ef95baab8e8c
Revises: 7fb0213bbeb9
Create Date: 2023-08-21 00:17:30.603708

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ef95baab8e8c'
down_revision: Union[str, None] = '7fb0213bbeb9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('elevator_logs', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('elevator_logs', 'description')
    # ### end Alembic commands ###
