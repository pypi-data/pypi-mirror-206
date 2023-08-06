import setuptools
from pathlib import Path

setuptools.setup(
    name='urgxy_env',
    author="GXY",
    version='0.1.7',
    description="An OpenAI Gym Env for dual UR5",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(include="urgxy_env*"),
    install_requires=['gym', 'pybullet', 'numpy'],
    python_requires='>=3.6'
)

