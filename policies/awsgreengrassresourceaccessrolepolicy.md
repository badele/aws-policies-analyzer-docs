# Policy: AWSGreengrassResourceAccessRolePolicy

ARN: `arn:aws:iam::aws:policy/service-role/AWSGreengrassResourceAccessRolePolicy`

## Attached Roles

## Attached Services

| Service |
|---------|
| iot |
| greengrass |
| lambda |
| secretsmanager |
| sagemaker |
| s3 |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `greengrass` | [greengrass:*](../actions.md#greengrass:all) |

| `iot` | [iot:DeleteThingShadow](../actions.md#iot:deletethingshadow) |

| `iot` | [iot:DescribeCertificate](../actions.md#iot:describecertificate) |

| `iot` | [iot:DescribeThing](../actions.md#iot:describething) |

| `iot` | [iot:GetThingShadow](../actions.md#iot:getthingshadow) |

| `iot` | [iot:UpdateThingShadow](../actions.md#iot:updatethingshadow) |

| `lambda` | [lambda:GetFunction](../actions.md#lambda:getfunction) |

| `lambda` | [lambda:GetFunctionConfiguration](../actions.md#lambda:getfunctionconfiguration) |

| `s3` | [s3:GetBucketLocation](../actions.md#s3:getbucketlocation) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `sagemaker` | [sagemaker:DescribeTrainingJob](../actions.md#sagemaker:describetrainingjob) |

| `secretsmanager` | [secretsmanager:GetSecretValue](../actions.md#secretsmanager:getsecretvalue) |
