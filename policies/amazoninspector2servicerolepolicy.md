# Policy: AmazonInspector2ServiceRolePolicy

ARN: `arn:aws:iam::aws:policy/aws-service-role/AmazonInspector2ServiceRolePolicy`

## Attached Roles

## Attached Services

| Service |
|---------|
| events |
| codeguru-security |
| ssm |
| cloudtrail |
| lambda |
| cloudwatch |
| elasticloadbalancing |
| organizations |
| iam |
| directconnect |
| ecr |
| ec2 |
| tiros |
| network-firewall |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `cloudtrail` | [cloudtrail:CreateServiceLinkedChannel](../actions.md#cloudtrail:createservicelinkedchannel) |

| `cloudtrail` | [cloudtrail:DeleteServiceLinkedChannel](../actions.md#cloudtrail:deleteservicelinkedchannel) |

| `cloudtrail` | [cloudtrail:ListServiceLinkedChannels](../actions.md#cloudtrail:listservicelinkedchannels) |

| `cloudwatch` | [cloudwatch:GetMetricData](../actions.md#cloudwatch:getmetricdata) |

| `cloudwatch` | [cloudwatch:PutMetricData](../actions.md#cloudwatch:putmetricdata) |

| `codeguru-security` | [codeguru-security:BatchGetFindings](../actions.md#codeguru-security:batchgetfindings) |

| `codeguru-security` | [codeguru-security:CreateScan](../actions.md#codeguru-security:createscan) |

| `codeguru-security` | [codeguru-security:DeleteScansByCategory](../actions.md#codeguru-security:deletescansbycategory) |

| `codeguru-security` | [codeguru-security:GetAccountConfiguration](../actions.md#codeguru-security:getaccountconfiguration) |

| `codeguru-security` | [codeguru-security:GetFindings](../actions.md#codeguru-security:getfindings) |

| `codeguru-security` | [codeguru-security:GetScan](../actions.md#codeguru-security:getscan) |

| `codeguru-security` | [codeguru-security:ListFindings](../actions.md#codeguru-security:listfindings) |

| `directconnect` | [directconnect:DescribeConnections](../actions.md#directconnect:describeconnections) |

| `directconnect` | [directconnect:DescribeDirectConnectGatewayAssociations](../actions.md#directconnect:describedirectconnectgatewayassociations) |

| `directconnect` | [directconnect:DescribeDirectConnectGatewayAttachments](../actions.md#directconnect:describedirectconnectgatewayattachments) |

| `directconnect` | [directconnect:DescribeDirectConnectGateways](../actions.md#directconnect:describedirectconnectgateways) |

| `directconnect` | [directconnect:DescribeVirtualGateways](../actions.md#directconnect:describevirtualgateways) |

| `directconnect` | [directconnect:DescribeVirtualInterfaces](../actions.md#directconnect:describevirtualinterfaces) |

| `ec2` | [ec2:DescribeAvailabilityZones](../actions.md#ec2:describeavailabilityzones) |

| `ec2` | [ec2:DescribeCustomerGateways](../actions.md#ec2:describecustomergateways) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeInternetGateways](../actions.md#ec2:describeinternetgateways) |

| `ec2` | [ec2:DescribeManagedPrefixLists](../actions.md#ec2:describemanagedprefixlists) |

| `ec2` | [ec2:DescribeNatGateways](../actions.md#ec2:describenatgateways) |

| `ec2` | [ec2:DescribeNetworkAcls](../actions.md#ec2:describenetworkacls) |

| `ec2` | [ec2:DescribeNetworkInterfaces](../actions.md#ec2:describenetworkinterfaces) |

| `ec2` | [ec2:DescribePrefixLists](../actions.md#ec2:describeprefixlists) |

| `ec2` | [ec2:DescribeRegions](../actions.md#ec2:describeregions) |

| `ec2` | [ec2:DescribeRouteTables](../actions.md#ec2:describeroutetables) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeTransitGatewayAttachments](../actions.md#ec2:describetransitgatewayattachments) |

| `ec2` | [ec2:DescribeTransitGatewayConnects](../actions.md#ec2:describetransitgatewayconnects) |

| `ec2` | [ec2:DescribeTransitGatewayPeeringAttachments](../actions.md#ec2:describetransitgatewaypeeringattachments) |

| `ec2` | [ec2:DescribeTransitGatewayRouteTables](../actions.md#ec2:describetransitgatewayroutetables) |

| `ec2` | [ec2:DescribeTransitGatewayVpcAttachments](../actions.md#ec2:describetransitgatewayvpcattachments) |

| `ec2` | [ec2:DescribeTransitGateways](../actions.md#ec2:describetransitgateways) |

| `ec2` | [ec2:DescribeVpcEndpointServiceConfigurations](../actions.md#ec2:describevpcendpointserviceconfigurations) |

| `ec2` | [ec2:DescribeVpcEndpoints](../actions.md#ec2:describevpcendpoints) |

| `ec2` | [ec2:DescribeVpcPeeringConnections](../actions.md#ec2:describevpcpeeringconnections) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `ec2` | [ec2:DescribeVpnConnections](../actions.md#ec2:describevpnconnections) |

| `ec2` | [ec2:DescribeVpnGateways](../actions.md#ec2:describevpngateways) |

| `ec2` | [ec2:GetManagedPrefixListEntries](../actions.md#ec2:getmanagedprefixlistentries) |

| `ec2` | [ec2:GetTransitGatewayRouteTablePropagations](../actions.md#ec2:gettransitgatewayroutetablepropagations) |

| `ec2` | [ec2:SearchTransitGatewayRoutes](../actions.md#ec2:searchtransitgatewayroutes) |

| `ecr` | [ecr:BatchGetImage](../actions.md#ecr:batchgetimage) |

| `ecr` | [ecr:BatchGetRepositoryScanningConfiguration](../actions.md#ecr:batchgetrepositoryscanningconfiguration) |

| `ecr` | [ecr:DescribeImages](../actions.md#ecr:describeimages) |

| `ecr` | [ecr:DescribeRegistry](../actions.md#ecr:describeregistry) |

| `ecr` | [ecr:DescribeRepositories](../actions.md#ecr:describerepositories) |

| `ecr` | [ecr:GetAuthorizationToken](../actions.md#ecr:getauthorizationtoken) |

| `ecr` | [ecr:GetDownloadUrlForLayer](../actions.md#ecr:getdownloadurlforlayer) |

| `ecr` | [ecr:GetRegistryScanningConfiguration](../actions.md#ecr:getregistryscanningconfiguration) |

| `ecr` | [ecr:ListImages](../actions.md#ecr:listimages) |

| `ecr` | [ecr:PutRegistryScanningConfiguration](../actions.md#ecr:putregistryscanningconfiguration) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeListeners](../actions.md#elasticloadbalancing:describelisteners) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeLoadBalancerAttributes](../actions.md#elasticloadbalancing:describeloadbalancerattributes) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeLoadBalancers](../actions.md#elasticloadbalancing:describeloadbalancers) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeRules](../actions.md#elasticloadbalancing:describerules) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeTags](../actions.md#elasticloadbalancing:describetags) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeTargetGroupAttributes](../actions.md#elasticloadbalancing:describetargetgroupattributes) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeTargetGroups](../actions.md#elasticloadbalancing:describetargetgroups) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeTargetHealth](../actions.md#elasticloadbalancing:describetargethealth) |

| `events` | [events:DeleteRule](../actions.md#events:deleterule) |

| `events` | [events:DescribeRule](../actions.md#events:describerule) |

| `events` | [events:ListTargetsByRule](../actions.md#events:listtargetsbyrule) |

| `events` | [events:PutRule](../actions.md#events:putrule) |

| `events` | [events:PutTargets](../actions.md#events:puttargets) |

| `events` | [events:RemoveTargets](../actions.md#events:removetargets) |

| `iam` | [iam:GetPolicy](../actions.md#iam:getpolicy) |

| `iam` | [iam:GetPolicyVersion](../actions.md#iam:getpolicyversion) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `iam` | [iam:GetRolePolicy](../actions.md#iam:getrolepolicy) |

| `iam` | [iam:ListAttachedRolePolicies](../actions.md#iam:listattachedrolepolicies) |

| `iam` | [iam:ListPolicies](../actions.md#iam:listpolicies) |

| `iam` | [iam:ListPolicyVersions](../actions.md#iam:listpolicyversions) |

| `iam` | [iam:ListRolePolicies](../actions.md#iam:listrolepolicies) |

| `lambda` | [lambda:GetFunction](../actions.md#lambda:getfunction) |

| `lambda` | [lambda:GetLayerVersion](../actions.md#lambda:getlayerversion) |

| `lambda` | [lambda:ListFunctions](../actions.md#lambda:listfunctions) |

| `lambda` | [lambda:ListTags](../actions.md#lambda:listtags) |

| `lambda` | [lambda:ListVersionsByFunction](../actions.md#lambda:listversionsbyfunction) |

| `network-firewall` | [network-firewall:DescribeFirewall](../actions.md#network-firewall:describefirewall) |

| `network-firewall` | [network-firewall:DescribeFirewallPolicy](../actions.md#network-firewall:describefirewallpolicy) |

| `network-firewall` | [network-firewall:DescribeResourcePolicy](../actions.md#network-firewall:describeresourcepolicy) |

| `network-firewall` | [network-firewall:DescribeRuleGroup](../actions.md#network-firewall:describerulegroup) |

| `network-firewall` | [network-firewall:ListFirewallPolicies](../actions.md#network-firewall:listfirewallpolicies) |

| `network-firewall` | [network-firewall:ListFirewalls](../actions.md#network-firewall:listfirewalls) |

| `network-firewall` | [network-firewall:ListRuleGroups](../actions.md#network-firewall:listrulegroups) |

| `organizations` | [organizations:DescribeAccount](../actions.md#organizations:describeaccount) |

| `organizations` | [organizations:DescribeOrganization](../actions.md#organizations:describeorganization) |

| `organizations` | [organizations:ListAccounts](../actions.md#organizations:listaccounts) |

| `ssm` | [ssm:CreateAssociation](../actions.md#ssm:createassociation) |

| `ssm` | [ssm:CreateResourceDataSync](../actions.md#ssm:createresourcedatasync) |

| `ssm` | [ssm:DeleteAssociation](../actions.md#ssm:deleteassociation) |

| `ssm` | [ssm:DeleteParameter](../actions.md#ssm:deleteparameter) |

| `ssm` | [ssm:DeleteResourceDataSync](../actions.md#ssm:deleteresourcedatasync) |

| `ssm` | [ssm:DescribeAssociation](../actions.md#ssm:describeassociation) |

| `ssm` | [ssm:DescribeAssociationExecutions](../actions.md#ssm:describeassociationexecutions) |

| `ssm` | [ssm:DescribeInstanceInformation](../actions.md#ssm:describeinstanceinformation) |

| `ssm` | [ssm:GetCommandInvocation](../actions.md#ssm:getcommandinvocation) |

| `ssm` | [ssm:GetParameters](../actions.md#ssm:getparameters) |

| `ssm` | [ssm:ListAssociations](../actions.md#ssm:listassociations) |

| `ssm` | [ssm:ListResourceDataSync](../actions.md#ssm:listresourcedatasync) |

| `ssm` | [ssm:PutParameter](../actions.md#ssm:putparameter) |

| `ssm` | [ssm:SendCommand](../actions.md#ssm:sendcommand) |

| `ssm` | [ssm:SendCommand](../actions.md#ssm:sendcommand) |

| `ssm` | [ssm:StartAssociationsOnce](../actions.md#ssm:startassociationsonce) |

| `ssm` | [ssm:UpdateAssociation](../actions.md#ssm:updateassociation) |

| `tiros` | [tiros:CreateQuery](../actions.md#tiros:createquery) |

| `tiros` | [tiros:GetQueryAnswer](../actions.md#tiros:getqueryanswer) |
