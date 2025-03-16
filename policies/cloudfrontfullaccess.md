# Policy: CloudFrontFullAccess

ARN: `arn:aws:iam::aws:policy/CloudFrontFullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| waf |
| cloudfront-keyvaluestore |
| acm |
| kinesis |
| elasticloadbalancing |
| iam |
| wafv2 |
| cloudfront |
| s3 |
| ec2 |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `acm` | [acm:ListCertificates](../actions.md#acm:listcertificates) |

| `cloudfront` | [cloudfront:*](../actions.md#cloudfront:all) |

| `cloudfront-keyvaluestore` | [cloudfront-keyvaluestore:*](../actions.md#cloudfront-keyvaluestore:all) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeInternetGateways](../actions.md#ec2:describeinternetgateways) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeLoadBalancers](../actions.md#elasticloadbalancing:describeloadbalancers) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `iam` | [iam:ListServerCertificates](../actions.md#iam:listservercertificates) |

| `kinesis` | [kinesis:DescribeStream](../actions.md#kinesis:describestream) |

| `kinesis` | [kinesis:ListStreams](../actions.md#kinesis:liststreams) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `waf` | [waf:GetWebACL](../actions.md#waf:getwebacl) |

| `waf` | [waf:ListWebACLs](../actions.md#waf:listwebacls) |

| `wafv2` | [wafv2:GetWebACL](../actions.md#wafv2:getwebacl) |

| `wafv2` | [wafv2:ListWebACLs](../actions.md#wafv2:listwebacls) |
