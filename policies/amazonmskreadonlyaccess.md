# Policy: AmazonMSKReadOnlyAccess

ARN: `arn:aws:iam::aws:policy/AmazonMSKReadOnlyAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| ec2 |
| kms |
| kafka |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `ec2` | [ec2:DescribeNetworkInterfaces](../actions.md#ec2:describenetworkinterfaces) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `kafka` | [kafka:Describe*](../actions.md#kafka:describeall) |

| `kafka` | [kafka:Get*](../actions.md#kafka:getall) |

| `kafka` | [kafka:List*](../actions.md#kafka:listall) |

| `kms` | [kms:DescribeKey](../actions.md#kms:describekey) |
