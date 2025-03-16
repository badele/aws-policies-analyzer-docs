# Policy: CloudWatchAutomaticDashboardsAccess

ARN: `arn:aws:iam::aws:policy/CloudWatchAutomaticDashboardsAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| elasticloadbalancing |
| ecs |
| rds |
| synthetics |
| cloudfront |
| lambda |
| sqs |
| ec2 |
| tag |
| s3 |
| autoscaling |
| elasticbeanstalk |
| route53 |
| apigateway |
| elasticfilesystem |
| sns |
| resource-groups |
| kinesis |
| elasticache |
| dynamodb |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `apigateway` | [apigateway:GET](../actions.md#apigateway:get) |

| `autoscaling` | [autoscaling:DescribeAutoScalingGroups](../actions.md#autoscaling:describeautoscalinggroups) |

| `cloudfront` | [cloudfront:GetDistribution](../actions.md#cloudfront:getdistribution) |

| `cloudfront` | [cloudfront:ListDistributions](../actions.md#cloudfront:listdistributions) |

| `dynamodb` | [dynamodb:DescribeTable](../actions.md#dynamodb:describetable) |

| `dynamodb` | [dynamodb:ListTables](../actions.md#dynamodb:listtables) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeVolumes](../actions.md#ec2:describevolumes) |

| `ecs` | [ecs:DescribeClusters](../actions.md#ecs:describeclusters) |

| `ecs` | [ecs:DescribeContainerInstances](../actions.md#ecs:describecontainerinstances) |

| `ecs` | [ecs:ListClusters](../actions.md#ecs:listclusters) |

| `ecs` | [ecs:ListContainerInstances](../actions.md#ecs:listcontainerinstances) |

| `ecs` | [ecs:ListServices](../actions.md#ecs:listservices) |

| `elasticache` | [elasticache:DescribeCacheClusters](../actions.md#elasticache:describecacheclusters) |

| `elasticbeanstalk` | [elasticbeanstalk:DescribeEnvironments](../actions.md#elasticbeanstalk:describeenvironments) |

| `elasticfilesystem` | [elasticfilesystem:DescribeFileSystems](../actions.md#elasticfilesystem:describefilesystems) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeLoadBalancers](../actions.md#elasticloadbalancing:describeloadbalancers) |

| `kinesis` | [kinesis:DescribeStream](../actions.md#kinesis:describestream) |

| `kinesis` | [kinesis:ListStreams](../actions.md#kinesis:liststreams) |

| `lambda` | [lambda:GetFunction](../actions.md#lambda:getfunction) |

| `lambda` | [lambda:ListFunctions](../actions.md#lambda:listfunctions) |

| `rds` | [rds:DescribeDBClusters](../actions.md#rds:describedbclusters) |

| `rds` | [rds:DescribeDBInstances](../actions.md#rds:describedbinstances) |

| `resource-groups` | [resource-groups:ListGroupResources](../actions.md#resource-groups:listgroupresources) |

| `resource-groups` | [resource-groups:ListGroups](../actions.md#resource-groups:listgroups) |

| `route53` | [route53:GetHealthCheck](../actions.md#route53:gethealthcheck) |

| `route53` | [route53:ListHealthChecks](../actions.md#route53:listhealthchecks) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `sns` | [sns:ListTopics](../actions.md#sns:listtopics) |

| `sqs` | [sqs:GetQueueAttributes](../actions.md#sqs:getqueueattributes) |

| `sqs` | [sqs:GetQueueUrl](../actions.md#sqs:getqueueurl) |

| `sqs` | [sqs:ListQueues](../actions.md#sqs:listqueues) |

| `synthetics` | [synthetics:DescribeCanariesLastRun](../actions.md#synthetics:describecanarieslastrun) |

| `tag` | [tag:GetResources](../actions.md#tag:getresources) |
