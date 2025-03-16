# Policy: AWSFaultInjectionSimulatorEC2Access

ARN: `arn:aws:iam::aws:policy/service-role/AWSFaultInjectionSimulatorEC2Access`

## Attached Roles

## Attached Services

| Service |
|---------|
| ssm |
| ec2 |
| kms |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:RebootInstances](../actions.md#ec2:rebootinstances) |

| `ec2` | [ec2:SendSpotInstanceInterruptions](../actions.md#ec2:sendspotinstanceinterruptions) |

| `ec2` | [ec2:StartInstances](../actions.md#ec2:startinstances) |

| `ec2` | [ec2:StopInstances](../actions.md#ec2:stopinstances) |

| `ec2` | [ec2:TerminateInstances](../actions.md#ec2:terminateinstances) |

| `kms` | [kms:CreateGrant](../actions.md#kms:creategrant) |

| `ssm` | [ssm:CancelCommand](../actions.md#ssm:cancelcommand) |

| `ssm` | [ssm:ListCommands](../actions.md#ssm:listcommands) |

| `ssm` | [ssm:SendCommand](../actions.md#ssm:sendcommand) |
