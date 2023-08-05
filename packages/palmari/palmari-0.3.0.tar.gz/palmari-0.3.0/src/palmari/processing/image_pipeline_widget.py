from __future__ import annotations
from typing import Any
import napari
from napari.layers import Image
from qtpy import QtCore
from qtpy.QtWidgets import (
    QDialog,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QSplitter,
    QGroupBox,
    QFileDialog,
    QScrollArea,
    QTabWidget,
)
from qtpy.compat import getsavefilename

from magicgui.widgets import FileEdit
from functools import partial


from napari.qt import thread_worker
from magicgui.widgets import (
    create_widget,
    Container,
    ComboBox,
    FloatSpinBox,
    FloatSlider,
)
import enum
import dask.array as da
import dask_image
import pandas as pd
import logging
import os
from ..data_structure.acquisition import Acquisition
from .image_pipeline import ImagePipeline, ProcessingStep
from .edit_pipeline_window import PipelineEditor


class handled_types(enum.Enum):
    image = "Image"
    points = "Points"
    tracks = "Tracks"
    detections = "Detections"
    image_locs_and_pixel_size = "Image_locs_and_pixel_size"


class ProcessingStepWidget(Container):
    def __init__(self, step: ProcessingStep):
        self.widgets_dict = {}
        for param, value in step.__dict__.items():
            if param[0] == "_":
                continue
            logging.debug("Adding widget for %s" % param)
            w_type = (
                step.widget_types[param]
                if param in step.widget_types
                else None
            )
            w_options = (
                step.widget_options[param]
                if param in step.widget_options
                else {}
            )
            widget = create_widget(
                value=value,
                name=param,
                options=w_options,
                widget_type=w_type,
            )
            self.widgets_dict[param] = widget

            widget.changed.connect(partial(step.update_param, param))
        super().__init__(widgets=[w for _, w in self.widgets_dict.items()])


