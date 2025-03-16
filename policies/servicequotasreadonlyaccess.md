# Policy: ServiceQuotasReadOnlyAccess

ARN: `arn:aws:iam::aws:policy/ServiceQuotasReadOnlyAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| autoscaling |
| servicequotas |
| cloudformation |
| route53 |
| cloudwatch |
| kinesis |
| elasticloadbalancing |
| iam |
| organizations |
| rds |
| tag |
| dynamodb |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `autoscaling` | [autoscaling:DescribeAccountLimits](../actions.md#autoscaling:describeaccountlimits) |

| `cloudformation` | [cloudformation:DescribeAccountLimits](../actions.md#cloudformation:describeaccountlimits) |

| `cloudwatch` | [cloudwatch:DescribeAlarms](../actions.md#cloudwatch:describealarms) |

| `cloudwatch` | [cloudwatch:DescribeAlarmsForMetric](../actions.md#cloudwatch:describealarmsformetric) |

| `cloudwatch` | [cloudwatch:GetMetricData](../actions.md#cloudwatch:getmetricdata) |

| `cloudwatch` | [cloudwatch:GetMetricStatistics](../actions.md#cloudwatch:getmetricstatistics) |

| `dynamodb` | [dynamodb:DescribeLimits](../actions.md#dynamodb:describelimits) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeAccountLimits](../actions.md#elasticloadbalancing:describeaccountlimits) |

| `iam` | [iam:GetAccountSummary](../actions.md#iam:getaccountsummary) |

| `kinesis` | [kinesis:DescribeLimits](../actions.md#kinesis:describelimits) |

| `organizations` | [organizations:DescribeAccount](../actions.md#organizations:describeaccount) |

| `organizations` | [organizations:DescribeOrganization](../actions.md#organizations:describeorganization) |

| `organizations` | [organizations:ListAWSServiceAccessForOrganization](../actions.md#organizations:listawsserviceaccessfororganization) |

| `rds` | [rds:DescribeAccountAttributes](../actions.md#rds:describeaccountattributes) |

| `route53` | [route53:GetAccountLimit](../actions.md#route53:getaccountlimit) |

| `servicequotas` | [servicequotas:GetAWSDefaultServiceQuota](../actions.md#servicequotas:getawsdefaultservicequota) |

| `servicequotas` | [servicequotas:GetAssociationForServiceQuotaTemplate](../actions.md#servicequotas:getassociationforservicequotatemplate) |

| `servicequotas` | [servicequotas:GetRequestedServiceQuotaChange](../actions.md#servicequotas:getrequestedservicequotachange) |

| `servicequotas` | [servicequotas:GetServiceQuota](../actions.md#servicequotas:getservicequota) |

| `servicequotas` | [servicequotas:GetServiceQuotaIncreaseRequestFromTemplate](../actions.md#servicequotas:getservicequotaincreaserequestfromtemplate) |

| `servicequotas` | [servicequotas:ListAWSDefaultServiceQuotas](../actions.md#servicequotas:listawsdefaultservicequotas) |

| `servicequotas` | [servicequotas:ListRequestedServiceQuotaChangeHistory](../actions.md#servicequotas:listrequestedservicequotachangehistory) |

| `servicequotas` | [servicequotas:ListRequestedServiceQuotaChangeHistoryByQuota](../actions.md#servicequotas:listrequestedservicequotachangehistorybyquota) |

| `servicequotas` | [servicequotas:ListServiceQuotaIncreaseRequestsInTemplate](../actions.md#servicequotas:listservicequotaincreaserequestsintemplate) |

| `servicequotas` | [servicequotas:ListServiceQuotas](../actions.md#servicequotas:listservicequotas) |

| `servicequotas` | [servicequotas:ListServices](../actions.md#servicequotas:listservices) |

| `servicequotas` | [servicequotas:ListTagsForResource](../actions.md#servicequotas:listtagsforresource) |

| `tag` | [tag:GetTagKeys](../actions.md#tag:gettagkeys) |

| `tag` | [tag:GetTagValues](../actions.md#tag:gettagvalues) |
