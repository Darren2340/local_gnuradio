
#!/bin/python2

import sys, os, re
sys.path.append('/home/darren/repos/local_gnuradio/gnuradio/gnuradio-runtime/python')
os.environ['srcdir'] = '/home/darren/repos/local_gnuradio/gnuradio/gr-fec/include/gnuradio/fec'
os.chdir('/home/darren/repos/local_gnuradio/gnuradio/build_release/gr-fec/include/gnuradio/fec')

if __name__ == '__main__':
    import build_utils
    root, inp = sys.argv[1:3]
    for sig in sys.argv[3:]:
        name = re.sub ('X+', sig, root)
        d = build_utils.standard_dict(name, sig, 'fec')
        build_utils.expand_template(d, inp)

