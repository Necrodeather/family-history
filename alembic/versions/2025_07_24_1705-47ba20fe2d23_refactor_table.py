"""refactor table

Revision ID: 47ba20fe2d23
Revises: 2cba25e79c25
Create Date: 2025-07-24 17:05:30.519157

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '47ba20fe2d23'
down_revision: Union[str, None] = '2cba25e79c25'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table('expenses_categories', 'expenses_category')
    op.rename_table('incomes_categories', 'incomes_category')
    op.rename_table('users', 'user')
    op.rename_table('incomes', 'income')

    op.drop_constraint(
        'fk_expenses_categories_user_id_users',
        'expenses_category',
        type_='foreignkey',
    )
    op.drop_constraint(
        'fk_expenses_categories_updated_user_id_users',
        'expenses_category',
        type_='foreignkey',
    )
    op.create_foreign_key(
        'fk_expenses_category_user_id_users',
        'expenses_category',
        'user',
        ['user_id'],
        ['id'],
    )
    op.create_foreign_key(
        'fk_expenses_category_updated_user_id_users',
        'expenses_category',
        'user',
        ['updated_user_id'],
        ['id'],
    )

    op.drop_constraint(
        'fk_incomes_categories_user_id_users',
        'incomes_category',
        type_='foreignkey',
    )
    op.drop_constraint(
        'fk_incomes_categories_updated_user_id_users',
        'incomes_category',
        type_='foreignkey',
    )
    op.create_foreign_key(
        'fk_incomes_category_user_id_users',
        'incomes_category',
        'user',
        ['user_id'],
        ['id'],
    )
    op.create_foreign_key(
        'fk_incomes_category_updated_user_id_users',
        'incomes_category',
        'user',
        ['updated_user_id'],
        ['id'],
    )

    op.drop_constraint(
        'fk_expenses_category_id_expenses_categories',
        'expenses',
        type_='foreignkey',
    )
    op.drop_constraint(
        'fk_expenses_user_id_users',
        'expenses',
        type_='foreignkey',
    )
    op.drop_constraint(
        'fk_expenses_updated_user_id_users',
        'expenses',
        type_='foreignkey',
    )
    op.create_foreign_key(
        'fk_expenses_category_id_expenses_category',
        'expenses',
        'expenses_category',
        ['category_id'],
        ['id'],
    )
    op.create_foreign_key(
        'fk_expenses_user_id_users',
        'expenses',
        'user',
        ['user_id'],
        ['id'],
    )
    op.create_foreign_key(
        'fk_expenses_updated_user_id_users',
        'expenses',
        'user',
        ['updated_user_id'],
        ['id'],
    )

    op.drop_constraint(
        'fk_incomes_category_id_incomes_categories',
        'income',
        type_='foreignkey',
    )
    op.drop_constraint(
        'fk_incomes_updated_user_id_users',
        'income',
        type_='foreignkey',
    )
    op.drop_constraint(
        'fk_incomes_user_id_users',
        'income',
        type_='foreignkey',
    )
    op.create_foreign_key(
        'fk_incomes_category_id_incomes_category',
        'income',
        'incomes_category',
        ['category_id'],
        ['id'],
    )
    op.create_foreign_key(
        'fk_incomes_user_id_users',
        'income',
        'user',
        ['user_id'],
        ['id'],
    )
    op.create_foreign_key(
        'fk_incomes_updated_user_id_users',
        'income',
        'user',
        ['updated_user_id'],
        ['id'],
    )


def downgrade() -> None:
    op.rename_table('expenses_category', 'expenses_categories')
    op.rename_table('incomes_category', 'incomes_categories')
    op.rename_table('user', 'users')
    op.rename_table('income', 'incomes')

    op.drop_constraint(
        'fk_expenses_category_user_id_users',
        'expenses_categories',
        type_='foreignkey',
    )
    op.drop_constraint(
        'fk_expenses_category_updated_user_id_users',
        'expenses_categories',
        type_='foreignkey',
    )
    op.create_foreign_key(
        'fk_expenses_categories_user_id_users',
        'expenses_categories',
        'users',
        ['user_id'],
        ['id'],
    )
    op.create_foreign_key(
        'fk_expenses_categories_updated_user_id_users',
        'expenses_categories',
        'users',
        ['updated_user_id'],
        ['id'],
    )

    op.drop_constraint(
        'fk_incomes_category_user_id_users',
        'incomes_categories',
        type_='foreignkey',
    )
    op.drop_constraint(
        'fk_incomes_category_updated_user_id_users',
        'incomes_categories',
        type_='foreignkey',
    )
    op.create_foreign_key(
        'fk_incomes_categories_user_id_users',
        'incomes_categories',
        'users',
        ['user_id'],
        ['id'],
    )
    op.create_foreign_key(
        'fk_incomes_categories_updated_user_id_users',
        'incomes_categories',
        'users',
        ['updated_user_id'],
        ['id'],
    )

    op.drop_constraint(
        'fk_expenses_category_id_expenses_category',
        'expenses',
        type_='foreignkey',
    )
    op.drop_constraint(
        'fk_expenses_user_id_users',
        'expenses',
        type_='foreignkey',
    )
    op.drop_constraint(
        'fk_expenses_updated_user_id_users',
        'expenses',
        type_='foreignkey',
    )
    op.create_foreign_key(
        'fk_expenses_category_id_expenses_categories',
        'expenses',
        'expenses_categories',
        ['category_id'],
        ['id'],
    )
    op.create_foreign_key(
        'fk_expenses_user_id_users',
        'expenses',
        'users',
        ['user_id'],
        ['id'],
    )
    op.create_foreign_key(
        'fk_expenses_updated_user_id_users',
        'expenses',
        'users',
        ['updated_user_id'],
        ['id'],
    )

    op.drop_constraint(
        'fk_incomes_category_id_incomes_category',
        'incomes',
        type_='foreignkey',
    )
    op.drop_constraint(
        'fk_incomes_updated_user_id_users',
        'incomes',
        type_='foreignkey',
    )
    op.drop_constraint(
        'fk_incomes_user_id_users',
        'incomes',
        type_='foreignkey',
    )
    op.create_foreign_key(
        'fk_incomes_category_id_incomes_categories',
        'incomes',
        'incomes_categories',
        ['category_id'],
        ['id'],
    )
    op.create_foreign_key(
        'fk_incomes_user_id_users',
        'incomes',
        'users',
        ['user_id'],
        ['id'],
    )
    op.create_foreign_key(
        'fk_incomes_updated_user_id_users',
        'incomes',
        'users',
        ['updated_user_id'],
        ['id'],
    )
