import setuptools

setuptools.setup(
    name="dr-converter",
    version="1.0.0",
    description="DR Font Converter.",
    author="Tom Joad",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={"console_scripts": ["drconv=DRConverter.dr_converter:main"]},
    install_requires=[
        "fonttools>=4.39.3",
        "skia-pathops>=0.7.4",
        "brotli>=1.0.9",
        "cffsubr>=0.2.9.post1",
        "afdko==3.9.5",
        "pathvalidate>=2.5.2",
        "PyQt6==6.5.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    python_requires=">=3.7",
    zip_safe=False,
)