class ImagePipelineWidget(QWidget):
    def __init__(
        self, image_pipeline: ImagePipeline, napari_viewer: napari.Viewer
    ):
        super().__init__()

        self.pixel_size = 1.00
        self.delta_t = 0.03
        self.to_export = None
        self.viewer = napari_viewer
        self.tp = image_pipeline
        self._init_layers_dict()
        self.setup_ui()

    def activate_buttons(self, last_clicked: int = 0):
        for button_index, button in self._buttons.items():
            enable = button_index <= last_clicked + 1
            button.setEnabled(enable)

    def add_button(self, button: QPushButton):
        index = len(self._buttons)
        self._buttons[index] = button
        return index

    def drop_layers_after(self, first_idx_to_remove: int):
        original_layers = dict(self._layers)
        for idx, existing_layer in original_layers.items():
            if idx >= first_idx_to_remove:
                self.viewer.layers.remove(existing_layer)
                if idx in self._layers:
                    self._layers.pop(idx)
                logging.debug("Removed layer %d" % idx)

    def set_input_image(self, layer: Image = None):

        # Remove subsequent layers
        self.drop_layers_after(1)
        self.to_export = None
        self.export_locs_button.setEnabled(False)

        if layer is not None:
            # Convert data to Dask array
            # Store it
            logging.debug("Set Input Image %s" % layer.name)
            layer.data = layer.data.astype(float)
            if not isinstance(layer.data, da.Array):
                layer.data = da.from_array(layer.data)

            self._layers[0] = layer
            self.rescale_image_layers()

    def rescale_image_layers(self):
        rescaled = False
        for key, layer in self._layers.items():
            if isinstance(layer, Image):
                layer.scale = (1, self.pixel_size, self.pixel_size)
                rescaled = True
        if rescaled:
            self.viewer.reset_view()

    def setup_ui(self):
        main_layout = QVBoxLayout()

        main_layout.addLayout(self.choose_pipeline_layout())
        main_layout.addLayout(self.input_layout())

        main_layout.addWidget(QLabel("Processing steps :"))
        self.pipeline_widget = self.get_pipeline_widget()
        main_layout.addWidget(self.pipeline_widget)

        # main_layout.addStretch(-1)

        main_layout.addLayout(self.export_layout())

        self.setLayout(main_layout)

        self.init_buttons()
        self.viewer.layers.events.removed.connect(
            self._possibly_reset_pipeline
        )
        self.viewer.layers.events.inserted.connect(
            self._possibly_activate_button
        )

    def _init_layers_dict(self):
        self._layers = {}
        for layer in self.viewer.layers:
            if isinstance(layer, Image):
                self._layers[0] = layer

    def _possibly_reset_pipeline(self, event):
        key_of_removed = None
        original_items = dict(self._layers)
        for key, value in original_items.items():
            if event.value == value:
                key_of_removed = key
                break
        if key_of_removed is None:
            return
        print("Removed item had key %s" % key)
        for key, value in original_items.items():
            if key >= key_of_removed:
                self._layers.pop(key)
        self.activate_buttons(last_clicked=key - 2)

    def _possibly_activate_button(self, event):
        if isinstance(event.value, Image):
            self.activate_buttons(-1)

    def choose_pipeline_layout(self):

        main_layout = QHBoxLayout()
        main_layout.addWidget(QLabel("Load pipeline :"))
        self.select_file_widget = FileEdit(
            mode="r",
            filter="*.yaml",
            label="Pipeline file",
            name="Pipeline file",
        )
        self.select_file_widget.changed.connect(self.load_pipeline)
        main_layout.addWidget(self.select_file_widget._widget._qwidget)

        editPipelineButton = QPushButton("Edit current pipeline")

        def openEditWindow():
            editDialog = PipelineEditor(self.tp)
            if editDialog.exec():
                new_pipeline_widget = self.get_pipeline_widget()
                self.layout().replaceWidget(
                    self.pipeline_widget, new_pipeline_widget
                )
                self.pipeline_widget = new_pipeline_widget

        editPipelineButton.clicked.connect(openEditWindow)
        main_layout.addWidget(editPipelineButton)
        return main_layout

    def input_layout(self):
        main_layout = QVBoxLayout()
        input_widget: ComboBox = create_widget(
            annotation=Image,
            name="input_image",
            label="Input image : ",
            options={
                "tooltip": "Raw image on which the pipeline is run",
            },
        )
        input_widget.changed.connect(self.set_input_image)
        self.viewer.layers.events.inserted.connect(input_widget.reset_choices)
        self.viewer.layers.events.changed.connect(input_widget.reset_choices)
        self.viewer.layers.events.removed.connect(input_widget.reset_choices)
        self.viewer.layers.events.reordered.connect(input_widget.reset_choices)
        self.viewer.events.status.connect(input_widget.reset_choices)
        self.input_widget = input_widget

        delta_t_widget = FloatSpinBox(
            name="delta_t",
            label="delta t (s)",
            value=self.delta_t,
            step=0.005,
        )

        def set_delta_t(x: float):
            self.delta_t = x

        delta_t_widget.changed.connect(set_delta_t)

        pixel_size_widget = FloatSpinBox(
            name="pixel_size",
            label="pixel size (um)",
            value=self.pixel_size,
            step=0.001,
        )

        def set_pixel_size(x: float):
            self.pixel_size = x
            self.rescale_image_layers()

        pixel_size_widget.changed.connect(set_pixel_size)

        container = Container(
            widgets=[input_widget, delta_t_widget, pixel_size_widget]
        )
        main_layout.addWidget(container._widget._qwidget)

        main_box = QGroupBox("Input : ")
        main_box.setLayout(main_layout)
        main_layout = QVBoxLayout()
        main_layout.addWidget(main_box)

        return main_layout

    def load_pipeline(self, file_path):
        try:
            tp = ImagePipeline.from_yaml(file_path)
        except BaseException as e:
            logging.error(e)
            logging.error(
                "Could not load pipeline from file %s, check the format"
                % file_path
            )
            return
        self.tp = tp
        self.pipeline_widget.setWidget(self.get_pipeline_widget())
        self.setWindowTitle("Palmari | %s" % tp.name)
        self.init_buttons()

    def init_buttons(self):
        self.activate_buttons(last_clicked=-1 if 0 in self._layers else -2)

    def get_pipeline_widget(self):

        self._buttons = {}

        pipeline_widget = QWidget()
        pipeline_layout = QVBoxLayout()

        preprocessing_widget = self.preprocessing_widget()
        if preprocessing_widget is not None:
            pipeline_layout.addWidget(preprocessing_widget)

        pipeline_layout.addWidget(self.detection_widget())
        pipeline_layout.addWidget(self.localization_widget())

        post_processing_widget = self.locs_processing_widget()
        if post_processing_widget is not None:
            pipeline_layout.addWidget(post_processing_widget)

        pipeline_layout.addWidget(self.tracking_widget())
        pipeline_widget.setLayout(pipeline_layout)
        pipeline_widget.setContentsMargins(0, 0, 10, 0)

        pipeline_container = QScrollArea()
        pipeline_container.setWidget(pipeline_widget)
        pipeline_container.setWidgetResizable(False)
        pipeline_widget.setFixedHeight(pipeline_widget.sizeHint().height())
        pipeline_container.setWidgetResizable(True)

        return pipeline_container

    def export_layout(self):
        main_layout = QVBoxLayout()
        self.export_locs_button = QPushButton(text="Save locs and tracks")
        export_pipeline_button = QPushButton(text="Save pipeline")
        main_layout.addWidget(self.export_locs_button)
        main_layout.addWidget(export_pipeline_button)

        self.export_locs_button.clicked.connect(self.export_locs)
        export_pipeline_button.clicked.connect(self.export_pipeline)

        return main_layout

    def export_locs(self):
        assert self.to_export is not None
        fileName, _ = getsavefilename(
            parent=self,
            caption="Export localizations and tracks",
            )
        logging.debug(fileName)
        if fileName is not None and len(fileName) > 2:
            if "." not in fileName:
                fileName = "%s.csv" % fileName
            self.to_export.to_csv(fileName, index=True)

    def export_pipeline(self):
        fileName, _ = getsavefilename(
            parent=self,
            basedir=self.tp.last_storage_path,
            caption="Save pipeline parameters",
        )
        
        logging.debug(fileName)

        if fileName is not None and len(fileName) > 2:
            if ".yaml" not in fileName:
                fileName = "%s.yaml" % fileName
            self.tp.to_yaml(fileName)

    def preprocessing_widget(self):

        if len(self.tp.movie_preprocessors) == 0:
            return None

        main_widget = QGroupBox(title="Image pre-processing")
        main_layout = QVBoxLayout()
        for i, step in enumerate(self.tp.movie_preprocessors):
            step_layout = self.setup_layout_for_step(
                step,
                input_type=handled_types.image,
                output_type=handled_types.image,
            )
            main_layout.addLayout(step_layout)
            if i < len(self.tp.movie_preprocessors) - 1:
                main_layout.addWidget(QSplitter())
        main_widget.setLayout(main_layout)

        return main_widget

    def detection_widget(self):

        main_widget = QGroupBox(title="Detection : %s" % self.tp.detector.name)
        main_layout = QVBoxLayout()
        main_layout.addLayout(
            self.setup_layout_for_step(
                self.tp.detector,
                input_type=handled_types.image,
                output_type=handled_types.detections,
                skip_title=True,
            )
        )
        main_widget.setLayout(main_layout)
        return main_widget

    def localization_widget(self):

        main_widget = QGroupBox(
            title="Localization : %s" % self.tp.localizer.name
        )
        main_layout = QVBoxLayout()
        main_layout.addLayout(
            self.setup_layout_for_step(
                self.tp.localizer,
                input_type=handled_types.detections,
                output_type=handled_types.points,
                skip_title=True,
            )
        )
        main_widget.setLayout(main_layout)
        return main_widget

    def locs_processing_widget(self):

        if len(self.tp.loc_processors) == 0:
            return None

        main_widget = QGroupBox(title="Post-processing of localizations")
        main_layout = QVBoxLayout()
        for i, step in enumerate(self.tp.loc_processors):
            step_layout = self.setup_layout_for_step(
                step,
                input_type=handled_types.image_locs_and_pixel_size,
                output_type=handled_types.points,
            )
            main_layout.addLayout(step_layout)
            if i < len(self.tp.loc_processors) - 1:
                main_layout.addWidget(QSplitter())
        main_widget.setLayout(main_layout)

        return main_widget

    def tracking_widget(self):

        main_widget = QGroupBox(title="Tracking : %s" % self.tp.tracker.name)
        main_layout = QVBoxLayout()
        main_layout.addLayout(
            self.setup_layout_for_step(
                self.tp.tracker,
                input_type=handled_types.points,
                output_type=handled_types.tracks,
                skip_title=True,
                is_final_step=True,
            )
        )
        main_widget.setLayout(main_layout)
        return main_widget

    def setup_layout_for_step(
        self,
        step: ProcessingStep,
        input_type: handled_types,
        output_type: handled_types,
        skip_title: bool = False,
        is_final_step: bool = False,
    ) -> QVBoxLayout:
        step_layout = QVBoxLayout()
        if not skip_title:
            step_layout.addWidget(QLabel(step.name))
        step_container = ProcessingStepWidget(step)
        if len(step_container.widgets_dict) > 0:
            step_layout.addWidget(step_container._widget._qwidget)
        step_run_btn = QPushButton(step.action_name)
        btn_index = self.add_button(step_run_btn)
        step_layout.addWidget(step_run_btn)
        input_layer_idx = btn_index
        output_layer_idx = btn_index + 1

        def add_layer(data):
            logging.debug(
                "Adding layer %d -> %s" % (input_layer_idx, output_layer_idx)
            )
            if step.is_localizer:
                data["t"] = (
                    data["frame"] - data["frame"].min()
                ) * self.delta_t
                data[["x", "y"]] *= self.pixel_size

            if step.is_detector:
                data[["x", "y"]] = data[["y", "x"]]

            self.drop_layers_after(output_layer_idx)
            if data.shape[0] > 0:
                self.add_layer_of_type(
                    data=data,
                    data_type=output_type,
                    layer_idx=output_layer_idx,
                    step_name=step.name,
                )
            self.setEnabled(True)
            if data.shape[0] > 0:
                self.activate_buttons(last_clicked=btn_index)
            else:
                self.activate_buttons(last_clicked=btn_index - 1)
            if is_final_step:
                self.to_export = data
            else:
                self.to_export = None
            self.export_locs_button.setEnabled(is_final_step)

        def to_dask(array):
            if isinstance(array, da.Array):
                return array
            else:
                return da.from_array(array)

        @thread_worker(connect={"returned": add_layer})
        def run_step(checked: bool = True):
            logging.debug(self._layers)
            assert input_layer_idx in self._layers
            self.setEnabled(False)
            if input_type == handled_types.image:
                input_data = (to_dask(self._layers[input_layer_idx].data),)
            elif input_type == handled_types.points:
                input_data = (self._layers[input_layer_idx].result,)
            elif input_type == handled_types.tracks:
                input_data = (self._layers[input_layer_idx].result,)
            elif input_type == handled_types.detections:
                detections = pd.DataFrame(
                    data=self._layers[input_layer_idx].data.copy(),
                    columns=["frame", "x", "y"],
                )
                detections[["x", "y"]] /= self.pixel_size
                # On inverse x et y volontairement
                detections[["y", "x"]] = detections[["x", "y"]].astype(int)
                input_data = (
                    to_dask(self._layers[input_layer_idx - 1].data),
                    detections,
                )
            elif input_type == handled_types.image_locs_and_pixel_size:
                input_data = (
                    to_dask(self._layers[0].data),
                    self._layers[input_layer_idx].result,
                    self.pixel_size,
                )
            return step.process(*input_data)

        step_run_btn.clicked.connect(run_step)

        return step_layout

    def add_layer_of_type(
        self,
        data: Any,
        data_type: handled_types,
        layer_idx: int,
        step_name: str,
    ):
        if data is None:
            logging.debug("Nothing returned by %s" % step_name)

        if data_type == handled_types.image:
            self.add_image_layer(
                returned_image=data, layer_idx=layer_idx, step_name=step_name
            )
        elif data_type == handled_types.tracks:
            self.add_tracks_layer(
                tracks=data, layer_idx=layer_idx, step_name=step_name
            )
        elif data_type == handled_types.points:
            self.add_points_layer(
                points=data,
                layer_idx=layer_idx,
                step_name=step_name,
            )
        elif data_type == handled_types.detections:
            self.add_points_layer(
                points=data, layer_idx=layer_idx, step_name=step_name
            )

    def add_image_layer(self, returned_image, layer_idx: int, step_name: str):

        if layer_idx not in self._layers:
            new_layer = self.viewer.add_image(
                data=returned_image,
                name="%s : %s" % (self._layers[0].name, step_name),
                scale=(1, self.pixel_size, self.pixel_size),
            )
            self._layers[layer_idx] = new_layer
        else:
            self._layers[layer_idx].data = returned_image

    def add_points_layer(
        self,
        points: pd.DataFrame,
        layer_idx: int,
        step_name: str,
    ):

        if layer_idx not in self._layers:
            points_ = points.astype({"x":float,"y":float,"frame":float})
            properties = points_[
                    [
                        c
                        for c in points_.columns
                        if (c not in ["x", "y"])
                        and (points_[c].dtype.kind in "uifb")
                    ]
                ].to_dict(orient="list")
            new_layer = self.viewer.add_points(
                points_[["frame", "x", "y"]].values,
                properties=properties,
                symbol="disc",
                size=0.25,
                edge_width=0.1,
                face_color="transparent" if (points.shape[0] > 0) else None,
                edge_color="frame" if (points.shape[0] > 0) else None,
                edge_colormap="rainbow",
                blending="translucent_no_depth",
                name="%s : %s" % (self._layers[0].name, step_name),
            )
            new_layer.editable = False
            self._layers[layer_idx] = new_layer
        else:
            self._layers[layer_idx].data = points

        self._layers[layer_idx].result = points

    def add_tracks_layer(self, tracks, layer_idx: int, step_name: str):

        if layer_idx not in self._layers:
            new_layer = self.viewer.add_tracks(
                data=tracks[["n", "frame", "x", "y"]],
                tail_width=1,
                tail_length=10,
                head_length=0,
                properties=pd.merge(
                    tracks[["n"]],
                    tracks.groupby("n")
                    .agg({"x": "count", "frame": "min"})
                    .rename(columns={"x": "length", "frame": "start_frame"}),
                    how="left",
                    left_on="n",
                    right_index=True,
                ),
                name="%s : %s" % (self._layers[0].name, step_name),
            )
            self._layers[layer_idx] = new_layer
        else:
            self._layers[layer_idx].tracks = tracks

        self._layers[layer_idx].result = tracks

    @classmethod
    def view_pipeline(
        cls,
        image_pipeline: ImagePipeline,
        acq: Acquisition = None,
        image_file: str = None,
    ):
        napari.Viewer()
        viewer = napari.current_viewer()
        widget = cls(image_pipeline, viewer)

        if acq is not None:
            widget.pixel_size = acq.experiment.pixel_size
            widget.delta_t = acq.experiment.DT
            viewer.add_image(
                data=acq.image,
                name=acq.image_file.split(os.path.sep)[-1],
                scale=(1.0, widget.pixel_size, widget.pixel_size),
            )
        elif image_file is not None:
            viewer.open(image_file)

        viewer.window.add_dock_widget(
            widget=widget,
            name="PALM pipeline : %s" % image_pipeline.name,
            area="right",
        )
        widget.rescale_image_layers()
