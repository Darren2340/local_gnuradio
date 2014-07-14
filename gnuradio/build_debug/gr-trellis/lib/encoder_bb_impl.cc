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

#include "encoder_bb_impl.h"
#include <gnuradio/io_signature.h>
#include <iostream>

namespace gr {
  namespace trellis {

    encoder_bb::sptr
    encoder_bb::make(const fsm &FSM, int ST)
    {
      return gnuradio::get_initial_sptr
	(new encoder_bb_impl(FSM,ST));
    }

    encoder_bb_impl::encoder_bb_impl(const fsm &FSM, int ST)
    : sync_block("encoder_bb",
		    io_signature::make(1, -1, sizeof(unsigned char)),
		    io_signature::make(1, -1, sizeof(unsigned char))),
      d_FSM(FSM),
      d_ST(ST)
    {
    }

    encoder_bb_impl::~encoder_bb_impl()
    {
    }

    int
    encoder_bb_impl::work(int noutput_items,
		      gr_vector_const_void_star &input_items,
		      gr_vector_void_star &output_items)
    {
      int ST_tmp = 0;
      int nstreams = input_items.size();

      for(int m=0;m<nstreams;m++) {
	const unsigned char *in = (const unsigned char*)input_items[m];
	unsigned char *out = (unsigned char *) output_items[m];
	ST_tmp = d_ST;

	// per stream processing
	for(int i = 0; i < noutput_items; i++) {
	  out[i] = (unsigned char)d_FSM.OS()[ST_tmp*d_FSM.I()+in[i]]; // direction of time?
	  ST_tmp = (int)d_FSM.NS()[ST_tmp*d_FSM.I()+in[i]];
	}
	// end per stream processing
      }
      d_ST = ST_tmp;

      return noutput_items;
    }

  } /* namespace trellis */
} /* namespace gr */
