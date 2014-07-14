/* -*- c++ -*- */
/*
 * Copyright 2004,2010,2012 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * GNU Radio is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * GNU Radio is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with GNU Radio; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

// WARNING: this file is machine generated. Edits will be overwritten

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include "sccc_decoder_combined_cb_impl.h"
#include <gnuradio/io_signature.h>
#include <iostream>
#include <gnuradio/trellis/core_algorithms.h>

namespace gr {
  namespace trellis {

    static const float INF = 1.0e9;

    sccc_decoder_combined_cb::sptr
    sccc_decoder_combined_cb::make(const fsm &FSMo, int STo0, int SToK,
		      const fsm &FSMi, int STi0, int STiK,
		      const interleaver &INTERLEAVER,
		      int blocklength,
		      int repetitions,
		      siso_type_t SISO_TYPE,
		      int D,
		      const std::vector<gr_complex> &TABLE,
		      digital::trellis_metric_type_t METRIC_TYPE,
		      float scaling)
    {
      return gnuradio::get_initial_sptr
	(new sccc_decoder_combined_cb_impl(FSMo, STo0, SToK, FSMi, STi0, STiK,
			 INTERLEAVER, blocklength, repetitions,
			 SISO_TYPE, D, TABLE,METRIC_TYPE, scaling));
    }

    sccc_decoder_combined_cb_impl::sccc_decoder_combined_cb_impl(const fsm &FSMo, int STo0, int SToK,
			     const fsm &FSMi, int STi0, int STiK,
			     const interleaver &INTERLEAVER,
			     int blocklength,
			     int repetitions,
			     siso_type_t SISO_TYPE,
			     int D,
			     const std::vector<gr_complex> &TABLE,
			     digital::trellis_metric_type_t METRIC_TYPE,
			     float scaling)
    : block("sccc_decoder_combined_cb",
	       io_signature::make(1, 1, sizeof(gr_complex)),
	       io_signature::make(1, 1, sizeof(unsigned char))),
      d_FSMo(FSMo), d_STo0(STo0), d_SToK(SToK),
      d_FSMi(FSMi), d_STi0(STi0), d_STiK(STiK),
      d_INTERLEAVER(INTERLEAVER),
      d_blocklength(blocklength),
      d_repetitions(repetitions),
      d_SISO_TYPE(SISO_TYPE),
      d_D(D),
      d_TABLE(TABLE),
      d_METRIC_TYPE(METRIC_TYPE),
      d_scaling(scaling)
    {
      set_relative_rate(1.0 / ((double) d_D));
      set_output_multiple(d_blocklength);
    }

    sccc_decoder_combined_cb_impl::~sccc_decoder_combined_cb_impl()
    {
    }

    void
    sccc_decoder_combined_cb_impl::set_scaling(float scaling)
    {
      d_scaling = scaling;
    }

    void
    sccc_decoder_combined_cb_impl::forecast(int noutput_items,
			  gr_vector_int &ninput_items_required)
    {
      int input_required =  d_D * noutput_items ;
      ninput_items_required[0] = input_required;
    }

    //===========================================================

    int
    sccc_decoder_combined_cb_impl::general_work(int noutput_items,
			      gr_vector_int &ninput_items,
			      gr_vector_const_void_star &input_items,
			      gr_vector_void_star &output_items)
    {
      int nblocks = noutput_items / d_blocklength;
      float (*p2min)(float, float) = NULL;

      if(d_SISO_TYPE == TRELLIS_MIN_SUM)
	p2min = &min;
      else if(d_SISO_TYPE == TRELLIS_SUM_PRODUCT)
	p2min = &min_star;

      const gr_complex *in = (const gr_complex*)input_items[0];
      unsigned char *out = (unsigned char*)output_items[0];

      for(int n = 0; n < nblocks; n++) {
	sccc_decoder_combined(d_FSMo, d_STo0, d_SToK,
			      d_FSMi, d_STi0, d_STiK,
			      d_INTERLEAVER, d_blocklength, d_repetitions,
			      p2min,
			      d_D,d_TABLE,
			      d_METRIC_TYPE,
			      d_scaling,
			      &(in[n*d_blocklength*d_D]),
			      &(out[n*d_blocklength]));
      }

      consume_each(d_D * noutput_items);
      return noutput_items;
    }

  } /* namespace trellis */
} /* namespace gr */
