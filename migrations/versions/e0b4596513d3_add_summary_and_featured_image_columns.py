"""add summary and featured_image columns

Revision ID: e0b4596513d3
Revises: 
Create Date: 2025-12-29 09:34:53.342568

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0b4596513d3'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    
    if not inspector.has_table('posts'):
        op.create_table(
            'posts',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('title', sa.String(), nullable=True),
            sa.Column('content', sa.Text(), nullable=True),
            sa.Column('created_at', sa.DateTime(), nullable=True),
            sa.PrimaryKeyConstraint('id')
        )
        op.create_index('ix_posts_id', 'posts', ['id'], unique=False)
        op.create_index('ix_posts_title', 'posts', ['title'], unique=False)
    
    columns = [c['name'] for c in inspector.get_columns('posts')]
    
    if 'summary' not in columns:
        op.add_column('posts', sa.Column('summary', sa.String(), nullable=True))
    if 'featured_image' not in columns:
        op.add_column('posts', sa.Column('featured_image', sa.String(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    columns = [c['name'] for c in inspector.get_columns('posts')]

    if 'featured_image' in columns:
        op.drop_column('posts', 'featured_image')
    if 'summary' in columns:
        op.drop_column('posts', 'summary')
