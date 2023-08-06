"use strict";
(self["webpackChunkgenki_widgets"] = self["webpackChunkgenki_widgets"] || []).push([["lib_bar_js-lib_dashboard_js-lib_line_js-lib_spectrogram_js-lib_trace_js"],{

/***/ "./lib/bar.js":
/*!********************!*\
  !*** ./lib/bar.js ***!
  \********************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


// Copyright (c) bjarni
// Distributed under the terms of the Modified BSD License.
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.BarView = exports.BarModel = void 0;
const base_1 = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
const version_1 = __webpack_require__(/*! ./version */ "./lib/version.js");
const baseplot_view_1 = __webpack_require__(/*! ./baseplot_view */ "./lib/baseplot_view.js");
const options_1 = __webpack_require__(/*! ./options */ "./lib/options.js");
class BarModel extends base_1.DOMWidgetModel {
    defaults() {
        return {
            ...super.defaults(),
            _model_name: BarModel.model_name,
            _model_module: BarModel.model_module,
            _model_module_version: BarModel.model_module_version,
            _view_name: BarModel.view_name,
            _view_module: BarModel.view_module,
            _view_module_version: BarModel.view_module_version,
        };
    }
}
BarModel.model_name = 'BarModel';
BarModel.model_module = version_1.MODULE_NAME;
BarModel.model_module_version = version_1.MODULE_VERSION;
BarModel.view_name = 'BarView'; // Set to null if no view
BarModel.view_module = version_1.MODULE_NAME; // Set to null if no view
BarModel.view_module_version = version_1.MODULE_VERSION;
BarModel.serializers = {
    ...base_1.DOMWidgetModel.serializers,
};
exports.BarModel = BarModel;
class BarView extends baseplot_view_1.BasePlotView {
    render() {
        this.setup(options_1.BAR_OPTIONS);
    }
}
exports.BarView = BarView;


/***/ }),

/***/ "./lib/baseplot_view.js":
/*!******************************!*\
  !*** ./lib/baseplot_view.js ***!
  \******************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.BasePlotView = void 0;
const base_1 = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
const scichart_1 = __webpack_require__(/*! scichart */ "webpack/sharing/consume/default/scichart/scichart");
const helpers_1 = __webpack_require__(/*! ./utils/helpers */ "./lib/utils/helpers.js");
const utils_1 = __webpack_require__(/*! ./utils */ "./lib/utils.js");
class BasePlotView extends base_1.DOMWidgetView {
    constructor() {
        super(...arguments);
        this.plot = null;
    }
    setup(plot_option_keys) {
        (0, utils_1.load_scichart)();
        const plot_widget = document.createElement('div');
        plot_widget.setAttribute('id', Date.now().toString()); // Hack to make sure the id is unique
        plot_widget.setAttribute('style', 'width: 100%; height: 450px;');
        // plot_widget.classList.add('scichart-root'); // Should be styled by css/widget.css but doesn't work
        this.el.appendChild(plot_widget);
        const promise = scichart_1.SciChartSurface.create(plot_widget);
        promise.then((value) => {
            const { sciChartSurface, wasmContext } = value;
            const sub_surface = sciChartSurface.addSubChart(helpers_1.sub_surface_options);
            const options = (0, utils_1.get_all_from_model)(this.model, plot_option_keys);
            this.plot = (0, utils_1.create_plot_from_model)(this.model, wasmContext, sub_surface, options);
            this.model.on('change:data', () => {
                const data = this.model.get('data');
                this.plot.update(data);
            });
            for (const key of plot_option_keys) {
                this.model.on(`change:${key}`, () => {
                    const options = this.plot.get_options();
                    options[key] = this.model.get(key);
                    this.plot.set_options(options);
                });
            }
        });
    }
    remove() {
        if (this.plot) {
            this.plot.delete();
            this.plot = null;
        }
        this.model.off();
        super.remove();
    }
}
exports.BasePlotView = BasePlotView;


/***/ }),

/***/ "./lib/dashboard.js":
/*!**************************!*\
  !*** ./lib/dashboard.js ***!
  \**************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


// Copyright (c) bjarni
// Distributed under the terms of the Modified BSD License.
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.DashboardView = exports.DashboardModel = void 0;
const version_1 = __webpack_require__(/*! ./version */ "./lib/version.js");
const base_1 = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
const scichart_1 = __webpack_require__(/*! scichart */ "webpack/sharing/consume/default/scichart/scichart");
const dashboard_1 = __webpack_require__(/*! ./scicharts/dashboard */ "./lib/scicharts/dashboard.js");
const utils_1 = __webpack_require__(/*! ./utils */ "./lib/utils.js");
const options_1 = __webpack_require__(/*! ./options */ "./lib/options.js");
class DashboardModel extends base_1.DOMWidgetModel {
    defaults() {
        return {
            ...super.defaults(),
            _model_name: DashboardModel.model_name,
            _model_module: DashboardModel.model_module,
            _model_module_version: DashboardModel.model_module_version,
            _view_name: DashboardModel.view_name,
            _view_module: DashboardModel.view_module,
            _view_module_version: DashboardModel.view_module_version,
            plots: [],
        };
    }
}
DashboardModel.serializers = {
    ...base_1.DOMWidgetModel.serializers,
    plot_widgets: { deserialize: utils_1.unpack_models }
};
DashboardModel.model_name = 'DashboardModel';
DashboardModel.model_module = version_1.MODULE_NAME;
DashboardModel.model_module_version = version_1.MODULE_VERSION;
DashboardModel.view_name = 'DashboardView'; // Set to null if no view
DashboardModel.view_module = version_1.MODULE_NAME; // Set to null if no view
DashboardModel.view_module_version = version_1.MODULE_VERSION;
exports.DashboardModel = DashboardModel;
class DashboardView extends base_1.DOMWidgetView {
    constructor() {
        super(...arguments);
        this.dashboard = null;
        this.plot_widgets = [];
    }
    render() {
        (0, utils_1.load_scichart)();
        const dashboard_el = document.createElement('div');
        dashboard_el.setAttribute('id', Date.now().toString());
        dashboard_el.setAttribute('style', 'width: 100%; height: 450px; background-color: transparent;');
        // dashboard_el.classList.add('scichart-root'); // Should be styled by css/widget.css but doesn't work
        this.el.appendChild(dashboard_el);
        const promise = scichart_1.SciChartSurface.create(dashboard_el);
        promise.then((value) => {
            const { sciChartSurface, wasmContext } = value;
            this.plot_widgets = this.model.get('plot_widgets');
            this.dashboard = new dashboard_1.Dashboard(sciChartSurface, wasmContext);
            this.plot_widgets.forEach((plot_widget, i) => {
                const sig_x = plot_widget.get('sig_x');
                const sig_y = plot_widget.get('sig_y');
                const plot_type = plot_widget.get('_plot_type');
                this.dashboard.add_plot(plot_type, -1);
                const subplot = this.dashboard.plots[i];
                const options = (0, utils_1.get_all_from_model)(plot_widget, options_1.OPTIONS[plot_type]);
                subplot.set_signals(sig_x, sig_y);
                subplot.set_options(options);
                for (const key of options_1.OPTIONS[plot_type]) {
                    plot_widget.on(`change:${key}`, () => {
                        const options = subplot.get_options();
                        options[key] = plot_widget.get(key);
                        //@ts-ignore
                        subplot.set_options(options);
                    });
                }
            });
            this.model.on('change:data', () => {
                const data = this.model.get('data');
                this.dashboard.update(data);
            });
        });
    }
    remove() {
        if (this.dashboard) {
            this.dashboard.delete();
            this.dashboard = null;
        }
        this.model.off();
        this.plot_widgets.forEach((plot_widget) => plot_widget.off());
        this.plot_widgets = [];
        super.remove();
    }
}
exports.DashboardView = DashboardView;


