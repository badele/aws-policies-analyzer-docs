# Policy: AWSStorageGatewayReadOnlyAccess

ARN: `arn:aws:iam::aws:policy/AWSStorageGatewayReadOnlyAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| ssm |
| ec2 |
| storagegateway |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `ec2` | [ec2:DescribeSnapshots](../actions.md#ec2:describesnapshots) |

| `ssm` | [ssm:GetParameters](../actions.md#ssm:getparameters) |

| `storagegateway` | [storagegateway:Describe*](../actions.md#storagegateway:describeall) |

| `storagegateway` | [storagegateway:List*](../actions.md#storagegateway:listall) |
