"""Initial migration

Revision ID: 21435918a37a
Revises: 
Create Date: 2025-01-09 16:36:49.627761

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '21435918a37a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_customers_id'), 'customers', ['id'], unique=False)
    op.create_index(op.f('ix_customers_phone_number'), 'customers', ['phone_number'], unique=True)
    op.add_column('users', sa.Column('first_name', sa.String(length=50), nullable=False))
    op.add_column('users', sa.Column('second_name', sa.String(length=50), nullable=False))
    op.add_column('users', sa.Column('id_number', sa.String(), nullable=False))
    op.add_column('users', sa.Column('pin', sa.String(length=4), nullable=False))
    op.add_column('users', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('is_staff', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('is_superuser', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('created_at', sa.String(), nullable=True))
    op.add_column('users', sa.Column('updated_at', sa.String(), nullable=True))
    op.drop_index('ix_users_email', table_name='users')
    op.drop_index('ix_users_username', table_name='users')
    op.create_index(op.f('ix_users_id_number'), 'users', ['id_number'], unique=True)
    op.drop_column('users', 'username')
    op.drop_column('users', 'email')
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_users_id_number'), table_name='users')
    op.create_index('ix_users_username', 'users', ['username'], unique=True)
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'created_at')
    op.drop_column('users', 'is_superuser')
    op.drop_column('users', 'is_staff')
    op.drop_column('users', 'is_active')
    op.drop_column('users', 'pin')
    op.drop_column('users', 'id_number')
    op.drop_column('users', 'second_name')
    op.drop_column('users', 'first_name')
    op.drop_index(op.f('ix_customers_phone_number'), table_name='customers')
    op.drop_index(op.f('ix_customers_id'), table_name='customers')
    op.drop_table('customers')
    # ### end Alembic commands ###