/***/ }),

/***/ "./lib/line.js":
/*!*********************!*\
  !*** ./lib/line.js ***!
  \*********************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


// Copyright (c) BjarniHaukur
// Distributed under the terms of the Modified BSD License.
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.LineView = exports.LineModel = void 0;
const base_1 = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
const version_1 = __webpack_require__(/*! ./version */ "./lib/version.js");
const baseplot_view_1 = __webpack_require__(/*! ./baseplot_view */ "./lib/baseplot_view.js");
const options_1 = __webpack_require__(/*! ./options */ "./lib/options.js");
class LineModel extends base_1.DOMWidgetModel {
    defaults() {
        return {
            ...super.defaults(),
            _model_name: LineModel.model_name,
            _model_module: LineModel.model_module,
            _model_module_version: LineModel.model_module_version,
            _view_name: LineModel.view_name,
            _view_module: LineModel.view_module,
            _view_module_version: LineModel.view_module_version,
        };
    }
}
LineModel.model_name = 'LineModel';
LineModel.model_module = version_1.MODULE_NAME;
LineModel.model_module_version = version_1.MODULE_VERSION;
LineModel.view_name = 'LineView'; // Set to null if no view
LineModel.view_module = version_1.MODULE_NAME; // Set to null if no view
LineModel.view_module_version = version_1.MODULE_VERSION;
LineModel.serializers = {
    ...base_1.DOMWidgetModel.serializers,
};
exports.LineModel = LineModel;
class LineView extends baseplot_view_1.BasePlotView {
    render() {
        this.setup(options_1.LINE_OPTIONS);
    }
}
exports.LineView = LineView;


/***/ }),

/***/ "./lib/options.js":
/*!************************!*\
  !*** ./lib/options.js ***!
  \************************/
/***/ ((__unused_webpack_module, exports) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.OPTIONS = exports.SPECTRO_OPTIONS = exports.BAR_OPTIONS = exports.TRACE_OPTIONS = exports.LINE_OPTIONS = void 0;
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
exports.LINE_OPTIONS = [
    ...BASE_OPTIONS,
    'auto_range',
    'y_domain_max',
    'y_domain_min',
    'n_visible_points',
];
exports.TRACE_OPTIONS = [
    ...BASE_OPTIONS,
    'auto_range_x',
    'auto_range_y',
    'x_domain_max',
    'x_domain_min',
    'y_domain_max',
    'y_domain_min',
    'n_visible_points',
];
exports.BAR_OPTIONS = [
    ...BASE_OPTIONS,
    'auto_range',
    'y_domain_max',
    'y_domain_min',
];
exports.SPECTRO_OPTIONS = [
    ...BASE_OPTIONS,
    'window_size',
    'sample_rate',
    'n_visible_windows',
    'colormap_min',
    'colormap_max',
];
exports.OPTIONS = {
    'line': exports.LINE_OPTIONS,
    'trace': exports.TRACE_OPTIONS,
    'bar': exports.BAR_OPTIONS,
    'spectrogram': exports.SPECTRO_OPTIONS
};


/***/ }),

/***/ "./lib/scicharts/bar.js":
/*!******************************!*\
  !*** ./lib/scicharts/bar.js ***!
  \******************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Bar = exports.get_default_bar_plot_options = void 0;
const scichart_1 = __webpack_require__(/*! scichart */ "webpack/sharing/consume/default/scichart/scichart");
const baseplot_1 = __webpack_require__(/*! ./baseplot */ "./lib/scicharts/baseplot.js");
function get_default_bar_plot_options() {
    return {
        ...(0, baseplot_1.get_default_plot_options)(),
        name: 'Bar',
        auto_range: true,
        y_domain_max: 1,
        y_domain_min: 0
    };
}
exports.get_default_bar_plot_options = get_default_bar_plot_options;
class Bar extends baseplot_1.BasePlot {
    constructor(wasm_context, surface, plot_options = get_default_bar_plot_options(), sig_x_config = { key: '', idx: 0 }, sig_y_config = []) {
        super(wasm_context, surface, sig_x_config, sig_y_config);
        this.renderable_series = [];
        this.data_series = [];
        this.x_axis = new scichart_1.NumericAxis(this.wasm_context, { autoRange: scichart_1.EAutoRange.Always });
        this.y_axis = new scichart_1.NumericAxis(this.wasm_context, { growBy: new scichart_1.NumberRange(0, 0.2) });
        this.surface.xAxes.add(this.x_axis);
        this.surface.yAxes.add(this.y_axis);
        this.options = plot_options;
        this.sig_y.forEach(() => this.add_renderable(-1));
        this.update_y_domain();
        this.update_axes_alignment();
        this.update_axes_flipping();
        this.update_axes_visibility();
    }
    update_y_domain() {
        if (this.options.auto_range) {
            this.y_axis.autoRange = scichart_1.EAutoRange.Always;
        }
        else {
            this.y_axis.autoRange = scichart_1.EAutoRange.Never;
            this.y_axis.visibleRange = new scichart_1.NumberRange(this.options.y_domain_min, this.options.y_domain_max);
        }
    }
    update(data) {
        const data_series = this.data_series[0];
        if (data_series === undefined || this.data_series.length > 1)
            throw new Error('Bar should contain exactly one data series');
        data_series.clear();
        this.sig_y.forEach((sig_y, i) => {
            const y = this.check_and_fetch(data, sig_y);
            data_series.append(i, y[y.length - 1]);
        });
    }
    update_label_format() {
        const labels = this.sig_y.map((s) => s.name);
        const valid = labels.every((l) => l !== undefined);
        if (valid) {
            this.x_axis.labelProvider = new scichart_1.TextLabelProvider({
                labels: labels
            });
        }
        else {
            this.x_axis.labelProvider = new scichart_1.TextLabelProvider({
                labels: this.sig_y.map((sig) => sig.get_id())
            });
        }
    }
    add_renderable(at = -1) {
        if (at === -1)
            at = this.renderable_series.length;
        if (at > this.renderable_series.length)
            return;
        // Only one data series for bar plot
        if (this.data_series.length < 1) {
            const data_series = new scichart_1.XyDataSeries(this.wasm_context);
            data_series.isSorted = this.options.data_is_sorted;
            data_series.containsNaN = this.options.data_contains_nan;
            this.data_series.push(data_series);
        }
        const renderable_series = new scichart_1.FastColumnRenderableSeries(this.wasm_context, {
            dataLabels: {
                horizontalTextPosition: scichart_1.EHorizontalTextPosition.Center,
                verticalTextPosition: scichart_1.EVerticalTextPosition.Above,
                style: { fontFamily: "Arial", fontSize: 16, padding: new scichart_1.Thickness(0, 0, 20, 0) },
                color: "#FFFFFF",
            },
        });
        renderable_series.dataSeries = this.data_series[0];
        this.surface.renderableSeries.add(renderable_series);
        this.renderable_series.splice(at, 0, renderable_series);
        this.update_label_format();
    }
    update_all_options(options) {
        this.options = options;
        this.update_y_domain();
        this.update_axes_alignment();
        this.update_axes_flipping();
        this.update_axes_visibility();
        this.update_axes_visibility();
        this.update_data_optimizations();
        this.update_label_format();
    }
}
exports.Bar = Bar;


