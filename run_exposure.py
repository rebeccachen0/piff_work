import piff
import fitsio
import pixmappy
import numpy as np
import os
import logging

logger = logging.getLogger('run_piff')
pixmappy_dir = '/Users/rebeccachen/Piff/y3_test/pixmappy/'
# which_zone = fitsio.read(os.path.join(pixmappy_dir, 'which_zone.fits'))

piff_config = '/Users/rebeccachen/Piff/y3_test/piff.yaml'
expnum = 383252

#normal run
for i in [x for x in range(1, 63) if (x != 31 and x!= 61 and x!=2 and x!=5)]:
	ccdnum = i
	str_ccdnum = "%.2d" % ccdnum
	img_file = '/Users/rebeccachen/Desktop/Piff_work/y3_test/D00'+str(expnum)+'_r_c'+str_ccdnum+'_r2277p01_immasked.fits'

	# f = fitsio.FITS(img_file)
	# header_list = f[hdu].read_header_list()
	# header_list = [ d for d in header_list if 'CONTINUE' not in d['name'] ]
	# h = fitsio.FITSHDR(header_list)
	# detpos = h['DETPOS'].strip()
	# dp = detpos[ccdnum]
	# wz = np.where((which_zone['expnum'] == expnum) & (which_zone['detpos'] == dp))[0][0]
	# zone = which_zone['zone'][wz]

	# pixmappy = os.path.join(pixmappy_dir, 'zone%03d.astro'%zone)
	# wcs = pixmappy.GalSimWCS(pixmappy_file, exp=expnum, ccdnum=ccdnum, default_color=0)

	cat_file = '/Users/rebeccachen/Desktop/Piff_work/y3_test/'+str(expnum)+'_c'+str_ccdnum+'.fits'
	psf_file = '/Users/rebeccachen/Desktop/Piff_work/y3_test/D00'+str(expnum)+'_r_c'+str_ccdnum+'_r2277p01_gaiamatch.piff'


	config = piff.read_config(piff_config)
	config['input']['image_file_name'] = img_file
	config['input']['cat_file_name'] = cat_file
	config['output']['file_name'] = psf_file
	# config['input']['wcs']['file_name'] = pixmappy
	# config['input']['wcs']['exp'] = expnum
	# config['input']['wcs']['ccdnum'] = ccdnum
	piff.piffify(config, logger)


#gaia matches run
for i in [x for x in range(1, 63) if (x != 31 and x!= 61 and x!=2 and x!=5)]:
	ccdnum = i
	str_ccdnum = "%.2d" % ccdnum
	img_file = '/Users/rebeccachen/Desktop/Piff_work/y3_test/D00'+str(expnum)+'_r_c'+str_ccdnum+'_r2277p01_immasked.fits'

	# f = fitsio.FITS(img_file)
	# header_list = f[hdu].read_header_list()
	# header_list = [ d for d in header_list if 'CONTINUE' not in d['name'] ]
	# h = fitsio.FITSHDR(header_list)
	# detpos = h['DETPOS'].strip()
	# dp = detpos[ccdnum]
	# wz = np.where((which_zone['expnum'] == expnum) & (which_zone['detpos'] == dp))[0][0]
	# zone = which_zone['zone'][wz]

	# pixmappy = os.path.join(pixmappy_dir, 'zone%03d.astro'%zone)
	# wcs = pixmappy.GalSimWCS(pixmappy_file, exp=expnum, ccdnum=ccdnum, default_color=0)

	cat_file = '/Users/rebeccachen/Desktop/Piff_work/y3_test/'+str(expnum)+'_c'+str_ccdnum+'_gaiamatches.fits'
	psf_file = '/Users/rebeccachen/Desktop/Piff_work/y3_test/D00'+str(expnum)+'_r_c'+str_ccdnum+'_r2277p01.piff'


	config = piff.read_config(piff_config)
	config['input']['image_file_name'] = img_file
	config['input']['cat_file_name'] = cat_file
	config['output']['file_name'] = psf_file
	# config['input']['wcs']['file_name'] = pixmappy
	# config['input']['wcs']['exp'] = expnum
	# config['input']['wcs']['ccdnum'] = ccdnum
	piff.piffify(config, logger)