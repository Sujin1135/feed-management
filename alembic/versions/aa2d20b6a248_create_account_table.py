"""create account table

Revision ID: aa2d20b6a248
Revises: 
Create Date: 2022-07-12 02:15:03.610983

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa2d20b6a248'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "feeds",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("nickname", sa.String(50), nullable=False),
        sa.Column("password", sa.String(60), nullable=False),
        sa.Column("title", sa.String(10), nullable=False),
        sa.Column("text", sa.Text, nullable=False),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.current_timestamp()),
        sa.Column(
            "updated_at",
            sa.DateTime,
            server_default=sa.func.current_timestamp(),
            onupdate=sa.func.now(),
        ),
    )

    op.create_index(op.f('index_feeds_nickname'), 'feeds', ['nickname'], unique=False)


def downgrade() -> None:
    op.drop_table("feeds")
