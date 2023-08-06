from setuptools import find_packages, setup

setup(
    name='qa-keys-test',
    version='0.0.9',
    description='A repo is for xhis single source',
    include_package_data=True,
    url="https://github.com/OwenLuo123/qa-tag-test.git",
    # packages=['python','automation', 'config'],
    packages=find_packages(),
    package_data={
        'automation_qa_key_helper': ['config/qa_key.json'],
    },
    zip_safe=False
)
