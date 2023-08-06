#!/usr/bin/env python
# coding: utf-8

# Copyright (c) bjarni.
# Distributed under the terms of the Modified BSD License.

"""
TODO: Add module docstring
"""

from ipywidgets import DOMWidget, widget_serialization
import numpy as np

from traitlets import Dict, Unicode, List, Instance

from .baseplot import BasePlot
from ._frontend import module_name, module_version


class Dashboard(DOMWidget):
    plot_widgets = List(Instance(BasePlot)).tag(sync=True, **widget_serialization)

    def __init__(self, plot_widgets: list[BasePlot], **kwargs):
        super().__init__(**kwargs)

        self.plot_widgets = plot_widgets

    _model_name = Unicode('DashboardModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)

    _view_name = Unicode('DashboardView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    # Used to transfer data from python to typescript
    data = Dict().tag(sync=True)
    def update(self, new_data: dict[str, any]):
        for key, value in new_data.items():
            value = np.array(value)

            if np.iscomplexobj(value):
                value = np.log10(np.maximum(np.abs(value), 1e-10))

            if value.ndim < 2:
                value = value[None]

            new_data[key] = value.tolist()

        self.data = new_data
