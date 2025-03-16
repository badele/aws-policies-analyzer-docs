# Policy: AmazonEKSLoadBalancingPolicy

ARN: `arn:aws:iam::aws:policy/AmazonEKSLoadBalancingPolicy`

## Attached Roles

## Attached Services

| Service |
|---------|
| cognito-idp |
| acm |
| elasticloadbalancing |
| iam |
| wafv2 |
| shield |
| ec2 |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `acm` | [acm:DescribeCertificate](../actions.md#acm:describecertificate) |

| `acm` | [acm:ListCertificates](../actions.md#acm:listcertificates) |

| `cognito-idp` | [cognito-idp:DescribeUserPoolClient](../actions.md#cognito-idp:describeuserpoolclient) |

| `ec2` | [ec2:AuthorizeSecurityGroupIngress](../actions.md#ec2:authorizesecuritygroupingress) |

| `ec2` | [ec2:AuthorizeSecurityGroupIngress](../actions.md#ec2:authorizesecuritygroupingress) |

| `ec2` | [ec2:AuthorizeSecurityGroupIngress](../actions.md#ec2:authorizesecuritygroupingress) |

| `ec2` | [ec2:CreateSecurityGroup](../actions.md#ec2:createsecuritygroup) |

| `ec2` | [ec2:CreateSecurityGroup](../actions.md#ec2:createsecuritygroup) |

| `ec2` | [ec2:CreateTags](../actions.md#ec2:createtags) |

| `ec2` | [ec2:DescribeAccountAttributes](../actions.md#ec2:describeaccountattributes) |

| `ec2` | [ec2:DescribeAddresses](../actions.md#ec2:describeaddresses) |

| `ec2` | [ec2:DescribeClassicLinkInstances](../actions.md#ec2:describeclassiclinkinstances) |

| `ec2` | [ec2:DescribeCoipPools](../actions.md#ec2:describecoippools) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeInternetGateways](../actions.md#ec2:describeinternetgateways) |

| `ec2` | [ec2:DescribeNetworkInterfaces](../actions.md#ec2:describenetworkinterfaces) |

| `ec2` | [ec2:DescribeRouteTables](../actions.md#ec2:describeroutetables) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeVpcClassicLink](../actions.md#ec2:describevpcclassiclink) |

| `ec2` | [ec2:DescribeVpcPeeringConnections](../actions.md#ec2:describevpcpeeringconnections) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `ec2` | [ec2:GetCoipPoolUsage](../actions.md#ec2:getcoippoolusage) |

| `ec2` | [ec2:GetSecurityGroupsForVpc](../actions.md#ec2:getsecuritygroupsforvpc) |

| `ec2` | [ec2:RevokeSecurityGroupIngress](../actions.md#ec2:revokesecuritygroupingress) |

| `ec2` | [ec2:RevokeSecurityGroupIngress](../actions.md#ec2:revokesecuritygroupingress) |

| `elasticloadbalancing` | [elasticloadbalancing:AddListenerCertificates](../actions.md#elasticloadbalancing:addlistenercertificates) |

| `elasticloadbalancing` | [elasticloadbalancing:AddTags](../actions.md#elasticloadbalancing:addtags) |

| `elasticloadbalancing` | [elasticloadbalancing:CreateListener](../actions.md#elasticloadbalancing:createlistener) |

| `elasticloadbalancing` | [elasticloadbalancing:CreateLoadBalancer](../actions.md#elasticloadbalancing:createloadbalancer) |

| `elasticloadbalancing` | [elasticloadbalancing:CreateRule](../actions.md#elasticloadbalancing:createrule) |

| `elasticloadbalancing` | [elasticloadbalancing:CreateTargetGroup](../actions.md#elasticloadbalancing:createtargetgroup) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeTargetGroups](../actions.md#elasticloadbalancing:describetargetgroups) |

| `elasticloadbalancing` | [elasticloadbalancing:ModifyListener](../actions.md#elasticloadbalancing:modifylistener) |

| `elasticloadbalancing` | [elasticloadbalancing:ModifyListenerAttributes](../actions.md#elasticloadbalancing:modifylistenerattributes) |

| `elasticloadbalancing` | [elasticloadbalancing:ModifyLoadBalancerAttributes](../actions.md#elasticloadbalancing:modifyloadbalancerattributes) |

| `elasticloadbalancing` | [elasticloadbalancing:ModifyRule](../actions.md#elasticloadbalancing:modifyrule) |

| `elasticloadbalancing` | [elasticloadbalancing:ModifyTargetGroup](../actions.md#elasticloadbalancing:modifytargetgroup) |

| `elasticloadbalancing` | [elasticloadbalancing:ModifyTargetGroupAttributes](../actions.md#elasticloadbalancing:modifytargetgroupattributes) |

| `elasticloadbalancing` | [elasticloadbalancing:RegisterTargets](../actions.md#elasticloadbalancing:registertargets) |

| `elasticloadbalancing` | [elasticloadbalancing:RemoveListenerCertificates](../actions.md#elasticloadbalancing:removelistenercertificates) |

| `elasticloadbalancing` | [elasticloadbalancing:SetIpAddressType](../actions.md#elasticloadbalancing:setipaddresstype) |

| `elasticloadbalancing` | [elasticloadbalancing:SetSecurityGroups](../actions.md#elasticloadbalancing:setsecuritygroups) |

| `elasticloadbalancing` | [elasticloadbalancing:SetSubnets](../actions.md#elasticloadbalancing:setsubnets) |

| `elasticloadbalancing` | [elasticloadbalancing:SetWebAcl](../actions.md#elasticloadbalancing:setwebacl) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `shield` | [shield:CreateProtection](../actions.md#shield:createprotection) |

| `shield` | [shield:DeleteProtection](../actions.md#shield:deleteprotection) |

| `shield` | [shield:TagResource](../actions.md#shield:tagresource) |

| `wafv2` | [wafv2:AssociateWebACL](../actions.md#wafv2:associatewebacl) |

| `wafv2` | [wafv2:DisassociateWebACL](../actions.md#wafv2:disassociatewebacl) |

| `wafv2` | [wafv2:GetWebACL](../actions.md#wafv2:getwebacl) |

| `wafv2` | [wafv2:GetWebACLForResource](../actions.md#wafv2:getwebaclforresource) |
