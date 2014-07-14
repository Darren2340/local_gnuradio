/* -*- c++ -*- */
/*
 * Copyright 2006,2009,2013 Free Software Foundation, Inc.
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

#if HAVE_CONFIG_H
#include <config.h>
#endif

#include <gnuradio/constants.h>

namespace gr {

  const std::string
  prefix()
  {
    return "/home/darren/repos/local_gnuradio_release";
  }

  const std::string
  sysconfdir()
  {
    return "/home/darren/repos/local_gnuradio_release/etc";
  }

  const std::string
  prefsdir()
  {
    return "/home/darren/repos/local_gnuradio_release/etc/gnuradio/conf.d";
  }

  const std::string
  build_date()
  {
    return "Fri, 11 Jul 2014 16:43:47";
  }

  const std::string
  version()
  {
    return "v3.7.x-xxx-xunknown";
  }

  const std::string
  c_compiler()
  {
    return "cc (GCC) 4.8.2 20131212 (Red Hat 4.8.2-7) \nCopyright (C) 2013 Free Software Foundation, Inc. \nThis is free software see the source for copying conditions.  There is NO \nwarranty not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.";
  }    

  const std::string
  cxx_compiler()
  {
    return "c++ (GCC) 4.8.2 20131212 (Red Hat 4.8.2-7) \nCopyright (C) 2013 Free Software Foundation, Inc. \nThis is free software see the source for copying conditions.  There is NO \nwarranty not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.";
  }    

  const std::string
  compiler_flags()
  {
    return "/usr/lib64/ccache/cc:::-O3 -DNDEBUG  \n/usr/lib64/ccache/c++:::-O3 -DNDEBUG";
  }    

} /* namespace gr */
