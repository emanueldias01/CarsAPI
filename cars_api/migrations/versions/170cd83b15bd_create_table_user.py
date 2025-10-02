"""create table user

Revision ID: 170cd83b15bd
Revises: 9883b795462a
Create Date: 2025-10-02 08:30:58.036292

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '170cd83b15bd'
down_revision: Union[str, Sequence[str], None] = '9883b795462a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
