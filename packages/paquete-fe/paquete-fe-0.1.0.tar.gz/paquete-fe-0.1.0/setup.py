from setuptools import setup, find_packages

setup(
    name='paquete-fe',
    version='0.1.0',
    description='Descripción corta del paquete',
    author='Tu nombre',
    author_email='tu@email.com',
    url='https://tu-url.com/',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'lxml',
        'SQLAlchemy',
        'pyOpenSSL',
        'zeep',
        'requests',
        'pytz',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)