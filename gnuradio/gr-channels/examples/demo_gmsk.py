#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Demo Gmsk
# Author: mettus
# Generated: Wed Jul  9 16:41:15 2014
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import math
import sip
import sys
import time

class demo_gmsk(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Demo Gmsk")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Demo Gmsk")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "demo_gmsk")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.q_ofs = q_ofs = 0
        self.phasebal = phasebal = 0
        self.phase_noise_mag = phase_noise_mag = -100
        self.magbal = magbal = 0
        self.i_ofs = i_ofs = 0
        self.freq_offset = freq_offset = 0
        self.const_size = const_size = 4
        self.beta = beta = 0

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("addr=192.168.10.3", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(1399993750, 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"QT GUI Plot", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 4,0,1,1)
        self._q_ofs_layout = Qt.QVBoxLayout()
        self._q_ofs_tool_bar = Qt.QToolBar(self)
        self._q_ofs_layout.addWidget(self._q_ofs_tool_bar)
        self._q_ofs_tool_bar.addWidget(Qt.QLabel("Q offset"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._q_ofs_counter = qwt_counter_pyslot()
        self._q_ofs_counter.setRange(-1, 1, 0.001)
        self._q_ofs_counter.setNumButtons(2)
        self._q_ofs_counter.setValue(self.q_ofs)
        self._q_ofs_tool_bar.addWidget(self._q_ofs_counter)
        self._q_ofs_counter.valueChanged.connect(self.set_q_ofs)
        self._q_ofs_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._q_ofs_slider.setRange(-1, 1, 0.001)
        self._q_ofs_slider.setValue(self.q_ofs)
        self._q_ofs_slider.setMinimumWidth(200)
        self._q_ofs_slider.valueChanged.connect(self.set_q_ofs)
        self._q_ofs_layout.addWidget(self._q_ofs_slider)
        self.top_grid_layout.addLayout(self._q_ofs_layout, 2,1,1,1)
        self._phasebal_layout = Qt.QVBoxLayout()
        self._phasebal_tool_bar = Qt.QToolBar(self)
        self._phasebal_layout.addWidget(self._phasebal_tool_bar)
        self._phasebal_tool_bar.addWidget(Qt.QLabel("IQ Phase Imbalance"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._phasebal_counter = qwt_counter_pyslot()
        self._phasebal_counter.setRange(0, 45, 0.1)
        self._phasebal_counter.setNumButtons(2)
        self._phasebal_counter.setValue(self.phasebal)
        self._phasebal_tool_bar.addWidget(self._phasebal_counter)
        self._phasebal_counter.valueChanged.connect(self.set_phasebal)
        self._phasebal_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._phasebal_slider.setRange(0, 45, 0.1)
        self._phasebal_slider.setValue(self.phasebal)
        self._phasebal_slider.setMinimumWidth(200)
        self._phasebal_slider.valueChanged.connect(self.set_phasebal)
        self._phasebal_layout.addWidget(self._phasebal_slider)
        self.top_grid_layout.addLayout(self._phasebal_layout, 1,1,1,1)
        self._phase_noise_mag_layout = Qt.QVBoxLayout()
        self._phase_noise_mag_tool_bar = Qt.QToolBar(self)
        self._phase_noise_mag_layout.addWidget(self._phase_noise_mag_tool_bar)
        self._phase_noise_mag_tool_bar.addWidget(Qt.QLabel("Phase Noise Mag (dB)"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._phase_noise_mag_counter = qwt_counter_pyslot()
        self._phase_noise_mag_counter.setRange(-100, 0, 1)
        self._phase_noise_mag_counter.setNumButtons(2)
        self._phase_noise_mag_counter.setValue(self.phase_noise_mag)
        self._phase_noise_mag_tool_bar.addWidget(self._phase_noise_mag_counter)
        self._phase_noise_mag_counter.valueChanged.connect(self.set_phase_noise_mag)
        self._phase_noise_mag_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._phase_noise_mag_slider.setRange(-100, 0, 1)
        self._phase_noise_mag_slider.setValue(self.phase_noise_mag)
        self._phase_noise_mag_slider.setMinimumWidth(200)
        self._phase_noise_mag_slider.valueChanged.connect(self.set_phase_noise_mag)
        self._phase_noise_mag_layout.addWidget(self._phase_noise_mag_slider)
        self.top_grid_layout.addLayout(self._phase_noise_mag_layout, 0, 0, 1,1)
        self._magbal_layout = Qt.QVBoxLayout()
        self._magbal_tool_bar = Qt.QToolBar(self)
        self._magbal_layout.addWidget(self._magbal_tool_bar)
        self._magbal_tool_bar.addWidget(Qt.QLabel("IQ Magnitude Imbalance"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._magbal_counter = qwt_counter_pyslot()
        self._magbal_counter.setRange(0, 10, 0.1)
        self._magbal_counter.setNumButtons(2)
        self._magbal_counter.setValue(self.magbal)
        self._magbal_tool_bar.addWidget(self._magbal_counter)
        self._magbal_counter.valueChanged.connect(self.set_magbal)
        self._magbal_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._magbal_slider.setRange(0, 10, 0.1)
        self._magbal_slider.setValue(self.magbal)
        self._magbal_slider.setMinimumWidth(200)
        self._magbal_slider.valueChanged.connect(self.set_magbal)
        self._magbal_layout.addWidget(self._magbal_slider)
        self.top_grid_layout.addLayout(self._magbal_layout, 1,0,1,1)
        self._i_ofs_layout = Qt.QVBoxLayout()
        self._i_ofs_tool_bar = Qt.QToolBar(self)
        self._i_ofs_layout.addWidget(self._i_ofs_tool_bar)
        self._i_ofs_tool_bar.addWidget(Qt.QLabel("I offset"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._i_ofs_counter = qwt_counter_pyslot()
        self._i_ofs_counter.setRange(-1, 1, 0.001)
        self._i_ofs_counter.setNumButtons(2)
        self._i_ofs_counter.setValue(self.i_ofs)
        self._i_ofs_tool_bar.addWidget(self._i_ofs_counter)
        self._i_ofs_counter.valueChanged.connect(self.set_i_ofs)
        self._i_ofs_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._i_ofs_slider.setRange(-1, 1, 0.001)
        self._i_ofs_slider.setValue(self.i_ofs)
        self._i_ofs_slider.setMinimumWidth(200)
        self._i_ofs_slider.valueChanged.connect(self.set_i_ofs)
        self._i_ofs_layout.addWidget(self._i_ofs_slider)
        self.top_grid_layout.addLayout(self._i_ofs_layout, 2,0,1,1)
        self._freq_offset_layout = Qt.QVBoxLayout()
        self._freq_offset_tool_bar = Qt.QToolBar(self)
        self._freq_offset_layout.addWidget(self._freq_offset_tool_bar)
        self._freq_offset_tool_bar.addWidget(Qt.QLabel("Frequency Offset"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._freq_offset_counter = qwt_counter_pyslot()
        self._freq_offset_counter.setRange(-0.5, 0.5, 0.001)
        self._freq_offset_counter.setNumButtons(2)
        self._freq_offset_counter.setValue(self.freq_offset)
        self._freq_offset_tool_bar.addWidget(self._freq_offset_counter)
        self._freq_offset_counter.valueChanged.connect(self.set_freq_offset)
        self._freq_offset_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._freq_offset_slider.setRange(-0.5, 0.5, 0.001)
        self._freq_offset_slider.setValue(self.freq_offset)
        self._freq_offset_slider.setMinimumWidth(200)
        self._freq_offset_slider.valueChanged.connect(self.set_freq_offset)
        self._freq_offset_layout.addWidget(self._freq_offset_slider)
        self.top_grid_layout.addLayout(self._freq_offset_layout, 0,1,1,1)
        self._beta_layout = Qt.QVBoxLayout()
        self._beta_tool_bar = Qt.QToolBar(self)
        self._beta_layout.addWidget(self._beta_tool_bar)
        self._beta_tool_bar.addWidget(Qt.QLabel("k3 (IP3)"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._beta_counter = qwt_counter_pyslot()
        self._beta_counter.setRange(-.1, 0, 0.001)
        self._beta_counter.setNumButtons(2)
        self._beta_counter.setValue(self.beta)
        self._beta_tool_bar.addWidget(self._beta_counter)
        self._beta_counter.valueChanged.connect(self.set_beta)
        self._beta_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._beta_slider.setRange(-.1, 0, 0.001)
        self._beta_slider.setValue(self.beta)
        self._beta_slider.setMinimumWidth(200)
        self._beta_slider.valueChanged.connect(self.set_beta)
        self._beta_layout.addWidget(self._beta_slider)
        self.top_grid_layout.addLayout(self._beta_layout, 3,0,1,1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_const_sink_x_0, 0))


# QT sink close method reimplementation
    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "demo_gmsk")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_q_ofs(self):
        return self.q_ofs

    def set_q_ofs(self, q_ofs):
        self.q_ofs = q_ofs
        Qt.QMetaObject.invokeMethod(self._q_ofs_counter, "setValue", Qt.Q_ARG("double", self.q_ofs))
        Qt.QMetaObject.invokeMethod(self._q_ofs_slider, "setValue", Qt.Q_ARG("double", self.q_ofs))

    def get_phasebal(self):
        return self.phasebal

    def set_phasebal(self, phasebal):
        self.phasebal = phasebal
        Qt.QMetaObject.invokeMethod(self._phasebal_counter, "setValue", Qt.Q_ARG("double", self.phasebal))
        Qt.QMetaObject.invokeMethod(self._phasebal_slider, "setValue", Qt.Q_ARG("double", self.phasebal))

    def get_phase_noise_mag(self):
        return self.phase_noise_mag

    def set_phase_noise_mag(self, phase_noise_mag):
        self.phase_noise_mag = phase_noise_mag
        Qt.QMetaObject.invokeMethod(self._phase_noise_mag_counter, "setValue", Qt.Q_ARG("double", self.phase_noise_mag))
        Qt.QMetaObject.invokeMethod(self._phase_noise_mag_slider, "setValue", Qt.Q_ARG("double", self.phase_noise_mag))

    def get_magbal(self):
        return self.magbal

    def set_magbal(self, magbal):
        self.magbal = magbal
        Qt.QMetaObject.invokeMethod(self._magbal_counter, "setValue", Qt.Q_ARG("double", self.magbal))
        Qt.QMetaObject.invokeMethod(self._magbal_slider, "setValue", Qt.Q_ARG("double", self.magbal))

    def get_i_ofs(self):
        return self.i_ofs

    def set_i_ofs(self, i_ofs):
        self.i_ofs = i_ofs
        Qt.QMetaObject.invokeMethod(self._i_ofs_counter, "setValue", Qt.Q_ARG("double", self.i_ofs))
        Qt.QMetaObject.invokeMethod(self._i_ofs_slider, "setValue", Qt.Q_ARG("double", self.i_ofs))

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset
        Qt.QMetaObject.invokeMethod(self._freq_offset_counter, "setValue", Qt.Q_ARG("double", self.freq_offset))
        Qt.QMetaObject.invokeMethod(self._freq_offset_slider, "setValue", Qt.Q_ARG("double", self.freq_offset))

    def get_const_size(self):
        return self.const_size

    def set_const_size(self, const_size):
        self.const_size = const_size

    def get_beta(self):
        return self.beta

    def set_beta(self, beta):
        self.beta = beta
        Qt.QMetaObject.invokeMethod(self._beta_counter, "setValue", Qt.Q_ARG("double", self.beta))
        Qt.QMetaObject.invokeMethod(self._beta_slider, "setValue", Qt.Q_ARG("double", self.beta))

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = demo_gmsk()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
