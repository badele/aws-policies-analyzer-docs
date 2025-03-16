# Policy: CloudWatchReadOnlyAccess

ARN: `arn:aws:iam::aws:policy/CloudWatchReadOnlyAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| autoscaling |
| cloudwatch |
| application-autoscaling |
| logs |
| application-signals |
| rum |
| oam |
| iam |
| xray |
| synthetics |
| sns |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `application-autoscaling` | [application-autoscaling:DescribeScalingPolicies](../actions.md#application-autoscaling:describescalingpolicies) |

| `application-signals` | [application-signals:BatchGet*](../actions.md#application-signals:batchgetall) |

| `application-signals` | [application-signals:Get*](../actions.md#application-signals:getall) |

| `application-signals` | [application-signals:List*](../actions.md#application-signals:listall) |

| `autoscaling` | [autoscaling:Describe*](../actions.md#autoscaling:describeall) |

| `cloudwatch` | [cloudwatch:BatchGet*](../actions.md#cloudwatch:batchgetall) |

| `cloudwatch` | [cloudwatch:Describe*](../actions.md#cloudwatch:describeall) |

| `cloudwatch` | [cloudwatch:GenerateQuery](../actions.md#cloudwatch:generatequery) |

| `cloudwatch` | [cloudwatch:Get*](../actions.md#cloudwatch:getall) |

| `cloudwatch` | [cloudwatch:List*](../actions.md#cloudwatch:listall) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `logs` | [logs:Describe*](../actions.md#logs:describeall) |

| `logs` | [logs:FilterLogEvents](../actions.md#logs:filterlogevents) |

| `logs` | [logs:Get*](../actions.md#logs:getall) |

| `logs` | [logs:List*](../actions.md#logs:listall) |

| `logs` | [logs:StartLiveTail](../actions.md#logs:startlivetail) |

| `logs` | [logs:StartQuery](../actions.md#logs:startquery) |

| `logs` | [logs:StopLiveTail](../actions.md#logs:stoplivetail) |

| `logs` | [logs:StopQuery](../actions.md#logs:stopquery) |

| `logs` | [logs:TestMetricFilter](../actions.md#logs:testmetricfilter) |

| `oam` | [oam:ListAttachedLinks](../actions.md#oam:listattachedlinks) |

| `oam` | [oam:ListSinks](../actions.md#oam:listsinks) |

| `rum` | [rum:BatchGet*](../actions.md#rum:batchgetall) |

| `rum` | [rum:Get*](../actions.md#rum:getall) |

| `rum` | [rum:List*](../actions.md#rum:listall) |

| `sns` | [sns:Get*](../actions.md#sns:getall) |

| `sns` | [sns:List*](../actions.md#sns:listall) |

| `synthetics` | [synthetics:Describe*](../actions.md#synthetics:describeall) |

| `synthetics` | [synthetics:Get*](../actions.md#synthetics:getall) |

| `synthetics` | [synthetics:List*](../actions.md#synthetics:listall) |

| `xray` | [xray:BatchGet*](../actions.md#xray:batchgetall) |

| `xray` | [xray:CancelTraceRetrieval](../actions.md#xray:canceltraceretrieval) |

| `xray` | [xray:Get*](../actions.md#xray:getall) |

| `xray` | [xray:List*](../actions.md#xray:listall) |

| `xray` | [xray:StartTraceRetrieval](../actions.md#xray:starttraceretrieval) |
