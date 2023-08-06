const BASE_OPTIONS = [
    'name',
    'x_axis_align',
    'y_axis_align',
    'x_axis_flipped',
    'y_axis_flipped',
    'x_axis_visible',
    'y_axis_visible',
    'data_contains_nan',
    'data_is_sorted',
];

export const LINE_OPTIONS = [
    ... BASE_OPTIONS,
    'auto_range',
    'y_domain_max',
    'y_domain_min',
    'n_visible_points',
];

export const TRACE_OPTIONS = [
    ... BASE_OPTIONS,
    'auto_range_x',
    'auto_range_y',
    'x_domain_max',
    'x_domain_min',
    'y_domain_max',
    'y_domain_min',
    'n_visible_points',
];

export const BAR_OPTIONS = [
    ... BASE_OPTIONS,
    'auto_range',
    'y_domain_max',
    'y_domain_min',
];

export const SPECTRO_OPTIONS = [
    ... BASE_OPTIONS,
    'window_size',
    'sample_rate',
    'n_visible_windows',
    'colormap_min',
    'colormap_max',
];

export const OPTIONS = {
    'line': LINE_OPTIONS,
    'trace': TRACE_OPTIONS,
    'bar': BAR_OPTIONS,
    'spectrogram': SPECTRO_OPTIONS
}
