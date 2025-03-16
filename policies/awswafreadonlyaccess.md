# Policy: AWSWAFReadOnlyAccess

ARN: `arn:aws:iam::aws:policy/AWSWAFReadOnlyAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| cognito-idp |
| apprunner |
| waf |
| waf-regional |
| wafv2 |
| ec2 |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `apprunner` | [apprunner:DescribeWebAclForService](../actions.md#apprunner:describewebaclforservice) |

| `apprunner` | [apprunner:ListAssociatedServicesForWebAcl](../actions.md#apprunner:listassociatedservicesforwebacl) |

| `apprunner` | [apprunner:ListServices](../actions.md#apprunner:listservices) |

| `cognito-idp` | [cognito-idp:GetWebACLForResource](../actions.md#cognito-idp:getwebaclforresource) |

| `cognito-idp` | [cognito-idp:ListResourcesForWebACL](../actions.md#cognito-idp:listresourcesforwebacl) |

| `ec2` | [ec2:DescribeVerifiedAccessInstanceWebAclAssociations](../actions.md#ec2:describeverifiedaccessinstancewebaclassociations) |

| `ec2` | [ec2:GetVerifiedAccessInstanceWebAcl](../actions.md#ec2:getverifiedaccessinstancewebacl) |

| `waf` | [waf:Get*](../actions.md#waf:getall) |

| `waf` | [waf:List*](../actions.md#waf:listall) |

| `waf-regional` | [waf-regional:Get*](../actions.md#waf-regional:getall) |

| `waf-regional` | [waf-regional:List*](../actions.md#waf-regional:listall) |

| `wafv2` | [wafv2:CheckCapacity](../actions.md#wafv2:checkcapacity) |

| `wafv2` | [wafv2:Describe*](../actions.md#wafv2:describeall) |

| `wafv2` | [wafv2:Get*](../actions.md#wafv2:getall) |

| `wafv2` | [wafv2:List*](../actions.md#wafv2:listall) |
