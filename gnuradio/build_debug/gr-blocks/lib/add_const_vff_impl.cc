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

#include <add_const_vff_impl.h>
#include <gnuradio/io_signature.h>

namespace gr {
  namespace blocks {

    add_const_vff::sptr add_const_vff::make(std::vector<float> k)
    {
      return gnuradio::get_initial_sptr(new add_const_vff_impl(k));
    }

    add_const_vff_impl::add_const_vff_impl(std::vector<float> k)
      : sync_block ("add_const_vff",
		       io_signature::make (1, 1, sizeof (float)*k.size()),
		       io_signature::make (1, 1, sizeof (float)*k.size())),
      d_k(k)
    {
    }

    int
    add_const_vff_impl::work(int noutput_items,
		      gr_vector_const_void_star &input_items,
		      gr_vector_void_star &output_items)
    {
      float *iptr = (float *)input_items[0];
      float *optr = (float *)output_items[0];
      
      int nitems_per_block = output_signature()->sizeof_stream_item(0)/sizeof(float);
      
      for (int i = 0; i < noutput_items; i++)
	for (int j = 0; j < nitems_per_block; j++)
	  *optr++ = *iptr++ + d_k[j];
      
      return noutput_items;
    }

  } /* namespace blocks */
} /* namespace gr */
