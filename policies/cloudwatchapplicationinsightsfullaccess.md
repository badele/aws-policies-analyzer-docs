# Policy: CloudWatchApplicationInsightsFullAccess

ARN: `arn:aws:iam::aws:policy/CloudWatchApplicationInsightsFullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| autoscaling |
| lambda |
| sns |
| logs |
| applicationinsights |
| eks |
| elasticloadbalancing |
| sqs |
| states |
| iam |
| rds |
| ecs |
| fsx |
| apigateway |
| ec2 |
| s3 |
| dynamodb |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `apigateway` | [apigateway:GET](../actions.md#apigateway:get) |

| `applicationinsights` | [applicationinsights:*](../actions.md#applicationinsights:all) |

| `autoscaling` | [autoscaling:DescribeAutoScalingGroups](../actions.md#autoscaling:describeautoscalinggroups) |

| `dynamodb` | [dynamodb:ListTables](../actions.md#dynamodb:listtables) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeVolumes](../actions.md#ec2:describevolumes) |

| `ecs` | [ecs:DescribeTaskDefinition](../actions.md#ecs:describetaskdefinition) |

| `ecs` | [ecs:ListClusters](../actions.md#ecs:listclusters) |

| `ecs` | [ecs:ListServices](../actions.md#ecs:listservices) |

| `ecs` | [ecs:ListTasks](../actions.md#ecs:listtasks) |

| `eks` | [eks:ListClusters](../actions.md#eks:listclusters) |

| `eks` | [eks:ListNodegroups](../actions.md#eks:listnodegroups) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeLoadBalancers](../actions.md#elasticloadbalancing:describeloadbalancers) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeTargetGroups](../actions.md#elasticloadbalancing:describetargetgroups) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeTargetHealth](../actions.md#elasticloadbalancing:describetargethealth) |

| `fsx` | [fsx:DescribeFileSystems](../actions.md#fsx:describefilesystems) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `lambda` | [lambda:ListFunctions](../actions.md#lambda:listfunctions) |

| `logs` | [logs:DescribeLogGroups](../actions.md#logs:describeloggroups) |

| `rds` | [rds:DescribeDBClusters](../actions.md#rds:describedbclusters) |

| `rds` | [rds:DescribeDBInstances](../actions.md#rds:describedbinstances) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `sns` | [sns:ListTopics](../actions.md#sns:listtopics) |

| `sqs` | [sqs:ListQueues](../actions.md#sqs:listqueues) |

| `states` | [states:ListStateMachines](../actions.md#states:liststatemachines) |
