# Python FastAPI on AWS Lambda with CDK
[![Python Test](https://github.com/yoshitaka-motomura/fastapi-with-aws-lambda-example/actions/workflows/python-ci.yml/badge.svg)](https://github.com/yoshitaka-motomura/fastapi-with-aws-lambda-example/actions/workflows/python-ci.yml)
[![Coverage Status](https://coveralls.io/repos/github/yoshitaka-motomura/fastapi-with-aws-lambda-example/badge.svg?branch=main)](https://coveralls.io/github/yoshitaka-motomura/fastapi-with-aws-lambda-example?branch=main)
## Overview
This project is a demonstration of how to deploy a Python FastAPI application on AWS Lambda using the AWS Cloud Development Kit (CDK).

> [!IMPORTANT]
> AWS Lambda and API Gateway are powerful and widely adopted choices for serverless architectures. These services offer automatic scaling and enhanced security, helping to accelerate development. However, as the number of endpoints increases, the complexity of management also grows, making it crucial to choose the right architecture based on project requirements.
> Especially for small projects or applications dealing with variable traffic, the combination of Lambda and API Gateway is effective. This approach helps reduce the burden of infrastructure management while ensuring high availability and scalability.


## FastAPI
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. It is based on standard Python type hints, which makes it easy to use and understand. FastAPI is a great choice for building APIs with Python.


## Prerequisites
- [Python 3.8+](https://www.python.org/downloads/)
- [Node.js 20.x](https://nodejs.org/en/download/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html)


## Project Structure
```
.
├── README.md
├── app
│   ├── __init__.py
│   ├── __pycache__
│   ├── main.py
│   └── requirements.txt
├── bin
│   └── cdk.ts
├── cdk.json
├── jest.config.js
├── lib
│   └── app-stack.ts
├── package-lock.json
├── package.json
├── requirements.txt
├── test
│   └── cdk.test.ts
└── tsconfig.json
```
| Directory/File | Description |
| --- | --- |
| app | Contains the FastAPI application code |
| app/main.py | FastAPI application code |
| app/requirements.txt | FastAPI application dependencies |
| bin | Contains the CDK application code |
| bin/cdk.ts | CDK application code |
| cdk.json | CDK configuration file |
| lib | Contains the CDK application code |
| lib/app-stack.ts | CDK application code |

---
## References
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [mangum](https://mangum.io/)
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/home.html)
- [AWS CDK Python](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html)
- [AWS CDK Python API Reference](https://docs.aws.amazon.com/cdk/api/latest/python/index.html)
- [Docker](https://docs.docker.com/get-docker/)
- [AWS Account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/)
- [AWS IAM User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)
- [AWS IAM Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html)
- [AWS IAM Policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html)
- [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html)
### Articles
- [Serverless FastAPI with AWS Lambda, API Gateway, and AWS CDK, Author: Thomas Taylor](https://how.wtf/serverless-fastapi-with-aws-lambda-api-gateway-and-aws-cdk.html)

### AWS CDK
This is a blank project for CDK development with TypeScript.
The `cdk.json` file tells the CDK Toolkit how to execute your app.
### Useful commands

* `npm run build`   compile typescript to js
* `npm run watch`   watch for changes and compile
* `npm run test`    perform the jest unit tests
* `npx cdk deploy`  deploy this stack to your default AWS account/region
* `npx cdk diff`    compare deployed stack with current state
* `npx cdk synth`   emits the synthesized CloudFormation template
