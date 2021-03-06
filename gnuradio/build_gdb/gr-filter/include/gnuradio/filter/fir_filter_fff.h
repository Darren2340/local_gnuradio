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

#ifndef INCLUDED_FILTER_FIR_FILTER_FFF_H
#define	INCLUDED_FILTER_FIR_FILTER_FFF_H

#include <gnuradio/filter/api.h>
#include <gnuradio/sync_decimator.h>

namespace gr {
  namespace filter {

    /*!
     * \brief FIR filter with float input, float output, and float taps
     * \ingroup filter_blk
     *
     * \details
     * The fir_filter_XXX blocks create finite impulse response
     * (FIR) filters that perform the convolution in the time
     * domain:
     *
     * \code
     *   out = 0
     *   for i in ntaps:
     *      out += input[n-i] * taps[i]
     * \endcode
     *
     * The taps are a C++ vector (or Python list) of values of the
     * type specified by the third letter in the block's suffix. For
     * this block, the value is of type float. Taps can be
     * created using the firdes or optfir tools.
     *
     * These versions of the filter can also act as down-samplers
     * (or decimators) by specifying an integer value for \p
     * decimation.
     */
    class FILTER_API fir_filter_fff : virtual public sync_decimator
    {
    public:

      // gr::filter::fir_filter_fff::sptr
      typedef boost::shared_ptr<fir_filter_fff> sptr;

      /*!
       * \brief FIR filter with float input, float output, and float taps
       *
       * \param decimation set the integer decimation rate
       * \param taps a vector/list of taps of type float
       */
      static sptr make(int decimation,
                       const std::vector<float> &taps);

      virtual void set_taps(const std::vector<float> &taps) = 0;
      virtual std::vector<float> taps() const = 0;
    };

  } /* namespace filter */
} /* namespace gr */

#endif /* INCLUDED_FILTER_FIR_FILTER_FFF_H */
