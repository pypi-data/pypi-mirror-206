from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='rsisa',
    version='0.1.1',
    description='Remote Sensing Instance Segmentation Algorithms',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ZhiangChen/instance_segmentation_remote_sensing',
    author='Zhiang Chen',
    author_email='zxc251@case.edu',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'numpy>=1.24.2',
        'pandas>=2.0.0',
        'geopandas>=0.12.0',
        'rasterio>=1.3.6',
        'rioxarray>=0.13.4',
        'opencv-python>=4.7.0.72',
        'tqdm>=4.65.0',
        'shapely>=2.0.1',
        'matplotlib>=3.7.1',
        'fiona>=1.9.3',
        'pyproj>=3.5.0',
        'GDAL>=3.3.2',
    ],
)

