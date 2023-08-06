import json
from abc import abstractmethod
from typing import Any, Callable, Dict, List

from looqbox.global_calling import GlobalCalling
from looqbox.utils.utils import _format_quotes


class BaseFlow:
    def __init__(self, script_info: str):
        script_data = json.loads(script_info)
        self.input_json_file = script_data["responseParameters"]
        self.script_file = script_data["vars"]["response_path"]
        self.output_json_file = script_data["resultPath"]
        self.upload_file = script_data["UploadFile"]
        self.vars = script_data["vars"]
        self.data: Dict[str, Any] | str = {}
        self.global_variables = GlobalCalling().looq

    def read_response_parameters(self) -> None:
        raw_file = open(self.input_json_file, 'r', encoding='utf-8').read()
        self.data = _format_quotes(raw_file)
        self.data = json.loads(self.data)

    def response_enricher(self) -> None:
        self.data.update(self.vars)

    def define_global_variables(self) -> None:
        for key, value in self.vars.items():
            setattr(self.global_variables, key, value)

    def response_writer(self) -> None:
        with open(self.output_json_file, 'w') as file:
            file.write(self.data)
            file.close()

    @staticmethod
    def run_steps(steps: List[Callable]) -> None:
        [step() for step in steps]

    @abstractmethod
    def run(self) -> None:
        ...
