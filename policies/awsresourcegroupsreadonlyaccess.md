# Policy: AWSResourceGroupsReadOnlyAccess

ARN: `arn:aws:iam::aws:policy/AWSResourceGroupsReadOnlyAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| elasticbeanstalk |
| ssm |
| cloudformation |
| route53 |
| storagegateway |
| resource-groups |
| route53domains |
| kinesis |
| elasticache |
| elasticloadbalancing |
| s3 |
| rds |
| glacier |
| elasticmapreduce |
| redshift |
| ec2 |
| tag |
| opsworks |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `cloudformation` | [cloudformation:DescribeStacks](../actions.md#cloudformation:describestacks) |

| `cloudformation` | [cloudformation:ListStackResources](../actions.md#cloudformation:liststackresources) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSnapshots](../actions.md#ec2:describesnapshots) |

| `ec2` | [ec2:DescribeVolumes](../actions.md#ec2:describevolumes) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `elasticache` | [elasticache:DescribeCacheClusters](../actions.md#elasticache:describecacheclusters) |

| `elasticache` | [elasticache:DescribeSnapshots](../actions.md#elasticache:describesnapshots) |

| `elasticache` | [elasticache:ListTagsForResource](../actions.md#elasticache:listtagsforresource) |

| `elasticbeanstalk` | [elasticbeanstalk:DescribeEnvironments](../actions.md#elasticbeanstalk:describeenvironments) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeLoadBalancers](../actions.md#elasticloadbalancing:describeloadbalancers) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeTags](../actions.md#elasticloadbalancing:describetags) |

| `elasticmapreduce` | [elasticmapreduce:DescribeCluster](../actions.md#elasticmapreduce:describecluster) |

| `elasticmapreduce` | [elasticmapreduce:ListClusters](../actions.md#elasticmapreduce:listclusters) |

| `glacier` | [glacier:DescribeVault](../actions.md#glacier:describevault) |

| `glacier` | [glacier:ListTagsForVault](../actions.md#glacier:listtagsforvault) |

| `glacier` | [glacier:ListVaults](../actions.md#glacier:listvaults) |

| `kinesis` | [kinesis:DescribeStream](../actions.md#kinesis:describestream) |

| `kinesis` | [kinesis:ListStreams](../actions.md#kinesis:liststreams) |

| `kinesis` | [kinesis:ListTagsForStream](../actions.md#kinesis:listtagsforstream) |

| `opsworks` | [opsworks:DescribeStacks](../actions.md#opsworks:describestacks) |

| `opsworks` | [opsworks:ListTags](../actions.md#opsworks:listtags) |

| `rds` | [rds:DescribeDBInstances](../actions.md#rds:describedbinstances) |

| `rds` | [rds:DescribeDBSnapshots](../actions.md#rds:describedbsnapshots) |

| `rds` | [rds:ListTagsForResource](../actions.md#rds:listtagsforresource) |

| `redshift` | [redshift:DescribeClusters](../actions.md#redshift:describeclusters) |

| `redshift` | [redshift:DescribeTags](../actions.md#redshift:describetags) |

| `resource-groups` | [resource-groups:Get*](../actions.md#resource-groups:getall) |

| `resource-groups` | [resource-groups:List*](../actions.md#resource-groups:listall) |

| `resource-groups` | [resource-groups:Search*](../actions.md#resource-groups:searchall) |

| `route53` | [route53:GetHealthCheck](../actions.md#route53:gethealthcheck) |

| `route53` | [route53:GetHostedZone](../actions.md#route53:gethostedzone) |

| `route53` | [route53:ListHealthChecks](../actions.md#route53:listhealthchecks) |

| `route53` | [route53:ListHostedZones](../actions.md#route53:listhostedzones) |

| `route53` | [route53:ListTagsForResource](../actions.md#route53:listtagsforresource) |

| `route53domains` | [route53domains:ListDomains](../actions.md#route53domains:listdomains) |

| `s3` | [s3:GetBucketTagging](../actions.md#s3:getbuckettagging) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `ssm` | [ssm:ListDocuments](../actions.md#ssm:listdocuments) |

| `storagegateway` | [storagegateway:DescribeGatewayInformation](../actions.md#storagegateway:describegatewayinformation) |

| `storagegateway` | [storagegateway:ListGateways](../actions.md#storagegateway:listgateways) |

| `storagegateway` | [storagegateway:ListTagsForResource](../actions.md#storagegateway:listtagsforresource) |

| `tag` | [tag:Get*](../actions.md#tag:getall) |
