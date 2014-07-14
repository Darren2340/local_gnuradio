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

#ifndef INCLUDED_ANALOG_FASTNOISE_SOURCE_I_H
#define INCLUDED_ANALOG_FASTNOISE_SOURCE_I_H

#include <gnuradio/analog/api.h>
#include <gnuradio/analog/noise_type.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace analog {

    /*!
     * \brief Random number source
     * \ingroup source_blk
     *
     * \details
     * Generate random values from different distributions.
     * Currently, only Gaussian and uniform are enabled.
     */
    class ANALOG_API fastnoise_source_i : virtual public sync_block
    {
    public:
      // gr::analog::fastnoise_source_i::sptr
      typedef boost::shared_ptr<fastnoise_source_i> sptr;

      /*! \brief Make a fast noise source
       * \param type    the random distribution to use (see gnuradio/analog/noise_type.h)
       * \param ampl    a scaling factor for the output; for Gaussian sources, this is the std. dev.
       * \param seed    seed for random generators. Note that for uniform and
       *                Gaussian distributions, this should be a negative number.
       * \param samples Number of samples to pre-generate
       */
      static sptr make(noise_type_t type, float ampl,
		       long seed = 0, long samples=1024*16);
      virtual int sample() = 0;
      virtual int sample_unbiased() = 0;

      virtual void set_type(noise_type_t type) = 0;
      virtual void set_amplitude(float ampl) = 0;

      virtual noise_type_t type() const = 0;
      virtual float amplitude() const = 0;
    };

  } /* namespace analog */
} /* namespace gr */


#endif /* INCLUDED_ANALOG_FASTNOISE_SOURCE_I_H */