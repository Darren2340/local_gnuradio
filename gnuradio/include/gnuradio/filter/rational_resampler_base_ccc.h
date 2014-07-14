/* -*- c++ -*- */
/*
 * Copyright 2005,2012 Free Software Foundation, Inc.
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

#ifndef INCLUDED_FILTER_RATIONAL_RESAMPLER_BASE_CCC_H
#define	INCLUDED_FILTER_RATIONAL_RESAMPLER_BASE_CCC_H

#include <gnuradio/filter/api.h>
#include <gnuradio/block.h>


namespace gr {
  namespace filter {

    /*!
     * \brief Rational Resampling Polyphase FIR filter with gr_complex
     * input, gr_complex output and gr_complex taps.
     * \ingroup resamplers_blk
     */
    class FILTER_API rational_resampler_base_ccc : virtual public block
    {
    public:
      // gr::filter::rational_resampler_base_ccc::sptr
      typedef boost::shared_ptr<rational_resampler_base_ccc> sptr;

      static sptr make(unsigned interpolation,
                       unsigned decimation,
                       const std::vector<gr_complex> &taps);

      virtual unsigned interpolation() const = 0;
      virtual unsigned decimation() const = 0;

      virtual void set_taps(const std::vector<gr_complex> &taps) = 0;
      virtual std::vector<gr_complex> taps() const = 0;
    };

  } /* namespace filter */
} /* namespace gr */

#endif /* INCLUDED_FILTER_RATIONAL_RESAMPLER_BASE_CCC_H */
