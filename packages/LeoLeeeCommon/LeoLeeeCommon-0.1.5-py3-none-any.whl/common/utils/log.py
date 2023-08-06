import os
import yaml
import logging.config


### init log #
def setup_logging(default_path="conf/logging.yml", default_level=logging.INFO, env_key="LOG_CFG"):
    # 加载日志配置
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            # load config
            config = yaml.load(f, Loader=yaml.FullLoader)

            # init log path / log file
            path_log = config['path']
            if not os.path.isdir(path_log):
                os.makedirs(path_log)
            path_log_info = config['handlers']['info_file_handler']['filename']
            if not os.path.exists(path_log_info):
                fp = open(path_log_info, 'w')
                fp.close()
            path_log_error = config['handlers']['error_file_handler']['filename']
            if not os.path.exists(path_log_error):
                fp = open(path_log_error, 'w')
                fp.close()

            # setup config
            logging.config.dictConfig(config)
    else:
        raise Exception("未找到路径：default_path (setup_logging)")
        # logging.basicConfig(level=default_level)