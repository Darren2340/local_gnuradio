/* -*- c++ -*- */
/*
 * Copyright 2012 Free Software Foundation, Inc.
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

#include <vector_insert_b_impl.h>
#include <algorithm>
#include <gnuradio/io_signature.h>
#include <stdexcept>
#include <stdio.h>

namespace gr {
  namespace blocks {

    vector_insert_b::sptr
    vector_insert_b::make(const std::vector<unsigned char> &data, int periodicity, int offset)
    {
      return gnuradio::get_initial_sptr
        (new vector_insert_b_impl(data, periodicity, offset));
    }

    vector_insert_b_impl::vector_insert_b_impl(const std::vector<unsigned char> &data,
                             int periodicity, int offset)
    : block("vector_insert_b",
               io_signature::make(1, 1, sizeof(unsigned char)),
               io_signature::make(1, 1, sizeof(unsigned char))),
      d_data(data),
      d_offset(offset),
      d_periodicity(periodicity)
    {
      //printf("INITIAL: periodicity = %d, offset = %d\n", periodicity, offset);
      // some sanity checks
      assert(offset < periodicity);
      assert(offset >= 0);
      assert((size_t)periodicity > data.size());
    }

    vector_insert_b_impl::~vector_insert_b_impl()
    {}

    int
    vector_insert_b_impl::general_work(int noutput_items,
                              gr_vector_int &ninput_items,
                              gr_vector_const_void_star &input_items,
                              gr_vector_void_star &output_items)
    {
      unsigned char *out = (unsigned char *)output_items[0];
      const unsigned char *in = (const unsigned char *)input_items[0];

      int ii(0), oo(0);

      while((oo < noutput_items) && (ii < ninput_items[0])) {
        //printf("oo = %d, ii = %d, d_offset = %d, noutput_items = %d, ninput_items[0] = %d", oo, ii, d_offset, noutput_items, ninput_items[0]);
        //printf(", d_periodicity = %d\n", d_periodicity);
    
        if(d_offset >= ((int)d_data.size())) { // if we are in the copy region
          int max_copy = std::min(std::min(noutput_items - oo, ninput_items[0] - ii),
                                  d_periodicity - d_offset);
          //printf("copy %d from input\n", max_copy);
          memcpy( &out[oo], &in[ii], sizeof(unsigned char)*max_copy );
          //printf(" * memcpy returned.\n");
          ii += max_copy;
          oo += max_copy;
          d_offset = (d_offset + max_copy)%d_periodicity;
        } 
        else { // if we are in the insertion region
          int max_copy = std::min(noutput_items - oo, ((int)d_data.size()) - d_offset);
          //printf("copy %d from d_data[%d] to out[%d]\n", max_copy, d_offset, oo);
          memcpy(&out[oo], &d_data[d_offset], sizeof(unsigned char)*max_copy);
          //printf(" * memcpy returned.\n");
          oo += max_copy; 
          d_offset = (d_offset + max_copy)%d_periodicity;
          //printf(" ## (inelse) oo = %d, d_offset = %d\n", oo, d_offset);
        }
    
        //printf(" # exit else, on to next loop.\n");
      }
      //printf(" # got out of loop\n");

      //printf("consume = %d, produce = %d\n", ii, oo);
      consume_each(ii);
      return oo;
    }

  } /* namespace blocks */
} /* namespace gr */
