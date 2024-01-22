from collections import namedtuple

Point = namedtuple("Point2D", ("x", "y"))

A = Point(6, 9)
B = Point(6, 10)

import rich; from rich import inspect; from rich import print as rprint; import ipdb; ipdb.set_trace()