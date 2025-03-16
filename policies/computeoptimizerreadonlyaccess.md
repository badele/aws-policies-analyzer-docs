# Policy: ComputeOptimizerReadOnlyAccess

ARN: `arn:aws:iam::aws:policy/ComputeOptimizerReadOnlyAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| autoscaling |
| lambda |
| cloudwatch |
| compute-optimizer |
| organizations |
| ecs |
| rds |
| ec2 |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `autoscaling` | [autoscaling:DescribeAutoScalingGroups](../actions.md#autoscaling:describeautoscalinggroups) |

| `autoscaling` | [autoscaling:DescribeAutoScalingInstances](../actions.md#autoscaling:describeautoscalinginstances) |

| `cloudwatch` | [cloudwatch:GetMetricData](../actions.md#cloudwatch:getmetricdata) |

| `compute-optimizer` | [compute-optimizer:DescribeRecommendationExportJobs](../actions.md#compute-optimizer:describerecommendationexportjobs) |

| `compute-optimizer` | [compute-optimizer:GetAutoScalingGroupRecommendations](../actions.md#compute-optimizer:getautoscalinggrouprecommendations) |

| `compute-optimizer` | [compute-optimizer:GetEBSVolumeRecommendations](../actions.md#compute-optimizer:getebsvolumerecommendations) |

| `compute-optimizer` | [compute-optimizer:GetEC2InstanceRecommendations](../actions.md#compute-optimizer:getec2instancerecommendations) |

| `compute-optimizer` | [compute-optimizer:GetEC2RecommendationProjectedMetrics](../actions.md#compute-optimizer:getec2recommendationprojectedmetrics) |

| `compute-optimizer` | [compute-optimizer:GetECSServiceRecommendationProjectedMetrics](../actions.md#compute-optimizer:getecsservicerecommendationprojectedmetrics) |

| `compute-optimizer` | [compute-optimizer:GetECSServiceRecommendations](../actions.md#compute-optimizer:getecsservicerecommendations) |

| `compute-optimizer` | [compute-optimizer:GetEffectiveRecommendationPreferences](../actions.md#compute-optimizer:geteffectiverecommendationpreferences) |

| `compute-optimizer` | [compute-optimizer:GetEnrollmentStatus](../actions.md#compute-optimizer:getenrollmentstatus) |

| `compute-optimizer` | [compute-optimizer:GetEnrollmentStatusesForOrganization](../actions.md#compute-optimizer:getenrollmentstatusesfororganization) |

| `compute-optimizer` | [compute-optimizer:GetIdleRecommendations](../actions.md#compute-optimizer:getidlerecommendations) |

| `compute-optimizer` | [compute-optimizer:GetLambdaFunctionRecommendations](../actions.md#compute-optimizer:getlambdafunctionrecommendations) |

| `compute-optimizer` | [compute-optimizer:GetLicenseRecommendations](../actions.md#compute-optimizer:getlicenserecommendations) |

| `compute-optimizer` | [compute-optimizer:GetRDSDatabaseRecommendationProjectedMetrics](../actions.md#compute-optimizer:getrdsdatabaserecommendationprojectedmetrics) |

| `compute-optimizer` | [compute-optimizer:GetRDSDatabaseRecommendations](../actions.md#compute-optimizer:getrdsdatabaserecommendations) |

| `compute-optimizer` | [compute-optimizer:GetRecommendationPreferences](../actions.md#compute-optimizer:getrecommendationpreferences) |

| `compute-optimizer` | [compute-optimizer:GetRecommendationSummaries](../actions.md#compute-optimizer:getrecommendationsummaries) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeVolumes](../actions.md#ec2:describevolumes) |

| `ecs` | [ecs:ListClusters](../actions.md#ecs:listclusters) |

| `ecs` | [ecs:ListServices](../actions.md#ecs:listservices) |

| `lambda` | [lambda:ListFunctions](../actions.md#lambda:listfunctions) |

| `lambda` | [lambda:ListProvisionedConcurrencyConfigs](../actions.md#lambda:listprovisionedconcurrencyconfigs) |

| `organizations` | [organizations:DescribeAccount](../actions.md#organizations:describeaccount) |

| `organizations` | [organizations:DescribeOrganization](../actions.md#organizations:describeorganization) |

| `organizations` | [organizations:ListAccounts](../actions.md#organizations:listaccounts) |

| `rds` | [rds:DescribeDBClusters](../actions.md#rds:describedbclusters) |

| `rds` | [rds:DescribeDBInstances](../actions.md#rds:describedbinstances) |
