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

#ifndef INCLUDED_TRELLIS_ENCODER_II_H
#define INCLUDED_TRELLIS_ENCODER_II_H

#include <gnuradio/trellis/api.h>
#include <gnuradio/trellis/fsm.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace trellis {

    /*!
     * \brief Convolutional encoder.
     * \ingroup trellis_coding_blk
     */
    class TRELLIS_API encoder_ii : virtual public sync_block
    {
    public:
      // gr::trellis::encoder_ii::sptr
      typedef boost::shared_ptr<encoder_ii> sptr;

      static sptr make(const fsm &FSM, int ST);

      virtual fsm FSM() const = 0;
      virtual int ST() const = 0;
    };

  } /* namespace trellis */
} /* namespace gr */

#endif /* INCLUDED_TRELLIS_ENCODER_II_H */
