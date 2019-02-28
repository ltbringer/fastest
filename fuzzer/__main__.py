import multiprocessing
from fuzzer.cli.args import cli_args
from fuzzer.rest_fuzzer import fuzz
from fuzzer.rest_fuzzer.json_schema import make_schema_object

server_host = cli_args.host
server_port = cli_args.port
api_list = cli_args.api_json

process_args = [(
    server_host,
    server_port,
    api_object,
    make_schema_object(api_object['body'])
) for api_object in api_list]


with multiprocessing.Pool(len(api_list)) as proc:
    proc.map(fuzz.api, process_args)
