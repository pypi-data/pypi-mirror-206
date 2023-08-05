from setuptools import setup

setup(
    name='WWOpenLabeling',
    version='1.0.5',
    description='OpenLabeling based annotator',
    author='',
    author_email='',
    packages=['WWOpenLabeling', 'WWOpenLabeling.helper_utils'],
    install_requires=[
        'lxml==4.3.0',
        'numpy==1.16.0',
        'opencv-contrib-python==3.4.9.33',
        'tqdm==4.29.1',
        'torch==1.5.1',
        'boto3==1.26.123',
        'm3u8==3.4.0',
        'aiohttp==3.8.4'
    ],
    python_requires='==3.7.16'
)
