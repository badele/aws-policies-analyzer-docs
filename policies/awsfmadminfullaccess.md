# Policy: AWSFMAdminFullAccess

ARN: `arn:aws:iam::aws:policy/AWSFMAdminFullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| waf |
| route53resolver |
| firehose |
| elasticloadbalancing |
| waf-regional |
| organizations |
| wafv2 |
| shield |
| iam |
| fms |
| ec2 |
| s3 |
| network-firewall |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `ec2` | [ec2:DescribeAvailabilityZones](../actions.md#ec2:describeavailabilityzones) |

| `ec2` | [ec2:DescribeRegions](../actions.md#ec2:describeregions) |

| `elasticloadbalancing` | [elasticloadbalancing:SetWebACL](../actions.md#elasticloadbalancing:setwebacl) |

| `firehose` | [firehose:ListDeliveryStreams](../actions.md#firehose:listdeliverystreams) |

| `fms` | [fms:*](../actions.md#fms:all) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `network-firewall` | [network-firewall:DescribeRuleGroup](../actions.md#network-firewall:describerulegroup) |

| `network-firewall` | [network-firewall:DescribeRuleGroupMetadata](../actions.md#network-firewall:describerulegroupmetadata) |

| `network-firewall` | [network-firewall:ListRuleGroups](../actions.md#network-firewall:listrulegroups) |

| `organizations` | [organizations:DeregisterDelegatedAdministrator](../actions.md#organizations:deregisterdelegatedadministrator) |

| `organizations` | [organizations:DescribeAccount](../actions.md#organizations:describeaccount) |

| `organizations` | [organizations:DescribeOrganization](../actions.md#organizations:describeorganization) |

| `organizations` | [organizations:EnableAWSServiceAccess](../actions.md#organizations:enableawsserviceaccess) |

| `organizations` | [organizations:ListAccounts](../actions.md#organizations:listaccounts) |

| `organizations` | [organizations:ListAccountsForParent](../actions.md#organizations:listaccountsforparent) |

| `organizations` | [organizations:ListChildren](../actions.md#organizations:listchildren) |

| `organizations` | [organizations:ListDelegatedAdministrators](../actions.md#organizations:listdelegatedadministrators) |

| `organizations` | [organizations:ListOrganizationalUnitsForParent](../actions.md#organizations:listorganizationalunitsforparent) |

| `organizations` | [organizations:ListRoots](../actions.md#organizations:listroots) |

| `organizations` | [organizations:RegisterDelegatedAdministrator](../actions.md#organizations:registerdelegatedadministrator) |

| `route53resolver` | [route53resolver:GetFirewallRuleGroup](../actions.md#route53resolver:getfirewallrulegroup) |

| `route53resolver` | [route53resolver:ListFirewallRuleGroups](../actions.md#route53resolver:listfirewallrulegroups) |

| `s3` | [s3:GetBucketPolicy](../actions.md#s3:getbucketpolicy) |

| `s3` | [s3:PutBucketPolicy](../actions.md#s3:putbucketpolicy) |

| `shield` | [shield:GetSubscriptionState](../actions.md#shield:getsubscriptionstate) |

| `waf` | [waf:*](../actions.md#waf:all) |

| `waf-regional` | [waf-regional:*](../actions.md#waf-regional:all) |

| `wafv2` | [wafv2:CheckCapacity](../actions.md#wafv2:checkcapacity) |

| `wafv2` | [wafv2:ListAvailableManagedRuleGroupVersions](../actions.md#wafv2:listavailablemanagedrulegroupversions) |

| `wafv2` | [wafv2:ListAvailableManagedRuleGroups](../actions.md#wafv2:listavailablemanagedrulegroups) |

| `wafv2` | [wafv2:ListRuleGroups](../actions.md#wafv2:listrulegroups) |

| `wafv2` | [wafv2:PutLoggingConfiguration](../actions.md#wafv2:putloggingconfiguration) |
