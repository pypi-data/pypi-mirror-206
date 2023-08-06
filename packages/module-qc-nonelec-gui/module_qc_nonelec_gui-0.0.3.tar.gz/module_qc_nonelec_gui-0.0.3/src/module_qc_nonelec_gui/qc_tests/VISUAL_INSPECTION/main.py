from __future__ import annotations

import json
import logging
import pprint
import shutil
import subprocess
from pathlib import Path

from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox

from module_qc_nonelec_gui.dbinterface import localdb_uploader
from module_qc_nonelec_gui.qc_tests.VISUAL_INSPECTION import (
    inspection_win,
    shaping_win,
    splitimg_win,
    summary_win,
    vi_initial_win,
)
from module_qc_nonelec_gui.qc_tests.VISUAL_INSPECTION.functions.cv2_func import (
    cv2,
    img_rotate,
    read_img,
    write_img,
)

log = logging.getLogger(__name__)


class TestWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.parent = parent

        self.setGeometry(0, 0, 500, 300)

        self.temp_dir_path = "/var/tmp/modulq-qc-nonelec-gui/vi"
        try:
            Path(self.temp_dir_path).mkdir(parents=True)
        except FileExistsError:
            shutil.rmtree(self.temp_dir_path)
            Path(self.temp_dir_path).mkdir(parents=True)

        # window title
        self.setWindowTitle("Visual Inspection GUI")

        # list and dict of anomalies
        self.anomaly_dic = {}
        self.comment_dic = {}
        self.img_dic = {}

        # component and user information
        self.atlsn = self.parent.info_dict["component"]
        self.type_name = self.parent.info_dict["componentType"]
        # self.original_institution = self.parent.info_dict["institution"]
        # self.current_location = self.parent.info_dict["currentLocation"]
        if self.type_name in ["MODULE", "PCB"]:
            self.stage = self.parent.info_dict["currentStage"]
            self.inspector = self.parent.db_user
        else:
            self.stage = ""
            self.inspector = ""

        # load configuration file
        log.info(f"type_name = {self.type_name}")
        log.info(f"stage = {self.stage}")

        stage_alt = self.stage.replace("/", "__")

        if self.type_name in ["MODULE", "PCB"]:
            self.json_default = str(
                Path(__file__).parent / f"config/config_{self.type_name}_default.json"
            )
            self.json_config = str(
                Path(__file__).parent
                / f"config/config_{self.type_name}_{stage_alt}.json"
            )

        with Path(self.json_default).open() as f:
            self.config = json.load(f)
        with Path(self.json_config).open() as f:
            self.custom = json.load(f)

            for key in [
                "frontside_goldenmodule_path",
                "backside_goldenmodule_path",
                "ntile",
                "nsplit",
                "backside",
            ]:
                if key in self.custom:
                    self.config[key] = self.custom[key]

            if "checklist" in self.custom:
                for side in ["front", "back"]:
                    if side in self.custom["checklist"]:
                        for flag in ["Yellow", "Red"]:
                            if flag in self.custom["checklist"][side]:
                                self.config["checklist"][side][flag] = (
                                    self.custom["checklist"][side][flag]
                                    + self.config["checklist"][side][flag]
                                )

        if self.config.get("backside") is True:
            QMessageBox.warning(
                self,
                "Warning",
                "Back-side inspection is required in this stage: please make sure that the photograph is already recorded at this point, otherwise you will be required to re-do the front-side inspection again!",
            )

        log.info(pprint.pformat(self.config))

        self.origImgPath = {"front": "", "back": ""}
        self.mode = "front"

        # checked page list
        self.rev = 0
        self.tot_page = int(self.config["ntile"])
        self.nsplit = int(self.config["nsplit"])
        self.page_checked = []
        for i in range(self.tot_page):
            self.page_checked.insert(i, False)

    def init_ui(self):
        # check the presence of golden modules

        try:
            self.path_gm = str(
                Path(__file__).parent
                / self.config[f"{self.mode}side_goldenmodule_path"]
            )

        except Exception:
            QMessageBox.warning(
                self,
                "Warning",
                f"{self.mode.capitalize()}-side Golden module path is undefined in the config file!",
            )

        try:
            with (Path(self.path_gm).parent / ".version").open() as f:
                version_info = f.read()

                if version_info.find("2023-04-04") < 0:
                    msg = "Golden module version outdated"
                    raise Exception(msg)

        except Exception as e:
            log.exception("missing the golden image file: " + str(e))

            QMessageBox.warning(
                self,
                "Warning",
                "Golden module image bank is being downloaded...\nWait for a minute.",
            )

            log.info(f"Golden module not found on {self.path_gm}, deploying it...")

            subprocess.run(
                "cd /var/tmp; rm -rf golden_module*; curl -O https://cernbox.cern.ch/remote.php/dav/public-files/EAbb7RxrEqyCyrS/golden_module_20230404.zip",
                shell=True,
            )
            subprocess.run("cd /var/tmp; unzip golden_module_*.zip", shell=True)

            shutil.rmtree(str(Path(self.path_gm).parent))

            subprocess.run(
                "mv -f /var/tmp/golden_module {}; rm -rf golden_module*".format(
                    str(Path(self.path_gm).parent.parent)
                ),
                shell=True,
            )

            with Path(self.path_gm + "/main_img.jpg").open() as f:
                pass

            QMessageBox.warning(
                self,
                "Information",
                "The latest golden module image bank was deployed.",
            )

        for index, _check in enumerate(self.page_checked):
            self.page_checked[index] = False

        self.anomaly_dic = {}
        self.comment_dic = {}
        self.img_dic = {}

        # check list
        self.checklist_dict = {}

        checklist = self.config["checklist"].get(self.mode)

        for tile in range(36):
            if checklist:
                self.checklist_dict[str(tile)] = checklist

        self.initial_wid = vi_initial_win.InitialWindow(self)
        self.parent.update_widget(self.initial_wid)

    def close_and_return(self):
        self.close()
        self.parent.back_from_test()

    def update_img(self, img):
        self.rev = self.rev + 1
        path = f"{self.temp_dir_path}/img_{self.mode}_{self.rev}.jpg"
        write_img(img, path)
        log.info(f"dumped image {path}")
        self.img_bgr, self.img_h, self.img_w, self.img_d = read_img(path)

    def undo_img(self):
        if self.rev == 0:
            self.rev = self.rev
        else:
            self.rev = self.rev - 1
        path = f"{self.temp_dir_path}/img_{self.mode}_{self.rev}.jpg"
        self.img_bgr, self.img_h, self.img_w, self.img_d = read_img(path)

    def load_img(self, mode="front"):
        options = QFileDialog.Options()
        inputFileName, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "Images (*.bmp *.dib *.pbm *.pgm *.ppm *.sr *.ras *.jpeg *.jpg *.jpe *.jp2 *.png *.tiff *.tif);;Any files (*)",
            options=options,
        )
        if not inputFileName:
            log.info("image is not chosen")
        else:
            self.statusBar().showMessage(inputFileName)
            log.info(inputFileName)

            self.img_bgr, self.img_h, self.img_w, self.img_d = read_img(inputFileName)

            self.mode = mode

            self.origImgPath[
                self.mode
            ] = f"{self.temp_dir_path}/img_{self.mode}_org.jpg"
            write_img(self.img_bgr, self.origImgPath[self.mode])

            if self.img_h > 1000 and self.img_w > 1000:
                self.scale = 10
            else:
                self.scale = 1
            self.n_page = 0
            log.info("OpenCV image read success.")

            self.rev = 0

            self.shape_img()

    def shape_img(self):
        log.info("shape_img()")
        img, h, w, d = read_img(self.origImgPath.get(self.mode))

        if self.mode == "front":
            self.shape_img_wid = shaping_win.QuadFrontTrimmer(self)
        elif self.mode == "back":
            self.shape_img_wid = shaping_win.QuadBackTrimmer(self)

        self.parent.update_widget(self.shape_img_wid)

    def rotate_img(self):
        try:
            img, h, w, d = read_img(
                f"{self.temp_dir_path}/img_{self.mode}_{self.rev}.jpg"
            )
        except Exception:
            img, h, w, d = read_img(self.origImgPath.get(self.mode))

        img, h, w, d = img_rotate(img)
        self.update_img(img)

    def split_img(self):
        self.split_img_wid = splitimg_win.SplitImageWindow(self)
        self.parent.update_widget(self.split_img_wid)

    def inspection(self):
        # Guiding dialog
        self.msg_map = {
            "MODULE/ASSEMBLY": "Check carefully:\n * Glue must not reach the edge of sensor/PCB;\n * Glue does not infiltrate the pads or back-side of the sensor;\n",
            "MODULE/WIREBONDING": "Check carefully:\n * All wires match the wire bond map;\n * No shorts due to bad bonding.",
            "MODULE/PARYLENE_MASKING": "Check carefully:\n * All wires match the wire bond map;\n * No shorts due to bad bonding.",
            "MODULE/PARYLENE_COATING": "",
            "MODULE/PARYLENE_UNMASKING": 'Check carefully:\n * Has the parylene coating penetrated the pickup and strain relief or connector areas?\n * Are there any areas where de-lamination of the parylene layer is seen that may result in contamination of the module?\n * Is the back of the module free of parylene such that only small "witness marks" are visible on the edges of the ASICs?',
            "MODULE/WIREBOND_PROTECTION": "",
            "MODULE/THERMAL_CYCLES": "",
            "PCB_RECEPTION": "",
            "PCB_POPULATION": "",
            "PCB_CUTTING": "",
            "PCB_RECEPTION_MODULE_SITE": "",
        }

        if self.n_page == 0:
            QMessageBox.information(
                self,
                "Note",
                "\n\n".join(
                    [
                        self.parent.info_dict.get("currentStage", ""),
                        self.msg_map.get(self.parent.info_dict.get("currentStage", "")),
                        "Key-binds:\n * X: Checkout Tile\n * F: Next Page\n * B: Previous Page\n * S: Switch Target/Reference",
                    ]
                ),
            )

        inspection_wid = inspection_win.InspectionWindow(self)
        self.parent.update_widget(inspection_wid)

    def make_result(self):
        path_target = f"{self.temp_dir_path}/main_{self.mode}_img.jpg"
        cv2.imwrite(path_target, self.img_bgr)

        oid_target = str(
            localdb_uploader.jpeg_formatter(self.parent.localDB, path_target)
        )

        for page, path_jpeg in self.img_dic.items():
            self.img_dic[page] = str(
                localdb_uploader.jpeg_formatter(self.parent.localDB, path_jpeg)
            )

        self.parent.testRun["results"]["metadata"][
            f"{self.mode}_defects"
        ] = self.anomaly_dic
        self.parent.testRun["results"]["metadata"][
            f"{self.mode}_comments"
        ] = self.comment_dic
        self.parent.testRun["results"]["metadata"][f"{self.mode}_image"] = oid_target
        self.parent.testRun["results"]["metadata"][
            f"{self.mode}_defect_images"
        ] = self.img_dic

        if self.config.get("backside") is True and self.mode == "front":
            self.mode = "back"
            self.init_ui()

        else:
            self.return_result()

    def go_to_summary(self, sub):
        sub.hide()
        summary_wid = summary_win.SummaryWindow(self)
        self.parent.update_widget(summary_wid)

    def return_result(self):
        self.parent.receive_result(self)
