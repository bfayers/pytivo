from distutils.core import setup

setup(
      name = 'pytivo',
      packages = ['pytivo'],
      package_dir = {'pytivo': 'pytivo'},
      package_data = {'pytivo': ['keycodes.json']},
      version = '0.0.1',
      description = 'Library To Control TiVo Devices',
      author = 'Ben Fayers',
      author_email = 'ben.fayers@gmail.com',
      url = 'https://github.com/bfayers/pytivo',
      download_url = 'https://github.com/bfayers/pytivo/archive/0.0.1.tar.gz',
      keywords = ['tivo', 'pytivo', 'control'],
)