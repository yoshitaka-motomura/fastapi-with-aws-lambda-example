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

    /**
     * Create a new API Gateway with a single endpoint that points to the FastAPI Lambda function.
     * The API Gateway will be deployed to a stage called 'v1'.
     * If you don't want to use stage as a route, you should consider HttpAPI
     */
    const api = new aws_apigateway.LambdaRestApi(this, 'FastApi', {
      handler: fastApiFunction,
      deployOptions: {
        stageName: 'v1', // stage to version in prod.
      }
    });
  }
}
