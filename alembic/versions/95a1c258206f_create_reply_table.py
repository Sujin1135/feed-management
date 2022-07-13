"""create reply table

Revision ID: 95a1c258206f
Revises: aa2d20b6a248
Create Date: 2022-07-13 18:41:37.393078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95a1c258206f'
down_revision = 'aa2d20b6a248'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "replies",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("feed_id", sa.Integer, nullable=False),
        sa.Column("parent_id", sa.Integer, nullable=True),
        sa.Column("depth", sa.Integer, default=0),
        sa.Column("nickname", sa.String(50), nullable=False),
        sa.Column("comment", sa.String(255), nullable=False),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.current_timestamp()),
        sa.Column(
            "updated_at",
            sa.DateTime,
            server_default=sa.func.current_timestamp(),
            onupdate=sa.func.now(),
        ),
        sa.Column("deleted_at", sa.DateTime),
    )

    op.create_index(op.f('index_replies_nickname'), 'replies', ['nickname'], unique=False)
    op.create_index(op.f('index_replies_feed_id'), 'replies', ['feed_id'], unique=False)


def downgrade() -> None:
    op.drop_table("feeds")
