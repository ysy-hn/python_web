import logging


FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT, filename='日志.log')
d = {'clientip': '127.0.0.1', 'user': 'the5file'}
logger = logging.getLogger(__name__)

logger.info('this is %s level', 'info', extra=d)

