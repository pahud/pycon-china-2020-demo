# vscode
VSCode template for CDK development workspace

# AWS SSO for AWS CDK

Configure your `default` AWS_PROFILE with AWS SSO
```sh
aws configure sso --profile default 
```

Configure `credential_process` for the `default` profile

```sh
aws configure set credential_process ${PWD}/.devcontainer/bin/aws-sso-credential-process
```

export `AWS_SHARED_CREDENTIALS_FILE` 

```sh
export AWS_SHARED_CREDENTIALS_FILE=~/.aws/config
```
# pycon-china-2020-demo
