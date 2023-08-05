import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="maharashtra-forts", # Replace with the name of your package
    version="0.8", # Replace with the version of your package
    author="Rahul Bhoyar",
    author_email="rahulbhoyaroffice@gmail.com",
    description="A Python library for exploring forts in Maharashtra",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/maharashtra-forts",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # Add any third-party libraries your package depends on
        # Example: "numpy>=1.16.0"
    ],
    entry_points={
        # Add any console scripts or command-line interfaces
        # Example: "console_scripts": ["mycommand=mypackage.myfile:myfunction"]
    },
)
