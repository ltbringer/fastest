import multiprocessing
from fuzzer.cli.args import cli_args
from fuzzer.rest_fuzzer import fuzz
from fuzzer.rest_fuzzer.json_schema import make_schema_object


# server_host = cli_args.host
# server_port = cli_args.port
# api_list = cli_args.api_json

server_host = 'http://localhost'
server_port = 3000
api_list = [{
    'url': '/',
    'method': 'POST',
    'body': {}
}, {
    'url': '/test',
    'method': 'POST',
    'body': {
        'messageObject': {
            'message': 'hello world'
        }
    }
}]


process_args = [{
    'host': server_host,
    'port': server_port,
    'req_body': api_object,
    'req_body_schema': make_schema_object(api_object['body'])
} for api_object in api_list]


def test_apis():
    with multiprocessing.Pool(multiprocessing.cpu_count()) as proc:
        proc.map(fuzz.api_nx, process_args)


if __name__ == '__main__':
    test_apis()
