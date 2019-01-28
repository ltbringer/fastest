import coloredlogs, logging

# Create a logger object.
logger = logging.getLogger(__name__)

# By default the install() function installs a handler on the root logger,
# this means that log messages from your code and log messages from the
# libraries that you use will all show up on the terminal.
coloredlogs.install(fmt='%(hostname)s %(asctime)s %(levelname)s %(message)s', level='DEBUG', logger=logger)
