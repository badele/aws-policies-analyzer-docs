# Policy: AWSCodeDeployRoleForECS

ARN: `arn:aws:iam::aws:policy/AWSCodeDeployRoleForECS`

## Attached Roles

## Attached Services

| Service |
|---------|
| lambda |
| cloudwatch |
| elasticloadbalancing |
| iam |
| ecs |
| s3 |
| sns |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `cloudwatch` | [cloudwatch:DescribeAlarms](../actions.md#cloudwatch:describealarms) |

| `ecs` | [ecs:CreateTaskSet](../actions.md#ecs:createtaskset) |

| `ecs` | [ecs:DeleteTaskSet](../actions.md#ecs:deletetaskset) |

| `ecs` | [ecs:DescribeServices](../actions.md#ecs:describeservices) |

| `ecs` | [ecs:UpdateServicePrimaryTaskSet](../actions.md#ecs:updateserviceprimarytaskset) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeListeners](../actions.md#elasticloadbalancing:describelisteners) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeRules](../actions.md#elasticloadbalancing:describerules) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeTargetGroups](../actions.md#elasticloadbalancing:describetargetgroups) |

| `elasticloadbalancing` | [elasticloadbalancing:ModifyListener](../actions.md#elasticloadbalancing:modifylistener) |

| `elasticloadbalancing` | [elasticloadbalancing:ModifyRule](../actions.md#elasticloadbalancing:modifyrule) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `lambda` | [lambda:InvokeFunction](../actions.md#lambda:invokefunction) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:GetObjectVersion](../actions.md#s3:getobjectversion) |

| `sns` | [sns:Publish](../actions.md#sns:publish) |
