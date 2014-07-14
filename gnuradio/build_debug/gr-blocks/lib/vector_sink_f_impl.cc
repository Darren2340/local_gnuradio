/* -*- c++ -*- */
/*
 * Copyright 2004,2008,2010,2013 Free Software Foundation, Inc.
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
#include <config.h>
#endif

#include <vector_sink_f_impl.h>
#include <gnuradio/io_signature.h>
#include <algorithm>
#include <iostream>

namespace gr {
  namespace blocks {

    vector_sink_f::sptr
    vector_sink_f::make(int vlen)
    {
      return gnuradio::get_initial_sptr
        (new vector_sink_f_impl(vlen));
    }
  
    vector_sink_f_impl::vector_sink_f_impl(int vlen)
    : sync_block("vector_sink_f",
                    io_signature::make(1, 1, sizeof(float) * vlen),
                    io_signature::make(0, 0, 0)),
    d_vlen(vlen)
    {
    }

    vector_sink_f_impl::~vector_sink_f_impl()
    {}

    std::vector<float>
    vector_sink_f_impl::data() const
    {
      return d_data;
    }

    std::vector<tag_t>
    vector_sink_f_impl::tags() const
    {
      return d_tags;
    }

    int
    vector_sink_f_impl::work(int noutput_items,
                      gr_vector_const_void_star &input_items,
                      gr_vector_void_star &output_items)
    {
      float *iptr = (float*)input_items[0];

      for(int i = 0; i < noutput_items * d_vlen; i++)
        d_data.push_back (iptr[i]);
      std::vector<tag_t> tags;
      get_tags_in_range(tags, 0, nitems_read(0), nitems_read(0) + noutput_items);
      d_tags.insert(d_tags.end(), tags.begin(), tags.end());
      return noutput_items;
    }

  } /* namespace blocks */
} /* namespace gr */
