#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: NBFM Receiver/Deviation Meter
# Generated: Wed Jul 22 20:11:04 2020
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import wx

class NBFMRcvrDev(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="NBFM Receiver/Deviation Meter")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.volume = volume = .4
        self.thresh = thresh = -24
        self.samp_rate = samp_rate = 2.40e6
        self.ramp = ramp = 1
        self.alpha = alpha = .01
        self.RF_Gain = RF_Gain = 50
        self.Freq = Freq = 144.39

        ##################################################
        # Blocks
        ##################################################
        _volume_sizer = wx.BoxSizer(wx.VERTICAL)
        self._volume_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	label="Volume",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._volume_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	minimum=0,
        	maximum=3,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_volume_sizer, 1, 1, 1, 1)
        _thresh_sizer = wx.BoxSizer(wx.VERTICAL)
        self._thresh_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_thresh_sizer,
        	value=self.thresh,
        	callback=self.set_thresh,
        	label="Squelch",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._thresh_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_thresh_sizer,
        	value=self.thresh,
        	callback=self.set_thresh,
        	minimum=-70,
        	maximum=0,
        	num_steps=70,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_thresh_sizer, 2, 1, 1, 1)
        self._ramp_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.ramp,
        	callback=self.set_ramp,
        	label="Ramp",
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._ramp_text_box, 3, 0, 1, 1)
        self._alpha_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.alpha,
        	callback=self.set_alpha,
        	label="alpha",
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._alpha_text_box, 3, 1, 1, 1)
        _RF_Gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._RF_Gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_RF_Gain_sizer,
        	value=self.RF_Gain,
        	callback=self.set_RF_Gain,
        	label="RF Gain",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._RF_Gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_RF_Gain_sizer,
        	value=self.RF_Gain,
        	callback=self.set_RF_Gain,
        	minimum=0,
        	maximum=50,
        	num_steps=50,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_RF_Gain_sizer, 2, 0, 1, 1)
        self._Freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.Freq,
        	callback=self.set_Freq,
        	label="Frequency (MHz)",
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._Freq_text_box, 1, 0, 1, 1)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=48000,
        	v_scale=2,
        	v_offset=0,
        	t_scale=2e-3,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="KHz Deviation",
        )
        self.GridAdd(self.wxgui_scopesink2_0.win, 0, 0, 1, 1)
        self.single_pole_iir_filter_xx_0 = filter.single_pole_iir_filter_ff(38.55e-3, 1)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(Freq*1e6, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(0, 0)
        self.rtlsdr_source_0.set_gain(RF_Gain, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(1, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)

        self.low_pass_filter_0 = filter.fir_filter_ccf(50, firdes.low_pass(
        	1, samp_rate, 7.5e3, 3e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((6.5, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
        self.audio_sink_0 = audio.sink(48000, "", True)
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_cc(thresh, alpha, ramp, False)
        self.analog_fm_demod_cf_0 = analog.fm_demod_cf(
        	channel_rate=48000,
        	audio_decim=1,
        	deviation=10000,
        	audio_pass=3500,
        	audio_stop=4000,gnu
        	gain=1.0,
        	tau=1e-6,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.rtlsdr_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_pwr_squelch_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.analog_fm_demod_cf_0, 0))
        self.connect((self.analog_fm_demod_cf_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.analog_fm_demod_cf_0, 0), (self.single_pole_iir_filter_xx_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))


# QT sink close method reimplementation

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.blocks_multiply_const_vxx_0.set_k((self.volume, ))
        self._volume_slider.set_value(self.volume)
        self._volume_text_box.set_value(self.volume)

    def get_thresh(self):
        return self.thresh

    def set_thresh(self, thresh):
        self.thresh = thresh
        self.analog_pwr_squelch_xx_0.set_threshold(self.thresh)
        self._thresh_slider.set_value(self.thresh)
        self._thresh_text_box.set_value(self.thresh)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 7.5e3, 3e3, firdes.WIN_HAMMING, 6.76))

    def get_ramp(self):
        return self.ramp

    def set_ramp(self, ramp):
        self.ramp = ramp
        self._ramp_text_box.set_value(self.ramp)

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.analog_pwr_squelch_xx_0.set_alpha(self.alpha)
        self._alpha_text_box.set_value(self.alpha)

    def get_RF_Gain(self):
        return self.RF_Gain

    def set_RF_Gain(self, RF_Gain):
        self.RF_Gain = RF_Gain
        self.rtlsdr_source_0.set_gain(self.RF_Gain, 0)
        self._RF_Gain_slider.set_value(self.RF_Gain)
        self._RF_Gain_text_box.set_value(self.RF_Gain)

    def get_Freq(self):
        return self.Freq

    def set_Freq(self, Freq):
        self.Freq = Freq
        self.rtlsdr_source_0.set_center_freq(self.Freq*1e6, 0)
        self._Freq_text_box.set_value(self.Freq)

if __name__ == '__main__':
    import ctypes
    import os
    if os.name == 'posix':
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = NBFMRcvrDev()
    tb.Start(True)
    tb.Wait()
