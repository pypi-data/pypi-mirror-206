import {
	FastColumnRenderableSeries,
    EAutoRange,
	NumberRange,
	NumericAxis,
	SciChartSubSurface,
	XyDataSeries,
    EHorizontalTextPosition,
    EVerticalTextPosition,
    TextLabelProvider,
    Thickness,
	type TSciChart
} from 'scichart';

import { BasePlot, get_default_plot_options, type PlotOptions } from './baseplot';
import type { IArrayDict } from './interfaces';
import type { ISignalConfig } from './signal';

export interface BarPlotOptions extends PlotOptions {
    /** If auto range is true, then y_domain_max and y_domain_min are not used */
	auto_range: boolean;
	y_domain_max: number;
	y_domain_min: number;
}
export function get_default_bar_plot_options(): BarPlotOptions {
	return {
		...get_default_plot_options(),
		name: 'Bar',
        auto_range: true,
		y_domain_max: 1,
		y_domain_min: 0
	};
}

export class Bar extends BasePlot {
	x_axis: NumericAxis;
	y_axis: NumericAxis;
	options: BarPlotOptions;

	renderable_series: FastColumnRenderableSeries[] = [];
	data_series: XyDataSeries[] = [];

	constructor(
		wasm_context: TSciChart,
		surface: SciChartSubSurface,
		plot_options: BarPlotOptions = get_default_bar_plot_options(),
		sig_x_config: ISignalConfig = { key: '', idx: 0 },
		sig_y_config: ISignalConfig[] = []
	) {
		super(wasm_context, surface, sig_x_config, sig_y_config);

		this.x_axis = new NumericAxis(this.wasm_context, {autoRange: EAutoRange.Always});
		this.y_axis = new NumericAxis(this.wasm_context, {growBy: new NumberRange(0,0.2)});
		this.surface.xAxes.add(this.x_axis);
		this.surface.yAxes.add(this.y_axis);

		this.options = plot_options;

		this.sig_y.forEach(() => this.add_renderable(-1));

		this.update_y_domain();
		this.update_axes_alignment();
		this.update_axes_flipping();
		this.update_axes_visibility();
	}

	private update_y_domain(): void {
		if (this.options.auto_range) {
			this.y_axis.autoRange = EAutoRange.Always;
		} else {
			this.y_axis.autoRange = EAutoRange.Never;
			this.y_axis.visibleRange = new NumberRange(
				this.options.y_domain_min,
				this.options.y_domain_max
			);
		}
	}

	public update(data: IArrayDict): void {
		const data_series = this.data_series[0];
		if (data_series === undefined || this.data_series.length > 1) throw new Error('Bar should contain exactly one data series');
        data_series.clear();
		this.sig_y.forEach((sig_y, i) => {
			const y = this.check_and_fetch(data, sig_y);
			data_series.append(i, y[y.length-1]);
		});
	}

	private update_label_format(){
		const labels = this.sig_y.map((s) => s.name);
		
		const valid = labels.every((l) => l !== undefined);

		if (valid) {
			this.x_axis.labelProvider = new TextLabelProvider({
				labels: labels
			});
		}
		else {
			this.x_axis.labelProvider = new TextLabelProvider({
				labels: this.sig_y.map((sig) => sig.get_id())
			});
		}
    }

	protected add_renderable(at: number = -1): void {
		if (at === -1) at = this.renderable_series.length;
		if (at > this.renderable_series.length) return;
		
		// Only one data series for bar plot
		if (this.data_series.length < 1) {
			const data_series = new XyDataSeries(this.wasm_context);
			data_series.isSorted = this.options.data_is_sorted;
			data_series.containsNaN = this.options.data_contains_nan;
			this.data_series.push(data_series);
		}

		const renderable_series = new FastColumnRenderableSeries(this.wasm_context, {
            dataLabels: {
                horizontalTextPosition: EHorizontalTextPosition.Center,
                verticalTextPosition: EVerticalTextPosition.Above,
                style: { fontFamily: "Arial", fontSize: 16, padding: new Thickness(0,0,20,0) },
                color: "#FFFFFF",
            },
        });
		renderable_series.dataSeries = this.data_series[0];

		this.surface.renderableSeries.add(renderable_series);
		this.renderable_series.splice(at, 0, renderable_series);

        this.update_label_format();
	}


	public update_all_options(options: BarPlotOptions): void {
		this.options = options

		this.update_y_domain();
		this.update_axes_alignment();
		this.update_axes_flipping();
		this.update_axes_visibility();
		this.update_axes_visibility();
		this.update_data_optimizations();
		this.update_label_format();
	}
}
