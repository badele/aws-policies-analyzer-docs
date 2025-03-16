# Policy: AmazonSSMFullAccess

ARN: `arn:aws:iam::aws:policy/AmazonSSMFullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| ssm |
| cloudwatch |
| logs |
| ssmmessages |
| iam |
| ec2messages |
| ds |
| ec2 |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `cloudwatch` | [cloudwatch:PutMetricData](../actions.md#cloudwatch:putmetricdata) |

| `ds` | [ds:CreateComputer](../actions.md#ds:createcomputer) |

| `ds` | [ds:DescribeDirectories](../actions.md#ds:describedirectories) |

| `ec2` | [ec2:DescribeInstanceStatus](../actions.md#ec2:describeinstancestatus) |

| `ec2messages` | [ec2messages:*](../actions.md#ec2messages:all) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:DeleteServiceLinkedRole](../actions.md#iam:deleteservicelinkedrole) |

| `iam` | [iam:GetServiceLinkedRoleDeletionStatus](../actions.md#iam:getservicelinkedroledeletionstatus) |

| `logs` | [logs:*](../actions.md#logs:all) |

| `ssm` | [ssm:*](../actions.md#ssm:all) |

| `ssmmessages` | [ssmmessages:CreateControlChannel](../actions.md#ssmmessages:createcontrolchannel) |

| `ssmmessages` | [ssmmessages:CreateDataChannel](../actions.md#ssmmessages:createdatachannel) |

| `ssmmessages` | [ssmmessages:OpenControlChannel](../actions.md#ssmmessages:opencontrolchannel) |

| `ssmmessages` | [ssmmessages:OpenDataChannel](../actions.md#ssmmessages:opendatachannel) |
