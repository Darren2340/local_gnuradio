/* -*- c++ -*- */
/*
 * Copyright 2004,2008,2009,2013 Free Software Foundation, Inc.
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

#ifndef INCLUDED_BLOCKS_VECTOR_SINK_C_H
#define INCLUDED_BLOCKS_VECTOR_SINK_C_H

#include <gnuradio/blocks/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace blocks {

    /*!
     * \brief gr_complex sink that writes to a vector
     * \ingroup debug_tools_blk
     */
    class BLOCKS_API vector_sink_c : virtual public sync_block
    {
    public:
      // gr::blocks::vector_sink_c::sptr
      typedef boost::shared_ptr<vector_sink_c> sptr;

      static sptr make(int vlen = 1);

      virtual void reset() = 0;
      virtual std::vector<gr_complex> data() const = 0;
      virtual std::vector<tag_t> tags() const = 0;
    };

  } /* namespace blocks */
} /* namespace gr */

#endif /* INCLUDED_BLOCKS_VECTOR_SINK_C_H */
