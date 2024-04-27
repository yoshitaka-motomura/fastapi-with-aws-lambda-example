import {App} from 'aws-cdk-lib';
import {Template} from 'aws-cdk-lib/assertions';
import {AppStack} from '../lib/app-stack'

describe('AppStack', () => {
    const app = new App();
    const stack = new AppStack(app, 'MyTestStack');
    const template = Template.fromStack(stack);
    it('should lambda functions count is one', () => {
        template.resourceCountIs('AWS::Lambda::Function', 1);
    })
    it('should api gateway count is one', () => {
        template.resourceCountIs('AWS::ApiGateway::RestApi', 1);
    })
})