import qtex.jq.utils as jqu
import logging
logger = logging.getLogger()


DATA_TYPE_CONFIG = dict()

def persist_target_positions(dateid, target_positions,
                             **db_config):
    if target_positions is None or len(target_positions)==0:
        return None

    cols =['AccountId', 'StrategyId', 'DateId', 'SecurityCode', 'SideId',
           'Signal', 'Quantity', 'MV', 'Weight']
    cols = [col for col in cols if col in target_positions.columns]
    data = target_positions[cols]

    # db_type_d, host_d, port_d, user_d, password_d, database_d = \
    #     DATA_TYPE_CONFIG.get('TARGET_POSITION',
    #                          ('POSTGRES', None, None, None, None, None))
    #
    # db_type = kwargs.get('db_type', db_type_d)
    # host = kwargs.get('host', host_d)
    # port = kwargs.get('port', port_d)
    # user = kwargs.get('user', user_d)
    # password = kwargs.get('password', password_d)
    # database = kwargs.get('database', database_d)
    #
    # conn = jqu.get_conn(
    #     db_type=db_type,
    #     host=host,
    #     port=port,
    #     user=user,
    #     password=password,
    #     database=database
    # )
    conn = jqu.get_conn_data_type(data_type='TARGET_POSITION',
                                  **db_config)
    schema = 'signal'
    table_name = 'TargetPosition'
    # upsert_method = dbu.create_upsert_method(db_code=database, schema=schema,
    #                                          extra_update_fields={'UpdateDateTime': "NOW()"})

    num_rows = data.to_sql(table_name,
                           con=conn, schema=schema,
                           if_exists='append', index=False)

    logger.info(f'{table_name} with shape {data.shape} on dateid={dateid} '
                f'persisted into "{database}"."{schema}"."{table_name}" .')

    return data