/***/ }),

/***/ "./lib/scicharts/baseplot.js":
/*!***********************************!*\
  !*** ./lib/scicharts/baseplot.js ***!
  \***********************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.BasePlot = exports.get_default_plot_options = void 0;
const scichart_1 = __webpack_require__(/*! scichart */ "webpack/sharing/consume/default/scichart/scichart");
const signal_1 = __webpack_require__(/*! ./signal */ "./lib/scicharts/signal.js");
function get_default_plot_options() {
    return {
        name: 'no_name',
        x_axis_align: 'bottom',
        y_axis_align: 'left',
        x_axis_flipped: false,
        y_axis_flipped: false,
        x_axis_visible: true,
        y_axis_visible: true,
        data_contains_nan: false,
        data_is_sorted: true
    };
}
exports.get_default_plot_options = get_default_plot_options;
class BasePlot {
    // #######################################################################################################
    constructor(wasm_context, surface, sig_x_config, sig_y_config) {
        this.wasm_context = wasm_context;
        this.surface = surface;
        this.sig_x = signal_1.Signal.from_config(sig_x_config);
        this.sig_y = sig_y_config.map((config) => signal_1.Signal.from_config(config));
    }
    /**
     * @param at - The index of the data series. If at is negative, then the index is counted from the end.
     * @returns The x-value at index at.
     */
    get_native_x(at) {
        const data_series = this.data_series[0]; // All series have the same x-values
        if (data_series === undefined)
            throw new Error('Data series is undefined');
        const count = data_series.count();
        const x_values = data_series.getNativeXValues();
        if (at < 0) {
            return x_values.get(Math.max(count + at, 0));
        }
        if (at >= count) {
            throw new Error(`Index ${at} out of bounds`);
        }
        return x_values.get(at);
    }
    axis_alignment(axis, axis_alignment) {
        switch (axis_alignment) {
            case 'top':
                axis.axisAlignment = scichart_1.EAxisAlignment.Top;
                break;
            case 'bottom':
                axis.axisAlignment = scichart_1.EAxisAlignment.Bottom;
                break;
            case 'left':
                axis.axisAlignment = scichart_1.EAxisAlignment.Left;
                break;
            case 'right':
                axis.axisAlignment = scichart_1.EAxisAlignment.Right;
                break;
            default:
                throw new Error(`Invalid axis alignment: ${axis_alignment}`);
        }
    }
    update_axes_alignment() {
        const x_is_horiz = ["top", "bottom"].includes(this.options.x_axis_align);
        const y_is_horiz = ["top", "bottom"].includes(this.options.y_axis_align);
        if (x_is_horiz != y_is_horiz) {
            this.axis_alignment(this.x_axis, this.options.x_axis_align);
            this.axis_alignment(this.y_axis, this.options.y_axis_align);
        }
    }
    update_axes_flipping() {
        this.x_axis.flippedCoordinates = this.options.x_axis_flipped;
        this.y_axis.flippedCoordinates = this.options.y_axis_flipped;
    }
    update_axes_visibility() {
        this.x_axis.isVisible = this.options.x_axis_visible;
        this.y_axis.isVisible = this.options.y_axis_visible;
    }
    update_data_optimizations() {
        this.data_series.forEach((ds) => {
            ds.containsNaN = this.options.data_contains_nan;
            ds.isSorted = this.options.data_is_sorted;
        });
    }
    get_options() {
        return this.options;
    }
    set_options(options) {
        this.update_all_options(options);
    }
    get_signal_configs() {
        return { 'sig_x': this.sig_x.get_config(), 'sig_y': this.sig_y.map((sig) => sig.get_config()) };
    }
    set_signals(sig_x, sig_y) {
        this.change_sig_x(sig_x);
        this.change_sig_y(sig_y);
    }
    /**
     * Updates the signal config for the x-axis. If the new signal config is different from the old one,
     * then all data series are cleared.
     * @param sig_x - The new signal config for the x-axis.
     */
    change_sig_x(config) {
        if (!(this.sig_x.compare_to(config))) {
            this.data_series.forEach((ds) => ds.clear());
            this.sig_x.set_config(config);
        }
    }
    /**
     * Updates the signal configs for the y-axis.
     * If old signals are no longer present in the new list, then the corresponding plots are removed.
     * If new signals are present in the new list, then new plots are created.
     * @param sig_y - The new signal configs for the y-axis.
     */
    change_sig_y(sig_y) {
        const new_signals = sig_y.map((config) => signal_1.Signal.from_config(config));
        // Note: Can be faster
        // Remove all signals that should no longer be drawn
        this.sig_y.forEach((old_sig, at) => {
            let is_old = true;
            new_signals.forEach((new_sig) => {
                if (new_sig.compare_to(old_sig)) {
                    is_old = false;
                }
            });
            if (is_old) {
                this.sig_y.splice(at, 1);
                this.remove_renderable(at);
            }
        });
        // Add all new signals that are not being drawn
        new_signals.forEach((new_sig) => {
            let is_new = true;
            this.sig_y.forEach((old_sig) => {
                if (new_sig.compare_to(old_sig)) {
                    old_sig.name = new_sig.name;
                    is_new = false;
                }
            });
            if (is_new) {
                this.sig_y.push(new_sig);
                this.add_renderable(-1);
            }
        });
    }
    /**
     * Access the data with the given signal config and throws errors.
     * @param data - The data to access
     * @param sig - The signal config to access
     * @returns data[sig.sig_key][sig.sig_idx]
     */
    check_and_fetch(data, sig) {
        if (sig === undefined)
            return [];
        if (!(sig.key in data))
            return []; //throw new Error(`sig_key ${sig_key} not in data`);
        if (sig.idx >= data[sig.key].length)
            return []; //throw new Error(`sig_idx ${sig_idx} out of bounds`);
        return data[sig.key][sig.idx];
    }
    /**
     * A function that specifies how to remove the renderable series, dataseries etc.
     * @param at - The index of the renderable series to remove, -1 for last.
     */
    remove_renderable(at) {
        if (at === -1)
            at = this.renderable_series.length - 1;
        if (at >= this.renderable_series.length)
            return;
        this.surface.renderableSeries.remove(this.renderable_series[at]);
        this.renderable_series[at]?.delete();
        this.renderable_series.splice(at, 1);
        // this.data_series[at]?.clear();
        this.data_series[at]?.delete();
        this.data_series.splice(at, 1);
    }
    delete() {
        this.surface.xAxes.remove(this.x_axis);
        this.surface.yAxes.remove(this.y_axis);
        this.x_axis.delete();
        this.y_axis.delete();
        this.renderable_series.forEach((rs) => rs.delete());
        this.data_series.forEach((ds) => ds.delete());
        this.surface.delete();
    }
}
exports.BasePlot = BasePlot;


/***/ }),

