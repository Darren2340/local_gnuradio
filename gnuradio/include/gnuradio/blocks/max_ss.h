/* -*- c++ -*- */
/*
 * Copyright 2007,2013-2014 Free Software Foundation, Inc.
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

#ifndef INCLUDED_BLOCKS_MAX_SS_H
#define INCLUDED_BLOCKS_MAX_SS_H

#include <gnuradio/blocks/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace blocks {

    /*!
     * \brief Compares vectors from multiple streams and determines
     * the maximum value from each vector over all streams.
     * \ingroup math_operators_blk
     *
     * \details
     * Data is passed in as a vector of length \p vlen from multiple
     * input sources. It will look through these streams of \p vlen
     * data items and the output stream will contain the maximum value
     * in the vector.
     */
    class BLOCKS_API max_ss : virtual public sync_block
    {
    public:
      // gr::blocks::max_ss::sptr
      typedef boost::shared_ptr<max_ss> sptr;

      static sptr make(size_t vlen);
    };

  } /* namespace blocks */
} /* namespace gr */

#endif /* INCLUDED_BLOCKS_MAX_SS_H */