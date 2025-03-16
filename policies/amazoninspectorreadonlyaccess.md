# Policy: AmazonInspectorReadOnlyAccess

ARN: `arn:aws:iam::aws:policy/AmazonInspectorReadOnlyAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| inspector |
| events |
| ec2 |
| sns |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeTags](../actions.md#ec2:describetags) |

| `events` | [events:DescribeRule](../actions.md#events:describerule) |

| `events` | [events:ListRuleNamesByTarget](../actions.md#events:listrulenamesbytarget) |

| `inspector` | [inspector:Describe*](../actions.md#inspector:describeall) |

| `inspector` | [inspector:Get*](../actions.md#inspector:getall) |

| `inspector` | [inspector:List*](../actions.md#inspector:listall) |

| `inspector` | [inspector:Preview*](../actions.md#inspector:previewall) |

| `sns` | [sns:ListTopics](../actions.md#sns:listtopics) |
