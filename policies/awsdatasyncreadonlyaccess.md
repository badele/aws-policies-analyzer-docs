# Policy: AWSDataSyncReadOnlyAccess

ARN: `arn:aws:iam::aws:policy/AWSDataSyncReadOnlyAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| datasync |
| logs |
| iam |
| s3 |
| fsx |
| ec2 |
| elasticfilesystem |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `datasync` | [datasync:Describe*](../actions.md#datasync:describeall) |

| `datasync` | [datasync:List*](../actions.md#datasync:listall) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `elasticfilesystem` | [elasticfilesystem:DescribeFileSystems](../actions.md#elasticfilesystem:describefilesystems) |

| `elasticfilesystem` | [elasticfilesystem:DescribeMountTargets](../actions.md#elasticfilesystem:describemounttargets) |

| `fsx` | [fsx:DescribeFileSystems](../actions.md#fsx:describefilesystems) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `logs` | [logs:DescribeLogGroups](../actions.md#logs:describeloggroups) |

| `logs` | [logs:DescribeResourcePolicies](../actions.md#logs:describeresourcepolicies) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |
