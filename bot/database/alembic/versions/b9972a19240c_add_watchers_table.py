"""Add watchers table

Revision ID: b9972a19240c
Revises: 
Create Date: 2024-06-08 19:31:31.687526

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b9972a19240c"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "watchers",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("message_id", sa.BigInteger(), nullable=False),
        sa.Column("channel_id", sa.BigInteger(), nullable=False),
        sa.Column("guild_id", sa.BigInteger(), nullable=False),
        sa.Column("refresh_interval_seconds", sa.Integer(), nullable=False),
        sa.Column("last_refresh_time", sa.DateTime(), nullable=True),
        sa.Column(
            "resource_type", sa.Enum("pods", name="resourcetype"), nullable=False
        ),
        sa.Column("namespace", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("watchers")
    # ### end Alembic commands ###
