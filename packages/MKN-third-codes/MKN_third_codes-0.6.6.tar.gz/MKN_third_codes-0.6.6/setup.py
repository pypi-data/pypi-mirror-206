from setuptools import setup

setup(
    name='MKN_third_codes',
    version='0.6.6',
    description='Python library with standart solutions for probability tasks',
    author='Dolgun Ivan',
    author_email='vanadolgun@gmail.com',
    packages=['mfcn'],
    license='MIT',
    long_description= open('./README.md', 'r', encoding="utf-8").read() + '\n#\n' + open('./CHANGELOG.md', 'r', encoding="utf-8").read(),
    long_description_content_type='text/markdown'
)