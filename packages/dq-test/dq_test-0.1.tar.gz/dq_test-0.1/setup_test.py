# from setuptools import setup
import setuptools
setuptools.setup(
    name='dq_test',
    version='0.1',
    author='deepak',
    author_email='deepak.pal@tredence.com',
    description="sample poc for DQ framework",
    py_modules=['dq_test','test_fun','indp_fun'],
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',    # NumPy as a required library
        'pandas',   # pandas as a required library
   
    ],
)

# from setuptools import setup, find_packages

# setup(
#     name='dq_test',
#     version='1.0',
#     packages=find_packages(),
#     install_requires=[
#         'numpy',    # NumPy as a required library
#         'pandas',   # pandas as a required library
   
#     ],
# )