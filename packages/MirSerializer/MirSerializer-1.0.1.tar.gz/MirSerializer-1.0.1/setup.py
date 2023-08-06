from setuptools import setup, find_packages


setup(
    name="MirSerializer",
    version="1.0.1",
    description="Library for serialization JSON, XML",
    author="Mirolyubov Ilya",
    author_email="ilyamir1@mail.ru",
    packages=find_packages(),
    py_modules=['json_serializer', 'xml_serializer'],
    include_package_data=True,
)
