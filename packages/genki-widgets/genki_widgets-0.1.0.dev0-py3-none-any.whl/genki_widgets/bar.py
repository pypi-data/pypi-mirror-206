#!/usr/bin/env python
# coding: utf-8

# Copyright (c) bjarni.
# Distributed under the terms of the Modified BSD License.

"""
"""
from __future__ import annotations

from traitlets import Unicode, Bool, Float

from .baseplot import BasePlot


class Bar(BasePlot):
    _plot_type = Unicode('bar').tag(sync=True)

    auto_range = Bool(default_value=True).tag(sync=True)
    y_domain_max = Float(default_value=1).tag(sync=True)
    y_domain_min = Float(default_value=0).tag(sync=True)

    _model_name = Unicode('BarModel').tag(sync=True)
    _view_name = Unicode('BarView').tag(sync=True)

    def __init__(self,
        y_a: tuple[str, int] | tuple[str, int, str] | list[tuple[str, int]] | list[tuple[str, int, str]],
        **kwargs
    ):
        super().__init__(**kwargs)

        y_a = y_a if isinstance(y_a, list) else [y_a]
        self.sig_y = [{
            'key': y[0],
            'idx': y[1],
            'name': y[2] if len(y) > 2 else '',
        } for y in y_a]

