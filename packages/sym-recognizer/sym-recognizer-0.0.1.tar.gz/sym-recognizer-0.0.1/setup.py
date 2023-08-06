from distutils.core import setup
import glob

files = glob.glob('recognizer/data/*.png')

setup(name='sym-recognizer',
      version='0.0.1',
      description='Python Symbol recognition library',
      author='Mixx3',
      author_email='mmiikkllee@yandex.ru',
      url='https://github.com/mixx3/SymRecognizer',
      license='BSD 2-Clause "Simplified"',
      packages=['recognizer', 'recognizer.methods'],
      data_files=[('data', files)],
      install_requires=["numpy", "matplotlib", "opencv-python"],
      )
