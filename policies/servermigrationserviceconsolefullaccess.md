# Policy: ServerMigrationServiceConsoleFullAccess

ARN: `arn:aws:iam::aws:policy/ServerMigrationServiceConsoleFullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| cloudformation |
| sms |
| iam |
| ec2 |
| s3 |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `cloudformation` | [cloudformation:DescribeStackResources](../actions.md#cloudformation:describestackresources) |

| `cloudformation` | [cloudformation:DescribeStacks](../actions.md#cloudformation:describestacks) |

| `cloudformation` | [cloudformation:ListStacks](../actions.md#cloudformation:liststacks) |

| `ec2` | [ec2:DescribeKeyPairs](../actions.md#ec2:describekeypairs) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:GetInstanceProfile](../actions.md#iam:getinstanceprofile) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `sms` | [sms:*](../actions.md#sms:all) |
