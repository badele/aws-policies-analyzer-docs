# Policy: AmazonInspectorFullAccess

ARN: `arn:aws:iam::aws:policy/AmazonInspectorFullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| inspector |
| events |
| iam |
| ec2 |
| sns |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeTags](../actions.md#ec2:describetags) |

| `events` | [events:DescribeRule](../actions.md#events:describerule) |

| `events` | [events:ListRuleNamesByTarget](../actions.md#events:listrulenamesbytarget) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `inspector` | [inspector:*](../actions.md#inspector:all) |

| `sns` | [sns:ListTopics](../actions.md#sns:listtopics) |
