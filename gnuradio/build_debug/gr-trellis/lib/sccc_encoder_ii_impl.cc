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

#include "sccc_encoder_ii_impl.h"
#include <gnuradio/io_signature.h>
#include <iostream>

namespace gr {
  namespace trellis {

    sccc_encoder_ii::sptr
    sccc_encoder_ii::make(const fsm &FSMo, int STo,
		      const fsm &FSMi, int STi,
		      const interleaver &INTERLEAVER,
		      int blocklength)
    {
      return gnuradio::get_initial_sptr
	(new sccc_encoder_ii_impl(FSMo, STo, FSMi, STi, INTERLEAVER, blocklength));
    }

    sccc_encoder_ii_impl::sccc_encoder_ii_impl(const fsm &FSMo, int STo,
			     const fsm &FSMi, int STi,
			     const interleaver &INTERLEAVER,
			     int blocklength)
    : sync_block("sccc_encoder_ii",
		    io_signature::make(1, 1, sizeof(int)),
		    io_signature::make(1, 1, sizeof(int))),
      d_FSMo(FSMo), d_STo(STo),
      d_FSMi(FSMi), d_STi(STi),
      d_INTERLEAVER(INTERLEAVER),
      d_blocklength(blocklength)
    {
      set_output_multiple(d_blocklength);
      d_buffer.resize(d_blocklength);
    }

    sccc_encoder_ii_impl::~sccc_encoder_ii_impl()
    {
    }

    int
    sccc_encoder_ii_impl::work(int noutput_items,
		      gr_vector_const_void_star &input_items,
		      gr_vector_void_star &output_items)
    {
      for(int b = 0; b < noutput_items/d_blocklength; b++) {
	const int *in = (const int*)input_items[0]+b*d_blocklength;
	int *out = (int*)output_items[0]+b*d_blocklength;

	int STo_tmp = d_STo;
	for(int i = 0; i < d_blocklength; i++) {
	  d_buffer[i] = d_FSMo.OS()[STo_tmp*d_FSMo.I()+in[i]];
	  STo_tmp = (int) d_FSMo.NS()[STo_tmp*d_FSMo.I()+in[i]];
	}

	int STi_tmp = d_STi;
	for(int i = 0; i < d_blocklength; i++) {
	  int k = d_INTERLEAVER.INTER()[i];
	  out[i] = (int) d_FSMi.OS()[STi_tmp*d_FSMi.I()+d_buffer[k]];
	  STi_tmp = (int) d_FSMi.NS()[STi_tmp*d_FSMi.I()+d_buffer[k]];
	}
      }
      return noutput_items;
    }

  } /* namespace trellis */
} /* namespace gr */

