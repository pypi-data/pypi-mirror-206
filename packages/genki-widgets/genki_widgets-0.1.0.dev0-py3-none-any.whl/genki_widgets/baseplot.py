#!/usr/bin/env python
# coding: utf-8

# Copyright (c) bjarni.
# Distributed under the terms of the Modified BSD License.

"""
TODO: Add module docstring
"""

from ipywidgets import DOMWidget
import numpy as np

from traitlets import Dict, List, Unicode, Bool, Int, Enum
from ._frontend import module_name, module_version



# name is optional
sig_value_trait = {
    'key': Unicode(),
    'idx': Int(),
    'name': Unicode(''),
}

class BasePlot(DOMWidget):
    # Defines which data is accessed for each plot
    sig_x = Dict(
        per_key_traits=sig_value_trait,
        default_value={'key': '', 'idx': 0, 'name': ''}
    ).tag(sync=True)
    sig_y = List(Dict(
        per_key_traits=sig_value_trait,
        default_value=[]
    )).tag(sync=True)

    name = Unicode(default_value="noname").tag(sync=True)
    x_axis_align = Enum(
        ['bottom', 'top', 'left', 'right'],
        default_value='bottom'
    ).tag(sync=True)
    y_axis_align = Enum(
        ['bottom', 'top', 'left', 'right'],
        default_value='left'
    ).tag(sync=True)
    x_axis_flipped = Bool(default_value=False).tag(sync=True)
    y_axis_flipped = Bool(default_value=False).tag(sync=True)
    x_axis_visible = Bool(default_value=True).tag(sync=True)
    y_axis_visible = Bool(default_value=True).tag(sync=True)
    data_contains_nan = Bool(default_value=False).tag(sync=True)
    data_is_sorted = Bool(default_value=True).tag(sync=True)

    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
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



