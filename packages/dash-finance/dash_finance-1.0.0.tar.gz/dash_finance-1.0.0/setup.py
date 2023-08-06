from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))


VERSION = '1.0.0'
DESCRIPTION = 'Lightweight finance chart plotter '
LONG_DESCRIPTION = 'A package that allows to plot candlesticks, line charts and text in simpler and easy way'

# Setting up
setup(
    name="dash_finance",
    version=VERSION,
    author="Amit Buyo",
    author_email="amitbuyo2021@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    setup_requires = ["wheel"],
    install_requires=['dash', 'pandas', 'plotly'],
    keywords=['python', 'dash', 'finance', 'plotly'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)