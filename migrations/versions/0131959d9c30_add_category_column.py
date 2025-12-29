"""add category column

Revision ID: 0131959d9c30
Revises: e0b4596513d3
Create Date: 2025-12-29 09:40:29.367932

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0131959d9c30'
down_revision: Union[str, Sequence[str], None] = 'e0b4596513d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    columns = [c['name'] for c in inspector.get_columns('posts')]
    
    if 'category' not in columns:
        op.add_column('posts', sa.Column('category', sa.String(), nullable=True, server_default='Journal'))

def downgrade() -> None:
    """Downgrade schema."""
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    columns = [c['name'] for c in inspector.get_columns('posts')]

    if 'category' in columns:
        op.drop_column('posts', 'category')
