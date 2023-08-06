// Copyright (c) bjarni
// Distributed under the terms of the Modified BSD License.

import {
  DOMWidgetModel,
  type ISerializers,
} from '@jupyter-widgets/base';


import { MODULE_NAME, MODULE_VERSION } from './version';


import { BasePlotView } from './baseplot_view';
import { BAR_OPTIONS } from './options';


export class BarModel extends DOMWidgetModel {
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

  static model_name = 'BarModel';
  static model_module = MODULE_NAME;
  static model_module_version = MODULE_VERSION;
  static view_name = 'BarView'; // Set to null if no view
  static view_module = MODULE_NAME; // Set to null if no view
  static view_module_version = MODULE_VERSION;

  static serializers: ISerializers = {
    ...DOMWidgetModel.serializers,
  };
}

export class BarView extends BasePlotView {
  render() {
    this.setup(BAR_OPTIONS)
  }
}
