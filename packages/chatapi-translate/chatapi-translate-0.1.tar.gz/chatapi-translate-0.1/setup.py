# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

if os.path.exists('readme.md'):
    long_description = open('readme.md', 'r', encoding='utf8').read()
else:
    long_description = 'code: https://github.com/aitsc/chatapi-translate'

setup(
    name='chatapi-translate',
    version='0.1',
    description="ChatGPT OpenAI API 流式反向代理，自动翻译中文到英文对话，实现用英文进行高质量的对话",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='aitsc',
    license='MIT',
    url='https://github.com/aitsc/chatapi-translate',
    keywords='tools',
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries',
    ],
    entry_points={
        'console_scripts': [
            'chatapi-translate=chatapi_translate.api:main',
        ],
    },
    install_requires=[
        'fastapi>=0.95.1',
        'uvicorn>=0.22.0',
        'sse-starlette>=1.3.4',
        'requests>=2.29.0',
        'commentjson>=0.9.0',
        'asyncio>=3.4.3',
        'httpx>=0.24.0',
        'aiohttp>=3.8.4',
        'aiolimiter>=1.0.0',
        'watchdog>=3.0.0',
    ],
    python_requires='>=3.7',
)