/***/ "./lib/scicharts/dashboard.js":
/*!************************************!*\
  !*** ./lib/scicharts/dashboard.js ***!
  \************************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Dashboard = void 0;
const line_1 = __webpack_require__(/*! ./line */ "./lib/scicharts/line.js");
const trace_1 = __webpack_require__(/*! ./trace */ "./lib/scicharts/trace.js");
const bar_1 = __webpack_require__(/*! ./bar */ "./lib/scicharts/bar.js");
const spectrogram_1 = __webpack_require__(/*! ./spectrogram */ "./lib/scicharts/spectrogram.js");
const layouts_1 = __webpack_require__(/*! ./layouts */ "./lib/scicharts/layouts.js");
const helpers_1 = __webpack_require__(/*! ../utils/helpers */ "./lib/utils/helpers.js");
class Dashboard {
    constructor(scichart_surface, wasm_context, layout_mode = layouts_1.ELayoutMode.DynamicGrid) {
        this.plots = [];
        this.scichart_surface = scichart_surface;
        this.wasm_context = wasm_context;
        this.layout = (0, layouts_1.layout_factory)(layout_mode);
    }
    /**
     *
     * @param type - The type of plot to add.
     * @param at - The index to add the plot at. If -1, the plot is added at the end.
    */
    add_plot(type, at = -1) {
        let plot;
        const sub_surface = this.scichart_surface.addSubChart(helpers_1.sub_surface_options);
        switch (type) {
            case "line":
                plot = new line_1.Line(this.wasm_context, sub_surface, (0, line_1.get_default_line_plot_options)());
                break;
            case "trace":
                plot = new trace_1.Trace(this.wasm_context, sub_surface, (0, trace_1.get_default_trace_plot_options)());
                break;
            case "bar":
                plot = new bar_1.Bar(this.wasm_context, sub_surface, (0, bar_1.get_default_bar_plot_options)());
                break;
            case "spectrogram":
                plot = new spectrogram_1.Spectrogram(this.wasm_context, sub_surface, (0, spectrogram_1.get_default_spectrogram_plot_options)());
                break;
            default:
                throw new Error("Unknown plot type: " + type);
        }
        if (at === -1)
            at = this.plots.length;
        this.plots.splice(at, 0, plot);
        this.update_layout();
    }
    /**
     * Change the layout of the dashboard which automatically updates.
     * @param mode - The layout mode to use.
     */
    set_layout_mode(mode) {
        this.layout = (0, layouts_1.layout_factory)(mode);
        this.update_layout();
    }
    update_layout() {
        this.layout.apply_layout(this.plots);
    }
    // TODO: Make this use id instead of index
    /**
     * @param at - The index of the plot to remove. If -1, the last plot is removed.
     */
    remove_plot(at = -1) {
        if (at === -1)
            at = this.plots.length - 1;
        if (at < 0 || at >= this.plots.length) {
            throw new Error(`Index ${at} not in range [0, ${this.plots.length})`);
        }
        this.scichart_surface.removeSubChart(this.plots[at]?.surface);
        this.plots[at]?.delete();
        this.plots.splice(at, 1);
        this.update_layout();
    }
    // ################################## Interface implementations ##################################
    update(data) {
        this.plots.forEach((plot) => plot.update(data));
    }
    delete() {
        this.plots.forEach((plot) => plot.delete());
        this.scichart_surface.delete();
    }
    [Symbol.iterator]() {
        let index = 0;
        const plots = this.plots;
        return {
            next: function () {
                if (index < plots.length) {
                    return { value: plots[index++], done: false };
                }
                else {
                    return { value: undefined, done: true };
                }
            },
        };
    }
}
exports.Dashboard = Dashboard;


/***/ }),

/***/ "./lib/scicharts/layouts.js":
/*!**********************************!*\
  !*** ./lib/scicharts/layouts.js ***!
  \**********************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.layout_factory = exports.Layout = exports.ELayoutMode = void 0;
const scichart_1 = __webpack_require__(/*! scichart */ "webpack/sharing/consume/default/scichart/scichart");
const helpers_1 = __webpack_require__(/*! ../utils/helpers */ "./lib/utils/helpers.js");
var ELayoutMode;
(function (ELayoutMode) {
    ELayoutMode["FixedGrid"] = "FixedGrid";
    ELayoutMode["DynamicGrid"] = "DynamicGrid";
    ELayoutMode["Custom"] = "Custom";
})(ELayoutMode = exports.ELayoutMode || (exports.ELayoutMode = {}));
class Layout {
}
exports.Layout = Layout;
class FixedGridLayout extends Layout {
    constructor(n_columns, n_rows) {
        super();
        const width = 1 / n_columns;
        const height = 1 / n_rows;
        this.rects = Array(n_rows * n_columns).fill(new scichart_1.Rect(0, 0, 1, 1)).map((_, i) => {
            const { row_idx, col_idx } = (0, helpers_1.get_position_index)(i, n_columns);
            const top = row_idx / n_rows;
            const left = col_idx / n_columns;
            return new scichart_1.Rect(left, top, width, height);
        });
    }
    apply_layout(plots) {
        plots.forEach((plot, i) => {
            const rect = this.rects[i % this.rects.length];
            if (rect === undefined) {
                throw new Error(`Rect at index ${i} is undefined`);
            }
            plot.surface.subPosition = rect;
        });
    }
}
class DynamicGridLayout extends Layout {
    apply_layout(plots) {
        const n_plots = plots.length;
        const n_columns = Math.ceil(Math.sqrt(n_plots));
        // coordinate system is [0, 1] x [0, 1]
        const width = 1 / n_columns;
        const height = 1 / Math.ceil(n_plots / n_columns);
        plots.forEach((plot, i) => {
            const { row_idx, col_idx } = (0, helpers_1.get_position_index)(i, n_columns);
            const top = row_idx * height;
            const left = col_idx * width;
            const rect = new scichart_1.Rect(left, top, width, height);
            plot.surface.subPosition = rect;
        });
    }
}
function layout_factory(mode) {
    switch (mode) {
        case ELayoutMode.FixedGrid:
            return new FixedGridLayout(2, 2);
        case ELayoutMode.DynamicGrid:
            return new DynamicGridLayout();
        case ELayoutMode.Custom:
            throw new Error("Not implemented");
        default:
            throw new Error("Unknown layout mode: " + mode);
    }
}
exports.layout_factory = layout_factory;


/***/ }),

