
#!/bin/python2

import sys, os, re
sys.path.append('/home/darren/repos/local_gnuradio/gnuradio/gnuradio-runtime/python')
os.environ['srcdir'] = '/home/darren/repos/local_gnuradio/gnuradio/gr-analog/include/gnuradio/analog'
os.chdir('/home/darren/repos/local_gnuradio/gnuradio/build_gdb/gr-analog/include/gnuradio/analog')

if __name__ == '__main__':
    import build_utils
    root, inp = sys.argv[1:3]
    for sig in sys.argv[3:]:
        name = re.sub ('X+', sig, root)
        d = build_utils.standard_dict2(name, sig, 'analog')
        build_utils.expand_template(d, inp)

