"""
    配置信息
    ~~~~~~~~~~~~~~
    项目的基础配置信息.

    :copyright: (c) 2016-10-26 by datochan.
"""
import logging
import os
from datetime import datetime

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

config = {
    "indexes": [
        [1, "000015", 20031231],  # 上证50
        [1, "000016", 20031231],  # 上证50
        [1, "000300", 20041231],  # 沪深300
        [1, "000852", 20041231],  # 中证1000
        [1, "000905", 20041231],  # 中证500
        [1, "000913", 20041231],  # 300医药
        [1, "000932", 20041231],  # 中证消费
        [1, "000992", 20041231],  # 全指金融
        [0, "399005", 20061227],  # 中小板指
        [0, "399006", 20100601],  # 创业扳指
        [0, "399441", 20150120],  # 医药生物
        [0, "399967", 20041231],  # 中证军工
        [0, "399971", 20101231],  # 中证传媒
        [0, "399975", 20070630],  # 中证证券公司
        [0, "399986", 20041231]   # 中证银行
    ],
    "logger": {
        "level": logging.DEBUG,
        "format": '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        "filename": "dtgear-%s.log" % str(datetime.now())[:10]
    },
    "urls": {
        "fin_list_prex": "tdxfin",  # 财务数据文件列表

        'china_bond_list': 'http://yield.chinabond.com.cn/cbweb-pbc-web/pbc/historyQuery?startDate=%s&endDate=%s'
                           '&gjqx=0&qxId=hzsylqx&locale=cn_ZH',
        'china_bond_item': 'http://yield.chinabond.com.cn/cbweb-pbc-web/pbc/queryGjqxInfo?&workTime=%s&locale=cn_ZH',
        "server_time": "https://s.thsi.cn/js/chameleon/time.%d.js",  # 用于更新同花顺服务器时间解密cookie信息
        "report_time": "http://data.10jqka.com.cn/financial/yypl/date/%s"
                       "/board/ALL/field/stockcode/order/DESC/page/%d/ajax/1/"
    },
    "files": {
        'calendar': "%s/data/calendar.csv" % PROJECT_ROOT,  # 股票交易日历
        'bond': "%s/data/bond.csv" % PROJECT_ROOT,
        'stocks': "%s/data/stocks.csv" % PROJECT_ROOT,
        'stock_a': "%s/data/a.csv" % PROJECT_ROOT,
        'st': "%s/data/st.csv" % PROJECT_ROOT,
        'bonus': "%s/data/bonus.csv" % PROJECT_ROOT,
        'reports': "%s/data/reports.csv" % PROJECT_ROOT,  # 股票财报目录
        'report_item': "%s/data/reports/%s.zip",  # 股票财报目录
        'rt_item': "%s/data/reports/rt%s.csv",  # 股票财报目录
        'index': "%s/data/indexes/%s.csv",  # 指定指数的历史成分列表
        'plots': "%s/data/plots/%s/%d-%s.csv",  # 策略执行结果的保存 粗略方法名/市场-代码.csv
    },
    "tdx": {
        "hq_server": {
            # "host": "121.14.110.200",
            # "port": 443
            # # 金融终端V7.43
            "host": "221.194.181.176",
            "port": 7709
        },
        "cw_server": {
            # 财务数据
            # calc.tdx.com.cn, calc2.tdx.com.cn
            "host": "120.76.152.87",   # 101.132.147.181
            "port": 7709
        },

    },
    "db": {
        "mongodb": "mongodb://dtgear:a11111111@127.0.0.1:27017/",
        "database": "DTGear"
    }
}


class Config:
    def __init__(self):
        pass

    CACHE_TYPE = "simple"
    CACHE_DEFAULT_TIMEOUT = 300

    SECRET_KEY = 'hard to guess string'
    SSL_DISABLE = True

    LOGGER_LEVEL = logging.DEBUG
    LOGGER_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    LOGGER_DATE_FORMAT = '%a, %d %b %Y %H:%M:%S'
    LOGGER_FILENAME = 'dtgear.log'
    LOGGER_FILEMODE = 'w'

    MONGO_URI = "%s%s" % (config.get("db").get("mongodb"), config.get("db").get("database"))
    MAKO_TRANSLATE_EXCEPTIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


# web应用的基础配置
settings = {
    "dev": DevelopmentConfig
}
