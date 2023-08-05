import qtex.jq.utils as jqu
import logging
logger = logging.getLogger()


DATA_TYPE_CONFIG = dict()

def persist_cne5(dateid, securities=None,
                 **kwargs):
    global DATA_TYPE_CONFIG

    datestr = dtu.dateid_to_datestr(dateid=dateid)
    if securities is None:
        securities = get_all_securities(types=['stock'], date=datestr)
        securities = securities.index.to_list()
    else:
        securities = list(mu.iterable_to_tuple(securities, raw_type='str'))

    if len(securities) == 0:
        return None

    factor_names = ['size', 'beta', 'momentum', 'residual_volatility', 'non_linear_size',
                    'book_to_price_ratio', 'liquidity', 'earnings_yield', 'growth', 'leverage']
    factor_data = jqf.get_factor_values(
        securities=securities,
        factors=factor_names,
        start_date=datestr, end_date=datestr
    )

    data = pd.concat([factor_data[fn].unstack().to_frame(fn) for fn in factor_data.keys()], axis=1)
    data.index.names = ['ts_code', 'trade_date']
    data.reset_index(inplace=True)
    data['trade_date'] = data['trade_date'].dt.strftime('%Y%m%d').astype(int)
    data['ts_code'] = data['ts_code'].apply(lambda x: x.replace('.XSHE', '.SZ').replace('.XSHG', 'SH'))
    logger.info(f'data.shape={data.shape}. Examples:\n{data.head()}')

    user_d, password_d, database_d = \
        DATA_TYPE_CONFIG.get('CNE5',
                             (None, None, 'CN-EQUITY-VENDOR'))
    if 'user' not in kwargs:
        user = user_d
    if 'password' not in kwargs:
        password = password_d
    if 'database' not in kwargs:
        database = database_d

    conn = jqu.get_conn(user=user, password=password, database=database)
    schema = 'joinquant'
    table_name = 'CNE5'
    # upsert_method = dbu.create_upsert_method(db_code=database, schema=schema,
    #                                          extra_update_fields={'UpdateDateTime': "NOW()"})

    # conn.execute(f'DELETE FROM "{schema}"."{table_name}" WHERE "DateId"={dateid}')
    num_rows = data.to_sql(table_name,
                           con=conn, schema=schema,
                           if_exists='append', index=False)

    logger.info(f'{table_name} with shape {data.shape} on dateid={dateid} '
                f'persisted into "{database}"."{schema}"."{table_name}" .')

    return data
