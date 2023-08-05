from setuptools import setup

install_requires = [
    'bottle >= 0.12',
    'numpy >= 1.7',
    'PyYAML >= 3.10',
    'urllib3 >= 1.10',
    'python-dateutil',
]

setup(
    name = 'ligo-scald',
    description = 'SCalable Analytics for Ligo Data',
    long_description = "file: README.md",
    long_description_content_type = "text/markdown",
    version = '0.8.4',
    author = 'Patrick Godwin',
    author_email = 'patrick.godwin@ligo.org',
    url = 'https://git.ligo.org/gstlal-visualisation/ligo-scald.git',
    license = 'GPLv2+',

    packages = ['ligo', 'ligo.scald', 'ligo.scald.io', 'ligo.scald.tests', 'static', 'templates'],
    namespace_packages = ['ligo'],

    package_data = {
        'static': ['*'],
        'templates': ['*'],
    },

    entry_points = {
        'console_scripts': [
            'scald = ligo.scald.__main__:main',
        ],
    },

    python_requires = '>=3.6',
    install_requires = install_requires,
    zip_safe = False,

    classifiers = [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Science/Research',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
    ],

)
