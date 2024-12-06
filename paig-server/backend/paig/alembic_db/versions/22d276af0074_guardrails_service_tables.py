"""guardrails_service_tables

Revision ID: 22d276af0074
Revises: 5e805b526efa
Create Date: 2024-10-21 14:14:06.374881

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import core.db_models.utils


# revision identifiers, used by Alembic.
revision: str = '22d276af0074'
down_revision: Union[str, None] = 'a95b604c47fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('guardrail',
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=4000), nullable=True),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.Column('enabled_providers', core.db_models.utils.CommaSeparatedList(length=255), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=False),
    sa.Column('update_time', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_guardrail_create_time'), 'guardrail', ['create_time'], unique=False)
    op.create_index(op.f('ix_guardrail_id'), 'guardrail', ['id'], unique=False)
    op.create_index(op.f('ix_guardrail_update_time'), 'guardrail', ['update_time'], unique=False)
    op.create_table('guardrail_connection',
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=4000), nullable=True),
    sa.Column('guardrail_provider', sa.Enum('AWS', 'PAIG', 'LLAMA', 'OPENAI', 'MULTIPLE', name='guardrailprovider'), nullable=False),
    sa.Column('connection_details', sa.JSON(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=False),
    sa.Column('update_time', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_guardrail_connection_create_time'), 'guardrail_connection', ['create_time'], unique=False)
    op.create_index(op.f('ix_guardrail_connection_id'), 'guardrail_connection', ['id'], unique=False)
    op.create_index(op.f('ix_guardrail_connection_update_time'), 'guardrail_connection', ['update_time'], unique=False)
    op.create_table('guardrail_application',
    sa.Column('guardrail_id', sa.Integer(), nullable=False),
    sa.Column('application_id', sa.Integer(), nullable=True),
    sa.Column('application_name', sa.String(length=255), nullable=True),
    sa.Column('application_key', sa.String(length=255), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=False),
    sa.Column('update_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['guardrail_id'], ['guardrail.id'], name='fk_guardrail_application_guardrail_id', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_guardrail_application_create_time'), 'guardrail_application', ['create_time'], unique=False)
    op.create_index(op.f('ix_guardrail_application_id'), 'guardrail_application', ['id'], unique=False)
    op.create_index(op.f('ix_guardrail_application_application_key'), 'guardrail_application', ['application_key'], unique=False)
    op.create_index(op.f('ix_guardrail_application_update_time'), 'guardrail_application', ['update_time'], unique=False)
    op.create_table('guardrail_config',
    sa.Column('guardrail_id', sa.Integer(), nullable=False),
    sa.Column('guardrail_provider', sa.Enum('AWS', 'PAIG', 'LLAMA', 'OPENAI', 'MULTIPLE', name='guardrailprovider'), nullable=False),
    sa.Column('config_type', sa.Enum('CONTENT_MODERATION', 'SENSITIVE_DATA', 'OFF_TOPIC', 'DENIED_TERMS', 'PROMPT_SAFETY', name='guardrailconfigtype'), nullable=False),
    sa.Column('config_data', sa.JSON(), nullable=False),
    sa.Column('response_message', sa.String(length=4000), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=False),
    sa.Column('update_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['guardrail_id'], ['guardrail.id'], name='fk_guardrail_config_guardrail_id', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_guardrail_config_create_time'), 'guardrail_config', ['create_time'], unique=False)
    op.create_index(op.f('ix_guardrail_config_id'), 'guardrail_config', ['id'], unique=False)
    op.create_index(op.f('ix_guardrail_config_update_time'), 'guardrail_config', ['update_time'], unique=False)
    op.create_table('guardrail_provider_response',
    sa.Column('guardrail_id', sa.Integer(), nullable=False),
    sa.Column('guardrail_provider', sa.Enum('AWS', 'PAIG', 'LLAMA', 'OPENAI', 'MULTIPLE', name='guardrailprovider'), nullable=False),
    sa.Column('response_data', sa.JSON(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=False),
    sa.Column('update_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['guardrail_id'], ['guardrail.id'], name='fk_guardrail_provider_response_guardrail_id', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_guardrail_provider_response_create_time'), 'guardrail_provider_response', ['create_time'], unique=False)
    op.create_index(op.f('ix_guardrail_provider_response_id'), 'guardrail_provider_response', ['id'], unique=False)
    op.create_index(op.f('ix_guardrail_provider_response_update_time'), 'guardrail_provider_response', ['update_time'], unique=False)
    op.create_table('guardrail_application_version',
    sa.Column('application_key', sa.String(length=255), nullable=False),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=False),
    sa.Column('update_time', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_guardrail_application_version_application_key'), 'guardrail_application_version', ['application_key'], unique=False)
    op.create_index(op.f('ix_guardrail_application_version_create_time'), 'guardrail_application_version', ['create_time'], unique=False)
    op.create_index(op.f('ix_guardrail_application_version_id'), 'guardrail_application_version', ['id'], unique=False)
    op.create_index(op.f('ix_guardrail_application_version_update_time'), 'guardrail_application_version', ['update_time'], unique=False)
    op.create_table('guardrail_connection_mapping',
    sa.Column('guardrail_id', sa.Integer(), nullable=False),
    sa.Column('gr_connection_id', sa.Integer(), nullable=False),
    sa.Column('guardrail_provider', sa.Enum('AWS', 'PAIG', 'LLAMA', 'OPENAI', 'MULTIPLE', name='guardrailprovider'), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=False),
    sa.Column('update_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['gr_connection_id'], ['guardrail_connection.id'],
    name='fk_guardrail_connection_mapping_gr_connection_id'),
    sa.ForeignKeyConstraint(['guardrail_id'], ['guardrail.id'],
    name='fk_guardrail_connection_mapping_guardrail_id', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_guardrail_connection_mapping_create_time'), 'guardrail_connection_mapping',
                    ['create_time'], unique=False)
    op.create_index(op.f('ix_guardrail_connection_mapping_id'), 'guardrail_connection_mapping', ['id'], unique=False)
    op.create_index(op.f('ix_guardrail_connection_mapping_update_time'), 'guardrail_connection_mapping',
                    ['update_time'], unique=False)

    # ### Create view for guardrail by joining guardrail, guardrail_connection, guardrail_application, guardrail_config and guardrail_provider_response
    connection = op.get_bind()
    connection.execute(
        sa.text("""
            CREATE VIEW paig_guardrail_view AS
                SELECT
                    gr.status,
                    gr.create_time,
                    gr.update_time,
                    gr.name,
                    gr.description,
                    gr.version,
                    gr_conf.id,
                    gr_conf.guardrail_id,
                    gr_conf.guardrail_provider,
                    gr_conf.config_type,
                    gr_conf.config_data,
                    gr_conf.response_message,
                    GROUP_CONCAT(DISTINCT gr_app.application_key) AS application_keys
                FROM
                    guardrail gr
                        LEFT JOIN guardrail_config gr_conf            ON gr.id = gr_conf.guardrail_id
                        LEFT JOIN guardrail_application gr_app        ON gr.id = gr_app.guardrail_id
                GROUP BY
                    gr_conf.id;
        """))

    connection.execute(
        sa.text("""
            CREATE VIEW paig_guardrail_connection_view AS
                SELECT
                    gr_conn_map.guardrail_id,
                    gr_conn.status,
                    gr_conn.create_time,
                    gr_conn.update_time,
                    gr_conn.name,
                    gr_conn.description,
                    gr_conn.guardrail_provider,
                    gr_conn.connection_details,
                    gr_conn.id
                FROM
                    guardrail_connection gr_conn
                        LEFT JOIN guardrail_connection_mapping gr_conn_map ON gr_conn.id = gr_conn_map.gr_connection_id;
        """))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("DROP VIEW IF EXISTS paig_guardrail_connection_view;")
    op.execute("DROP VIEW IF EXISTS paig_guardrail_view;")
    op.drop_index(op.f('ix_guardrail_connection_mapping_update_time'), table_name='guardrail_connection_mapping')
    op.drop_index(op.f('ix_guardrail_connection_mapping_id'), table_name='guardrail_connection_mapping')
    op.drop_index(op.f('ix_guardrail_connection_mapping_create_time'), table_name='guardrail_connection_mapping')
    op.drop_table('guardrail_connection_mapping')
    op.drop_index(op.f('ix_guardrail_application_version_update_time'), table_name='guardrail_application_version')
    op.drop_index(op.f('ix_guardrail_application_version_id'), table_name='guardrail_application_version')
    op.drop_index(op.f('ix_guardrail_application_version_create_time'), table_name='guardrail_application_version')
    op.drop_index(op.f('ix_guardrail_application_version_application_key'), table_name='guardrail_application_version')
    op.drop_table('guardrail_application_version')
    op.drop_index(op.f('ix_guardrail_provider_response_update_time'), table_name='guardrail_provider_response')
    op.drop_index(op.f('ix_guardrail_provider_response_id'), table_name='guardrail_provider_response')
    op.drop_index(op.f('ix_guardrail_provider_response_create_time'), table_name='guardrail_provider_response')
    op.drop_table('guardrail_provider_response')
    op.drop_index(op.f('ix_guardrail_config_update_time'), table_name='guardrail_config')
    op.drop_index(op.f('ix_guardrail_config_id'), table_name='guardrail_config')
    op.drop_index(op.f('ix_guardrail_config_create_time'), table_name='guardrail_config')
    op.drop_table('guardrail_config')
    op.drop_index(op.f('ix_guardrail_application_update_time'), table_name='guardrail_application')
    op.drop_index(op.f('ix_guardrail_application_id'), table_name='guardrail_application')
    op.drop_index(op.f('ix_guardrail_application_application_key'), table_name='guardrail_application')
    op.drop_index(op.f('ix_guardrail_application_create_time'), table_name='guardrail_application')
    op.drop_table('guardrail_application')
    op.drop_index(op.f('ix_paig_guardrail_view_update_time'), table_name='paig_guardrail_view')
    op.drop_index(op.f('ix_paig_guardrail_view_id'), table_name='paig_guardrail_view')
    op.drop_index(op.f('ix_paig_guardrail_view_create_time'), table_name='paig_guardrail_view')
    op.drop_table('guardrail_connection')
    op.drop_index(op.f('ix_guardrail_update_time'), table_name='guardrail')
    op.drop_index(op.f('ix_guardrail_id'), table_name='guardrail')
    op.drop_index(op.f('ix_guardrail_create_time'), table_name='guardrail')
    op.drop_table('guardrail')
    # ### end Alembic commands ###
