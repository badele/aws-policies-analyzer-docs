# Policy: Route53RecoveryReadinessServiceRolePolicy

ARN: `arn:aws:iam::aws:policy/aws-service-role/Route53RecoveryReadinessServiceRolePolicy`

## Attached Roles

## Attached Services

| Service |
|---------|
| autoscaling |
| servicequotas |
| route53 |
| lambda |
| sns |
| application-autoscaling |
| cloudwatch |
| elasticloadbalancing |
| iam |
| sqs |
| rds |
| kafka |
| apigateway |
| ec2 |
| dynamodb |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `apigateway` | [apigateway:GET](../actions.md#apigateway:get) |

| `application-autoscaling` | [application-autoscaling:DescribeScalableTargets](../actions.md#application-autoscaling:describescalabletargets) |

| `application-autoscaling` | [application-autoscaling:DescribeScalingPolicies](../actions.md#application-autoscaling:describescalingpolicies) |

| `autoscaling` | [autoscaling:DescribeAccountLimits](../actions.md#autoscaling:describeaccountlimits) |

| `autoscaling` | [autoscaling:DescribeAutoScalingGroups](../actions.md#autoscaling:describeautoscalinggroups) |

| `autoscaling` | [autoscaling:DescribeAutoScalingInstances](../actions.md#autoscaling:describeautoscalinginstances) |

| `autoscaling` | [autoscaling:DescribeLifecycleHooks](../actions.md#autoscaling:describelifecyclehooks) |

| `autoscaling` | [autoscaling:DescribeLoadBalancerTargetGroups](../actions.md#autoscaling:describeloadbalancertargetgroups) |

| `autoscaling` | [autoscaling:DescribeLoadBalancers](../actions.md#autoscaling:describeloadbalancers) |

| `autoscaling` | [autoscaling:DescribeNotificationConfigurations](../actions.md#autoscaling:describenotificationconfigurations) |

| `autoscaling` | [autoscaling:DescribePolicies](../actions.md#autoscaling:describepolicies) |

| `cloudwatch` | [cloudwatch:DescribeAlarms](../actions.md#cloudwatch:describealarms) |

| `cloudwatch` | [cloudwatch:GetMetricData](../actions.md#cloudwatch:getmetricdata) |

| `dynamodb` | [dynamodb:DescribeLimits](../actions.md#dynamodb:describelimits) |

| `dynamodb` | [dynamodb:DescribeReservedCapacity](../actions.md#dynamodb:describereservedcapacity) |

| `dynamodb` | [dynamodb:DescribeReservedCapacityOfferings](../actions.md#dynamodb:describereservedcapacityofferings) |

| `dynamodb` | [dynamodb:DescribeTable](../actions.md#dynamodb:describetable) |

| `dynamodb` | [dynamodb:DescribeTimeToLive](../actions.md#dynamodb:describetimetolive) |

| `dynamodb` | [dynamodb:ListGlobalTables](../actions.md#dynamodb:listglobaltables) |

| `dynamodb` | [dynamodb:ListTables](../actions.md#dynamodb:listtables) |

| `ec2` | [ec2:DescribeAvailabilityZones](../actions.md#ec2:describeavailabilityzones) |

| `ec2` | [ec2:DescribeCustomerGateways](../actions.md#ec2:describecustomergateways) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeVolumes](../actions.md#ec2:describevolumes) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `ec2` | [ec2:DescribeVpnConnections](../actions.md#ec2:describevpnconnections) |

| `ec2` | [ec2:DescribeVpnGateways](../actions.md#ec2:describevpngateways) |

| `ec2` | [ec2:GetEbsDefaultKmsKeyId](../actions.md#ec2:getebsdefaultkmskeyid) |

| `ec2` | [ec2:GetEbsEncryptionByDefault](../actions.md#ec2:getebsencryptionbydefault) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeInstanceHealth](../actions.md#elasticloadbalancing:describeinstancehealth) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeLoadBalancerAttributes](../actions.md#elasticloadbalancing:describeloadbalancerattributes) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeLoadBalancers](../actions.md#elasticloadbalancing:describeloadbalancers) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeTargetGroups](../actions.md#elasticloadbalancing:describetargetgroups) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeTargetHealth](../actions.md#elasticloadbalancing:describetargethealth) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `kafka` | [kafka:DescribeCluster](../actions.md#kafka:describecluster) |

| `kafka` | [kafka:DescribeConfigurationRevision](../actions.md#kafka:describeconfigurationrevision) |

| `lambda` | [lambda:GetFunctionConcurrency](../actions.md#lambda:getfunctionconcurrency) |

| `lambda` | [lambda:GetFunctionConfiguration](../actions.md#lambda:getfunctionconfiguration) |

| `lambda` | [lambda:GetProvisionedConcurrencyConfig](../actions.md#lambda:getprovisionedconcurrencyconfig) |

| `lambda` | [lambda:ListAliases](../actions.md#lambda:listaliases) |

| `lambda` | [lambda:ListEventSourceMappings](../actions.md#lambda:listeventsourcemappings) |

| `lambda` | [lambda:ListFunctions](../actions.md#lambda:listfunctions) |

| `lambda` | [lambda:ListProvisionedConcurrencyConfigs](../actions.md#lambda:listprovisionedconcurrencyconfigs) |

| `lambda` | [lambda:ListVersionsByFunction](../actions.md#lambda:listversionsbyfunction) |

| `rds` | [rds:DescribeAccountAttributes](../actions.md#rds:describeaccountattributes) |

| `rds` | [rds:DescribeDBClusters](../actions.md#rds:describedbclusters) |

| `rds` | [rds:DescribeDBInstances](../actions.md#rds:describedbinstances) |

| `route53` | [route53:GetHealthCheck](../actions.md#route53:gethealthcheck) |

| `route53` | [route53:GetHealthCheckStatus](../actions.md#route53:gethealthcheckstatus) |

| `route53` | [route53:GetHostedZone](../actions.md#route53:gethostedzone) |

| `route53` | [route53:ListResourceRecordSets](../actions.md#route53:listresourcerecordsets) |

| `servicequotas` | [servicequotas:ListAWSDefaultServiceQuotas](../actions.md#servicequotas:listawsdefaultservicequotas) |

| `servicequotas` | [servicequotas:ListRequestedServiceQuotaChangeHistory](../actions.md#servicequotas:listrequestedservicequotachangehistory) |

| `servicequotas` | [servicequotas:ListServiceQuotas](../actions.md#servicequotas:listservicequotas) |

| `servicequotas` | [servicequotas:ListServices](../actions.md#servicequotas:listservices) |

| `servicequotas` | [servicequotas:RequestServiceQuotaIncrease](../actions.md#servicequotas:requestservicequotaincrease) |

| `sns` | [sns:GetEndpointAttributes](../actions.md#sns:getendpointattributes) |

| `sns` | [sns:GetSubscriptionAttributes](../actions.md#sns:getsubscriptionattributes) |

| `sns` | [sns:GetTopicAttributes](../actions.md#sns:gettopicattributes) |

| `sns` | [sns:ListSubscriptionsByTopic](../actions.md#sns:listsubscriptionsbytopic) |

| `sqs` | [sqs:GetQueueAttributes](../actions.md#sqs:getqueueattributes) |

| `sqs` | [sqs:GetQueueUrl](../actions.md#sqs:getqueueurl) |