/***/ "./lib/scicharts/line.js":
/*!*******************************!*\
  !*** ./lib/scicharts/line.js ***!
  \*******************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Line = exports.get_default_line_plot_options = void 0;
const scichart_1 = __webpack_require__(/*! scichart */ "webpack/sharing/consume/default/scichart/scichart");
const baseplot_1 = __webpack_require__(/*! ./baseplot */ "./lib/scicharts/baseplot.js");
function get_default_line_plot_options() {
    return {
        ...(0, baseplot_1.get_default_plot_options)(),
        name: 'Line',
        auto_range: true,
        y_domain_max: 1,
        y_domain_min: 0,
        n_visible_points: 1000
    };
}
exports.get_default_line_plot_options = get_default_line_plot_options;
class Line extends baseplot_1.BasePlot {
    constructor(wasm_context, surface, plot_options = get_default_line_plot_options(), sig_x_config = { key: '', idx: 0 }, sig_y_config = []) {
        super(wasm_context, surface, sig_x_config, sig_y_config);
        this.renderable_series = [];
        this.data_series = [];
        this.x_axis = new scichart_1.NumericAxis(this.wasm_context);
        this.y_axis = new scichart_1.NumericAxis(this.wasm_context);
        this.surface.xAxes.add(this.x_axis);
        this.surface.yAxes.add(this.y_axis);
        this.options = plot_options;
        this.sig_y.forEach(() => this.add_renderable(-1));
        // this.surface.chartModifiers.add(new MouseWheelZoomModifier());
        // this.surface.chartModifiers.add(new ZoomPanModifier());
        // this.surface.chartModifiers.add(new ZoomExtentsModifier({isAnimated: false}));
        // this.surface.chartModifiers.add(new LegendModifier({showCheckBoxes: false, showSeriesMarkers: true}));
        this.update_y_domain();
        this.update_axes_alignment();
        this.update_axes_flipping();
        this.update_axes_visibility();
    }
    update_x_domain() {
        const x_max = this.get_native_x(-1);
        const x_min = this.get_native_x(-this.options.n_visible_points);
        this.x_axis.visibleRange = new scichart_1.NumberRange(x_min, x_max);
    }
    update_y_domain() {
        if (this.options.auto_range) {
            this.y_axis.autoRange = scichart_1.EAutoRange.Always;
        }
        else {
            this.y_axis.autoRange = scichart_1.EAutoRange.Never;
            this.y_axis.visibleRange = new scichart_1.NumberRange(this.options.y_domain_min, this.options.y_domain_max);
        }
    }
    update(data) {
        const x = this.check_and_fetch(data, this.sig_x);
        this.sig_y.forEach((sig, i) => {
            const y = this.check_and_fetch(data, sig);
            this.data_series[i].appendRange(x, y);
        });
        if (this.sig_y.length === 0 || this.surface.zoomState == scichart_1.EZoomState.UserZooming)
            return;
        this.update_x_domain();
    }
    add_renderable(at = -1) {
        if (at === -1)
            at = this.renderable_series.length;
        if (at > this.renderable_series.length)
            return;
        const data_series = new scichart_1.XyDataSeries(this.wasm_context);
        data_series.isSorted = this.options.data_is_sorted;
        data_series.containsNaN = this.options.data_contains_nan;
        const renderable_series = new scichart_1.FastLineRenderableSeries(this.wasm_context, {
            stroke: 'auto',
            strokeThickness: 2,
        });
        renderable_series.dataSeries = data_series;
        this.surface.renderableSeries.add(renderable_series);
        this.renderable_series.splice(at, 0, renderable_series);
        this.data_series.splice(at, 0, data_series);
    }
    update_all_options(options) {
        this.options = options;
        this.update_x_domain();
        this.update_y_domain();
        this.update_axes_alignment();
        this.update_axes_flipping();
        this.update_axes_visibility();
        this.update_data_optimizations();
    }
}
exports.Line = Line;


/***/ }),

/***/ "./lib/scicharts/signal.js":
/*!*********************************!*\
  !*** ./lib/scicharts/signal.js ***!
  \*********************************/
/***/ ((__unused_webpack_module, exports) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Signal = void 0;
class Signal {
    constructor(key, idx, name) {
        this.name = '';
        this.key = key;
        this.idx = idx;
        this.update_name(name);
    }
    static from_config(sig) {
        return new Signal(sig.key, sig.idx, sig.name);
    }
    get_config() {
        return {
            key: this.key,
            idx: this.idx,
            name: this.name,
        };
    }
    set_config(sig) {
        this.key = sig.key;
        this.idx = sig.idx;
        this.update_name(sig.name);
    }
    // TODO: This is a bit of a hack but we want key and idx to be indicators of equality
    get_id() {
        return `${this.key}_${this.idx}`;
    }
    compare_to(o) {
        const other_signal = o instanceof Signal ? o : Signal.from_config(o);
        return this.get_id() === other_signal.get_id();
    }
    update_name(name) {
        if (name) {
            this.name = name;
        }
        else {
            this.name = `${this.key}_${this.idx}`;
        }
    }
}
exports.Signal = Signal;


/***/ }),

/***/ "./lib/scicharts/spectrogram.js":
/*!**************************************!*\
  !*** ./lib/scicharts/spectrogram.js ***!
  \**************************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Spectrogram = exports.get_default_spectrogram_plot_options = void 0;
const scichart_1 = __webpack_require__(/*! scichart */ "webpack/sharing/consume/default/scichart/scichart");
const baseplot_1 = __webpack_require__(/*! ./baseplot */ "./lib/scicharts/baseplot.js");
function get_default_spectrogram_plot_options() {
    return {
        ...(0, baseplot_1.get_default_plot_options)(),
        name: 'Spectrogram',
        window_size: 256,
        sample_rate: 100,
        n_visible_windows: 100,
        colormap_min: 0,
        colormap_max: 1,
    };
}
exports.get_default_spectrogram_plot_options = get_default_spectrogram_plot_options;
class Spectrogram extends baseplot_1.BasePlot {
    constructor(wasm_context, surface, plot_options = get_default_spectrogram_plot_options(), sig_x_config = { key: '', idx: 0 }, sig_y_config = []) {
        super(wasm_context, surface, sig_x_config, sig_y_config);
        this.renderable_series = [];
        this.data_series = [];
        this.x_axis = new scichart_1.NumericAxis(this.wasm_context, {
            autoRange: scichart_1.EAutoRange.Never,
            drawLabels: false,
            drawMinorTickLines: false,
            drawMajorTickLines: false,
        });
        this.y_axis = new scichart_1.NumericAxis(this.wasm_context, {
            autoRange: scichart_1.EAutoRange.Never,
            drawMinorTickLines: false,
            drawMajorTickLines: false,
        });
        this.surface.xAxes.add(this.x_axis);
        this.surface.yAxes.add(this.y_axis);
        this.options = plot_options;
        this.window_size = this.options.window_size;
        this.sample_rate = this.options.sample_rate;
        this.bin_count = Math.floor(this.window_size / 2) + 1;
        this.z_values = this.create_empty_2d();
        this.surface.chartModifiers.add(new scichart_1.MouseWheelZoomModifier());
        this.surface.chartModifiers.add(new scichart_1.ZoomPanModifier());
        this.surface.chartModifiers.add(new scichart_1.ZoomExtentsModifier());
        this.add_renderable();
        this.update_axes_alignment();
        this.update_axes_flipping();
        this.update_axes_visibility();
    }
    create_empty_2d() {
        return (0, scichart_1.zeroArray2D)([this.bin_count, this.options.n_visible_windows]);
    }
    update(data) {
        if (this.sig_y.length !== 1)
            return; // if no x signal is defined, then we can't update the plot
        const sig_key = this.sig_y[0].key;
        if (!(sig_key in data))
            throw new Error(`sig_key ${sig_key} not in data`);
        if (data[sig_key][0].length == 0)
            return; // no new data
        this.z_values = this.z_values.map((row, i) => row.concat(data[sig_key][i]).slice(-this.options.n_visible_windows));
        this.data_series[0].setZValues(this.z_values);
    }
    add_renderable(at = -1) {
        if (this.renderable_series.length > 0)
            return;
        this.data_series[0]?.delete();
        this.renderable_series[0]?.delete();
        this.data_series = [];
        this.renderable_series = [];
        const renderable_series = new scichart_1.UniformHeatmapRenderableSeries(this.wasm_context, {
            colorMap: new scichart_1.HeatmapColorMap({
                minimum: this.options.colormap_min,
                maximum: this.options.colormap_max,
                gradientStops: [
                    { offset: 0, color: "#000000" },
                    { offset: 0.25, color: "#800080" },
                    { offset: 0.5, color: "#FF0000" },
                    { offset: 0.75, color: "#FFFF00" },
                    { offset: 1, color: "#FFFFFF" }
                ]
            }),
            dataLabels: {
                numericFormat: scichart_1.ENumericFormat.NoFormat,
                precision: 10,
            }
        });
        this.z_values = this.create_empty_2d();
        const data_series = new scichart_1.UniformHeatmapDataSeries(this.wasm_context, {
            xStart: 0,
            xStep: 1,
            yStart: 0,
            yStep: this.options.sample_rate / this.options.window_size,
            zValues: this.z_values
        });
        renderable_series.dataSeries = data_series;
        this.surface.renderableSeries.add(renderable_series);
        this.renderable_series.push(renderable_series);
        this.data_series.push(data_series);
        this.x_axis.visibleRange = new scichart_1.NumberRange(0, this.options.n_visible_windows);
        this.y_axis.visibleRange = new scichart_1.NumberRange(0, (this.bin_count - 1) * this.options.sample_rate / this.options.window_size);
        this.x_axis.visibleRangeLimit = this.x_axis.visibleRange;
        this.y_axis.visibleRangeLimit = this.y_axis.visibleRange;
    }
    update_color_gradient() {
        this.renderable_series[0].colorMap = new scichart_1.HeatmapColorMap({
            minimum: this.options.colormap_min,
            maximum: this.options.colormap_max,
            gradientStops: [
                { offset: 0, color: "#000000" },
                { offset: 0.05, color: "#800080" },
                { offset: 0.2, color: "#FF0000" },
                { offset: 0.5, color: "#FFFF00" },
                { offset: 1, color: "#FFFFFF" }
            ]
        });
    }
    update_all_options(options) {
        this.options = options;
        this.bin_count = Math.floor(this.window_size / 2) + 1; // Should bin count be handled in the options?
        this.update_color_gradient();
        this.update_axes_alignment();
        this.update_axes_flipping();
        this.update_axes_visibility();
    }
}
exports.Spectrogram = Spectrogram;


