# Policy: CloudWatchFullAccessV2

ARN: `arn:aws:iam::aws:policy/CloudWatchFullAccessV2`

## Attached Roles

## Attached Services

| Service |
|---------|
| autoscaling |
| cloudwatch |
| application-autoscaling |
| logs |
| application-signals |
| iam |
| oam |
| rum |
| xray |
| synthetics |
| sns |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `application-autoscaling` | [application-autoscaling:DescribeScalingPolicies](../actions.md#application-autoscaling:describescalingpolicies) |

| `application-signals` | [application-signals:*](../actions.md#application-signals:all) |

| `autoscaling` | [autoscaling:DescribeAutoScalingGroups](../actions.md#autoscaling:describeautoscalinggroups) |

| `autoscaling` | [autoscaling:DescribePolicies](../actions.md#autoscaling:describepolicies) |

| `cloudwatch` | [cloudwatch:*](../actions.md#cloudwatch:all) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:GetPolicy](../actions.md#iam:getpolicy) |

| `iam` | [iam:GetPolicyVersion](../actions.md#iam:getpolicyversion) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `logs` | [logs:*](../actions.md#logs:all) |

| `oam` | [oam:ListAttachedLinks](../actions.md#oam:listattachedlinks) |

| `oam` | [oam:ListSinks](../actions.md#oam:listsinks) |

| `rum` | [rum:*](../actions.md#rum:all) |

| `sns` | [sns:CreateTopic](../actions.md#sns:createtopic) |

| `sns` | [sns:ListSubscriptions](../actions.md#sns:listsubscriptions) |

| `sns` | [sns:ListSubscriptionsByTopic](../actions.md#sns:listsubscriptionsbytopic) |

| `sns` | [sns:ListTopics](../actions.md#sns:listtopics) |

| `sns` | [sns:Subscribe](../actions.md#sns:subscribe) |

| `synthetics` | [synthetics:*](../actions.md#synthetics:all) |

| `xray` | [xray:*](../actions.md#xray:all) |
