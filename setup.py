#!/usr/bin/env python3
"""
English Learning Shooter Game Setup Script
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "An innovative educational game that makes learning English fun and engaging through action-packed gameplay!"

# Read requirements
def read_requirements():
    req_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    try:
        with open(req_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        return ['pygame>=2.0.0']

setup(
    name="english-learning-shooter",
    version="1.1.0",
    author="English Learning Shooter Team",
    author_email="developer@englishlearningshooter.com",
    description="An innovative educational game that makes learning English fun through action-packed gameplay",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/english-learning-shooter",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/english-learning-shooter/issues",
        "Documentation": "https://github.com/yourusername/english-learning-shooter/wiki",
        "Source Code": "https://github.com/yourusername/english-learning-shooter",
    },
    packages=find_packages(),
    py_modules=["english_learning_shooter"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Education",
        "Topic :: Games/Entertainment",
        "Topic :: Games/Entertainment :: Arcade",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=0.5",
        ],
    },
    entry_points={
        "console_scripts": [
            "english-learning-shooter=english_learning_shooter:main",
        ],
    },
    keywords=[
        "education", "english", "learning", "game", "pygame", "vocabulary", 
        "grammar", "spelling", "esl", "language", "interactive", "educational"
    ],
    include_package_data=True,
    zip_safe=False,
)