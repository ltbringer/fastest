import argparse


parser = argparse.ArgumentParser(description='Fuzz the system')
parser.add_argument('--host', help='Api server\'s host-name.')
parser.add_argument('--port', help='Port on which the server is running.')
parser.add_argument('--api-json', help='File containing api endpoint and expected request objects')


cli_args = parser.parse_args()
