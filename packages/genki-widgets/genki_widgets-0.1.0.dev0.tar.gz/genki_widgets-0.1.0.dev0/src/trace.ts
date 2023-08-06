// Copyright (c) BjarniHaukur
// Distributed under the terms of the Modified BSD License.

import {
  DOMWidgetModel,
  type ISerializers,
} from '@jupyter-widgets/base';

import { MODULE_NAME, MODULE_VERSION } from './version';

import { BasePlotView } from './baseplot_view';
import { TRACE_OPTIONS } from './options';



export class TraceModel extends DOMWidgetModel {
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

  static model_name = 'TraceModel';
  static model_module = MODULE_NAME;
  static model_module_version = MODULE_VERSION;
  static view_name = 'TraceView'; // Set to null if no view
  static view_module = MODULE_NAME; // Set to null if no view
  static view_module_version = MODULE_VERSION;

  static serializers: ISerializers = {
    ...DOMWidgetModel.serializers,
  };
}

export class TraceView extends BasePlotView {
  render() {
    this.setup(TRACE_OPTIONS);
  }
}
