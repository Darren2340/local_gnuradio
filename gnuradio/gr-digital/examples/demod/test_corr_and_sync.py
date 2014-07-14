#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Test Corr And Sync
# Generated: Wed Jul  9 16:12:17 2014
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import numpy
import scipy
import sip
import sys

class test_corr_and_sync(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Test Corr And Sync")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Test Corr And Sync")
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

        self.settings = Qt.QSettings("GNU Radio", "test_corr_and_sync")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.nfilts = nfilts = 32
        self.eb = eb = 0.35
        self.time_offset = time_offset = 1
        self.samp_rate = samp_rate = 100000
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), eb, 5*sps*nfilts)
        self.preamble = preamble = [1,-1,1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,1,-1,1,1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1]
        self.phase = phase = 0
        self.payload_size = payload_size = 992
        self.noise = noise = 0
        self.matched_filter = matched_filter = firdes.root_raised_cosine(nfilts, nfilts, 1, eb, int(11*sps*nfilts))
        self.gap = gap = 20000
        self.freq_offset = freq_offset = 0
        self.constel = constel = digital.constellation_calcdist(([1,- 1]), ([0,1]), 2, 1).base()
        self.bb_filter = bb_filter = firdes.root_raised_cosine(sps, sps, 1, eb, 101)

        ##################################################
        # Blocks
        ##################################################
        self._time_offset_layout = Qt.QVBoxLayout()
        self._time_offset_label = Qt.QLabel("Timing Offset")
        self._time_offset_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._time_offset_slider.setRange(0.995, 1.005, 0.00001)
        self._time_offset_slider.setValue(self.time_offset)
        self._time_offset_slider.setMinimumWidth(200)
        self._time_offset_slider.valueChanged.connect(self.set_time_offset)
        self._time_offset_label.setAlignment(Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter)
        self._time_offset_layout.addWidget(self._time_offset_label)
        self._time_offset_layout.addWidget(self._time_offset_slider)
        self.top_grid_layout.addLayout(self._time_offset_layout, 4,1,1,1)
        self._noise_layout = Qt.QVBoxLayout()
        self._noise_label = Qt.QLabel("Noise")
        self._noise_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._noise_slider.setRange(0, 1, 0.005)
        self._noise_slider.setValue(self.noise)
        self._noise_slider.setMinimumWidth(200)
        self._noise_slider.valueChanged.connect(self.set_noise)
        self._noise_label.setAlignment(Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter)
        self._noise_layout.addWidget(self._noise_label)
        self._noise_layout.addWidget(self._noise_slider)
        self.top_grid_layout.addLayout(self._noise_layout, 3,0,1,1)
        self._freq_offset_layout = Qt.QVBoxLayout()
        self._freq_offset_label = Qt.QLabel("Frequency Offset")
        self._freq_offset_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._freq_offset_slider.setRange(-0.001, 0.001, 0.00002)
        self._freq_offset_slider.setValue(self.freq_offset)
        self._freq_offset_slider.setMinimumWidth(200)
        self._freq_offset_slider.valueChanged.connect(self.set_freq_offset)
        self._freq_offset_label.setAlignment(Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter)
        self._freq_offset_layout.addWidget(self._freq_offset_label)
        self._freq_offset_layout.addWidget(self._freq_offset_slider)
        self.top_grid_layout.addLayout(self._freq_offset_layout, 4,0,1,1)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	80000, #size
        	samp_rate, #samp_rate
        	"QT GUI Plot", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-200, 400)
        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 200, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        
        labels = ["|corr|^2", "Re{corr}", "Im{corr}", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_win, 1,0,1,2)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	50000, #size
        	samp_rate, #samp_rate
        	"QT GUI Plot", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 1, 0.1, 0, "time_est")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 0,0,1,1)
        (self.qtgui_time_sink_x_0).set_processor_affinity([0])
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1000, #size
        	"QT GUI Plot", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0, 0, "time_est")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        
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
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 0,1,1,1)
        self._phase_layout = Qt.QVBoxLayout()
        self._phase_label = Qt.QLabel("Phase offset")
        self._phase_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._phase_slider.setRange(-2*scipy.pi, 2*scipy.pi, 0.1)
        self._phase_slider.setValue(self.phase)
        self._phase_slider.setMinimumWidth(200)
        self._phase_slider.valueChanged.connect(self.set_phase)
        self._phase_label.setAlignment(Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter)
        self._phase_layout.addWidget(self._phase_label)
        self._phase_layout.addWidget(self._phase_slider)
        self.top_grid_layout.addLayout(self._phase_layout, 3,1,1,1)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, 2*3.14/100.0, (rrc_taps), nfilts, 0, 0.5, 1)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(1*3.14/50.0, 2)
        self.digital_correlate_and_sync_cc_0 = digital.correlate_and_sync_cc((preamble), (matched_filter), sps)
        self.digital_constellation_modulator_0 = digital.generic_mod(
          constellation=constel,
          differential=False,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=eb,
          verbose=False,
          log=False,
          )
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=noise,
        	frequency_offset=freq_offset,
        	epsilon=time_offset,
        	taps=(1.0, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_vector_source_x_0_0 = blocks.vector_source_b(map(lambda x: (-x+1)/2, preamble), True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_stream_mux_0_0_0 = blocks.stream_mux(gr.sizeof_char*1, (len(preamble)/8,payload_size))
        self.blocks_stream_mux_0_0 = blocks.stream_mux(gr.sizeof_gr_complex*1, ((len(preamble)+8*payload_size)*sps, gap))
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_null_source_0_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 100000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.qtgui_time_sink_x_1, 1))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.digital_correlate_and_sync_cc_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.blocks_null_source_0_0, 0), (self.blocks_stream_mux_0_0, 1))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_stream_mux_0_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.qtgui_time_sink_x_1, 2))
        self.connect((self.channels_channel_model_0, 0), (self.digital_correlate_and_sync_cc_0, 0))
        self.connect((self.blocks_stream_mux_0_0_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_stream_mux_0_0, 0))
        self.connect((self.digital_correlate_and_sync_cc_0, 1), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.digital_correlate_and_sync_cc_0, 1), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_stream_mux_0_0_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_stream_mux_0_0_0, 1))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_const_sink_x_0, 0))


