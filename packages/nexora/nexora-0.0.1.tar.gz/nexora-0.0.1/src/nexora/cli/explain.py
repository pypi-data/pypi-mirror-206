import os
import pandas as pd
import joblib
from argparse import ArgumentParser

from shapash import SmartExplainer

from . import BaseCommand


def explain_autotuna_command_factory(args):
    return ExplainAutoTunaCommand(args.model_path, args.data_path, args.config_path, args.port, args.host)


class ExplainAutoTunaCommand(BaseCommand):
    @staticmethod
    def register_subcommand(parser: ArgumentParser):
        _parser = parser.add_parser("explain", help="Explain AutoTuna Models")
        _parser.add_argument("--model_path", help="Path to model", required=True, type=str)
        _parser.add_argument("--data_path", help="Path to data", required=True, type=str)
        _parser.add_argument("--config_path", help="Path to config", required=True, type=str)
        _parser.add_argument("--port", help="Port to serve on", default=8080, type=int, required=False)
        _parser.add_argument("--host", help="Host to serve on", default="127.0.0.1", type=str, required=False)
        _parser.set_defaults(func=explain_autotuna_command_factory)

    def __init__(self, model_path, data_path, config_path, port, host):
        self.model_path = model_path
        self.data_path = data_path
        self.config_path = config_path
        self.port = port
        self.host = host

    def execute(self):
        os.environ["AUTOTUNA_MODEL_PATH"] = self.model_path
        model = joblib.load(self.model_path)
        config = joblib.load('xgb-trial-2/atuna.config')
        df = pd.read_feather(self.data_path)
        x=df[config.features]
        y=df[config.targets]
        xpl = SmartExplainer(model=model)
        xpl.compile(x=x, y_target=y)
        app = xpl.run_app(title_story=config.output, host=self.host, port=self.port)
