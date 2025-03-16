# Policy: AWSLambda_ReadOnlyAccess

ARN: `arn:aws:iam::aws:policy/AWSLambda_ReadOnlyAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| cloudformation |
| lambda |
| cloudwatch |
| logs |
| iam |
| states |
| xray |
| ec2 |
| tag |
| kms |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `cloudformation` | [cloudformation:DescribeStacks](../actions.md#cloudformation:describestacks) |

| `cloudformation` | [cloudformation:ListStackResources](../actions.md#cloudformation:liststackresources) |

| `cloudformation` | [cloudformation:ListStacks](../actions.md#cloudformation:liststacks) |

| `cloudwatch` | [cloudwatch:GetMetricData](../actions.md#cloudwatch:getmetricdata) |

| `cloudwatch` | [cloudwatch:ListMetrics](../actions.md#cloudwatch:listmetrics) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `iam` | [iam:GetPolicy](../actions.md#iam:getpolicy) |

| `iam` | [iam:GetPolicyVersion](../actions.md#iam:getpolicyversion) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `iam` | [iam:GetRolePolicy](../actions.md#iam:getrolepolicy) |

| `iam` | [iam:ListAttachedRolePolicies](../actions.md#iam:listattachedrolepolicies) |

| `iam` | [iam:ListRolePolicies](../actions.md#iam:listrolepolicies) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `kms` | [kms:ListAliases](../actions.md#kms:listaliases) |

| `lambda` | [lambda:Get*](../actions.md#lambda:getall) |

| `lambda` | [lambda:List*](../actions.md#lambda:listall) |

| `logs` | [logs:DescribeLogGroups](../actions.md#logs:describeloggroups) |

| `logs` | [logs:DescribeLogStreams](../actions.md#logs:describelogstreams) |

| `logs` | [logs:DescribeQueries](../actions.md#logs:describequeries) |

| `logs` | [logs:FilterLogEvents](../actions.md#logs:filterlogevents) |

| `logs` | [logs:GetLogEvents](../actions.md#logs:getlogevents) |

| `logs` | [logs:GetLogGroupFields](../actions.md#logs:getloggroupfields) |

| `logs` | [logs:GetLogRecord](../actions.md#logs:getlogrecord) |

| `logs` | [logs:GetQueryResults](../actions.md#logs:getqueryresults) |

| `logs` | [logs:StartQuery](../actions.md#logs:startquery) |

| `logs` | [logs:StopQuery](../actions.md#logs:stopquery) |

| `states` | [states:DescribeStateMachine](../actions.md#states:describestatemachine) |

| `states` | [states:ListStateMachines](../actions.md#states:liststatemachines) |

| `tag` | [tag:GetResources](../actions.md#tag:getresources) |

| `xray` | [xray:BatchGetTraces](../actions.md#xray:batchgettraces) |

| `xray` | [xray:GetTraceSummaries](../actions.md#xray:gettracesummaries) |
