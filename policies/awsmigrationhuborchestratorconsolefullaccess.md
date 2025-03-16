# Policy: AWSMigrationHubOrchestratorConsoleFullAccess

ARN: `arn:aws:iam::aws:policy/AWSMigrationHubOrchestratorConsoleFullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| discovery |
| secretsmanager |
| iam |
| mgh |
| ecs |
| account |
| migrationhub-orchestrator |
| ec2 |
| s3 |
| kms |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `account` | [account:ListRegions](../actions.md#account:listregions) |

| `discovery` | [discovery:DescribeConfigurations](../actions.md#discovery:describeconfigurations) |

| `discovery` | [discovery:GetDiscoverySummary](../actions.md#discovery:getdiscoverysummary) |

| `discovery` | [discovery:ListConfigurations](../actions.md#discovery:listconfigurations) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `ecs` | [ecs:ListClusters](../actions.md#ecs:listclusters) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `iam` | [iam:ListInstanceProfiles](../actions.md#iam:listinstanceprofiles) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `kms` | [kms:ListAliases](../actions.md#kms:listaliases) |

| `kms` | [kms:ListKeys](../actions.md#kms:listkeys) |

| `mgh` | [mgh:GetHomeRegion](../actions.md#mgh:gethomeregion) |

| `migrationhub-orchestrator` | [migrationhub-orchestrator:*](../actions.md#migrationhub-orchestrator:all) |

| `s3` | [s3:GetBucketAcl](../actions.md#s3:getbucketacl) |

| `s3` | [s3:GetBucketLocation](../actions.md#s3:getbucketlocation) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:ListBucketVersions](../actions.md#s3:listbucketversions) |

| `s3` | [s3:PutObject](../actions.md#s3:putobject) |

| `secretsmanager` | [secretsmanager:ListSecrets](../actions.md#secretsmanager:listsecrets) |
