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

/* WARNING: this file is machine generated. Edits will be overwritten */

#ifndef INCLUDED_DIGITAL_CHUNKS_TO_SYMBOLS_IF_IMPL_H
#define INCLUDED_DIGITAL_CHUNKS_TO_SYMBOLS_IF_IMPL_H

#include <gnuradio/digital/chunks_to_symbols_if.h>

namespace gr {
  namespace digital {

    class chunks_to_symbols_if_impl : public chunks_to_symbols_if
    {
    private:
      int d_D;
      std::vector<float> d_symbol_table;

    public:
      chunks_to_symbols_if_impl(const std::vector<float> &symbol_table, const int D = 1);

      ~chunks_to_symbols_if_impl();

      void set_vector_from_pmt(std::vector<float> &symbol_table, pmt::pmt_t &symbol_table_pmt);
      void set_vector_from_pmt(std::vector<gr_complex> &symbol_table, pmt::pmt_t &symbol_table_pmt);

      void handle_set_symbol_table(pmt::pmt_t symbol_table_pmt);
      void set_symbol_table(std::vector<float> &symbol_table);
      
      int D() const { return d_D; }
      std::vector<float> symbol_table() const { return d_symbol_table; }

      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);

      bool check_topology(int ninputs, int noutputs) { return ninputs == noutputs; }
    };

  } /* namespace digital */
} /* namespace gr */

#endif /* INCLUDED_DIGITAL_CHUNKS_TO_SYMBOLS_IF_IMPL_H */
