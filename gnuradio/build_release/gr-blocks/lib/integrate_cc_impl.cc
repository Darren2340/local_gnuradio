/* -*- c++ -*- */
/*
 * Copyright 2004,2009,2010,2012 Free Software Foundation, Inc.
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

#include <integrate_cc_impl.h>
#include <gnuradio/io_signature.h>

namespace gr {
  namespace blocks {

    integrate_cc::sptr integrate_cc::make(int decim)
    {
      return gnuradio::get_initial_sptr(new integrate_cc_impl(decim));
    }

    integrate_cc_impl::integrate_cc_impl(int decim)
      : sync_decimator("integrate_cc",
			  io_signature::make(1, 1, sizeof (gr_complex)),
			  io_signature::make(1, 1, sizeof (gr_complex)),
			  decim),
      d_decim(decim),
      d_count(0)
    {
    }

    int
    integrate_cc_impl::work(int noutput_items,
		      gr_vector_const_void_star &input_items,
		      gr_vector_void_star &output_items)
    {
      const gr_complex *in = (const gr_complex *)input_items[0];
      gr_complex *out = (gr_complex *)output_items[0];

      for (int i = 0; i < noutput_items; i++) {
	out[i] = (gr_complex)0;
	for (int j = 0; j < d_decim; j++)
	  out[i] += in[i*d_decim+j];
      }
      
      return noutput_items;
    }

  } /* namespace blocks */
} /* namespace gr */
