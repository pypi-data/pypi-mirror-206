from setuptools import setup, find_packages

setup(
    name='chan127-demo',
    version= '0.0.4',
    description='show one row of dataframe',
    long_description="123",
    long_description_content_type='text/markdown',
    install_requires=['pandas','click'],
    entry_points="""
    [console_scripts]
    showdf=showdf.main:main
    """,
    author='ck',
    author_email=None,
    packages=find_packages()
)
