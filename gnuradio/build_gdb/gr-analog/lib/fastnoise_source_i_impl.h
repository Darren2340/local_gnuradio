/* -*- c++ -*- */
/*
 * Copyright 2013 Free Software Foundation, Inc.
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

#ifndef INCLUDED_ANALOG_FASTNOISE_SOURCE_I_IMPL_H
#define INCLUDED_ANALOG_FASTNOISE_SOURCE_I_IMPL_H

#include <gnuradio/analog/fastnoise_source_i.h>
#include <gnuradio/random.h>

namespace gr {
  namespace analog {

    class fastnoise_source_i_impl : public fastnoise_source_i
    {
    private:
      noise_type_t d_type;
      float d_ampl;
      gr::random d_rng;
      std::vector<int> d_samples;

    public:
      fastnoise_source_i_impl(noise_type_t type, float ampl, long seed, long samples);
      ~fastnoise_source_i_impl();

      int sample();
      int sample_unbiased();

      void set_type(noise_type_t type);
      void set_amplitude(float ampl);
      void generate();

      noise_type_t type() const { return d_type; }
      float amplitude() const { return d_ampl; }

      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } /* namespace filter */
} /* namespace gr */

#endif /* INCLUDED_ANALOG_FASTNOISE_SOURCE_I_IMPL_H */
