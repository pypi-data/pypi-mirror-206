import os
from argparse import ArgumentParser

import optuna_dashboard

from . import BaseCommand


def monitor_autotuna_command_factory(args):
    return MonitorAutoTunaCommand(args.model_path, args.port, args.host, args.workers, args.debug)


class MonitorAutoTunaCommand(BaseCommand):
    @staticmethod
    def register_subcommand(parser: ArgumentParser):
        _parser = parser.add_parser("monitor", help="Explain AutoTuna Models")
        _parser.add_argument("--db_path", help="Path to db", required=True, type=str)
        _parser.add_argument("--port", help="Port to serve on", default=8080, type=int, required=False)
        _parser.add_argument("--host", help="Host to serve on", default="127.0.0.1", type=str, required=False)
        _parser.set_defaults(func=monitor_autotuna_command_factory)

    def __init__(self, db_path, port, host):
        self.db_path = db_path
        self.port = port
        self.host = host

    def execute(self):
        os.environ["AUTOTUNA_MODEL_PATH"] = self.model_path
        optuna_dashboard.run_server(storage=self.db_path, host=self.host, port=self.port)
