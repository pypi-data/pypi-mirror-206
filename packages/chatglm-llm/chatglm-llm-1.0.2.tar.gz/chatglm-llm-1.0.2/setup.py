
from setuptools import setup, find_packages


setup(name='chatglm-llm',
    version='1.0.2',
    description='chatglm llm',
    url='https://github.com/xxx',
    author='auth',
    author_email='xxx@gmail.com',
    license='MIT',
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(),
    install_requires=['sentence_transformers',
        'tensorboard',
        'requests',
        "protobuf",
        "cpm_kernels",
        "mdtex2html",
        "sentencepiece",
        "accelerate",
        'torch',
        'termcolor',
        'tqdm',
        'websockets',
        'websocket',
        'websocket-client',
        'transformers',
        'aiowebsocket',
        
        ],
    entry_points={
        'console_scripts': [
            'chatglm-web=chatglm_src.cmd:main',
        ]
    },

)
