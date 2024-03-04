from loguru import logger

# create a log_file.log
logger.add(
    '09/log_file.log',
    format =  "{time} <r>{level}</r> <g>{message}</g> {file}"
)


logger.info('Initialization processes, routine transactions, ...') 
logger.debug('Workflow applications') 
logger.warning('Situations that need attention but do not stop the system from working') 
logger.error('Some system operations failed')
logger.critical('Stop system operation')
