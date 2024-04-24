import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { PythonFunction} from "@aws-cdk/aws-lambda-python-alpha";
import { aws_apigateway } from "aws-cdk-lib";
import { Runtime } from "aws-cdk-lib/aws-lambda";

export class AppStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const fastApiFunction = new PythonFunction(this, 'FastApiFunction', {
      runtime: Runtime.PYTHON_3_11,
      entry: './app',
      index: 'main.py',
      memorySize: 512,
    })

    const api = new aws_apigateway.LambdaRestApi(this, 'FastApi', {
      handler: fastApiFunction,
    });
  }
}
