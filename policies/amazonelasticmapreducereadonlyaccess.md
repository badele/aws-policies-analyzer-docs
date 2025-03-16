# Policy: AmazonElasticMapReduceReadOnlyAccess

ARN: `arn:aws:iam::aws:policy/AmazonElasticMapReduceReadOnlyAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| cloudwatch |
| sdb |
| s3 |
| elasticmapreduce |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `cloudwatch` | [cloudwatch:GetMetricStatistics](../actions.md#cloudwatch:getmetricstatistics) |

| `elasticmapreduce` | [elasticmapreduce:Describe*](../actions.md#elasticmapreduce:describeall) |

| `elasticmapreduce` | [elasticmapreduce:GetBlockPublicAccessConfiguration](../actions.md#elasticmapreduce:getblockpublicaccessconfiguration) |

| `elasticmapreduce` | [elasticmapreduce:List*](../actions.md#elasticmapreduce:listall) |

| `elasticmapreduce` | [elasticmapreduce:ViewEventsFromAllClustersInConsole](../actions.md#elasticmapreduce:vieweventsfromallclustersinconsole) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `sdb` | [sdb:Select](../actions.md#sdb:select) |
