"""Module with general utility functions."""
from __future__ import annotations

__author__ = "Matteo Gabba"
__copyright__ = "Copyright 2022, all right reserved Gabba Scientific"
__status__ = "Development"

import inspect
import itertools
import math
from collections.abc import Iterator
from typing import Iterable

import more_itertools
import numpy as np


def get_class_properties(
    obj: object,
) -> dict[str, ...]:
    properties = {}

    for attr, value in inspect.getmembers(obj):
        # Remove private and protected functions
        if not attr.startswith("_"):
            # Remove methods
            if not inspect.ismethod(value):
                # Remove class attributes
                if isinstance(getattr(type(obj), attr, None), property):
                    properties[attr] = value
    return properties


def is_all_zeros_array(
    data: np.ndarray,
) -> bool:
    return not np.any(data)


def bin_edge_to_center(bin_edges: np.ndarray) -> np.ndarray:
    """
    Convert bin edges to bin center.

    Parameters
    ----------
        bin_edges : np.ndarray, (N,)
            Bin edges. For example as defined by numpy.histogram().

    Returns
    -------
        bin_centers : np.ndarray, (N,)
            Bin center position calculated as (left_edges + right_edges) / 2.
    """
    # Compute the bin center:
    left_edges = bin_edges[1:]
    right_edges = bin_edges[:-1]
    bin_centers = (left_edges + right_edges) / 2

    return bin_centers


def build_histogram(
    data: np.ndarray,
    hist_range: tuple[float, float],
    bins: int | str = "auto",
    density: bool = True,
) -> tuple[np.ndarray, np.ndarray, float]:

    values, bin_edges = np.histogram(
        data,
        range=hist_range,
        bins=bins,
        density=density,
    )

    bin_centers = bin_edge_to_center(bin_edges)
    bin_width = bin_edges[1] - bin_edges[0]

    return values, bin_centers, bin_width


def cluster_size_generator(
    values: Iterable[float],
) -> Iterator[tuple[float, np.ndarray, np.ndarray]]:
    """
    Yield generator with value, counts and index of groups of consecutive equal
     values in a 1D-list.

    Parameters
    ----------
        values : list
            1D list of values.

    Yields
    ------
        (value, counts, idx) : tuple[float, np.ndarray, np.ndarray]

    Notes
    -----
    Adapted from:
        <https://stackoverflow.com/questions/23023805/how-to-get-the-index-and-occurance-of-each-item-using-itertools-groupby>
    """
    # Set index indicating start of the first group
    group_start_idx = 0

    # For each group of consecutive equal values
    for value, group in itertools.groupby(values):
        # counts the consecutive equal values
        counts = len(list(group))

        # generate array of index corresponding to each group of consecutive
        # values
        idx = np.arange(group_start_idx, group_start_idx + counts)

        # yield generator with value, counts and index of each group
        yield value, counts, idx

        # re-set the start index for next group
        group_start_idx += counts


def _isnan(value: int | float) -> bool:
    if math.isnan(value):
        return True
    return False


def pop_iterator(iterator: Iterator) -> Iterator:
    """Pop last item from iterator object."""
    iter_1, iter_2 = itertools.tee(iterator, 2)
    n_items = more_itertools.ilen(iter_1)
    return more_itertools.take(n_items - 1, iter_2)
