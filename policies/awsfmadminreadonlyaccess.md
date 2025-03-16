# Policy: AWSFMAdminReadOnlyAccess

ARN: `arn:aws:iam::aws:policy/AWSFMAdminReadOnlyAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| waf |
| route53resolver |
| firehose |
| organizations |
| waf-regional |
| wafv2 |
| shield |
| fms |
| ec2 |
| s3 |
| network-firewall |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `ec2` | [ec2:DescribeAvailabilityZones](../actions.md#ec2:describeavailabilityzones) |

| `ec2` | [ec2:DescribeRegions](../actions.md#ec2:describeregions) |

| `firehose` | [firehose:ListDeliveryStreams](../actions.md#firehose:listdeliverystreams) |

| `fms` | [fms:Get*](../actions.md#fms:getall) |

| `fms` | [fms:List*](../actions.md#fms:listall) |

| `network-firewall` | [network-firewall:DescribeRuleGroup](../actions.md#network-firewall:describerulegroup) |

| `network-firewall` | [network-firewall:DescribeRuleGroupMetadata](../actions.md#network-firewall:describerulegroupmetadata) |

| `network-firewall` | [network-firewall:ListRuleGroups](../actions.md#network-firewall:listrulegroups) |

| `organizations` | [organizations:DescribeAccount](../actions.md#organizations:describeaccount) |

| `organizations` | [organizations:DescribeOrganization](../actions.md#organizations:describeorganization) |

| `organizations` | [organizations:ListAccounts](../actions.md#organizations:listaccounts) |

| `organizations` | [organizations:ListAccountsForParent](../actions.md#organizations:listaccountsforparent) |

| `organizations` | [organizations:ListChildren](../actions.md#organizations:listchildren) |

| `organizations` | [organizations:ListDelegatedAdministrators](../actions.md#organizations:listdelegatedadministrators) |

| `organizations` | [organizations:ListOrganizationalUnitsForParent](../actions.md#organizations:listorganizationalunitsforparent) |

| `organizations` | [organizations:ListRoots](../actions.md#organizations:listroots) |

| `route53resolver` | [route53resolver:GetFirewallRuleGroup](../actions.md#route53resolver:getfirewallrulegroup) |

| `route53resolver` | [route53resolver:ListFirewallRuleGroups](../actions.md#route53resolver:listfirewallrulegroups) |

| `s3` | [s3:GetBucketPolicy](../actions.md#s3:getbucketpolicy) |

| `shield` | [shield:GetSubscriptionState](../actions.md#shield:getsubscriptionstate) |

| `waf` | [waf:Get*](../actions.md#waf:getall) |

| `waf` | [waf:List*](../actions.md#waf:listall) |

| `waf-regional` | [waf-regional:Get*](../actions.md#waf-regional:getall) |

| `waf-regional` | [waf-regional:List*](../actions.md#waf-regional:listall) |

| `wafv2` | [wafv2:CheckCapacity](../actions.md#wafv2:checkcapacity) |

| `wafv2` | [wafv2:ListAvailableManagedRuleGroupVersions](../actions.md#wafv2:listavailablemanagedrulegroupversions) |

| `wafv2` | [wafv2:ListAvailableManagedRuleGroups](../actions.md#wafv2:listavailablemanagedrulegroups) |

| `wafv2` | [wafv2:ListRuleGroups](../actions.md#wafv2:listrulegroups) |
