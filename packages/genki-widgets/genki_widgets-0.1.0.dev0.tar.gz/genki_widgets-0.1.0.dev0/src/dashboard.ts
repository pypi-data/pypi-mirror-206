// Copyright (c) bjarni
// Distributed under the terms of the Modified BSD License.

import { MODULE_NAME, MODULE_VERSION } from './version';

import {
    DOMWidgetModel,
    DOMWidgetView,
    WidgetModel,
    type ISerializers,
} from '@jupyter-widgets/base';

import { SciChartSurface } from 'scichart';

import { Dashboard } from './scicharts/dashboard';
import { get_all_from_model, load_scichart, unpack_models } from './utils';
import { OPTIONS } from './options';

export class DashboardModel extends DOMWidgetModel {
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

    static serializers: ISerializers = {
        ...DOMWidgetModel.serializers,
        plot_widgets: { deserialize: unpack_models }
    };

    static model_name = 'DashboardModel';
    static model_module = MODULE_NAME;
    static model_module_version = MODULE_VERSION;
    static view_name = 'DashboardView'; // Set to null if no view
    static view_module = MODULE_NAME; // Set to null if no view
    static view_module_version = MODULE_VERSION;
}



export class DashboardView extends DOMWidgetView {
    dashboard: Dashboard = null;
    plot_widgets: WidgetModel[] = [];

    render() {
        load_scichart();
        const dashboard_el = document.createElement('div');
        dashboard_el.setAttribute('id', Date.now().toString());
        dashboard_el.setAttribute('style', 'width: 100%; height: 450px; background-color: transparent;');
        // dashboard_el.classList.add('scichart-root'); // Should be styled by css/widget.css but doesn't work
        this.el.appendChild(dashboard_el);

        const promise = SciChartSurface.create(dashboard_el);
        promise.then((value) => {
            const { sciChartSurface, wasmContext } = value;

            this.plot_widgets = this.model.get('plot_widgets');
            this.dashboard = new Dashboard(sciChartSurface, wasmContext);

            this.plot_widgets.forEach((plot_widget, i) => {
                const sig_x = plot_widget.get('sig_x');
                const sig_y = plot_widget.get('sig_y');
                const plot_type = plot_widget.get('_plot_type');
                this.dashboard.add_plot(plot_type, -1);
                const subplot = this.dashboard.plots[i];
                
                const options = get_all_from_model(plot_widget, OPTIONS[plot_type]);
                subplot.set_signals(sig_x, sig_y);
                subplot.set_options(options as any);

                for (const key of OPTIONS[plot_type]) {
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
