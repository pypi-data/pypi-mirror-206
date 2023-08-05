import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-recaptcha-authorizer",
    "version": "2.2.2",
    "description": "An AWS CDK construct library that provides a reCaptcha Authorizer for API Gateway REST APIs",
    "license": "Apache-2.0",
    "url": "https://constructs.dev/packages/cdk-recaptcha-authorizer",
    "long_description_content_type": "text/markdown",
    "author": "Aaron Lucia",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/engineal/cdk-recaptcha-authorizer.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_recaptcha_authorizer",
        "cdk_recaptcha_authorizer._jsii"
    ],
    "package_data": {
        "cdk_recaptcha_authorizer._jsii": [
            "cdk-recaptcha-authorizer@2.2.2.jsii.tgz"
        ],
        "cdk_recaptcha_authorizer": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib==2.77.0",
        "constructs>=10.0.0, <11.0.0",
        "jsii>=1.80.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
