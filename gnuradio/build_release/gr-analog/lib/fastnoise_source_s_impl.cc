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

/* WARNING: this file is machine generated. Edits will be overwritten */

#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

#include "fastnoise_source_s_impl.h"
#include <gnuradio/io_signature.h>
#include <stdexcept>

namespace gr {
  namespace analog {
    
    fastnoise_source_s::sptr
    fastnoise_source_s::make(noise_type_t type, float ampl, long seed, long samples)
    {
      return gnuradio::get_initial_sptr
	(new fastnoise_source_s_impl(type, ampl, seed, samples));
    }

    fastnoise_source_s_impl::fastnoise_source_s_impl(noise_type_t type, float ampl, long seed, long samples)
    : sync_block("fastnoise_source_s",
		    io_signature::make(0, 0, 0),
		    io_signature::make(1, 1, sizeof(short))),
      d_type(type),
      d_ampl(ampl),
      d_rng(seed)
    {
      d_samples.resize(samples);
      generate();
    }

    fastnoise_source_s_impl::~fastnoise_source_s_impl()
    {
    }

    void
    fastnoise_source_s_impl::set_type(noise_type_t type)
    {
      gr::thread::scoped_lock l(d_setlock);
      d_type = type;
      generate();
    }
    
    void
    fastnoise_source_s_impl::set_amplitude(float ampl) 
    {
      gr::thread::scoped_lock l(d_setlock);
      d_ampl = ampl;
      generate();
    }

    void
    fastnoise_source_s_impl::generate()
    {
      int noutput_items = d_samples.size();
      switch(d_type){
#if 0	// complex?

      case GR_UNIFORM:
	for(int i = 0; i < noutput_items; i++)
	  d_samples[i] = gr_complex(d_ampl * ((d_rng.ran1() * 2.0) - 1.0),
				    d_ampl * ((d_rng.ran1() * 2.0) - 1.0));
	break;

      case GR_GAUSSIAN:
	for(int i = 0; i < noutput_items; i++)
	  d_samples[i] = d_ampl * d_rng.rayleigh_complex();
	break;

#else			// nope...

      case GR_UNIFORM:
	for(int i = 0; i < noutput_items; i++)
	  d_samples[i] = (short)(d_ampl * ((d_rng.ran1() * 2.0) - 1.0));
	break;

      case GR_GAUSSIAN:
	for(int i = 0; i < noutput_items; i++)
	  d_samples[i] = (short)(d_ampl * d_rng.gasdev());
	break;

      case GR_LAPLACIAN:
	for(int i = 0; i < noutput_items; i++)
	  d_samples[i] = (short)(d_ampl * d_rng.laplacian());
	break;

      case GR_IMPULSE:	// FIXME changeable impulse settings
	for(int i = 0; i < noutput_items; i++)
	  d_samples[i] = (short)(d_ampl * d_rng.impulse(9));
	break;
#endif

      default:
	throw std::runtime_error("invalid type");
      }
    }

    int
    fastnoise_source_s_impl::work(int noutput_items,
		      gr_vector_const_void_star &input_items,
		      gr_vector_void_star &output_items)
    {
      gr::thread::scoped_lock l(d_setlock);

      short *out = (short*)output_items[0];

      for(int i=0; i<noutput_items; i++) {
        out[i] = sample();
      }

      return noutput_items;
    }

    short fastnoise_source_s_impl::sample()
    {
#ifdef __USE_GNU
        size_t idx = lrand48() % d_samples.size();
#else
        size_t idx = rand() % d_samples.size();
#endif
        return d_samples[idx];
    }

#ifndef FASTNOISE_RANDOM_SIGN
#ifdef _MSC_VER
#define FASTNOISE_RANDOM_SIGN       ((rand()%2==0)?1:-1)
#else
#define FASTNOISE_RANDOM_SIGN       ((lrand48()%2==0)?1:-1)
#endif
#endif

    short fastnoise_source_s_impl::sample_unbiased()
    {
#if 0 
        gr_complex s(sample());
        return gr_complex(FASTNOISE_RANDOM_SIGN * s.real(),
                          FASTNOISE_RANDOM_SIGN * s.imag());
#else
        return FASTNOISE_RANDOM_SIGN * sample();
#endif
    }

  } /* namespace analog */
} /* namespace gr */

