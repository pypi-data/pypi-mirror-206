import type { DOMWidgetModel, WidgetModel } from "@jupyter-widgets/base";

import { SciChartSurface, type SciChartSubSurface, type TSciChart } from "scichart";
import { libraryVersion } from "scichart/Core/BuildStamp";

import { Line, LinePlotOptions } from './scicharts/line';
import { Trace, TracePlotOptions } from './scicharts/trace';
import { Bar, BarPlotOptions } from './scicharts/bar';
import { Spectrogram, SpectrogramPlotOptions } from './scicharts/spectrogram';
import { SCICHART_KEY } from "./utils/constants";

export async function unpack_models(ipy_ids: string[], manager: any): Promise<DOMWidgetModel[]> {
  const promises = ipy_ids.map((ipy_id: string) => {
    // Check that the id starts with the expected prefix.
    const model_id_prefix = 'IPY_MODEL_';
    if (!ipy_id.startsWith(model_id_prefix)) throw new Error(`Invalid model id: ${ipy_id}`);
    // Get the model id.
    const model_id = ipy_id.slice(model_id_prefix.length);
    return manager.get_model(model_id);
  });
  return await Promise.all(promises);
}

export function get_all_from_model(model: WidgetModel, keys: string[]) {
  const options: { [k: string]: any } = {};
  for (const key of keys) {
      if (!(model.has(key))) throw new Error(`Key ${key} not found in model`);
      options[key] = model.get(key);
  }
  return options;
}

export function create_plot_from_model(
    model: WidgetModel,
    wasmContext: TSciChart,
    sub_surface: SciChartSubSurface,
    options: LinePlotOptions | TracePlotOptions | BarPlotOptions | SpectrogramPlotOptions
): Line | Trace | Bar | Spectrogram {
  const plot_type = model.get('_plot_type');
  const sig_x = model.get('sig_x');
  const sig_y = model.get('sig_y');
  switch (plot_type) {
      case 'line':
          return new Line(wasmContext, sub_surface, options as LinePlotOptions, sig_x, sig_y);
      case 'trace':
          return new Trace(wasmContext, sub_surface, options as TracePlotOptions, sig_x, sig_y);
      case 'bar':
          return new Bar(wasmContext, sub_surface, options as BarPlotOptions, sig_x, sig_y);
      case 'spectrogram':
          return new Spectrogram(wasmContext, sub_surface, options as SpectrogramPlotOptions, sig_x, sig_y);
      default:
          throw new Error(`Invalid plot type: ${plot_type}`);
  }
}

export function load_scichart() {
  SciChartSurface.configure({
      dataUrl: `https://cdn.jsdelivr.net/npm/scichart@${libraryVersion}/_wasm/scichart2d.data`,
      wasmUrl: `https://cdn.jsdelivr.net/npm/scichart@${libraryVersion}/_wasm/scichart2d.wasm`
  });
  SciChartSurface.setRuntimeLicenseKey(SCICHART_KEY);
}