/***/ }),

/***/ "./lib/scicharts/trace.js":
/*!********************************!*\
  !*** ./lib/scicharts/trace.js ***!
  \********************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Trace = exports.get_default_trace_plot_options = void 0;
const scichart_1 = __webpack_require__(/*! scichart */ "webpack/sharing/consume/default/scichart/scichart");
const baseplot_1 = __webpack_require__(/*! ./baseplot */ "./lib/scicharts/baseplot.js");
function get_default_trace_plot_options() {
    return {
        ...(0, baseplot_1.get_default_plot_options)(),
        name: 'Trace',
        data_is_sorted: false,
        auto_range_x: false,
        auto_range_y: false,
        x_domain_max: 2560,
        x_domain_min: 0,
        y_domain_max: 1440,
        y_domain_min: 0,
        n_visible_points: 100
    };
}
exports.get_default_trace_plot_options = get_default_trace_plot_options;
class Trace extends baseplot_1.BasePlot {
    constructor(wasm_context, surface, plot_options = get_default_trace_plot_options(), sig_x_config = { key: '', idx: 0 }, sig_y_config = []) {
        super(wasm_context, surface, sig_x_config, sig_y_config);
        this.renderable_series = [];
        this.data_series = [];
        this.x_axis = new scichart_1.NumericAxis(this.wasm_context);
        this.y_axis = new scichart_1.NumericAxis(this.wasm_context);
        this.surface.xAxes.add(this.x_axis);
        this.surface.yAxes.add(this.y_axis);
        this.options = plot_options;
        this.sig_y.forEach(() => this.add_renderable(-1));
        // this.surface.chartModifiers.add(new MouseWheelZoomModifier());
        // this.surface.chartModifiers.add(new ZoomPanModifier());
        // this.surface.chartModifiers.add(new ZoomExtentsModifier({onZoomExtents: () => {
        // 	if(!this.options.auto_range_x){
        // 		this.x_axis.visibleRange = new NumberRange(this.options.x_domain_min, this.options.x_domain_max);
        // 	}
        // 	if(!this.options.auto_range_y){
        // 		this.y_axis.visibleRange = new NumberRange(this.options.y_domain_min, this.options.y_domain_max);
        // 	}
        // 	return false
        // }}));
        this.update_axes_alignment();
        this.update_axes_flipping();
        this.update_axes_visibility();
        this.update_x_domains();
        this.update_y_domains();
        this.update_data_optimizations();
    }
    update_x_domains() {
        if (this.options.auto_range_x) {
            this.x_axis.autoRange = scichart_1.EAutoRange.Always;
            return;
        }
        this.x_axis.autoRange = scichart_1.EAutoRange.Never;
        const x_min = this.options.x_domain_min;
        const x_max = this.options.x_domain_max;
        this.x_axis.visibleRange = new scichart_1.NumberRange(x_min, x_max);
    }
    update_y_domains() {
        if (this.options.auto_range_y) {
            this.y_axis.autoRange = scichart_1.EAutoRange.Always;
            return;
        }
        this.y_axis.autoRange = scichart_1.EAutoRange.Never;
        const y_min = this.options.y_domain_min;
        const y_max = this.options.y_domain_max;
        this.y_axis.visibleRange = new scichart_1.NumberRange(y_min, y_max);
    }
    update(data) {
        const x = this.check_and_fetch(data, this.sig_x);
        this.sig_y.forEach((sig, i) => {
            const y = this.check_and_fetch(data, sig);
            const ds = this.data_series[i];
            if (ds === undefined)
                throw new Error(`Data series at ${i} is undefined`);
            ds.appendRange(x, y);
            if (ds.count() > this.options.n_visible_points) {
                ds.removeRange(0, ds.count() - this.options.n_visible_points);
            }
        });
    }
    add_renderable(at = -1) {
        if (at === -1)
            at = this.renderable_series.length;
        if (at > this.renderable_series.length)
            return;
        const data_series = new scichart_1.XyDataSeries(this.wasm_context);
        data_series.isSorted = this.options.data_is_sorted;
        data_series.containsNaN = this.options.data_contains_nan;
        const renderable_series = new scichart_1.FastLineRenderableSeries(this.wasm_context, {
            stroke: 'auto',
            strokeThickness: 2,
        });
        renderable_series.dataSeries = data_series;
        this.surface.renderableSeries.add(renderable_series);
        this.renderable_series.splice(at, 0, renderable_series);
        this.data_series.splice(at, 0, data_series);
    }
    update_all_options(options) {
        this.options = options;
        this.update_axes_alignment();
        this.update_axes_flipping();
        this.update_axes_visibility();
        this.update_x_domains();
        this.update_y_domains();
    }
}
exports.Trace = Trace;


/***/ }),

