from napari import Viewer
from napari.qt import thread_worker
import os

from .processing import ImagePipeline
from .processing.steps import *
from qtpy.QtWidgets import (
    QDialog,
    QErrorMessage,
    QLineEdit,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
)
from qtpy.QtCore import Signal
from magicgui.widgets import FileEdit, FloatSpinBox, LineEdit, ProgressBar
import dask


class PipelineRunner(QWidget):

    progressChanged = Signal(int)
    progressRunning = Signal(bool)
    nFilesChanged = Signal(int)
    nameProcessingFile = Signal(str)

    def __init__(self, napari_viewer: Viewer):
        super().__init__()
        self.setup_ui()
        self.running = False
        self.pixel_size = 0.097
        self.DT = 0.03
        self.file_pattern = ".tif"

        def updatePgBar(s):
            self.pgbar.value = s

        def updateNFiles(s):
            self.pgbar.max = s

        def showPgBar(s):
            self.pgbar.visible = s
            self.file_label.setVisible(s)
            self.running = s
            self.enable_run_button()

        def updateFileName(s):
            self.file_label.setText(s)

        self.progressChanged.connect(updatePgBar)
        self.progressRunning.connect(showPgBar)
        self.nFilesChanged.connect(updateNFiles)
        self.nameProcessingFile.connect(updateFileName)
        
        self.viewer = napari_viewer
        self.viewer.reset_view()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.choose_pipeline_layout())
        main_layout.addLayout(self.choose_input_folder_layout())
        main_layout.addLayout(self.choose_export_folder_layout())

        main_layout.addLayout(self.exp_params_layout())

        self.run_button = QPushButton("Process (?) files !")
        self.run_button.setEnabled(False)
        self.run_button.clicked.connect(self.run_pipeline)
        main_layout.addWidget(self.run_button)

        self.pgbar = ProgressBar(min=0, visible=False)
        main_layout.addWidget(self.pgbar._widget._qwidget)
        self.file_label = QLabel("")
        main_layout.addWidget(self.file_label)

        self.setLayout(main_layout)

    ###
    # LAYOUT PARTS
    ###

    def choose_pipeline_layout(self):

        main_layout = QHBoxLayout()
        main_layout.addWidget(QLabel("Pipeline :"))
        self.select_file_widget = FileEdit(
            mode="r",
            filter="*.yaml",
            label="Pipeline file",
            name="Pipeline file",
        )
        self.select_file_widget.changed.connect(self.load_pipeline)
        main_layout.addWidget(self.select_file_widget._widget._qwidget)
        return main_layout

    def choose_input_folder_layout(self):

        main_layout = QHBoxLayout()
        main_layout.addWidget(QLabel("Process folder :"))
        self.select_input_folder_widget = FileEdit(
            mode="d",
            label="Process folder...",
            name="Process folder...",
        )
        self.select_input_folder_widget.changed.connect(self.setInputFolder)
        main_layout.addWidget(self.select_input_folder_widget._widget._qwidget)
        return main_layout

    def choose_export_folder_layout(self):

        main_layout = QHBoxLayout()
        main_layout.addWidget(QLabel("Save to folder:"))
        self.select_export_folder_widget = FileEdit(
            mode="d",
            label="Save to folder...",
            name="Save to folder...",
        )
        self.select_export_folder_widget.changed.connect(self.setExportFolder)
        main_layout.addWidget(
            self.select_export_folder_widget._widget._qwidget
        )
        return main_layout

    def exp_params_layout(self):

        DT_layout = QHBoxLayout()
        DT_layout.addWidget(QLabel("Exposure (in s.):"))
        dt_widget = FloatSpinBox(value=0.03, min=0.0, step=0.001)
        dt_widget.changed.connect(self.setExpDT)
        DT_layout.addWidget(dt_widget._widget._qwidget)

        pixel_layout = QHBoxLayout()
        pixel_layout.addWidget(QLabel("Pixel size (in um):"))
        pixel_widget = FloatSpinBox(value=0.097, min=0.0, step=0.001)
        pixel_widget.changed.connect(self.setExpPixel)
        pixel_layout.addWidget(pixel_widget._widget._qwidget)

        pattern_layout = QHBoxLayout()
        pattern_layout.addWidget(QLabel("Files with ending:"))
        pattern_widget = LineEdit(value=".tif")
        pattern_widget.changed.connect(self.setExpPattern)
        pattern_layout.addWidget(pattern_widget._widget._qwidget)

        main = QVBoxLayout()
        main.addLayout(pattern_layout)
        main.addLayout(DT_layout)
        main.addLayout(pixel_layout)

        return main

    ###
    # ACTION
    ###

    def load_pipeline(self, file_path):
        try:
            tp = ImagePipeline.from_yaml(file_path)
            self.tp = tp
        except BaseException as e:
            print(e)
            em = QErrorMessage()
            em.showMessage(
                "Could not load pipeline from file %s, check the format"
                % file_path
            )

    def run_pipeline(self):
        self.running = True
        self.enable_run_button()
        worker = self._run_pipeline()
        worker.finished.connect(self._run_finished)
        worker.yielded.connect(self._run_progressed)
        worker.started.connect(self._run_started)
        worker.start()
        
    def _run_started(self):
        exp = self.exp
        assert exp is not None
        self.nFilesChanged.emit(len(exp.scan_folder()))
        self.progressChanged.emit(0)
        self.progressRunning.emit(True)
    
    def _run_finished(self):
        self.progressRunning.emit(False)
        self.enable_run_button()
        
    def _run_progressed(self, yielded):
        image_number, image_file = yielded
        if image_file != "DONE":
            self.nameProcessingFile.emit("Processing %s ..." % image_file)
        self.progressChanged.emit(image_number)

    @thread_worker
    def _run_pipeline(self):
        
        dask.config.set(scheduler='processes') 
        
        exp = self.exp
        for i, f in enumerate(exp):
            yield (i, f)
            acq = Acquisition(f, experiment=exp, image_pipeline=self.tp)
            if i == 0:
                pipeline_export_path_for_exp = self.tp.exp_params_path(acq)
                logging.info(
                    "Saving pipeline to %s" % pipeline_export_path_for_exp
                )
            self.tp.process(to_process=acq, force_reprocess=True)
        yield (i+1, "DONE")
        

    ###
    # PROPERTIES
    ###

    @property
    def tp(self):
        if hasattr(self, "_tp"):
            return self._tp
        else:
            return None

    @tp.setter
    def tp(self, tp: ImagePipeline):
        self._tp = tp
        self.enable_run_button()
        self.setWindowTitle("Palmari | %s" % tp.name)

    @property
    def exp(self):
        if hasattr(self, "_input_folder") and hasattr(self, "_export_folder"):
            exp = Experiment(
                data_folder=self.input_folder,
                export_folder=self.export_folder,
                DT=self.DT,
                file_pattern=self.file_pattern,
                pixel_size=self.pixel_size,
            )
            return exp
        else:
            return None

    @property
    def export_folder(self):
        if hasattr(self, "_export_folder"):
            return self._export_folder
        else:
            return None

    @export_folder.setter
    def export_folder(self, f: str):
        if os.path.exists(f) and os.path.isdir(f):
            self._export_folder = str(f)
            self.enable_run_button()

    def setExportFolder(self, f: str):
        self.export_folder = f

    @property
    def input_folder(self):
        if hasattr(self, "_input_folder"):
            return self._input_folder
        else:
            return None

    @input_folder.setter
    def input_folder(self, f: str):
        if os.path.exists(f) and os.path.isdir(f):
            self._input_folder = str(f)
            self.enable_run_button()

    def setInputFolder(self, f: str):
        self.input_folder = f

    ###
    # OTHERS
    ###

    def enable_run_button(self):
        exp = self.exp
        exp_has_files = False
        if self.running:
            self.run_button.setText("Processing...")
        else:
            if exp is not None:
                files = exp.scan_folder()
                n_files = len(files)
                exp_has_files = n_files > 0
                self.run_button.setText(
                    "Process %d files !" % n_files
                )
            else:
                self.run_button.setText("Process (?) files !")

        self.run_button.setEnabled(
            (self.tp is not None)
            and (self.export_folder is not None)
            and (self.input_folder is not None)
            and exp_has_files
            and (not self.running)
        )

    def setExpPixel(self, s: float):
        self.pixel_size = s

    def setExpPattern(self, p: str):
        self.file_pattern = p
        self.enable_run_button()

    def setExpDT(self, DT: float):
        self.DT = DT