from __future__ import annotations

import logging
import math

import cv2
import numpy as np
from PyQt5.QtGui import QDoubleValidator, QImage, QPixmap
from PyQt5.QtWidgets import (
    QGraphicsPixmapItem,
    QGraphicsScene,
    QGraphicsView,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QWidget,
)

from module_qc_nonelec_gui.qc_tests.VISUAL_INSPECTION.functions.cv2_func import (
    img_cvt_rgb,
)

log = logging.getLogger(__name__)


class Trimmer(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.parent = parent

        self.nLayoutRows = 0

        self.setupCommon1()
        self.setupCustom()
        self.setupCommon2()

        self.tmp_cropped_path = f"{self.parent.temp_dir_path}/tmp_cropped.jpg"
        self.tmp_preview_path = f"{self.parent.temp_dir_path}/tmp_preview.jpg"

        self.trim()

    def setupCommon1(self):
        self.layout = QGridLayout()

        # scene for module picture
        self.view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.srect = self.view.rect()
        self.view.setScene(self.scene)

        # load module picture
        img_org = cv2.imread(self.parent.origImgPath[self.parent.mode])
        h, w, d = img_org.shape
        scale = min(600.0 / float(h), 600.0 / float(w))

        resize_img = cv2.resize(img_org, dsize=None, fx=scale, fy=scale)

        img_rgb, h_rgb, w_rgb, d_rgb = img_cvt_rgb(resize_img)
        bytesPerLine = d_rgb * w_rgb

        self.image = QImage(
            img_rgb.data, w_rgb, h_rgb, bytesPerLine, QImage.Format_RGB888
        )
        self.item = QGraphicsPixmapItem(QPixmap.fromImage(self.image))
        self.scene.addItem(self.item)
        self.view.setScene(self.scene)
        self.view.setFixedWidth(650)
        self.view.setFixedHeight(650)

        self.layout.addWidget(self.view, self.nLayoutRows, 0, 1, 2)
        self.nLayoutRows = self.nLayoutRows + 1

        self.buttons = QHBoxLayout()

    def setupCustom(self):
        pass

    def setupCommon2(self):
        button_back = QPushButton("Back")
        button_back.clicked.connect(self.parent.load_img)

        button_rotate = QPushButton("Rotate")
        button_rotate.clicked.connect(self.rotate)

        button_crop = QPushButton("Preview")
        button_crop.clicked.connect(self.trim)

        button_ok = QPushButton("Next")
        button_ok.clicked.connect(self.go_next)

        self.buttons.addWidget(button_back)
        self.buttons.addWidget(button_rotate)
        self.buttons.addWidget(button_crop)
        self.buttons.addWidget(button_ok)

        self.layout.addLayout(self.buttons, self.nLayoutRows, 0)
        self.nLayoutRows = self.nLayoutRows + 1
        self.setLayout(self.layout)

    def rotate(self):
        self.parent.rotate_img()
        self.trim()

    def trim(self):
        try:
            self.trim_image(self.getParameters())

        except Exception as e:
            log.exception(e)

            QMessageBox.warning(
                self,
                "Warning",
                "Failed in cropping",
            )

        preview = cv2.imread(self.tmp_preview_path)

        self.cropped = cv2.imread(self.tmp_cropped_path)

        h, w, d = preview.shape

        scale = min(600.0 / float(h), 600.0 / float(w))

        resize_img = cv2.resize(preview, dsize=None, fx=scale, fy=scale)

        img_rgb, h_rgb, w_rgb, d_rgb = img_cvt_rgb(resize_img)
        bytesPerLine = d_rgb * w_rgb

        self.image = QImage(
            img_rgb.data, w_rgb, h_rgb, bytesPerLine, QImage.Format_RGB888
        )

        self.view.items().clear()
        self.scene.clear()

        self.item = QGraphicsPixmapItem(QPixmap.fromImage(self.image))
        self.scene.addItem(self.item)
        self.view.setScene(self.scene)

    def trim_image(self, params):
        log.info(params)
        return

    def getParameters(self):
        return {}

    def go_next(self):
        self.parent.update_img(self.cropped)
        self.parent.split_img()


#################################################################################################


class QuadFrontTrimmer(Trimmer):
    def setupCustom(self):
        self.handles = QHBoxLayout()
        self.handles2 = QHBoxLayout()

        label_rot = QLabel(self)
        label_rot.setText("Rotation: [-3.00, 3.00]")

        label_brightness = QLabel(self)
        label_brightness.setText("Brightness: [-100, 100]")

        label_contrast = QLabel(self)
        label_contrast.setText("Contrast: [0, 2]")

        label_blur = QLabel(self)
        label_blur.setText("Blur: [1, 5]")

        label_tweak = QLabel(self)
        label_tweak.setText("Tweak: [20, 50]")

        self.input_rot = QLineEdit(self)
        self.input_rot.setFixedWidth(40)
        self.input_rot.setValidator(QDoubleValidator(-3.0, 3.0, 2))
        self.input_rot.setText(str(0.00))

        self.input_brightness = QLineEdit(self)
        self.input_brightness.setFixedWidth(40)
        self.input_brightness.setValidator(QDoubleValidator(-100, 100, 0))
        self.input_brightness.setText(str(15))

        self.input_contrast = QLineEdit(self)
        self.input_contrast.setFixedWidth(40)
        self.input_contrast.setValidator(QDoubleValidator(0.0, 2.0, 1))
        self.input_contrast.setText(str(1.3))

        self.input_blur = QLineEdit(self)
        self.input_blur.setFixedWidth(40)
        self.input_blur.setValidator(QDoubleValidator(1, 5, 0))
        self.input_blur.setText(str(5))

        self.input_tweak = QLineEdit(self)
        self.input_tweak.setFixedWidth(40)
        self.input_tweak.setValidator(QDoubleValidator(20, 50, 0))
        self.input_tweak.setText(str(35))

        self.handles.addWidget(label_rot)
        self.handles.addWidget(self.input_rot)
        self.handles.addWidget(label_brightness)
        self.handles.addWidget(self.input_brightness)
        self.handles.addWidget(label_contrast)
        self.handles.addWidget(self.input_contrast)
        self.handles.addStretch()

        self.handles2.addWidget(label_blur)
        self.handles2.addWidget(self.input_blur)
        self.handles2.addWidget(label_tweak)
        self.handles2.addWidget(self.input_tweak)
        self.handles2.addStretch()

        self.layout.addLayout(self.handles, self.nLayoutRows, 0)
        self.nLayoutRows = self.nLayoutRows + 1

        self.layout.addLayout(self.handles2, self.nLayoutRows, 0)
        self.nLayoutRows = self.nLayoutRows + 1

    def getParameters(self):
        # get the original image
        rot_angle = float(self.input_rot.text())
        init_blur = int(self.input_blur.text())
        contrast = float(self.input_contrast.text())
        brightness = float(self.input_brightness.text())
        init_param2 = int(self.input_tweak.text())

        log.info(
            f"cropping with rot_angle {rot_angle}, init_blur {init_blur}, contrast {contrast}, brightness {brightness}, init_param2 {init_param2}"
        )

        return {
            "rot_angle": rot_angle,
            "init_blur": init_blur,
            "contrast": contrast,
            "brightness": brightness,
            "init_param2": init_param2,
        }

    def trim_image(self, params):
        rot_angle = params["rot_angle"]
        init_blur = params["init_blur"]
        contrast = params["contrast"]
        brightness = params["brightness"]
        init_param2 = params["init_param2"]

        image_1 = self.parent.img_bgr.copy()

        image_center = tuple(np.array(image_1.shape[1::-1]) / 2)
        rot_mat = cv2.getRotationMatrix2D(image_center, rot_angle, 1.0)
        image_2 = cv2.warpAffine(
            image_1, rot_mat, image_1.shape[1::-1], flags=cv2.INTER_LINEAR
        )

        image_3 = cv2.convertScaleAbs(image_2, alpha=contrast, beta=brightness)

        height_org, width_org, channel = image_3.shape

        resize_scale = (
            1200 / width_org if width_org >= height_org else 1200 / height_org
        )

        image_4 = cv2.resize(
            image_3, None, None, resize_scale, resize_scale, cv2.INTER_LINEAR
        )

        height, width, channel = image_4.shape

        for i in range(height):
            for j in range(width):
                image_3.itemset((i, j, 1), 0)

        gray = cv2.cvtColor(image_4, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(self.tmp_preview_path, gray)

        image_inverted = 255 - gray

        log.info("Searching pickup points...")

        gauge_dic = None
        pickup_points = None

        for blurSize in range(init_blur, 0, -1):
            try:
                gauge_dic, pickup_points = self.houghScan(
                    image_inverted, blurSize, init_param2
                )
                break
            except Exception as e:
                log.info(str(e))
                continue

        if not gauge_dic:
            msg = "failed to find any pickup points"
            raise Exception(msg)

        gauge_std = sum([g["length"] for g in gauge_dic]) / len(gauge_dic)
        center_x = int(sum(p[0] for p in pickup_points) / len(pickup_points))
        center_y = int(sum(p[1] for p in pickup_points) / len(pickup_points))

        pitch = gauge_std / 20.0  # pixels / mm

        log.info(
            f"gauge_std = {gauge_std:.3f} px: 1mm = {pitch:.3f} px, center = ( {center_x:6.3f}, {center_y:6.3f} )"
        )

        cropRange = 21.8  # mm

        x_edge1_0 = max(int(center_x - cropRange * pitch), 0)
        y_edge1_0 = max(int(center_y - cropRange * pitch), 0)
        x_edge2_0 = min(int(center_x + cropRange * pitch), width - 1)
        y_edge2_0 = min(int(center_y + cropRange * pitch), height - 1)

        x_edge1 = max(int((center_x - cropRange * pitch) / resize_scale), 0)
        y_edge1 = max(int((center_y - cropRange * pitch) / resize_scale), 0)
        x_edge2 = min(int((center_x + cropRange * pitch) / resize_scale), width_org - 1)
        y_edge2 = min(
            int((center_y + cropRange * pitch) / resize_scale), height_org - 1
        )

        crop_info = [[x_edge1, x_edge2], [y_edge1, y_edge2]]
        log.info(f"crop_info = {crop_info}")

        cropped = image_2[y_edge1:y_edge2, x_edge1:x_edge2].copy()

        cv2.imwrite(self.tmp_cropped_path, cropped)

        marker_width = int(0.005 * width)

        color = (0, 255, 128)

        # Draw the center reticle
        gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

        cv2.line(
            gray_bgr,
            (center_x - 20, center_y),
            (center_x + 20, center_y),
            color,
            marker_width,
        )
        cv2.line(
            gray_bgr,
            (center_x, center_y - 20),
            (center_x, center_y + 20),
            color,
            marker_width,
        )

        cv2.line(
            gray_bgr,
            (x_edge1_0, y_edge1_0),
            (x_edge1_0 + 50, y_edge1_0),
            color,
            marker_width,
        )
        cv2.line(
            gray_bgr,
            (x_edge1_0, y_edge1_0),
            (x_edge1_0, y_edge1_0 + 50),
            color,
            marker_width,
        )

        cv2.line(
            gray_bgr,
            (x_edge2_0, y_edge1_0),
            (x_edge2_0 - 50, y_edge1_0),
            color,
            marker_width,
        )
        cv2.line(
            gray_bgr,
            (x_edge2_0, y_edge1_0),
            (x_edge2_0, y_edge1_0 + 50),
            color,
            marker_width,
        )

        cv2.line(
            gray_bgr,
            (x_edge1_0, y_edge2_0),
            (x_edge1_0 + 50, y_edge2_0),
            color,
            marker_width,
        )
        cv2.line(
            gray_bgr,
            (x_edge1_0, y_edge2_0),
            (x_edge1_0, y_edge2_0 - 50),
            color,
            marker_width,
        )

        cv2.line(
            gray_bgr,
            (x_edge2_0, y_edge2_0),
            (x_edge2_0 - 50, y_edge2_0),
            color,
            marker_width,
        )
        cv2.line(
            gray_bgr,
            (x_edge2_0, y_edge2_0),
            (x_edge2_0, y_edge2_0 - 50),
            color,
            marker_width,
        )

        for p in pickup_points:
            cv2.circle(
                gray_bgr,
                (int(p[0]), int(p[1])),
                int(p[2]),
                color,
                int(marker_width * 0.5),
            )

        cv2.imwrite(self.tmp_preview_path, gray_bgr)

        return crop_info

    def houghScan(self, image_inverted, blurSize, param2):
        log.info(f"  Hough search: blurSize = {blurSize}")

        blur = cv2.blur(image_inverted, (blurSize, blurSize))

        height, width = image_inverted.shape

        while True:
            ret, image_4 = cv2.threshold(
                blur, thresh=120, maxval=255, type=cv2.THRESH_TOZERO
            )

            # detect circle
            circles = cv2.HoughCircles(
                image=image_4,
                method=cv2.HOUGH_GRADIENT,
                dp=1.0,
                minDist=min(width, height) * 0.12,
                param1=200,
                param2=param2,
                minRadius=int(min(width, height) * 0.03),
                maxRadius=int(min(width, height) * 0.10),
            )

            pickup_cands = []

            for i in circles[0, :]:
                # check if center is in middle of picture
                if (
                    i[0] < width * 0.05
                    or i[0] > width * 0.95
                    or i[1] < height * 0.05
                    or i[1] > height * 0.95
                ):
                    continue

                # draw the outer circle
                cv2.circle(image_4, (int(i[0]), int(i[1])), int(i[2]), (0, 0, 0), 2)

                # draw the center of the circle
                cv2.circle(image_4, (int(i[0]), int(i[1])), 2, (0, 0, 0), 3)

                pickup_cands += [i]

            gauge_dic = []
            pickup_points = set()

            for i in range(len(pickup_cands)):
                ci = pickup_cands[i]
                for j in range(i + 1, len(pickup_cands)):
                    cj = pickup_cands[j]

                    dx = abs(cj[0] - ci[0])
                    dy = abs(cj[1] - ci[1])

                    ang = math.atan(dy / (dx + 1.0e-7))
                    deg = math.atan(1) / 45.0
                    length = math.hypot(dx, dy)

                    isHorizontal = ang < 2 * deg
                    isVertical = ang > 88 * deg

                    if not (isHorizontal or isVertical):
                        # log.info( f'{length:.2f} px, {ang/deg:6.3f} deg ==> skipped' )
                        continue

                    # log.info( f'    {"Horizontal" if isHorizontal else "Vertical":12s}: {length:.2f} px, {ang/deg:6.3f} deg' )
                    cv2.line(
                        image_4,
                        (int(ci[0]), int(ci[1])),
                        (int(cj[0]), int(cj[1])),
                        (0, 0, 0),
                        1,
                    )
                    gauge_dic += [
                        {
                            "horizontal": isHorizontal,
                            "vertical": isVertical,
                            "length": length,
                            "angle": ang / deg,
                        }
                    ]

                    for p in [ci, cj]:
                        pickup_points.add((p[0], p[1], p[2]))

            if len(pickup_points) < 4:
                param2 -= 1

            elif len(pickup_points) > 4:
                param2 += 1

            else:
                break

            if param2 > 80:
                msg = "failure in detection: scanned all param2 range"
                log.info(msg)
                raise Exception(msg)

        if len(gauge_dic) != 4:
            msg = "failure in detection: did not find good gauges"
            log.info(msg)
            raise Exception(msg)

        log.info("")
        log.info("------------------")
        log.info("Detected pickup points:")
        for p in pickup_points:
            log.info(
                f"    Pickup point: center: ({p[0]:.2f}, {p[1]:.2f}), radius: {p[2]:.2f}"
            )

        log.info("Detected pickup points gauges:")
        for g in gauge_dic:
            log.info(
                f'    {"Horizontal" if g["horizontal"] else "Vertical":12s}: length = {g["length"]:7.2f} pixels, angle = {g["angle"]:6.3f} deg'
            )

        return gauge_dic, pickup_points


#################################################################################################


class QuadBackTrimmer(Trimmer):
    def setupCustom(self):
        self.handles = QHBoxLayout()
        self.handles2 = QHBoxLayout()

        label_rot = QLabel(self)
        label_rot.setText("Rotation: [-3.00, 3.00]")

        label_brightness = QLabel(self)
        label_brightness.setText("Brightness: [-100, 100]")

        label_contrast = QLabel(self)
        label_contrast.setText("Contrast: [0, 4]")

        label_blur = QLabel(self)
        label_blur.setText("Blur: [1, 5]")

        label_cannyThr1 = QLabel(self)
        label_cannyThr1.setText("Thr1: [0, 255]")

        label_cannyThr2 = QLabel(self)
        label_cannyThr2.setText("Thr2: [0, 255]")

        self.input_rot = QLineEdit(self)
        self.input_rot.setFixedWidth(40)
        self.input_rot.setValidator(QDoubleValidator(-3.0, 3.0, 2))
        self.input_rot.setText(str(0.00))

        self.input_brightness = QLineEdit(self)
        self.input_brightness.setFixedWidth(40)
        self.input_brightness.setValidator(QDoubleValidator(-100, 100, 0))
        self.input_brightness.setText(str(50))

        self.input_contrast = QLineEdit(self)
        self.input_contrast.setFixedWidth(40)
        self.input_contrast.setValidator(QDoubleValidator(0.0, 4.0, 1))
        self.input_contrast.setText(str(3.0))

        self.input_blur = QLineEdit(self)
        self.input_blur.setFixedWidth(40)
        self.input_blur.setValidator(QDoubleValidator(1, 5, 0))
        self.input_blur.setText(str(5))

        self.input_cannyThr1 = QLineEdit(self)
        self.input_cannyThr1.setFixedWidth(40)
        self.input_cannyThr1.setValidator(QDoubleValidator(0, 255, 0))
        self.input_cannyThr1.setText(str(100))

        self.input_cannyThr2 = QLineEdit(self)
        self.input_cannyThr2.setFixedWidth(40)
        self.input_cannyThr2.setValidator(QDoubleValidator(0, 255, 0))
        self.input_cannyThr2.setText(str(40))

        self.handles.addWidget(label_rot)
        self.handles.addWidget(self.input_rot)
        self.handles.addWidget(label_brightness)
        self.handles.addWidget(self.input_brightness)
        self.handles.addWidget(label_contrast)
        self.handles.addWidget(self.input_contrast)

        self.handles2.addWidget(label_blur)
        self.handles2.addWidget(self.input_blur)
        self.handles2.addWidget(label_cannyThr1)
        self.handles2.addWidget(self.input_cannyThr1)
        self.handles2.addWidget(label_cannyThr2)
        self.handles2.addWidget(self.input_cannyThr2)

        self.layout.addLayout(self.handles, self.nLayoutRows, 0)
        self.nLayoutRows = self.nLayoutRows + 1

        self.layout.addLayout(self.handles2, self.nLayoutRows, 0)
        self.nLayoutRows = self.nLayoutRows + 1

        self.handles.addStretch()
        self.handles2.addStretch()

    def getParameters(self):
        # get the original image
        rot_angle = float(self.input_rot.text())
        init_blur = int(self.input_blur.text())
        contrast = float(self.input_contrast.text())
        brightness = float(self.input_brightness.text())
        cannyThr1 = int(self.input_cannyThr1.text())
        cannyThr2 = int(self.input_cannyThr2.text())

        log.info(
            f"cropping with rot_angle {rot_angle}, init_blur {init_blur}, contrast {contrast}, brightness {brightness}, cannyThr [{cannyThr1}, {cannyThr2}]"
        )

        return {
            "rot_angle": rot_angle,
            "init_blur": init_blur,
            "contrast": contrast,
            "brightness": brightness,
            "cannyThr1": cannyThr1,
            "cannyThr2": cannyThr2,
        }

    def trim_image(self, params):
        rot_angle = params["rot_angle"]
        init_blur = params["init_blur"]
        contrast = params["contrast"]
        brightness = params["brightness"]
        cannyThr1 = params["cannyThr1"]
        cannyThr2 = params["cannyThr2"]

        image_1 = self.parent.img_bgr.copy()

        image_center = tuple(np.array(image_1.shape[1::-1]) / 2)
        rot_mat = cv2.getRotationMatrix2D(image_center, rot_angle, 1.0)
        image_2 = cv2.warpAffine(
            image_1, rot_mat, image_1.shape[1::-1], flags=cv2.INTER_LINEAR
        )

        image_3 = cv2.convertScaleAbs(image_2, alpha=contrast, beta=brightness)

        height_org, width_org, channel = image_3.shape
        log.info(f"original image: width {width_org}, height {height_org}")

        resize_scale = (
            1200 / width_org if width_org >= height_org else 1200 / height_org
        )
        log.info(f"resize_scale = {resize_scale}")

        image_4 = cv2.resize(
            image_3, None, None, resize_scale, resize_scale, cv2.INTER_LINEAR
        )

        height, width, channel = image_4.shape

        for i in range(height):
            for j in range(width):
                image_4.itemset((i, j, 1), 0)

        gray = cv2.cvtColor(image_4, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(self.tmp_preview_path, gray)

        blur = cv2.blur(gray, (init_blur, init_blur))

        edges = cv2.Canny(blur, cannyThr2, cannyThr1)

        rho = 1  # distance resolution in pixels of the Hough grid
        theta = (
            4.0 * math.atan(1.0) / 30.0
        )  # angular resolution in radians of the Hough grid
        threshold = 200  # minimum number of votes (intersections in Hough grid cell)
        min_line_length = 200  # minimum number of pixels making up a line
        max_line_gap = 1200  # maximum gap in pixels between connectable line segments

        lines = []

        # Run Hough on edge detected image
        # Output "lines" is an array containing endpoints of detected line segments
        lines = cv2.HoughLinesP(
            edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap
        )

        if len(lines) == 0:
            msg = "No edge lines were detected"
            raise Exception(msg)

        xEdges = []
        yEdges = []

        for line in lines:
            x1 = line[0][0]
            y1 = line[0][1]
            x2 = line[0][2]
            y2 = line[0][3]
            dx = abs(x1 - x2)
            dy = abs(y1 - y2)
            deg = math.atan(1) / 45.0
            ang = math.atan(dy / (dx + 1.0e-7))
            isHorizontal = ang < 2 * deg
            isVertical = ang > 88 * deg

            if not (isHorizontal or isVertical):
                continue

            if isVertical:
                xEdges += [x1]
            if isHorizontal:
                yEdges += [y1]

        xEdges.sort()
        yEdges.sort()

        if len(xEdges) == 0:
            msg = "No horizontal edge lines were detected"
            raise Exception(msg)

        if len(yEdges) == 0:
            msg = "No horizontal edge lines were detected"
            raise Exception(msg)

        center_x = int((xEdges[0] + xEdges[-1]) / 2.0)
        center_y = int((yEdges[0] + yEdges[-1]) / 2.0)

        horLength = abs(xEdges[0] - xEdges[-1])
        verLength = abs(yEdges[0] - yEdges[-1])
        pitch = (horLength / 42.2 + verLength / 41.1) / 2.0  # pixels / mm

        cropRange = 21.8  # mm
        marker_width0 = int(0.005 * width)

        x_edge1_0 = max(int(center_x - cropRange * pitch), 0)
        y_edge1_0 = max(int(center_y - cropRange * pitch), 0)
        x_edge2_0 = min(int(center_x + cropRange * pitch), width - 1)
        y_edge2_0 = min(int(center_y + cropRange * pitch), height - 1)

        # Draw the center reticle
        gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
        color = (0, 255, 128)

        cv2.line(
            gray_bgr,
            (center_x - 20, center_y),
            (center_x + 20, center_y),
            color,
            marker_width0,
        )
        cv2.line(
            gray_bgr,
            (center_x, center_y - 20),
            (center_x, center_y + 20),
            color,
            marker_width0,
        )

        cv2.line(
            gray_bgr,
            (x_edge1_0, y_edge1_0),
            (x_edge1_0 + 50, y_edge1_0),
            color,
            marker_width0,
        )
        cv2.line(
            gray_bgr,
            (x_edge1_0, y_edge1_0),
            (x_edge1_0, y_edge1_0 + 50),
            color,
            marker_width0,
        )

        cv2.line(
            gray_bgr,
            (x_edge2_0, y_edge1_0),
            (x_edge2_0 - 50, y_edge1_0),
            color,
            marker_width0,
        )
        cv2.line(
            gray_bgr,
            (x_edge2_0, y_edge1_0),
            (x_edge2_0, y_edge1_0 + 50),
            color,
            marker_width0,
        )

        cv2.line(
            gray_bgr,
            (x_edge1_0, y_edge2_0),
            (x_edge1_0 + 50, y_edge2_0),
            color,
            marker_width0,
        )
        cv2.line(
            gray_bgr,
            (x_edge1_0, y_edge2_0),
            (x_edge1_0, y_edge2_0 - 50),
            color,
            marker_width0,
        )

        cv2.line(
            gray_bgr,
            (x_edge2_0, y_edge2_0),
            (x_edge2_0 - 50, y_edge2_0),
            color,
            marker_width0,
        )
        cv2.line(
            gray_bgr,
            (x_edge2_0, y_edge2_0),
            (x_edge2_0, y_edge2_0 - 50),
            color,
            marker_width0,
        )

        cv2.imwrite(self.tmp_preview_path, gray_bgr)

        x_edge1 = max(int((center_x - cropRange * pitch) / width * width_org), 0)
        y_edge1 = max(int((center_y - cropRange * pitch) / height * height_org), 0)
        x_edge2 = min(
            int((center_x + cropRange * pitch) / width * width_org), width_org - 1
        )
        y_edge2 = min(
            int((center_y + cropRange * pitch) / height * height_org), height_org - 1
        )

        crop_info = [[x_edge1, x_edge2], [y_edge1, y_edge2]]
        log.info(f"crop_info = {crop_info}")

        # crop np.ndarray -- y first, x second!
        cropped = image_2[y_edge1:y_edge2, x_edge1:x_edge2].copy()

        cv2.imwrite(self.tmp_cropped_path, cropped)

        return crop_info
