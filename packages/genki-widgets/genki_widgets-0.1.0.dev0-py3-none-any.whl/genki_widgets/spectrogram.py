#!/usr/bin/env python
# coding: utf-8

# Copyright (c) bjarni.
# Distributed under the terms of the Modified BSD License.

"""
"""
from __future__ import annotations

from traitlets import Float, Unicode, Int

from .baseplot import BasePlot


class Spectrogram(BasePlot):
    _plot_type = Unicode('spectrogram').tag(sync=True)

    window_size = Int(default_value=256).tag(sync=True)
    sample_rate = Int(default_value=100).tag(sync=True)
    n_visible_windows = Int(default_value=100).tag(sync=True)
    colormap_min = Float(default_value=0.0).tag(sync=True)
    colormap_max = Float(default_value=1.0).tag(sync=True)

    _model_name = Unicode('SpectrogramModel').tag(sync=True)
    _view_name = Unicode('SpectrogramView').tag(sync=True)

    def __init__(self,
        y_a: tuple[str, int] | tuple[str, int, str],
        **kwargs
    ):
        super().__init__(**kwargs)

        self.sig_y = [{
            'key': y_a[0],
            'idx': y_a[1],
            'name': y_a[2] if len(y_a) > 2 else '',
        }]
