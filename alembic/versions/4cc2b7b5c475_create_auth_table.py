"""create auth table

Revision ID: 4cc2b7b5c475
Revises: 05be1a42c051
Create Date: 2024-11-01 23:38:38.758267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cc2b7b5c475'
down_revision = '05be1a42c051'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'auth',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('username', sa.String, unique=True, nullable=False),
        sa.Column('password', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now())
    )


def downgrade() -> None:
    pass
