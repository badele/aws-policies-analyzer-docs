# Policy: AWSWAFFullAccess

ARN: `arn:aws:iam::aws:policy/AWSWAFFullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| cognito-idp |
| apprunner |
| waf |
| logs |
| elasticloadbalancing |
| waf-regional |
| wafv2 |
| appsync |
| apigateway |
| ec2 |
| s3 |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `apigateway` | [apigateway:SetWebACL](../actions.md#apigateway:setwebacl) |

| `apprunner` | [apprunner:AssociateWebAcl](../actions.md#apprunner:associatewebacl) |

| `apprunner` | [apprunner:DescribeWebAclForService](../actions.md#apprunner:describewebaclforservice) |

| `apprunner` | [apprunner:DisassociateWebAcl](../actions.md#apprunner:disassociatewebacl) |

| `apprunner` | [apprunner:ListAssociatedServicesForWebAcl](../actions.md#apprunner:listassociatedservicesforwebacl) |

| `apprunner` | [apprunner:ListServices](../actions.md#apprunner:listservices) |

| `appsync` | [appsync:SetWebACL](../actions.md#appsync:setwebacl) |

| `cognito-idp` | [cognito-idp:AssociateWebACL](../actions.md#cognito-idp:associatewebacl) |

| `cognito-idp` | [cognito-idp:DisassociateWebACL](../actions.md#cognito-idp:disassociatewebacl) |

| `cognito-idp` | [cognito-idp:GetWebACLForResource](../actions.md#cognito-idp:getwebaclforresource) |

| `cognito-idp` | [cognito-idp:ListResourcesForWebACL](../actions.md#cognito-idp:listresourcesforwebacl) |

| `ec2` | [ec2:AssociateVerifiedAccessInstanceWebAcl](../actions.md#ec2:associateverifiedaccessinstancewebacl) |

| `ec2` | [ec2:DescribeVerifiedAccessInstanceWebAclAssociations](../actions.md#ec2:describeverifiedaccessinstancewebaclassociations) |

| `ec2` | [ec2:DisassociateVerifiedAccessInstanceWebAcl](../actions.md#ec2:disassociateverifiedaccessinstancewebacl) |

| `ec2` | [ec2:GetVerifiedAccessInstanceWebAcl](../actions.md#ec2:getverifiedaccessinstancewebacl) |

| `elasticloadbalancing` | [elasticloadbalancing:SetWebACL](../actions.md#elasticloadbalancing:setwebacl) |

| `logs` | [logs:CreateLogDelivery](../actions.md#logs:createlogdelivery) |

| `logs` | [logs:DeleteLogDelivery](../actions.md#logs:deletelogdelivery) |

| `logs` | [logs:DescribeLogGroups](../actions.md#logs:describeloggroups) |

| `logs` | [logs:DescribeResourcePolicies](../actions.md#logs:describeresourcepolicies) |

| `logs` | [logs:PutResourcePolicy](../actions.md#logs:putresourcepolicy) |

| `s3` | [s3:GetBucketPolicy](../actions.md#s3:getbucketpolicy) |

| `s3` | [s3:PutBucketPolicy](../actions.md#s3:putbucketpolicy) |

| `waf` | [waf:*](../actions.md#waf:all) |

| `waf-regional` | [waf-regional:*](../actions.md#waf-regional:all) |

| `wafv2` | [wafv2:*](../actions.md#wafv2:all) |
