# Landing Zone Organization

## Initial steps

Install and run the tests:

```shell
make install
make test
```

Check code complexity:

```shell
make complexity
```

Validate typing and formatting:

```shell
make lint
```

## Configuration

By default, this package does an assumption about your naming schema. It expects you use the following format:
`<PREFIX>-<WORKLOAD NAME>-<ENVIRONMENT>`. When you deviate from this schema you potentially need to provide 2 configuration
options. You can do this via 2 environment variable:

| **Name**                 | **Default Value** | **Description**                                                                                               |
|--------------------------|-------------------|---------------------------------------------------------------------------------------------------------------|
| PATTERN_WORKLOAD_NAME    | `.*?-(.*)-.*`     | The first match is used as the workload name.                                                                 |
| PATTERN_ENVIRONMENT_NAME | `.*-.*-(.*)`      | The first match is used as the environment name. For example: development, testing, acceptance or production. | 

### AWS Policies

In order to query the AWS Organizations, you either need to assume a role in the master payer account. Or you need to
delegate administration to another account. For more information read the [Delegated administrator for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_delegate_policies.html) page.

Here you see the least privileged delegated administrator policy that you can use:  

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ListRoot",
      "Effect": "Allow",
      "Principal": { "AWS": "<Delegated Account>" },
      "Action": [ "organizations:ListRoots" ],
      "Resource": [ "*" ]
    },
    {
      "Sid": "ListContent",
      "Effect": "Allow",
      "Principal": { "AWS": "Delegated Account" },
      "Action": [
        "organizations:DescribeOrganizationalUnit",
        "organizations:DescribeAccount",
        "organizations:ListChildren"
      ],
      "Resource": [
        "arn:aws:organizations::<Master Payer Account>:account/*",
        "arn:aws:organizations::<Master Payer Account>:ou/*",
        "arn:aws:organizations::<Master Payer Account>:root/*"
      ]
    }
  ]
}
```

## Using the CLI

Before you can execute any command you need to select the correct profile:

```shell
export CUSTOMER=<prefix used in your profiles>
export AWS_PROFILE=${CUSTOMER}-audit
```

### Download the organization structure

Before you can use the CLI commands you need to execute the following command:

```shell
landingzone-organization organization download
```

This command will query the AWS Organization API and store the aggregated data to a file in the current working directory.
This file will be reused for every other command.

### List all workloads

To get an overview of all the workloads within your organization you can execute the following command:

```shell
landingzone-organization workload list [--location "<OU NAME>"]
```

When you want to list a nested OU you can use comma separation: 

```shell
landingzone-organization workload list [--location "<OU NAME>,<OU NAME>"]
```

### View account by ID

Sometimes you have an Account ID and you need to know what account it is. To get more information about the given
Account ID you can execute the following command:  

```shell
landingzone-organization account view <ACCOUNT_ID>
```

## Using AWS Lambda

You can also use this module within an AWS Lambda function. AWS recommends to not use the master payer account for
anything other than providing AWS Organizations and billing. But in order to query the AWS Organization we need a role
in the master payer account that we can assume. In [`cloudformation/prerequisites.yaml`](./cloudformation/prerequisites.yaml)
you can see how you can create a role that can be assumed from another account.

You can than assume that role from any other account and initialize the module with accurate organization information.

See: [`cloudformation/read_organization/index.py`](./cloudformation/read_organization/index.py)
