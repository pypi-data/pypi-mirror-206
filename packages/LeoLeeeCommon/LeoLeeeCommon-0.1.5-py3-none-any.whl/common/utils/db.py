### init db
import os
import yaml
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.exc import NoSuchTableError

TMP_TABLE_PREFIX = '__tmp'


def clone_table_as_tmp(engine, table_name: str):
    # 1. 获取原表和元数据对象
    metadata = MetaData(bind=engine)
    src_table = Table(table_name, metadata, autoload=True, autoload_with=engine)

    # 2. 克隆原表结构
    src_table.name = get_tmp_table_name(table_name)
    clone_table = src_table.tometadata(metadata)

    # 3. 创建新表
    with engine.begin() as conn:
        clone_table.create(conn)


def drop_tmp_of_table(engine, table_name: str):
    # 1. 获取元数据对象和表对象
    metadata = MetaData(bind=engine)
    try:
        tmp_table = Table(get_tmp_table_name(table_name), metadata, autoload=True, autoload_with=engine)

        # 2. 删除表
        if tmp_table is not None:
            with engine.begin() as conn:
                conn.execute(f"DROP TABLE {tmp_table.name}")
    except NoSuchTableError as e:
        pass


def insert_ignore_from_tmp(engine, table_name: str, columns="*"):
    # 1. 获取元数据对象和表对象
    metadata = MetaData(bind=engine)
    src_table = Table(table_name, metadata, autoload=True, autoload_with=engine)
    tmp_table = Table(get_tmp_table_name(table_name), metadata, autoload=True, autoload_with=engine)

    # 2. 插入(ignore)数据
    # insert_ignore_statement = src_table.insert().prefix_with('IGNORE').from_select(tmp_table.columns, tmp_table.select())
    # engine.excute(insert_ignore_statement)
    with engine.begin() as conn:
        if columns == "*":
            conn.execute(f"INSERT IGNORE INTO {src_table.name} SELECT * FROM {tmp_table.name}")
        else:
            conn.execute(f"INSERT IGNORE INTO {src_table.name} ({columns}) SELECT {columns} FROM {tmp_table.name}")


def replace_from_tmp(engine, table_name: str, columns="*"):
    # 1. 获取元数据对象和表对象
    metadata = MetaData(bind=engine)
    src_table = Table(table_name, metadata, autoload=True, autoload_with=engine)
    tmp_table = Table(get_tmp_table_name(table_name), metadata, autoload=True, autoload_with=engine)

    # 2. 插入(replace)数据
    # replace_statement = src_table.replace().from_select(tmp_table.columns, tmp_table.select())
    # engine.excute(replace_statement)
    with engine.begin() as conn:
        if columns == "*":
            conn.execute(f"REPLACE INTO {src_table.name} SELECT * FROM {tmp_table.name}")
        else:
            conn.execute(f"REPLACE INTO {src_table.name} ({columns}) SELECT {columns} FROM {tmp_table.name}")


def get_tmp_table_name(table_name: str):
    return '{}_{}'.format(TMP_TABLE_PREFIX, table_name)


def init_db(config_path="conf/db.yml"):
    return __init_db_core(config_path)


def init_db_for_test(config_path="conf/db-test.yml"):
    return __init_db_core(config_path)


def __init_db_core(config_path: str, env_key="DB_CFG"):
    # 加载数据库配置
    path = config_path
    value = os.getenv(env_key, None)
    if value:
        path = value

    # init db
    if os.path.exists(path):
        with open(path, "r") as f:
            y = yaml.load(f, Loader=yaml.FullLoader)
            config = y.get(y.get('active'))
            engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8mb4'
                                   .format(config['username'], config['password'], config['ip'], config['port'],
                                           config['database']))
            return engine
    else:
        raise Exception("未找到路径：config_path (init_db)")