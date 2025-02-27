"""Ajout colonne token à users

Revision ID: 8397d2795482
Revises: 27f7d6129b28
Create Date: 2025-02-20 21:40:02.773870

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8397d2795482'
down_revision: Union[str, None] = '27f7d6129b28'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('token', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'token')
    # ### end Alembic commands ###
