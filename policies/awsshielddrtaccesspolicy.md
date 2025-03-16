# Policy: AWSShieldDRTAccessPolicy

ARN: `arn:aws:iam::aws:policy/service-role/AWSShieldDRTAccessPolicy`

## Attached Roles

## Attached Services

| Service |
|---------|
| globalaccelerator |
| waf |
| route53 |
| cloudwatch |
| elasticloadbalancing |
| waf-regional |
| wafv2 |
| shield |
| apigateway |
| cloudfront |
| ec2 |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `apigateway` | [apigateway:SetWebACL](../actions.md#apigateway:setwebacl) |

| `cloudfront` | [cloudfront:GetDistribution*](../actions.md#cloudfront:getdistributionall) |

| `cloudfront` | [cloudfront:List*](../actions.md#cloudfront:listall) |

| `cloudfront` | [cloudfront:UpdateDistribution](../actions.md#cloudfront:updatedistribution) |

| `cloudwatch` | [cloudwatch:Describe*](../actions.md#cloudwatch:describeall) |

| `cloudwatch` | [cloudwatch:Get*](../actions.md#cloudwatch:getall) |

| `cloudwatch` | [cloudwatch:List*](../actions.md#cloudwatch:listall) |

| `ec2` | [ec2:DescribeAddresses](../actions.md#ec2:describeaddresses) |

| `ec2` | [ec2:DescribeRegions](../actions.md#ec2:describeregions) |

| `elasticloadbalancing` | [elasticloadbalancing:Describe*](../actions.md#elasticloadbalancing:describeall) |

| `elasticloadbalancing` | [elasticloadbalancing:SetWebACL](../actions.md#elasticloadbalancing:setwebacl) |

| `globalaccelerator` | [globalaccelerator:DescribeAccelerator](../actions.md#globalaccelerator:describeaccelerator) |

| `globalaccelerator` | [globalaccelerator:ListAccelerators](../actions.md#globalaccelerator:listaccelerators) |

| `route53` | [route53:List*](../actions.md#route53:listall) |

| `shield` | [shield:*](../actions.md#shield:all) |

| `waf` | [waf:*](../actions.md#waf:all) |

| `waf-regional` | [waf-regional:*](../actions.md#waf-regional:all) |

| `wafv2` | [wafv2:*](../actions.md#wafv2:all) |
