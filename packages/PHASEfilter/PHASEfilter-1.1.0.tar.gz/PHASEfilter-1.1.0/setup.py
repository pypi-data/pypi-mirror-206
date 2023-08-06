#!/usr/bin/env python3
# encoding: utf-8

import setuptools
from PHASEfilter.lib.constants import version
from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

## 
## cd where setup.py is
## rm dist/*
## python3 setup.py sdist bdist_wheel --plat-name=linux_x86_64
## python3 -m twine upload dist/*
#### and press cancel in all windows
### to test in virtual env
## python3 -m pip install dist/PHASEfilter-0.1-py3-none-any.whl --install-option test


with open("README.md", 'r') as fh:
	long_description = fh.read()

class bdist_wheel(_bdist_wheel):
	def finalize_options(self):
		_bdist_wheel.finalize_options(self)
		# Mark us as not a pure python package
		self.root_is_pure = False
		
setuptools.setup(
	name='PHASEfilter',
	version=version.VERSION_package,
	scripts=['PHASEfilter/bin/phasefilter.py',
			'PHASEfilter/bin/phasefilter_single.py', 
			'PHASEfilter/bin/make_alignment.py',
			'PHASEfilter/bin/reference_statistics.py',
			'PHASEfilter/bin/synchronize_genomes.py',
			'PHASEfilter/bin/copy_raw_data_example_phasefilter.py',
			'PHASEfilter/bin/install_phasefilter_dependencies.sh'],
	author="Miguel Pinheiro",
	author_email="monsanto@ua.pt",
	description="Software package to filter variants, SNPs and INDELs, that are present in heterozygous form in phased genomes.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/ibigen/PHASEfilter",
	packages=setuptools.find_packages(),
	package_data={
			'PHASEfilter': ['tests/files/gff3/*',
						'tests/files/real_raw_data/*',
						'tests/files/ref/*',
						'tests/files/referenceSaccharo/*',
						'tests/files/result/*',
						'tests/files/software/*',
						'tests/files/synchronize/*',
						'tests/files/vcf/*'],
			},
	license='MIT',
	python_requires='>=3.5',
	include_package_data=True, # include other files
	platforms=['Linux'],
	classifiers=[
		# How mature is this project? Common values are
		#   Development Status :: 1 - Planning
		#	Development Status :: 2 - Pre-Alpha
		#	Development Status :: 3 - Alpha
		#	Development Status :: 4 - Beta
		#	Development Status :: 5 - Production/Stable
		#	Development Status :: 6 - Mature
		#	Development Status :: 7 - Inactive
		'Development Status :: 5 - Production/Stable',
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
#		"Programming Language :: Python :: 3.9",
		"License :: OSI Approved :: MIT License",
		"Operating System :: POSIX :: Linux",
#		'Operating System :: POSIX',
		"Operating System :: MacOS :: MacOS X",
		"Intended Audience :: Science/Research",
		"Topic :: Scientific/Engineering :: Bio-Informatics",
	],
	install_requires=[
		"pyvcf==0.6.8",
		"pysam==0.15.2",
		"biopython==1.78",
		"gff3tool==2.0.1",
		"pyliftover==0.4",
		"wheel",
	],
	entry_points={
		'console_scripts': [
			'make_alignment = PHASEfilter.bin.make_alignment:main',
			'reference_statistics = PHASEfilter.bin.reference_statistics:main',
			'phasefilter = PHASEfilter.bin.phasefilter:main',
			'phasefilter_single = PHASEfilter.bin.phasefilter_single:main',
			'synchronize_genomes = PHASEfilter.bin.synchronize_genomes:main',
			'copy_raw_data_example_phasefilter = PHASEfilter.bin.copy_raw_data_example_phasefilter:main',
		],
	},
	tests_require=['tox'],
	
	# Note that this is a string of words separated by whitespace, not a list.
	keywords='SNPs INDEL phased genome filtering bioinformatics',  # Optional
	
	project_urls={  # Optional
		'Bug Reports': 'https://github.com/ibigen/PHASEfilter/issues',
		'Source': 'https://github.com/ibigen/PHASEfilter',
		'Documentation': 'https://phasefilter.readthedocs.io/en/latest/index.html',
	},
	
)