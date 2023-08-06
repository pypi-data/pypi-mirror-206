"""
object oriented compiler pipeline
"""

from typing import Any, Callable, Dict, List, Optional, Union

from ..utils import is_sequence
from ..abstractcircuit import AbstractCircuit
from .qiskit_compiler import qiskit_compile


class Compiler:
    def __init__(
        self,
        compile_funcs: Union[Callable[..., Any], List[Callable[..., Any]]],
        compiled_options: Optional[List[Dict[str, Any]]] = None,
    ):
        if not is_sequence(compile_funcs):
            self.compile_funcs = [compile_funcs]
        else:
            self.compile_funcs = list(compile_funcs)  # type: ignore
        self.add_options(compiled_options)

    def add_options(
        self, compiled_options: Optional[List[Dict[str, Any]]] = None
    ) -> None:
        if not is_sequence(compiled_options):
            self.compiled_options = [compiled_options for _ in self.compile_funcs]
        else:
            assert len(compiled_options) == len(  # type: ignore
                self.compile_funcs
            ), "`compiled_options` must have the same list length as `compile_funcs`"
            self.compiled_options = list(compiled_options)  # type: ignore

    def __call__(
        self, circuit: AbstractCircuit, info: Optional[Dict[str, Any]] = None
    ) -> Any:
        for f, d in zip(self.compile_funcs, self.compiled_options):
            circuit, info = f(circuit, info, compiled_options=d)  # type: ignore
        return circuit, info


default_compiler = Compiler(qiskit_compile)
