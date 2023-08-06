import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="for-django-projects",
    version="1.0.1",
    author="Jasmany Sanchez Mendez",
    author_email="jasmanysanchez97@gmail.com",
    description="Package of libraries for Django projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jasmanysanchez/for-django-projects",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'Django>=2.2',
        'django-appconf>=1.0.5',
        'django-select2>=7.7.1',
        'numpy>=1.24.3',
        'pandas>=2.0.1',
        'python-dateutil>=2.8.2',
        'pytz>=2023.3',
        'six>=1.16.0',
        'sqlparse>=0.4.4',
        'tzdata>=2023.3',
        'xlwt>=1.3.0',
    ],
)