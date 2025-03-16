# Policy: AWSWAFConsoleReadOnlyAccess

ARN: `arn:aws:iam::aws:policy/AWSWAFConsoleReadOnlyAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| cognito-idp |
| apprunner |
| waf |
| cloudwatch |
| elasticloadbalancing |
| waf-regional |
| wafv2 |
| appsync |
| apigateway |
| cloudfront |
| ec2 |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `apigateway` | [apigateway:GET](../actions.md#apigateway:get) |

| `apprunner` | [apprunner:DescribeWebAclForService](../actions.md#apprunner:describewebaclforservice) |

| `apprunner` | [apprunner:ListAssociatedServicesForWebAcl](../actions.md#apprunner:listassociatedservicesforwebacl) |

| `apprunner` | [apprunner:ListServices](../actions.md#apprunner:listservices) |

| `appsync` | [appsync:ListGraphqlApis](../actions.md#appsync:listgraphqlapis) |

| `cloudfront` | [cloudfront:ListDistributions](../actions.md#cloudfront:listdistributions) |

| `cloudfront` | [cloudfront:ListDistributionsByWebACLId](../actions.md#cloudfront:listdistributionsbywebaclid) |

| `cloudwatch` | [cloudwatch:GetMetricData](../actions.md#cloudwatch:getmetricdata) |

| `cloudwatch` | [cloudwatch:GetMetricStatistics](../actions.md#cloudwatch:getmetricstatistics) |

| `cloudwatch` | [cloudwatch:ListMetrics](../actions.md#cloudwatch:listmetrics) |

| `cognito-idp` | [cognito-idp:GetWebACLForResource](../actions.md#cognito-idp:getwebaclforresource) |

| `cognito-idp` | [cognito-idp:ListResourcesForWebACL](../actions.md#cognito-idp:listresourcesforwebacl) |

| `cognito-idp` | [cognito-idp:ListUserPools](../actions.md#cognito-idp:listuserpools) |

| `ec2` | [ec2:DescribeRegions](../actions.md#ec2:describeregions) |

| `ec2` | [ec2:DescribeVerifiedAccessInstanceWebAclAssociations](../actions.md#ec2:describeverifiedaccessinstancewebaclassociations) |

| `ec2` | [ec2:DescribeVerifiedAccessInstances](../actions.md#ec2:describeverifiedaccessinstances) |

| `ec2` | [ec2:GetVerifiedAccessInstanceWebAcl](../actions.md#ec2:getverifiedaccessinstancewebacl) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeLoadBalancers](../actions.md#elasticloadbalancing:describeloadbalancers) |

| `waf` | [waf:Get*](../actions.md#waf:getall) |

| `waf` | [waf:List*](../actions.md#waf:listall) |

| `waf-regional` | [waf-regional:Get*](../actions.md#waf-regional:getall) |

| `waf-regional` | [waf-regional:List*](../actions.md#waf-regional:listall) |

| `wafv2` | [wafv2:CheckCapacity](../actions.md#wafv2:checkcapacity) |

| `wafv2` | [wafv2:Describe*](../actions.md#wafv2:describeall) |

| `wafv2` | [wafv2:Get*](../actions.md#wafv2:getall) |

| `wafv2` | [wafv2:List*](../actions.md#wafv2:listall) |