/***/ "./lib/spectrogram.js":
/*!****************************!*\
  !*** ./lib/spectrogram.js ***!
  \****************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


// Copyright (c) bjarni
// Distributed under the terms of the Modified BSD License.
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SpectrogramView = exports.SpectrogramModel = void 0;
const base_1 = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
const version_1 = __webpack_require__(/*! ./version */ "./lib/version.js");
const baseplot_view_1 = __webpack_require__(/*! ./baseplot_view */ "./lib/baseplot_view.js");
const options_1 = __webpack_require__(/*! ./options */ "./lib/options.js");
class SpectrogramModel extends base_1.DOMWidgetModel {
    defaults() {
        return {
            ...super.defaults(),
            _model_name: SpectrogramModel.model_name,
            _model_module: SpectrogramModel.model_module,
            _model_module_version: SpectrogramModel.model_module_version,
            _view_name: SpectrogramModel.view_name,
            _view_module: SpectrogramModel.view_module,
            _view_module_version: SpectrogramModel.view_module_version,
        };
    }
}
SpectrogramModel.model_name = 'SpectrogramModel';
SpectrogramModel.model_module = version_1.MODULE_NAME;
SpectrogramModel.model_module_version = version_1.MODULE_VERSION;
SpectrogramModel.view_name = 'SpectrogramView'; // Set to null if no view
SpectrogramModel.view_module = version_1.MODULE_NAME; // Set to null if no view
SpectrogramModel.view_module_version = version_1.MODULE_VERSION;
SpectrogramModel.serializers = {
    ...base_1.DOMWidgetModel.serializers,
};
exports.SpectrogramModel = SpectrogramModel;
class SpectrogramView extends baseplot_view_1.BasePlotView {
    render() {
        this.setup(options_1.SPECTRO_OPTIONS);
    }
}
exports.SpectrogramView = SpectrogramView;


/***/ }),

/***/ "./lib/trace.js":
/*!**********************!*\
  !*** ./lib/trace.js ***!
  \**********************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


// Copyright (c) BjarniHaukur
// Distributed under the terms of the Modified BSD License.
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.TraceView = exports.TraceModel = void 0;
const base_1 = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
const version_1 = __webpack_require__(/*! ./version */ "./lib/version.js");
const baseplot_view_1 = __webpack_require__(/*! ./baseplot_view */ "./lib/baseplot_view.js");
const options_1 = __webpack_require__(/*! ./options */ "./lib/options.js");
class TraceModel extends base_1.DOMWidgetModel {
    defaults() {
        return {
            ...super.defaults(),
            _model_name: TraceModel.model_name,
            _model_module: TraceModel.model_module,
            _model_module_version: TraceModel.model_module_version,
            _view_name: TraceModel.view_name,
            _view_module: TraceModel.view_module,
            _view_module_version: TraceModel.view_module_version,
        };
    }
}
TraceModel.model_name = 'TraceModel';
TraceModel.model_module = version_1.MODULE_NAME;
TraceModel.model_module_version = version_1.MODULE_VERSION;
TraceModel.view_name = 'TraceView'; // Set to null if no view
TraceModel.view_module = version_1.MODULE_NAME; // Set to null if no view
TraceModel.view_module_version = version_1.MODULE_VERSION;
TraceModel.serializers = {
    ...base_1.DOMWidgetModel.serializers,
};
exports.TraceModel = TraceModel;
class TraceView extends baseplot_view_1.BasePlotView {
    render() {
        this.setup(options_1.TRACE_OPTIONS);
    }
}
exports.TraceView = TraceView;


/***/ }),

/***/ "./lib/utils.js":
/*!**********************!*\
  !*** ./lib/utils.js ***!
  \**********************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.load_scichart = exports.create_plot_from_model = exports.get_all_from_model = exports.unpack_models = void 0;
const scichart_1 = __webpack_require__(/*! scichart */ "webpack/sharing/consume/default/scichart/scichart");
const BuildStamp_1 = __webpack_require__(/*! scichart/Core/BuildStamp */ "./node_modules/scichart/Core/BuildStamp.js");
const line_1 = __webpack_require__(/*! ./scicharts/line */ "./lib/scicharts/line.js");
const trace_1 = __webpack_require__(/*! ./scicharts/trace */ "./lib/scicharts/trace.js");
const bar_1 = __webpack_require__(/*! ./scicharts/bar */ "./lib/scicharts/bar.js");
const spectrogram_1 = __webpack_require__(/*! ./scicharts/spectrogram */ "./lib/scicharts/spectrogram.js");
const constants_1 = __webpack_require__(/*! ./utils/constants */ "./lib/utils/constants.js");
async function unpack_models(ipy_ids, manager) {
    const promises = ipy_ids.map((ipy_id) => {
        // Check that the id starts with the expected prefix.
        const model_id_prefix = 'IPY_MODEL_';
        if (!ipy_id.startsWith(model_id_prefix))
            throw new Error(`Invalid model id: ${ipy_id}`);
        // Get the model id.
        const model_id = ipy_id.slice(model_id_prefix.length);
        return manager.get_model(model_id);
    });
    return await Promise.all(promises);
}
exports.unpack_models = unpack_models;
function get_all_from_model(model, keys) {
    const options = {};
    for (const key of keys) {
        if (!(model.has(key)))
            throw new Error(`Key ${key} not found in model`);
        options[key] = model.get(key);
    }
    return options;
}
exports.get_all_from_model = get_all_from_model;
function create_plot_from_model(model, wasmContext, sub_surface, options) {
    const plot_type = model.get('_plot_type');
    const sig_x = model.get('sig_x');
    const sig_y = model.get('sig_y');
    switch (plot_type) {
        case 'line':
            return new line_1.Line(wasmContext, sub_surface, options, sig_x, sig_y);
        case 'trace':
            return new trace_1.Trace(wasmContext, sub_surface, options, sig_x, sig_y);
        case 'bar':
            return new bar_1.Bar(wasmContext, sub_surface, options, sig_x, sig_y);
        case 'spectrogram':
            return new spectrogram_1.Spectrogram(wasmContext, sub_surface, options, sig_x, sig_y);
        default:
            throw new Error(`Invalid plot type: ${plot_type}`);
    }
}
exports.create_plot_from_model = create_plot_from_model;
function load_scichart() {
    scichart_1.SciChartSurface.configure({
        dataUrl: `https://cdn.jsdelivr.net/npm/scichart@${BuildStamp_1.libraryVersion}/_wasm/scichart2d.data`,
        wasmUrl: `https://cdn.jsdelivr.net/npm/scichart@${BuildStamp_1.libraryVersion}/_wasm/scichart2d.wasm`
    });
    scichart_1.SciChartSurface.setRuntimeLicenseKey(constants_1.SCICHART_KEY);
}
exports.load_scichart = load_scichart;


/***/ }),

