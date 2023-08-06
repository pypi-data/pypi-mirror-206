import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="easy_mitk",
    version="0.0.1",  # 本版本可以不进行更新
    author="Daryl.Xu",
    author_email="ziqiang_xu@qq.com",
    description="Easy medical imaging toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/daryl6/easy-mitk",
    packages=setuptools.find_packages(),
    install_requires=[
        'pydicom', 'nibabel', 'pylibjpeg-rle', 'dicom2nifti'
        ],
    entry_points={
    },
    classifiers=(
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ),
)
