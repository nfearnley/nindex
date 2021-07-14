import os
from setuptools.config import read_configuration

c = read_configuration('setup.cfg')
package_name = c['options']['packages'][0]
old_version = c['metadata']['version']
run_number = os.environ.get('GITHUB_RUN_NUMBER')
new_version = old_version + '.post' + run_number
print('package-name=' + package_name)
print('old-version=' + old_version)
print('new-version=' + new_version)
