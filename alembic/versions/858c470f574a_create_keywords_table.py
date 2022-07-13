"""create keywords table

Revision ID: 858c470f574a
Revises: 95a1c258206f
Create Date: 2022-07-13 21:16:43.108524

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '858c470f574a'
down_revision = '95a1c258206f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "keywords",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("nickname", sa.String(50), nullable=False),
        sa.Column("keyword", sa.String(50), nullable=True),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.current_timestamp()),
        sa.Column(
            "updated_at",
            sa.DateTime,
            server_default=sa.func.current_timestamp(),
            onupdate=sa.func.now(),
        ),
        sa.Column("deleted_at", sa.DateTime),
    )

    op.create_index(op.f('index_keywords_nickname'), 'keywords', ['nickname'], unique=False)


def downgrade() -> None:
    op.drop_table("keywords")
