from setuptools import setup


setup(
    name="password_service",
    version='0.0.1',
    description='Generate and share passwords for a small team',
    author="Albert O'Connor <info@albertoconnor.ca>",
    author_email="info@albertoconnor.ca",
    url="https://github.com/AvocadoCoop/password-service",
    license="BSD License",
    packages=["password_service"],
    zip_safe=False,
    install_requires=["django>=1.7"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
)
