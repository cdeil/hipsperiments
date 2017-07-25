import matplotlib
matplotlib.use('agg')
from hips import HipsTileMeta, HipsTileAllskyArray
import matplotlib.pyplot as plt
from astropy.visualization.mpl_normalize import simple_norm

meta_jpg = HipsTileMeta(order=3, ipix=497, file_format='jpg')
url = 'https://github.com/hipspy/hips-extra/raw/master/datasets/samples/IRAC4/Norder3/Allsky.jpg'
allsky = HipsTileAllskyArray.fetch(meta_jpg, url)
data = allsky.data.astype('float')
norm = simple_norm(data, 'linear', min_cut=0, max_cut=data.max())
plt.figure()
plt.imshow(data, norm=norm, origin='lower')
plt.tight_layout()
plt.savefig('Allsky_from_JPG.jpg')

tile = allsky.tile(271)
data = tile.data
norm = simple_norm(data, 'linear', min_cut=0, max_cut=data.max())
plt.figure()
plt.imshow(data, norm=norm, origin='lower')
plt.tight_layout()
plt.savefig('Tile_from_JPG.jpg')

meta_fits = HipsTileMeta(order=3, ipix=497, file_format='fits')
url = 'https://github.com/hipspy/hips-extra/raw/master/datasets/samples/IRAC4/Norder3/Allsky.fits'
allsky = HipsTileAllskyArray.fetch(meta_fits, url)
data = allsky.data.astype('float')
norm = simple_norm(data, 'log', min_cut=0, max_cut=data.max())
plt.figure()
plt.imshow(data, norm=norm, origin='lower')
plt.tight_layout()
plt.savefig('Allsky_from_FITS.jpg')

tile = allsky.tile(271)
data = tile.data
norm = simple_norm(data, 'linear', min_cut=0, max_cut=data.max())
plt.figure()
plt.imshow(data, norm=norm, origin='lower')
plt.tight_layout()
plt.savefig('Tile_from_FITS.jpg')
