from __future__ import annotations

from hamilton.function_modifiers import dataloader
from hamilton.htypes import Collect, Parallelizable

"""Tests future annotations with common node types"""


def parallelized() -> Parallelizable[int]:
    yield 1
    yield 2
    yield 3


def standard(parallelized: int) -> int:
    return parallelized + 1


def collected(standard: Collect[int]) -> int:
    return sum(standard)


@dataloader()
def sample_dataloader() -> tuple[list[str], dict]:
    """Grouping here as the rest test annotations"""
    return ["a", "b", "c"], {}
