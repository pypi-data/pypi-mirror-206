from typing import Any

from jinja2 import Environment, FileSystemLoader, PackageLoader, Template

from .init_template import init_code


class TransitionGraphRenderer:
    __template: Template
    __environment: Environment

    def __init__(self) -> None:
        self.__environment = Environment(
            loader=PackageLoader(package_name="retentioneering", package_path="templates/transition_graph"),
            autoescape=False,
            trim_blocks=True,
            lstrip_blocks=True,
        )

        self.__body_template = self.__environment.get_template("body.html")
        self.__full = self.__environment.get_template("full.html")
        self.__inner_iframe = self.__environment.get_template("inner_iframe.html")
        self.__init = init_code

    def body(self, **kwargs: Any) -> str:
        return self.__body_template.render(**kwargs)

    def full(self, **kwargs: Any) -> str:
        return self.__full.render(**kwargs)

    def init(self, **kwargs: Any) -> str:
        return self.__init.format(**kwargs)

    def inner_iframe(self, **kwargs: Any) -> str:
        return self.__inner_iframe.render(**kwargs)
