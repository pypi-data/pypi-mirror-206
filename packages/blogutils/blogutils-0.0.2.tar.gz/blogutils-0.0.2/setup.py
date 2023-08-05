import setuptools

with open("README.md", "r") as fh:
 long_description = fh.read()

setuptools.setup(
 name='blogutils',
 version='0.0.2',
 author="Arvind Srivastav",
 author_email="alwen1928@gmail.com",
 description="A package for blog-related utilities",
 long_description=long_description,
 long_description_content_type="text/markdown",
 packages=setuptools.find_packages(),
 classifiers=[
 "Programming Language :: Python :: 3",
 "License :: OSI Approved :: MIT License",
 "Operating System :: OS Independent",
 ],
 python_requires='>=3.6',
)