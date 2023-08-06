import os
import pandas as pd
import qtc.utils.db_utils as dbu
import qtc.utils.cipher_utils as cu


# def get_conn(host='124.222.142.29',
#              port=7423,
#              user=None,
#              password=None,
#              database=None):
def get_conn(**db_config):
    db_type = db_config.get('db_type', 'POSTGRES')
    host = db_config.get('host', os.getenv('DB_HOST', None))
    port = db_config.get('port', os.getenv('DB_PORT', None))
    user = db_config.get('user', os.getenv('DB_USER', None))
    password = db_config.get('password', os.getenv('DB_PASSWORD', None))
    database = db_config.get('database', os.getenv('DB_DATABASE', None))

    conn = dbu._get_engine(
        db_type=db_type,
        host=host,
        port=port,
        user=user,
        password=cu.from_salted(secret_str=password),
        database=database
    )

    return conn


def get_conn_data_type(data_type, **db_config):
    import qtex.jq.etl.factor as etlf
    import qtex.jq.sync.position as syncp

    DATA_TYPE_CONFIG_MAP = {
        'CNE5': etlf.DATA_TYPE_CONFIG,
        'TARGET_POSITION': syncp.DATA_TYPE_CONFIG
    }

    data_type_config = DATA_TYPE_CONFIG_MAP[data_type]

    db_type_d, host_d, port_d, user_d, password_d, database_d = \
        data_type_config.get(data_type,
                             ('POSTGRES', None, None, None, None, None))

    db_type = db_config.get('db_type', db_type_d)
    host = db_config.get('host', host_d)
    port = db_config.get('port', port_d)
    user = db_config.get('user', user_d)
    password = db_config.get('password', password_d)
    database = db_config.get('database', database_d)

    conn = get_conn(
        db_type=db_type,
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )

    return conn, database


def load_factor_scores(jq_codes, factors,
                       end_date, start_date=None, count=None,
                       transpose=False):
    import jqfactor as jqf
    scores = jqf.get_factor_values(
        securities=jq_codes,
        factors=factors,
        start_date=start_date, end_date=end_date, count=count
    )

    scores = pd.concat(scores)
    scores.index.names = ['factor_code', 'trade_date']

    if count==1 and transpose:
#         scores = scores.droplevel(level='Date').T
        scores.index = scores.index.droplevel(level='Date')
        scores = scores.T

    return scores