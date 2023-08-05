import { Widget } from '@lumino/widgets';
import { Dialog } from '@jupyterlab/apputils';
import { Globals, SN_FILE_LIBRARY_URL } from './config';

export class SkillsNetworkFileLibraryWidget extends Widget {
    constructor(nbPanelId: string) {
      const frame = document.createElement('iframe');
      frame.src = `${SN_FILE_LIBRARY_URL}?atlas_token=${Globals.TOKENS.get(nbPanelId)}`
      frame.setAttribute("frameborder", "0")
      frame.setAttribute("allow", "clipboard-read; clipboard-write")
      frame.classList.add("sn-file-library-frame");
      super({ node: frame });
    }
}

export class SkillsNetworkFileLibrary {
    #nbPanelId: string;

    constructor(nbPanelId: string) {
      this.#nbPanelId = nbPanelId;
    }

    launch(){
      const imgLibDialog = new Dialog({title: "Skills Network File Library",
        body:  new SkillsNetworkFileLibraryWidget(this.#nbPanelId),
        hasClose: true,
        buttons: []
      });
      const dialogContent = imgLibDialog.node.querySelector(".jp-Dialog-content")
      if (dialogContent){
        dialogContent.classList.add("sn-file-library-dialog");
      }
      imgLibDialog.launch()
    }
}
