#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: UHD RX DPSK
# Generated: Tue Jul  8 16:14:09 2014
##################################################

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import constsink_gl
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx

class uhd_rx_dpsk(grc_wxgui.top_block_gui):

    def __init__(self, samp_rate=1e6, freq=2.45e9, gain=0, freq_offset=0, address="addr=192.168.10.3"):
        grc_wxgui.top_block_gui.__init__(self, title="UHD RX DPSK")

        ##################################################
        # Parameters
        ##################################################
        self.samp_rate = samp_rate
        self.freq = freq
        self.gain = gain
        self.freq_offset = freq_offset
        self.address = address

        ##################################################
        # Variables
        ##################################################
        self.tun_gain = tun_gain = gain
        self.tun_freq = tun_freq = freq
        self.timing_bw = timing_bw = 6.28/100.0
        self.samps_per_sym = samps_per_sym = 4
        self.rx_freq_off = rx_freq_off = freq_offset
        self.phase_bw = phase_bw = 6.28/100.0

        ##################################################
        # Blocks
        ##################################################
        _tun_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tun_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tun_gain_sizer,
        	value=self.tun_gain,
        	callback=self.set_tun_gain,
        	label="UHD Gain",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tun_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tun_gain_sizer,
        	value=self.tun_gain,
        	callback=self.set_tun_gain,
        	minimum=0,
        	maximum=20,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_tun_gain_sizer)
        _tun_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tun_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tun_freq_sizer,
        	value=self.tun_freq,
        	callback=self.set_tun_freq,
        	label="Freq (Hz)",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tun_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tun_freq_sizer,
        	value=self.tun_freq,
        	callback=self.set_tun_freq,
        	minimum=2.4e9,
        	maximum=2.5e9,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_tun_freq_sizer)
        _timing_bw_sizer = wx.BoxSizer(wx.VERTICAL)
        self._timing_bw_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_timing_bw_sizer,
        	value=self.timing_bw,
        	callback=self.set_timing_bw,
        	label="Timing Loop BW",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._timing_bw_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_timing_bw_sizer,
        	value=self.timing_bw,
        	callback=self.set_timing_bw,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_timing_bw_sizer)
        _rx_freq_off_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rx_freq_off_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rx_freq_off_sizer,
        	value=self.rx_freq_off,
        	callback=self.set_rx_freq_off,
        	label="RX Freq Offset (Hz)",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rx_freq_off_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rx_freq_off_sizer,
        	value=self.rx_freq_off,
        	callback=self.set_rx_freq_off,
        	minimum=-100e3,
        	maximum=+100e3,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_rx_freq_off_sizer)
        _phase_bw_sizer = wx.BoxSizer(wx.VERTICAL)
        self._phase_bw_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_phase_bw_sizer,
        	value=self.phase_bw,
        	callback=self.set_phase_bw,
        	label="Phase Loop BW",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._phase_bw_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_phase_bw_sizer,
        	value=self.phase_bw,
        	callback=self.set_phase_bw,
        	minimum=0,
        	maximum=1.0,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_phase_bw_sizer)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=tun_freq,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=10,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=30,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.wxgui_constellationsink2_0 = constsink_gl.const_sink_c(
        	self.GetWin(),
        	title="Constellation Plot",
        	sample_rate=samp_rate,
        	frame_rate=5,
        	const_size=2048,
        	M=4,
        	theta=0,
        	loop_bw=6.28/100.0,
        	fmax=0.06,
        	mu=0.5,
        	gain_mu=0.005,
        	symbol_rate=samp_rate/samps_per_sym,
        	omega_limit=0.005,
        )
        self.Add(self.wxgui_constellationsink2_0.win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join((address, "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(tun_freq+rx_freq_off, 0)
        self.uhd_usrp_source_0.set_gain(tun_gain, 0)
        self.digital_dxpsk_demod_0 = digital.dqpsk_demod(
        	samples_per_symbol=samps_per_sym,
        	excess_bw=0.35,
        	freq_bw=6.28/100.0,
        	phase_bw=6.28/100.0,
        	timing_bw=6.28/100.0,
        	mod_code="gray",
        	verbose=False,
        	log=False
        )
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_char*1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.digital_dxpsk_demod_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.digital_dxpsk_demod_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.wxgui_constellationsink2_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.wxgui_fftsink2_0, 0))


# QT sink close method reimplementation

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_constellationsink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.set_tun_freq(self.freq)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.set_tun_gain(self.gain)

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset
        self.set_rx_freq_off(self.freq_offset)

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_tun_gain(self):
        return self.tun_gain

    def set_tun_gain(self, tun_gain):
        self.tun_gain = tun_gain
        self._tun_gain_slider.set_value(self.tun_gain)
        self._tun_gain_text_box.set_value(self.tun_gain)
        self.uhd_usrp_source_0.set_gain(self.tun_gain, 0)

    def get_tun_freq(self):
        return self.tun_freq

    def set_tun_freq(self, tun_freq):
        self.tun_freq = tun_freq
        self._tun_freq_slider.set_value(self.tun_freq)
        self._tun_freq_text_box.set_value(self.tun_freq)
        self.wxgui_fftsink2_0.set_baseband_freq(self.tun_freq)
        self.uhd_usrp_source_0.set_center_freq(self.tun_freq+self.rx_freq_off, 0)

    def get_timing_bw(self):
        return self.timing_bw

    def set_timing_bw(self, timing_bw):
        self.timing_bw = timing_bw
        self._timing_bw_slider.set_value(self.timing_bw)
        self._timing_bw_text_box.set_value(self.timing_bw)

    def get_samps_per_sym(self):
        return self.samps_per_sym

    def set_samps_per_sym(self, samps_per_sym):
        self.samps_per_sym = samps_per_sym

    def get_rx_freq_off(self):
        return self.rx_freq_off

    def set_rx_freq_off(self, rx_freq_off):
        self.rx_freq_off = rx_freq_off
        self._rx_freq_off_slider.set_value(self.rx_freq_off)
        self._rx_freq_off_text_box.set_value(self.rx_freq_off)
        self.uhd_usrp_source_0.set_center_freq(self.tun_freq+self.rx_freq_off, 0)

    def get_phase_bw(self):
        return self.phase_bw

    def set_phase_bw(self, phase_bw):
        self.phase_bw = phase_bw
        self._phase_bw_slider.set_value(self.phase_bw)
        self._phase_bw_text_box.set_value(self.phase_bw)

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
    parser.add_option("-s", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(1e6),
        help="Set Sample Rate [default=%default]")
    parser.add_option("-f", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(2.45e9),
        help="Set Default Frequency [default=%default]")
    parser.add_option("-g", "--gain", dest="gain", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set Default Gain [default=%default]")
    parser.add_option("-o", "--freq-offset", dest="freq_offset", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set Rx Frequency Offset [default=%default]")
    parser.add_option("-a", "--address", dest="address", type="string", default="addr=192.168.10.3",
        help="Set IP Address [default=%default]")
    (options, args) = parser.parse_args()
    tb = uhd_rx_dpsk(samp_rate=options.samp_rate, freq=options.freq, gain=options.gain, freq_offset=options.freq_offset, address=options.address)
    tb.Start(True)
    tb.Wait()
