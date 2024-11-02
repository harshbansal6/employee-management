"""create employee model

Revision ID: 05be1a42c051
Revises: 
Create Date: 2024-11-01 22:52:34.420591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05be1a42c051'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'employees',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, unique=True, nullable=False),
        sa.Column('department', sa.String, nullable=True),
        sa.Column('role', sa.String, nullable=True),
        sa.Column('date_joined', sa.Date, server_default=sa.func.now()),
    )


def downgrade() -> None:
    pass
