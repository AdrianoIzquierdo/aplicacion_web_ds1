"""Mensaje de migración

Revision ID: 7839cb348df4
Revises: 2b7007ea2117
Create Date: 2024-08-09 11:01:41.726574

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7839cb348df4'
down_revision = '2b7007ea2117'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_index('ix_product_name')

    op.drop_table('product')
    with op.batch_alter_table('expense', schema=None) as batch_op:
        batch_op.drop_index('ix_expense_timestamp')

    op.drop_table('expense')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index('ix_user_email')
        batch_op.drop_index('ix_user_username')

    op.drop_table('user')
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_index('ix_order_timestamp')

    op.drop_table('order')
    op.drop_table('order_item')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order_item',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('quantity', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], name='order_item_order_id_fkey'),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name='order_item_product_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='order_item_pkey')
    )
    op.create_table('order',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('table_number', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='order_pkey')
    )
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.create_index('ix_order_timestamp', ['timestamp'], unique=False)

    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('is_admin', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('table_number', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index('ix_user_username', ['username'], unique=True)
        batch_op.create_index('ix_user_email', ['email'], unique=True)

    op.create_table('expense',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('description', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('amount', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='expense_pkey')
    )
    with op.batch_alter_table('expense', schema=None) as batch_op:
        batch_op.create_index('ix_expense_timestamp', ['timestamp'], unique=False)

    op.create_table('product',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('price', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('stock', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='product_pkey')
    )
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.create_index('ix_product_name', ['name'], unique=True)

    # ### end Alembic commands ###
