from setuptools import setup

setup(
    name="custom_rails",
    keywords=["wsgi", "framework", ],
    version="0.0.6",
    maintainer="Patcas Rares",
    package_data={"custom_rails": ["templates/*"]},
    description="An educational wsgi based python web framework",
    packages=["custom_rails"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={
        'console_scripts': [
            'custom_rails = custom_rails.cli:main',
        ]
    }
)
