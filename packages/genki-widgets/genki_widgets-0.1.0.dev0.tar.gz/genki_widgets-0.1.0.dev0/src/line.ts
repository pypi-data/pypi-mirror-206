// Copyright (c) BjarniHaukur
// Distributed under the terms of the Modified BSD License.

import {
  DOMWidgetModel,
  type ISerializers,
} from '@jupyter-widgets/base';


import { MODULE_NAME, MODULE_VERSION } from './version';

import { BasePlotView } from './baseplot_view';
import { LINE_OPTIONS } from './options';

export class LineModel extends DOMWidgetModel {
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

  static model_name = 'LineModel';
  static model_module = MODULE_NAME;
  static model_module_version = MODULE_VERSION;
  static view_name = 'LineView'; // Set to null if no view
  static view_module = MODULE_NAME; // Set to null if no view
  static view_module_version = MODULE_VERSION;

  static serializers: ISerializers = {
    ...DOMWidgetModel.serializers,
  };
}


export class LineView extends BasePlotView {
  render() {
    this.setup(LINE_OPTIONS);
  }
}


