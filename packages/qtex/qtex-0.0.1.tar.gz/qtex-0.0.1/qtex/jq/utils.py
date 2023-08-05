import os
import qtc.utils.db_utils as dbu
import qtc.utils.cipher_utils as cu


def get_conn(host='124.222.142.29',
             port=7423,
             # user='s_heimdal_etl',
             # password='390f1c1c05140241445767',
             user=None,
             password=None,
             database=None):
    if user is None:
        user = os.getenv('PG_USER')
    if password is None:
        password = os.getenv('PG_PASSWORD')

    conn = dbu._get_engine(
        db_type='POSTGRES',
        host=host,
        port=port,
        user=user,
        password=cu.from_salted(secret_str=password),
        database=database
    )

    return conn
