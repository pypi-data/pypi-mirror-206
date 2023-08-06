from __future__ import annotations

from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class ConfirmWindow(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.parent = parent

        titlebox = QVBoxLayout()
        layout = QVBoxLayout()
        button_box = QHBoxLayout()
        inner_box = QVBoxLayout()
        image_box = QVBoxLayout()

        label_title = QLabel()
        label_title.setText(
            '<center><font size="5">Confirm before uploading to the database</font></center>'
        )
        label_practice = QLabel()
        label_practice.setText(
            '<center><font size="4" color = "green"> Practice Mode</font></center>'
        )

        Upload_button = QPushButton("&Upload!")
        Upload_button.clicked.connect(self.upload_to_db)
        json_button = QPushButton("&Check json (for expert)")
        json_button.clicked.connect(self.check_json)
        back_button = QPushButton("&Back")
        back_button.clicked.connect(self.back_page)

        titlebox.addWidget(label_title)

        button_box.addWidget(back_button)
        button_box.addStretch()
        button_box.addWidget(json_button)
        button_box.addWidget(Upload_button)

        inner = QScrollArea()
        inner.setFixedHeight(220)
        inner.setFixedWidth(600)
        result_wid = QWidget()
        result_wid.setLayout(self.make_layout())

        inner.setWidgetResizable(True)
        inner.setWidget(result_wid)
        inner_box.addWidget(inner)

        self.doppo = Path(__file__).parent.joinpath("quad_module_file.png")
        image = QImage(self.doppo)
        self.width = 470
        self.height = 470
        image = image.scaled(
            self.width, self.height, Qt.KeepAspectRatio, Qt.FastTransformation
        )
        imageLabel = QLabel()
        imageLabel.setPixmap(QPixmap.fromImage(image))
        imageLabel.scaleFactor = 1.0
        image_box.addWidget(imageLabel)

        image_box_h = QHBoxLayout()
        image_box_h.addStretch()
        image_box_h.addLayout(image_box)
        image_box_h.addStretch()

        layout.addLayout(titlebox)
        layout.addLayout(inner_box)
        layout.addLayout(button_box)
        layout.addLayout(image_box_h)

        self.setLayout(layout)

    def back_page(self):
        self.parent.back_to_test()

    def check_json(self):
        self.parent.confirm_json()

    def upload_to_db(self):
        self.parent.upload_to_db()

    def add_info(self, Form_layout, label_str, form_text):
        label = QLabel()
        label.setText(label_str)

        if label_str == "Comment :":
            inner = QTextEdit()
            inner.setText(form_text)
            inner.setReadOnly(True)
            inner.setFocusPolicy(Qt.NoFocus)
            inner.setStyleSheet("background-color : linen; color: black;")

            editor = QScrollArea()
            editor.setWidgetResizable(True)
            editor.setWidget(inner)

        else:
            editor = QLineEdit()
            editor.setText(form_text)
            editor.setReadOnly(True)
            editor.setFocusPolicy(Qt.NoFocus)
            editor.setStyleSheet("background-color : linen; color: black;")
        #        editor.setStyleSheet("background-color : azure")

        Form_layout.addRow(label, editor)

    #################################################################
    def make_layout(self):
        if (
            self.parent.info_dict["componentType"] == "MODULE"
            or self.parent.info_dict["componentType"] == "practice"
        ):
            return self.layout_ModuleQC()
        return self.layout_ModuleQC()

    def layout_ModuleQC(self):
        HBox = QHBoxLayout()

        Form_layout = QFormLayout()
        self.add_info(
            Form_layout,
            "Current Stage :",
            self.parent.result_dict["localDB"]["currentStage"],
        )
        self.add_info(
            Form_layout, "Test Type :", self.parent.result_dict["localDB"]["testType"]
        )

        distance_top = "{:.6f} {}".format(
            self.parent.result_dict["localDB"]["results"]["distance top"], "mm"
        )
        distance_left = "{:.6f} {}".format(
            self.parent.result_dict["localDB"]["results"]["distance left"], "mm"
        )
        distance_right = "{:.6f} {}".format(
            self.parent.result_dict["localDB"]["results"]["distance right"], "mm"
        )
        distance_bottom = "{:.6f} {}".format(
            self.parent.result_dict["localDB"]["results"]["distance bottom"], "mm"
        )
        angle_top_left = "{:.6f} {}".format(
            self.parent.result_dict["localDB"]["results"]["angle top-left"], "mm"
        )
        angle_top_right = "{:.6f} {}".format(
            self.parent.result_dict["localDB"]["results"]["angle top-right"], "mm"
        )
        angle_bottom_left = "{:.6f} {}".format(
            self.parent.result_dict["localDB"]["results"]["angle bottom-left"], "mm"
        )
        angle_bottom_right = "{:.6f} {}".format(
            self.parent.result_dict["localDB"]["results"]["angle bottom-right"], "mm"
        )
        # module thickness pickup
        area_chip1 = "{:.6f} {}".format(
            self.parent.result_dict["localDB"]["results"][
                "module thickness pickup area chip1"
            ],
            "mm",
        )
        area_chip2 = "{:.6f} {}".format(
            self.parent.result_dict["localDB"]["results"][
                "module thickness pickup area chip2"
            ],
            "mm",
        )
        area_chip3 = "{:.6f} {}".format(
            self.parent.result_dict["localDB"]["results"][
                "module thickness pickup area chip3"
            ],
            "mm",
        )
        area_chip4 = "{:.6f} {}".format(
            self.parent.result_dict["localDB"]["results"][
                "module thickness pickup area chip4"
            ],
            "mm",
        )
        # module thickness
        edge_chip1 = "{:.6f} {}".format(
            self.parent.result_dict["localDB"]["results"][
                "module thickness edge chip1"
            ],
            "mm",
        )
        edge_chip2 = "{:.6f} {}".format(
            self.parent.result_dict["localDB"]["results"][
                "module thickness edge chip2"
            ],
            "mm",
        )
        edge_chip3 = "{:.6f} {}".format(
            self.parent.result_dict["localDB"]["results"][
                "module thickness edge chip3"
            ],
            "mm",
        )
        edge_chip4 = "{:.6f} {}".format(
            self.parent.result_dict["localDB"]["results"][
                "module thickness edge chip4"
            ],
            "mm",
        )
        # module thickness
        HV_capacitor = "{:.6f} {}".format(
            self.parent.result_dict["localDB"]["results"][
                "module thickness HV capacitor"
            ],
            "mm",
        )
        Data_connector = "{:.6f} {}".format(
            self.parent.result_dict["localDB"]["results"][
                "module thickness Data connector"
            ],
            "mm",
        )
        # planarity
        vacuum_on = "{}".format(
            self.parent.result_dict["localDB"]["results"]["planarity vacuum on"]
        )
        vacuum_on_std_dev = "{}".format(
            self.parent.result_dict["localDB"]["results"]["planarity vacuum on std dev"]
        )
        vacuum_off = "{}".format(
            self.parent.result_dict["localDB"]["results"]["planarity vacuum off"]
        )
        vacuum_off_std_dev = "{}".format(
            self.parent.result_dict["localDB"]["results"][
                "planarity vacuum off std dev"
            ]
        )

        self.add_info(Form_layout, "Distance Top :", distance_top)
        self.add_info(Form_layout, "Distance Left :", distance_left)
        self.add_info(Form_layout, "Distance Right :", distance_right)
        self.add_info(Form_layout, "Distance Bottom :", distance_bottom)
        self.add_info(Form_layout, "Angle Top-left :", angle_top_left)
        self.add_info(Form_layout, "Angle Top-right :", angle_top_right)
        self.add_info(Form_layout, "Angle Bottom-left :", angle_bottom_left)
        self.add_info(Form_layout, "Angle Bottom-right :", angle_bottom_right)
        self.add_info(Form_layout, "module thickness pickup area chip1 :", area_chip1)
        self.add_info(Form_layout, "module thickness pickup area chip2 :", area_chip2)
        self.add_info(Form_layout, "module thickness pickup area chip3 :", area_chip3)
        self.add_info(Form_layout, "module thickness pickup area chip4 :", area_chip4)
        self.add_info(Form_layout, "module thickness edge chip1 :", edge_chip1)
        self.add_info(Form_layout, "module thickness edge chip2 :", edge_chip2)
        self.add_info(Form_layout, "module thickness edge chip3 :", edge_chip3)
        self.add_info(Form_layout, "module thickness edge chip4 :", edge_chip4)
        self.add_info(Form_layout, "module thickness HV capacitor :", HV_capacitor)
        self.add_info(Form_layout, "module thickness Data connector :", Data_connector)
        self.add_info(Form_layout, "planarity vacuum on :", vacuum_on)
        self.add_info(Form_layout, "planarity vacuum on std dev :", vacuum_on_std_dev)
        self.add_info(Form_layout, "planarity vacuum off :", vacuum_off)
        self.add_info(Form_layout, "planarity vacuum off std dev :", vacuum_off_std_dev)

        self.add_info(
            Form_layout,
            "Comment :",
            self.parent.result_dict["localDB"]["results"]["comment"],
        )

        HBox.addLayout(Form_layout)

        return HBox
