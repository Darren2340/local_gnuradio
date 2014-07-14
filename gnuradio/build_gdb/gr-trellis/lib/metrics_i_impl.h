/* -*- c++ -*- */
/*
 * Copyright 2004,2012 Free Software Foundation, Inc.
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

#ifndef INCLUDED_TRELLIS_METRICS_I_IMPL_H
#define INCLUDED_TRELLIS_METRICS_I_IMPL_H

#include <gnuradio/trellis/metrics_i.h>

namespace gr {
  namespace trellis {

    class metrics_i_impl : public metrics_i
    {
    private:
      int d_O;
      int d_D;
      digital::trellis_metric_type_t d_TYPE;
      std::vector<int> d_TABLE;

    public:
      metrics_i_impl(int O, int D,  const std::vector<int> &TABLE,
		  digital::trellis_metric_type_t TYPE);
      ~metrics_i_impl();
      
      int O() const { return d_O; }
      int D() const { return d_D; }
      digital::trellis_metric_type_t TYPE() const { return d_TYPE; }
      std::vector<int> TABLE() const { return d_TABLE; }
      void set_TABLE(const std::vector<int> &table);

      void forecast(int noutput_items,
		    gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
		       gr_vector_int &ninput_items,
		       gr_vector_const_void_star &input_items,
		       gr_vector_void_star &output_items);
    };

  } /* namespace trellis */
} /* namespace gr */

#endif /* INCLUDED_TRELLIS_METRICS_I_IMPL_H */
