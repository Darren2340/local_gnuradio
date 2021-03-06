/* -*- c++ -*- */
/*
 * Copyright 2005,2010,2012-2013 Free Software Foundation, Inc.
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


#include <probe_signal_vb_impl.h>
#include <gnuradio/io_signature.h>

namespace gr {
  namespace blocks {

    probe_signal_vb::sptr
    probe_signal_vb::make(size_t size)
    {
      return gnuradio::get_initial_sptr
        (new probe_signal_vb_impl(size));
    }

    probe_signal_vb_impl::probe_signal_vb_impl(size_t size)
    : sync_block("probe_signal_vb",
                    io_signature::make(1, 1, size*sizeof(unsigned char)),
                    io_signature::make(0, 0, 0)),
      d_level(size, 0), d_size(size)
    {
    }

    probe_signal_vb_impl::~probe_signal_vb_impl()
    {
    }

    int
    probe_signal_vb_impl::work(int noutput_items,
                      gr_vector_const_void_star &input_items,
                      gr_vector_void_star &output_items)
    {
      const unsigned char *in = (const unsigned char *)input_items[0];

      for(size_t i=0; i<d_size; i++)
	d_level[i] = in[(noutput_items-1)*d_size+i];

      return noutput_items;
    }

  } /* namespace blocks */
} /* namespace gr */
