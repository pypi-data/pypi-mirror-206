// Copyright (c) BjarniHaukur
// Distributed under the terms of the Modified BSD License.

import { Application, IPlugin } from '@lumino/application';

import { Widget } from '@lumino/widgets';

import { IJupyterWidgetRegistry } from '@jupyter-widgets/base';

import * as lineExports from './line';
import * as traceExports from './trace';
import * as barExports from './bar';
import * as spectrogramExports from './spectrogram';
import * as dashboardExports from './dashboard';

import { MODULE_NAME, MODULE_VERSION } from './version';

const EXTENSION_ID = 'genki-widgets:plugin';

/**
 * The example plugin.
 */
const examplePlugin: IPlugin<Application<Widget>, void> = {
  id: EXTENSION_ID,
  requires: [IJupyterWidgetRegistry],
  activate: activateWidgetExtension,
  autoStart: true,
} as unknown as IPlugin<Application<Widget>, void>;
// the "as unknown as ..." typecast above is solely to support JupyterLab 1
// and 2 in the same codebase and should be removed when we migrate to Lumino.

export default examplePlugin;

/**
 * Activate the widget extension.
 */
function activateWidgetExtension(
  app: Application<Widget>,
  registry: IJupyterWidgetRegistry
): void {
  registry.registerWidget({
    name: MODULE_NAME,
    version: MODULE_VERSION,
    exports: lineExports,
  });
  registry.registerWidget({
    name: MODULE_NAME,
    version: MODULE_VERSION,
    exports: traceExports,
  });
  registry.registerWidget({
    name: MODULE_NAME,
    version: MODULE_VERSION,
    exports: barExports,
  });
  registry.registerWidget({
    name: MODULE_NAME,
    version: MODULE_VERSION,
    exports: spectrogramExports,
  });
  registry.registerWidget({
    name: MODULE_NAME,
    version: MODULE_VERSION,
    exports: dashboardExports,
  });
}