/***/ "./lib/utils/constants.js":
/*!********************************!*\
  !*** ./lib/utils/constants.js ***!
  \********************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.default_axis_options = exports.SCICHART_KEY = exports.MAX_BUFFER_SIZE = void 0;
const AutoRange_1 = __webpack_require__(/*! scichart/types/AutoRange */ "./node_modules/scichart/types/AutoRange.js");
const NumericFormat_1 = __webpack_require__(/*! scichart/types/NumericFormat */ "./node_modules/scichart/types/NumericFormat.js");
exports.MAX_BUFFER_SIZE = 10000000;
exports.SCICHART_KEY = 'V3gyfcWvx2tED1xhIYN88PAOAm81mECeXG/On8Mi7AHRU7xNoqSI0bfdzg9WaZt678Vv1kBZgLQVg/vZ2NU5wjyCZQ9b9nfpizcAB7vyq/BzXd4o8dlfEFsYdY76WoGmO2uduY95Vo18Rugw6ahktztv/uCw9Qe3RTZ7azrj4DBkkANuc8dkGSvZ0cEmthYiMVgzKiBDCu9TzXAH92GZrnpFZaiCv3Syicy6cSys6Y2UJW4uz7SfPjn6ORbF4TIAUm7jcVy0+/PCekZEcYQbFWhxCXsq3UX9V4WDjQcwrTLd6NvLoKWQhjL4970FaOkM2OXrHdeERg5jyresNn3TDMTOIo1uSQdlnSd3si89Kw9v/6VcRU3wm6lUywsuONUi8IoMdowg5UAPdhbzCHrDX+rVNDHQS8YmOzCe3EGFh9CwzQAGxuteYDkqXEhJ7wlkosOfJqT+Q9jtWmVLbJEYrfSJ6EJ94RUCjPwjwjyKUbkiq9Rv5buUbNouUsNNJWiX7vBV8+pJWxYh3skUQcsVOyg4xXVvsNl3GPsORqXB2YU9ZPwcOzOQrEqeraA6KMZxFM/M5jJo7zsItA==';
exports.default_axis_options = {
    useNativeText: true,
    isVisible: true,
    drawMajorBands: true,
    drawMinorGridLines: true,
    drawMinorTickLines: true,
    drawMajorTickLines: true,
    drawMajorGridLines: true,
    labelStyle: { fontSize: 8 },
    labelFormat: NumericFormat_1.ENumericFormat.Decimal,
    labelPrecision: 0,
    autoRange: AutoRange_1.EAutoRange.Never
};


/***/ }),

/***/ "./lib/utils/helpers.js":
/*!******************************!*\
  !*** ./lib/utils/helpers.js ***!
  \******************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.sub_surface_options = exports.get_position_index = void 0;
const Thickness_1 = __webpack_require__(/*! scichart/Core/Thickness */ "./node_modules/scichart/Core/Thickness.js");
const AnnotationBase_1 = __webpack_require__(/*! scichart/Charting/Visuals/Annotations/AnnotationBase */ "./node_modules/scichart/Charting/Visuals/Annotations/AnnotationBase.js");
/**
 * @param idx
 * @param n_cols
 * @returns Object with row_idx and col_idx properties.
 */
function get_position_index(idx, n_cols) {
    const row_idx = Math.floor(idx / n_cols);
    const col_idx = idx % n_cols;
    return { row_idx, col_idx };
}
exports.get_position_index = get_position_index;
// TODO: Here we can add Id / divId to the subchart options
exports.sub_surface_options = {
    coordinateMode: AnnotationBase_1.ECoordinateMode.Relative,
    subChartPadding: Thickness_1.Thickness.fromNumber(3),
    viewportBorder: {
        color: 'rgba(150, 74, 148, 0.51)',
        border: 2
    }
};


/***/ }),

/***/ "./lib/version.js":
/*!************************!*\
  !*** ./lib/version.js ***!
  \************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


// Copyright (c) BjarniHaukur
// Distributed under the terms of the Modified BSD License.
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MODULE_NAME = exports.MODULE_VERSION = void 0;
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
// eslint-disable-next-line @typescript-eslint/no-var-requires
const data = __webpack_require__(/*! ../package.json */ "./package.json");
/**
 * The _model_module_version/_view_module_version this package implements.
 *
 * The html widget manager assumes that this is the same as the npm package
 * version number.
 */
exports.MODULE_VERSION = data.version;
/*
 * The current package name.
 */
exports.MODULE_NAME = data.name;


/***/ }),

/***/ "./package.json":
/*!**********************!*\
  !*** ./package.json ***!
  \**********************/
/***/ ((module) => {

module.exports = JSON.parse('{"name":"genki-widgets","version":"0.1.0","description":"A custom plotting library using SciChartJS","keywords":["jupyter","jupyterlab","jupyterlab-extension","widgets"],"files":["lib/**/*.js","dist/*.js","css/*.css"],"homepage":"https://github.com/genkiinstruments/genki-widgets","bugs":{"url":"https://github.com/genkiinstruments/genki-widgets/issues"},"license":"BSD-3-Clause","author":{"name":"BjarniHaukur","email":"bjarni@genkiinstruments.com"},"main":"lib/index.js","types":"./lib/index.d.ts","repository":{"type":"git","url":"https://github.com/genkiinstruments/genki-widgets"},"scripts":{"build":"yarn run build:lib && yarn run build:nbextension && yarn run build:labextension:dev","build:prod":"yarn run build:lib && yarn run build:nbextension && yarn run build:labextension","build:labextension":"jupyter labextension build .","build:labextension:dev":"jupyter labextension build --development True .","build:lib":"tsc","build:nbextension":"webpack","clean":"yarn run clean:lib && yarn run clean:nbextension && yarn run clean:labextension","clean:lib":"rimraf lib","clean:labextension":"rimraf genki_widgets/labextension","clean:nbextension":"rimraf genki_widgets/nbextension/static/index.js","lint":"eslint . --ext .ts,.tsx --fix","lint:check":"eslint . --ext .ts,.tsx","prepack":"yarn run build:lib","test":"jest","watch":"npm-run-all -p watch:*","watch:lib":"tsc -w","watch:nbextension":"webpack --watch --mode=development","watch:labextension":"jupyter labextension watch ."},"dependencies":{"@jupyter-widgets/base":"^6","scichart":"^3.1.333"},"devDependencies":{"@babel/core":"^7.21.4","@babel/preset-env":"^7.21.4","@jupyter-widgets/base-manager":"^1.0.5","@jupyterlab/builder":"^3.6.3","@lumino/application":"^2.1.1","@lumino/widgets":"^2.1.1","@types/jest":"^29.5.1","@types/node":"^18.16.1","@types/webpack-env":"^1.18.0","@typescript-eslint/eslint-plugin":"^5.59.1","@typescript-eslint/parser":"^5.59.1","acorn":"^8.8.2","css-loader":"^6.7.3","eslint":"^8.39.0","eslint-config-prettier":"^8.8.0","eslint-plugin-prettier":"^4.2.1","fs-extra":"^11.1.1","identity-obj-proxy":"^3.0.0","jest":"^29.5.0","mkdirp":"^3.0.1","npm-run-all":"^4.1.5","prettier":"^2.8.8","rimraf":"^5.0.0","source-map-loader":"^4.0.1","style-loader":"^3.3.2","ts-jest":"^29.1.0","ts-loader":"^9.4.2","typescript":"~5.0.4","webpack":"^5.81.0","webpack-cli":"^5.0.2"},"jupyterlab":{"extension":"lib/plugin","outputDir":"genki_widgets/labextension/","sharedPackages":{"@jupyter-widgets/base":{"bundled":false,"singleton":true}}}}');

/***/ })

}]);
//# sourceMappingURL=lib_bar_js-lib_dashboard_js-lib_line_js-lib_spectrogram_js-lib_trace_js.8a25edd24886d9e09bba.js.map