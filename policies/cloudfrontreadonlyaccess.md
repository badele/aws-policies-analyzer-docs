# Policy: CloudFrontReadOnlyAccess

ARN: `arn:aws:iam::aws:policy/CloudFrontReadOnlyAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| waf |
| route53 |
| cloudfront-keyvaluestore |
| acm |
| iam |
| wafv2 |
| cloudfront |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `acm` | [acm:ListCertificates](../actions.md#acm:listcertificates) |

| `cloudfront` | [cloudfront:Describe*](../actions.md#cloudfront:describeall) |

| `cloudfront` | [cloudfront:Get*](../actions.md#cloudfront:getall) |

| `cloudfront` | [cloudfront:List*](../actions.md#cloudfront:listall) |

| `cloudfront-keyvaluestore` | [cloudfront-keyvaluestore:Describe*](../actions.md#cloudfront-keyvaluestore:describeall) |

| `cloudfront-keyvaluestore` | [cloudfront-keyvaluestore:Get*](../actions.md#cloudfront-keyvaluestore:getall) |

| `cloudfront-keyvaluestore` | [cloudfront-keyvaluestore:List*](../actions.md#cloudfront-keyvaluestore:listall) |

| `iam` | [iam:ListServerCertificates](../actions.md#iam:listservercertificates) |

| `route53` | [route53:List*](../actions.md#route53:listall) |

| `waf` | [waf:GetWebACL](../actions.md#waf:getwebacl) |

| `waf` | [waf:ListWebACLs](../actions.md#waf:listwebacls) |

| `wafv2` | [wafv2:GetWebACL](../actions.md#wafv2:getwebacl) |

| `wafv2` | [wafv2:ListWebACLs](../actions.md#wafv2:listwebacls) |
