from setuptools import setup, find_packages
import versioneer

project_name = 'menpofit'

# Versioneer allows us to automatically generate versioning from
# our git tagging system which makes releases simpler.
versioneer.VCS = 'git'
versioneer.versionfile_source = '{}/_version.py'.format(project_name)
versioneer.versionfile_build = '{}/_version.py'.format(project_name)
versioneer.tag_prefix = 'v'  # tags are like v1.2.0
versioneer.parentdir_prefix = project_name + '-'  # dirname like 'menpo-v1.2.0'


setup(name=project_name,
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Pickle anything to HDF5',
      author='James Booth',
      author_email='james.booth08@imperial.ac.uk',
      packages=find_packages(),
      install_requires=['numpy==1.9.0',
                        'scipy==0.14.0',
                        'wrapt==1.9.0'
                        ])