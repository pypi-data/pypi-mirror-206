import { JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application';
import { IMainMenu } from '@jupyterlab/mainmenu';
import { Menu, Widget } from '@lumino/widgets';
import { Dialog, showDialog } from '@jupyterlab/apputils';
import { INotebookTracker } from '@jupyterlab/notebook';
import { IDocumentManager } from '@jupyterlab/docmanager';
import { show_spinner, showFailureImportLabDialog } from '../dialog';
import { MODE } from '../config';
import { openLab } from '../tools';

export const menu: JupyterFrontEndPlugin<void> = {
  id: 'skillsnetwork-authoring-extension:menu',
  autoStart: true,
  requires: [IMainMenu, INotebookTracker, IDocumentManager],
  activate: async (app: JupyterFrontEnd, mainMenu: IMainMenu, notebookTracker: INotebookTracker, docManager: IDocumentManager) => {

    console.log('Activated skillsnetwork-authoring-extension menu plugin!');

    if (await MODE() == "learn") return

    const editLabFromToken = 'edit-lab-from-token';
    app.commands.addCommand(editLabFromToken, {
    label: 'Edit a Lab',
    execute: () => {
      showTokenDialog(notebookTracker, docManager);
    }
    })

    const { commands } = app;

    // Create a new menu
    const menu: Menu = new Menu({ commands });
    menu.title.label = 'Skills Network';
    mainMenu.addMenu(menu, { rank: 80 });

    // Add command to menu
    menu.addItem({
    command: editLabFromToken,
    args: {}
    });

    const showTokenDialog = (notebookTracker: INotebookTracker, docManager: IDocumentManager) => {

      // Generate Dialog body
      let bodyDialog = document.createElement('div');
      let nameLabel = document.createElement('label');
      nameLabel.textContent = "Enter your authorization token: "
      let tokenInput = document.createElement('input');
      tokenInput.className = "jp-mod-styled";
      bodyDialog.appendChild(nameLabel);
      bodyDialog.appendChild(tokenInput);

      showDialog({
        title: "Edit a Lab",
        body: new Widget({node: bodyDialog}),
        buttons: [Dialog.cancelButton(), Dialog.okButton()]
      }).then(async result => {
        if (result.button.accept){
          show_spinner('Loading up your lab...');

          const token = tokenInput.value
          await openLab(token, docManager);
        }
      })
      .catch((e) => {
        Dialog.flush(); //remove spinner
        showFailureImportLabDialog();
        console.log(e)
      });
    };
  }
};
