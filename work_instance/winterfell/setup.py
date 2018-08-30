import setuptools

try:
    import multiprocessing
except ImportError:
    pass

setuptools.setup(
    name='winterfell',
    version='1.0',
    packages=['winterfell'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['pecan']
)
