import setuptools

setuptools.setup(
    name="fpgapy",
    version="0.0.1",
    author="David Brochart",
    author_email="david.brochart@gmail.com",
    description="NumPy-like API accelerated with FPGA",
    long_description="NumPy-like API accelerated with FPGA",
    long_description_content_type="text/markdown",
    url="https://github.com/davidbrochart/fpgapy",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