# QT sink close method reimplementation
    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "test_corr_and_sync")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_matched_filter(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1, self.eb, int(11*self.sps*self.nfilts)))
        self.set_bb_filter(firdes.root_raised_cosine(self.sps, self.sps, 1, self.eb, 101))
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.eb, 5*self.sps*self.nfilts))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_matched_filter(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1, self.eb, int(11*self.sps*self.nfilts)))
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.eb, 5*self.sps*self.nfilts))

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb
        self.set_matched_filter(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1, self.eb, int(11*self.sps*self.nfilts)))
        self.set_bb_filter(firdes.root_raised_cosine(self.sps, self.sps, 1, self.eb, 101))
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.eb, 5*self.sps*self.nfilts))

    def get_time_offset(self):
        return self.time_offset

    def set_time_offset(self, time_offset):
        self.time_offset = time_offset
        self.channels_channel_model_0.set_timing_offset(self.time_offset)
        Qt.QMetaObject.invokeMethod(self._time_offset_slider, "setValue", Qt.Q_ARG("double", self.time_offset))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0.set_taps((self.rrc_taps))

    def get_preamble(self):
        return self.preamble

    def set_preamble(self, preamble):
        self.preamble = preamble

    def get_phase(self):
        return self.phase

    def set_phase(self, phase):
        self.phase = phase
        Qt.QMetaObject.invokeMethod(self._phase_slider, "setValue", Qt.Q_ARG("double", self.phase))

    def get_payload_size(self):
        return self.payload_size

    def set_payload_size(self, payload_size):
        self.payload_size = payload_size

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.channels_channel_model_0.set_noise_voltage(self.noise)
        Qt.QMetaObject.invokeMethod(self._noise_slider, "setValue", Qt.Q_ARG("double", self.noise))

    def get_matched_filter(self):
        return self.matched_filter

    def set_matched_filter(self, matched_filter):
        self.matched_filter = matched_filter

    def get_gap(self):
        return self.gap

    def set_gap(self, gap):
        self.gap = gap

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset
        self.channels_channel_model_0.set_frequency_offset(self.freq_offset)
        Qt.QMetaObject.invokeMethod(self._freq_offset_slider, "setValue", Qt.Q_ARG("double", self.freq_offset))

    def get_constel(self):
        return self.constel

    def set_constel(self, constel):
        self.constel = constel

    def get_bb_filter(self):
        return self.bb_filter

    def set_bb_filter(self, bb_filter):
        self.bb_filter = bb_filter

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
    tb = test_corr_and_sync()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
