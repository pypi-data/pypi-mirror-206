#!/usr/bin/env python
# coding: utf-8

# Copyright (c) bjarni.
# Distributed under the terms of the Modified BSD License.

"""
"""
from __future__ import annotations

from traitlets import Float, Unicode, Bool, Int

from .baseplot import BasePlot


class Line(BasePlot):
    # Super hacky way to get the correct model name
    _plot_type = Unicode('line').tag(sync=True)

    auto_range = Bool(default_value=True).tag(sync=True)
    y_domain_max = Float(default_value=1).tag(sync=True)
    y_domain_min = Float(default_value=0).tag(sync=True)
    n_visible_points = Int(default_value=1000).tag(sync=True)
    
    _model_name = Unicode('LineModel').tag(sync=True)
    _view_name = Unicode('LineView').tag(sync=True)

    def __init__(self,
        x_a: tuple[str, int] | tuple[str, int, str],
        y_a: tuple[str, int] | tuple[str, int, str] | list[tuple[str, int]] | list[tuple[str, int, str]],
        **kwargs
    ):
        super().__init__(**kwargs)

        y_a = y_a if isinstance(y_a, list) else [y_a]
        self.sig_x = {
            'key': x_a[0],
            'idx': x_a[1],
            'name': x_a[2] if len(x_a) > 2 else '',
        }
        self.sig_y = [{
            'key': y[0],
            'idx': y[1],
            'name': y[2] if len(y) > 2 else '',
        } for y in y_a]