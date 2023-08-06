import React from 'react';
import { JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application';
import { ISettingRegistry } from '@jupyterlab/settingregistry';
import { Scheduler } from '@jupyterlab/scheduler';
import { pluginIds } from '../constants';
import { CreateNotebookJob } from '../widgets/CreateNotebookJob';

// This should only load up when the open source @jupyterlab/scheduler extension is installed and activated
// autoStart is set to false as this should only load when a plugin requests the Scheduler.IAdvancedOptions token
const ScheduleNotebookPlugin: JupyterFrontEndPlugin<Scheduler.IAdvancedOptions> = {
  id: pluginIds.SchedulerPlugin,
  autoStart: false,
  requires: [ISettingRegistry],
  provides: Scheduler.IAdvancedOptions,
  activate: (app: JupyterFrontEnd, settingRegistry: ISettingRegistry) => {
    return (props) => {
      const requestClient = app.serviceManager.serverSettings;
      const contentClient = app.serviceManager.contents;

      return (
        <CreateNotebookJob
          requestClient={requestClient}
          contentsManager={contentClient}
          settingRegistry={settingRegistry}
          commands={app.commands}
          {...props}
        />
      );
    };
  },
};

export { ScheduleNotebookPlugin };
