"""empty message

Revision ID: 27aa2bd278f6
Revises: 71f77e6de04f
Create Date: 2023-10-06 14:38:50.290696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27aa2bd278f6'
down_revision = '71f77e6de04f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    with op.batch_alter_table('maps', schema=None) as batch_op:
        batch_op.add_column(sa.Column('start_time', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('end_time', sa.DateTime(), nullable=True))

    with op.batch_alter_table('pathes', schema=None) as batch_op:
        batch_op.alter_column('latitude',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=15),
               existing_nullable=False)
        batch_op.alter_column('longitude',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=15),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pathes', schema=None) as batch_op:
        batch_op.alter_column('longitude',
               existing_type=sa.Float(precision=15),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.alter_column('latitude',
               existing_type=sa.Float(precision=15),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('maps', schema=None) as batch_op:
        batch_op.drop_column('end_time')
        batch_op.drop_column('start_time')

    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###
