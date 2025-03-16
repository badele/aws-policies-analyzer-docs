# Policy: AWSCodeBuildReadOnlyAccess

ARN: `arn:aws:iam::aws:policy/AWSCodeBuildReadOnlyAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| events |
| codestar-notifications |
| codecommit |
| cloudwatch |
| logs |
| codestar-connections |
| codebuild |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `cloudwatch` | [cloudwatch:GetMetricStatistics](../actions.md#cloudwatch:getmetricstatistics) |

| `codebuild` | [codebuild:BatchGet*](../actions.md#codebuild:batchgetall) |

| `codebuild` | [codebuild:DescribeCodeCoverages](../actions.md#codebuild:describecodecoverages) |

| `codebuild` | [codebuild:DescribeTestCases](../actions.md#codebuild:describetestcases) |

| `codebuild` | [codebuild:GetResourcePolicy](../actions.md#codebuild:getresourcepolicy) |

| `codebuild` | [codebuild:List*](../actions.md#codebuild:listall) |

| `codecommit` | [codecommit:GetBranch](../actions.md#codecommit:getbranch) |

| `codecommit` | [codecommit:GetCommit](../actions.md#codecommit:getcommit) |

| `codecommit` | [codecommit:GetRepository](../actions.md#codecommit:getrepository) |

| `codestar-connections` | [codestar-connections:GetConnection](../actions.md#codestar-connections:getconnection) |

| `codestar-connections` | [codestar-connections:ListConnections](../actions.md#codestar-connections:listconnections) |

| `codestar-notifications` | [codestar-notifications:DescribeNotificationRule](../actions.md#codestar-notifications:describenotificationrule) |

| `codestar-notifications` | [codestar-notifications:ListEventTypes](../actions.md#codestar-notifications:listeventtypes) |

| `codestar-notifications` | [codestar-notifications:ListNotificationRules](../actions.md#codestar-notifications:listnotificationrules) |

| `codestar-notifications` | [codestar-notifications:ListTargets](../actions.md#codestar-notifications:listtargets) |

| `events` | [events:DescribeRule](../actions.md#events:describerule) |

| `events` | [events:ListRuleNamesByTarget](../actions.md#events:listrulenamesbytarget) |

| `events` | [events:ListTargetsByRule](../actions.md#events:listtargetsbyrule) |

| `logs` | [logs:GetLogEvents](../actions.md#logs:getlogevents) |
