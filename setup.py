from setuptools import setup

install_requires = [
    "matplotlib>=3.2.2",
    "numpy>=1.18.5,<1.24.0",
    "opencv-python>=4.1.1",
    "Pillow>=7.1.2",
    "PyYAML>=5.3.1",
    "requests>=2.23.0",
    "scipy>=1.4.1",
    "torch>=1.7.0",
    "torchvision>=0.8.1",
    "tqdm>=4.41.0",
    "protobuf<4.21.3",
    "pandas>=1.1.4",
    "seaborn>=0.11.0",
    "Cython",
    "psutil",
    "thop",
]

setup(
    name="yolov7",
    version="1.0",
    description="Modulize YOLOv7",
    packages=["yolov7"],
    install_requires=install_requires,
    license_files=("LICENSE.md")
)