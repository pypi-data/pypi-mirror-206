import setuptools
with open('hexo_inpainting/requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
 name='hexo_inpainting',
 version='1.0.5',
 author="Hexo.ai",
 author_email="saurabh@hexo.ai",
 description="This is an image editing tool",
 packages=setuptools.find_packages(),
 install_requires=required,
 classifiers=[
 "Programming Language :: Python :: 3",
 "License :: OSI Approved :: MIT License",
 "Operating System :: OS Independent",
 ],
)