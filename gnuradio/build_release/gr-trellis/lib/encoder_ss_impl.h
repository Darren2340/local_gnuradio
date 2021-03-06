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

#ifndef INCLUDED_TRELLIS_ENCODER_SS_IMPL_H
#define INCLUDED_TRELLIS_ENCODER_SS_IMPL_H

#include <gnuradio/trellis/encoder_ss.h>

namespace gr {
  namespace trellis {

    class encoder_ss_impl : public encoder_ss
    {
    private:
      fsm d_FSM;
      int d_ST;

    public:
      encoder_ss_impl(const fsm &FSM, int ST);
      ~encoder_ss_impl();

      fsm FSM() const { return d_FSM; }
      int ST() const { return d_ST; }

      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } /* namespace trellis */
} /* namespace gr */

#endif /* INCLUDED_TRELLIS_ENCODER_SS_IMPL_H */
