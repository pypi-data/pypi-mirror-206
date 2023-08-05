import { ILabShell, JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application';
import { ClusterStore } from './store';
import { ToolbarExtension } from './toolbar';
import { cellFactory } from './cellSelect';
import '../style/index.css';
import { LabIcon } from '@jupyterlab/ui-components';
import logoSvgStr from '../style/bodo-icon-green.svg';
import { BodoClusterListSidebar } from './sidebar';
import { plugin as terminalExtension } from './clusterTerminal/clusterTerminalExtension';

const activate = (app: JupyterFrontEnd, labShell: ILabShell): void => {
  console.log('Bodo JupyterLab extension activated!');

  const _cluster_store = new ClusterStore();

  // Toolbar (select cluster from inside notebook)
  app.docRegistry.addWidgetExtension('Notebook', new ToolbarExtension(_cluster_store, null));
  // Sidebar to display clusters
  const sidebar = new BodoClusterListSidebar(_cluster_store, app);
  sidebar.id = 'bodo-cluster-list';
  sidebar.title.icon = new LabIcon({
    name: 'bodo_jupyterlab:logo',
    svgstr: logoSvgStr,
  });
  sidebar.title.caption = 'Bodo Clusters';

  labShell.add(sidebar, 'left', { rank: 200 });
};

/**
 * Initialization for the bodo-jupyterlab extension.
 */
const plugins: JupyterFrontEndPlugin<any>[] = [
  {
    id: 'bodo-labextension:plugin',
    autoStart: true,
    requires: [ILabShell],
    activate,
  },
  terminalExtension,
  cellFactory,
];

export default plugins;
