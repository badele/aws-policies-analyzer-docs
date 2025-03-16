# Policy: AmazonSSMMaintenanceWindowRole

ARN: `arn:aws:iam::aws:policy/service-role/AmazonSSMMaintenanceWindowRole`

## Attached Roles

## Attached Services

| Service |
|---------|
| ssm |
| lambda |
| resource-groups |
| states |
| tag |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `lambda` | [lambda:InvokeFunction](../actions.md#lambda:invokefunction) |

| `resource-groups` | [resource-groups:ListGroupResources](../actions.md#resource-groups:listgroupresources) |

| `resource-groups` | [resource-groups:ListGroups](../actions.md#resource-groups:listgroups) |

| `ssm` | [ssm:GetAutomationExecution](../actions.md#ssm:getautomationexecution) |

| `ssm` | [ssm:GetParameters](../actions.md#ssm:getparameters) |

| `ssm` | [ssm:ListCommands](../actions.md#ssm:listcommands) |

| `ssm` | [ssm:SendCommand](../actions.md#ssm:sendcommand) |

| `ssm` | [ssm:StartAutomationExecution](../actions.md#ssm:startautomationexecution) |

| `states` | [states:DescribeExecution](../actions.md#states:describeexecution) |

| `states` | [states:StartExecution](../actions.md#states:startexecution) |

| `tag` | [tag:GetResources](../actions.md#tag:getresources) |
