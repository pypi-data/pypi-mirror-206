import { DOMWidgetView } from "@jupyter-widgets/base";


import { SciChartSurface } from "scichart";

import { sub_surface_options } from "./utils/helpers";
import { create_plot_from_model, get_all_from_model, load_scichart } from "./utils";
import { BasePlot } from "./scicharts/baseplot";


export class BasePlotView extends DOMWidgetView {
    plot: BasePlot = null;
    
    setup(plot_option_keys: string[]) {
        load_scichart();
        const plot_widget = document.createElement('div');
        plot_widget.setAttribute('id', Date.now().toString()); // Hack to make sure the id is unique
        plot_widget.setAttribute('style', 'width: 100%; height: 450px;');
        // plot_widget.classList.add('scichart-root'); // Should be styled by css/widget.css but doesn't work
        this.el.appendChild(plot_widget);

        const promise = SciChartSurface.create(plot_widget);
        promise.then((value) => {
            const { sciChartSurface, wasmContext } = value;
            const sub_surface = sciChartSurface.addSubChart(sub_surface_options);

            const options = get_all_from_model(this.model, plot_option_keys) as any;

            this.plot = create_plot_from_model(this.model, wasmContext, sub_surface, options);
            this.model.on('change:data', () => {
                const data = this.model.get('data');
                this.plot.update(data);
            });

            for (const key of plot_option_keys) {
                this.model.on(`change:${key}`, () => {
                    const options = this.plot.get_options() as any;
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


