from setuptools import setup,find_packages
VERSION = '0.0.3'
DESCRIPTION = 'Simple Simulator for Computer Vision'
LONG_DESCRIPTION = 'A package that allows to test how computer vision algorithms for advanced driving systems performs '

# Setting up
setup(
    name="systematica",
    version=VERSION,
    author="TucuAI (Tucudean Adrian-Ionut)",
    author_email="<Tucudean.Adrian.Ionut@outlook.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    
    packages=find_packages(),
    install_requires=['opencv-python', 'pygame'],
    keywords=['python', 'simulator', 'computer vision', 'advanced driving', 'camera stream', 'camera handler'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)