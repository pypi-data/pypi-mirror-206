// Copyright (c) bjarni
// Distributed under the terms of the Modified BSD License.

import {
  DOMWidgetModel,
  type ISerializers,
} from '@jupyter-widgets/base';


import { MODULE_NAME, MODULE_VERSION } from './version';

import { BasePlotView } from './baseplot_view';
import { SPECTRO_OPTIONS } from './options';


export class SpectrogramModel extends DOMWidgetModel {
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

  static model_name = 'SpectrogramModel';
  static model_module = MODULE_NAME;
  static model_module_version = MODULE_VERSION;
  static view_name = 'SpectrogramView'; // Set to null if no view
  static view_module = MODULE_NAME; // Set to null if no view
  static view_module_version = MODULE_VERSION;

  static serializers: ISerializers = {
    ...DOMWidgetModel.serializers,
  };
}


export class SpectrogramView extends BasePlotView {
  render() {
    this.setup(SPECTRO_OPTIONS);
  }
}
