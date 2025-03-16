# Policy: AmazonECS_FullAccess

ARN: `arn:aws:iam::aws:policy/AmazonECS_FullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| ssm |
| application-autoscaling |
| elasticloadbalancing |
| ecs |
| fsx |
| cloudformation |
| lambda |
| logs |
| servicediscovery |
| ec2 |
| autoscaling |
| events |
| route53 |
| iam |
| codedeploy |
| appmesh |
| elasticfilesystem |
| sns |
| cloudwatch |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `application-autoscaling` | [application-autoscaling:DeleteScalingPolicy](../actions.md#application-autoscaling:deletescalingpolicy) |

| `application-autoscaling` | [application-autoscaling:DeregisterScalableTarget](../actions.md#application-autoscaling:deregisterscalabletarget) |

| `application-autoscaling` | [application-autoscaling:DescribeScalableTargets](../actions.md#application-autoscaling:describescalabletargets) |

| `application-autoscaling` | [application-autoscaling:DescribeScalingActivities](../actions.md#application-autoscaling:describescalingactivities) |

| `application-autoscaling` | [application-autoscaling:DescribeScalingPolicies](../actions.md#application-autoscaling:describescalingpolicies) |

| `application-autoscaling` | [application-autoscaling:PutScalingPolicy](../actions.md#application-autoscaling:putscalingpolicy) |

| `application-autoscaling` | [application-autoscaling:RegisterScalableTarget](../actions.md#application-autoscaling:registerscalabletarget) |

| `appmesh` | [appmesh:DescribeVirtualGateway](../actions.md#appmesh:describevirtualgateway) |

| `appmesh` | [appmesh:DescribeVirtualNode](../actions.md#appmesh:describevirtualnode) |

| `appmesh` | [appmesh:ListMeshes](../actions.md#appmesh:listmeshes) |

| `appmesh` | [appmesh:ListVirtualGateways](../actions.md#appmesh:listvirtualgateways) |

| `appmesh` | [appmesh:ListVirtualNodes](../actions.md#appmesh:listvirtualnodes) |

| `autoscaling` | [autoscaling:CreateAutoScalingGroup](../actions.md#autoscaling:createautoscalinggroup) |

| `autoscaling` | [autoscaling:CreateLaunchConfiguration](../actions.md#autoscaling:createlaunchconfiguration) |

| `autoscaling` | [autoscaling:DeleteAutoScalingGroup](../actions.md#autoscaling:deleteautoscalinggroup) |

| `autoscaling` | [autoscaling:DeleteLaunchConfiguration](../actions.md#autoscaling:deletelaunchconfiguration) |

| `autoscaling` | [autoscaling:Describe*](../actions.md#autoscaling:describeall) |

| `autoscaling` | [autoscaling:UpdateAutoScalingGroup](../actions.md#autoscaling:updateautoscalinggroup) |

| `cloudformation` | [cloudformation:CreateStack](../actions.md#cloudformation:createstack) |

| `cloudformation` | [cloudformation:DeleteStack](../actions.md#cloudformation:deletestack) |

| `cloudformation` | [cloudformation:DescribeStack*](../actions.md#cloudformation:describestackall) |

| `cloudformation` | [cloudformation:UpdateStack](../actions.md#cloudformation:updatestack) |

| `cloudwatch` | [cloudwatch:DeleteAlarms](../actions.md#cloudwatch:deletealarms) |

| `cloudwatch` | [cloudwatch:DescribeAlarms](../actions.md#cloudwatch:describealarms) |

| `cloudwatch` | [cloudwatch:GetMetricStatistics](../actions.md#cloudwatch:getmetricstatistics) |

| `cloudwatch` | [cloudwatch:PutMetricAlarm](../actions.md#cloudwatch:putmetricalarm) |

| `codedeploy` | [codedeploy:BatchGetApplicationRevisions](../actions.md#codedeploy:batchgetapplicationrevisions) |

| `codedeploy` | [codedeploy:BatchGetApplications](../actions.md#codedeploy:batchgetapplications) |

| `codedeploy` | [codedeploy:BatchGetDeploymentGroups](../actions.md#codedeploy:batchgetdeploymentgroups) |

| `codedeploy` | [codedeploy:BatchGetDeployments](../actions.md#codedeploy:batchgetdeployments) |

| `codedeploy` | [codedeploy:ContinueDeployment](../actions.md#codedeploy:continuedeployment) |

| `codedeploy` | [codedeploy:CreateApplication](../actions.md#codedeploy:createapplication) |

| `codedeploy` | [codedeploy:CreateDeployment](../actions.md#codedeploy:createdeployment) |

| `codedeploy` | [codedeploy:CreateDeploymentGroup](../actions.md#codedeploy:createdeploymentgroup) |

| `codedeploy` | [codedeploy:GetApplication](../actions.md#codedeploy:getapplication) |

| `codedeploy` | [codedeploy:GetApplicationRevision](../actions.md#codedeploy:getapplicationrevision) |

| `codedeploy` | [codedeploy:GetDeployment](../actions.md#codedeploy:getdeployment) |

| `codedeploy` | [codedeploy:GetDeploymentConfig](../actions.md#codedeploy:getdeploymentconfig) |

| `codedeploy` | [codedeploy:GetDeploymentGroup](../actions.md#codedeploy:getdeploymentgroup) |

| `codedeploy` | [codedeploy:GetDeploymentTarget](../actions.md#codedeploy:getdeploymenttarget) |

| `codedeploy` | [codedeploy:ListApplicationRevisions](../actions.md#codedeploy:listapplicationrevisions) |

| `codedeploy` | [codedeploy:ListApplications](../actions.md#codedeploy:listapplications) |

| `codedeploy` | [codedeploy:ListDeploymentConfigs](../actions.md#codedeploy:listdeploymentconfigs) |

| `codedeploy` | [codedeploy:ListDeploymentGroups](../actions.md#codedeploy:listdeploymentgroups) |

| `codedeploy` | [codedeploy:ListDeploymentTargets](../actions.md#codedeploy:listdeploymenttargets) |

| `codedeploy` | [codedeploy:ListDeployments](../actions.md#codedeploy:listdeployments) |

| `codedeploy` | [codedeploy:RegisterApplicationRevision](../actions.md#codedeploy:registerapplicationrevision) |

| `codedeploy` | [codedeploy:StopDeployment](../actions.md#codedeploy:stopdeployment) |

| `ec2` | [ec2:AssociateRouteTable](../actions.md#ec2:associateroutetable) |

| `ec2` | [ec2:AttachInternetGateway](../actions.md#ec2:attachinternetgateway) |

| `ec2` | [ec2:AuthorizeSecurityGroupIngress](../actions.md#ec2:authorizesecuritygroupingress) |

| `ec2` | [ec2:CancelSpotFleetRequests](../actions.md#ec2:cancelspotfleetrequests) |

| `ec2` | [ec2:CreateInternetGateway](../actions.md#ec2:createinternetgateway) |

| `ec2` | [ec2:CreateLaunchTemplate](../actions.md#ec2:createlaunchtemplate) |

| `ec2` | [ec2:CreateRoute](../actions.md#ec2:createroute) |

| `ec2` | [ec2:CreateRouteTable](../actions.md#ec2:createroutetable) |

| `ec2` | [ec2:CreateSecurityGroup](../actions.md#ec2:createsecuritygroup) |

| `ec2` | [ec2:CreateSubnet](../actions.md#ec2:createsubnet) |

| `ec2` | [ec2:CreateVpc](../actions.md#ec2:createvpc) |

| `ec2` | [ec2:DeleteInternetGateway](../actions.md#ec2:deleteinternetgateway) |

| `ec2` | [ec2:DeleteLaunchTemplate](../actions.md#ec2:deletelaunchtemplate) |

| `ec2` | [ec2:DeleteRoute](../actions.md#ec2:deleteroute) |

| `ec2` | [ec2:DeleteRouteTable](../actions.md#ec2:deleteroutetable) |

| `ec2` | [ec2:DeleteSecurityGroup](../actions.md#ec2:deletesecuritygroup) |

| `ec2` | [ec2:DeleteSubnet](../actions.md#ec2:deletesubnet) |

| `ec2` | [ec2:DeleteVpc](../actions.md#ec2:deletevpc) |

| `ec2` | [ec2:Describe*](../actions.md#ec2:describeall) |

| `ec2` | [ec2:DetachInternetGateway](../actions.md#ec2:detachinternetgateway) |

| `ec2` | [ec2:DisassociateRouteTable](../actions.md#ec2:disassociateroutetable) |

| `ec2` | [ec2:ModifySubnetAttribute](../actions.md#ec2:modifysubnetattribute) |

| `ec2` | [ec2:ModifyVpcAttribute](../actions.md#ec2:modifyvpcattribute) |

| `ec2` | [ec2:RequestSpotFleet](../actions.md#ec2:requestspotfleet) |

| `ec2` | [ec2:RunInstances](../actions.md#ec2:runinstances) |

| `ecs` | [ecs:*](../actions.md#ecs:all) |

| `elasticfilesystem` | [elasticfilesystem:DescribeAccessPoints](../actions.md#elasticfilesystem:describeaccesspoints) |

| `elasticfilesystem` | [elasticfilesystem:DescribeFileSystems](../actions.md#elasticfilesystem:describefilesystems) |

| `elasticloadbalancing` | [elasticloadbalancing:AddTags](../actions.md#elasticloadbalancing:addtags) |

| `elasticloadbalancing` | [elasticloadbalancing:CreateListener](../actions.md#elasticloadbalancing:createlistener) |

| `elasticloadbalancing` | [elasticloadbalancing:CreateLoadBalancer](../actions.md#elasticloadbalancing:createloadbalancer) |

| `elasticloadbalancing` | [elasticloadbalancing:CreateRule](../actions.md#elasticloadbalancing:createrule) |

| `elasticloadbalancing` | [elasticloadbalancing:CreateTargetGroup](../actions.md#elasticloadbalancing:createtargetgroup) |

| `elasticloadbalancing` | [elasticloadbalancing:DeleteListener](../actions.md#elasticloadbalancing:deletelistener) |

| `elasticloadbalancing` | [elasticloadbalancing:DeleteLoadBalancer](../actions.md#elasticloadbalancing:deleteloadbalancer) |

| `elasticloadbalancing` | [elasticloadbalancing:DeleteRule](../actions.md#elasticloadbalancing:deleterule) |

| `elasticloadbalancing` | [elasticloadbalancing:DeleteTargetGroup](../actions.md#elasticloadbalancing:deletetargetgroup) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeListeners](../actions.md#elasticloadbalancing:describelisteners) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeLoadBalancers](../actions.md#elasticloadbalancing:describeloadbalancers) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeRules](../actions.md#elasticloadbalancing:describerules) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeTargetGroups](../actions.md#elasticloadbalancing:describetargetgroups) |

| `events` | [events:DeleteRule](../actions.md#events:deleterule) |

| `events` | [events:DescribeRule](../actions.md#events:describerule) |

| `events` | [events:ListRuleNamesByTarget](../actions.md#events:listrulenamesbytarget) |

| `events` | [events:ListTargetsByRule](../actions.md#events:listtargetsbyrule) |

| `events` | [events:PutRule](../actions.md#events:putrule) |

| `events` | [events:PutTargets](../actions.md#events:puttargets) |

| `events` | [events:RemoveTargets](../actions.md#events:removetargets) |

| `fsx` | [fsx:DescribeFileSystems](../actions.md#fsx:describefilesystems) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:ListAttachedRolePolicies](../actions.md#iam:listattachedrolepolicies) |

| `iam` | [iam:ListInstanceProfiles](../actions.md#iam:listinstanceprofiles) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `lambda` | [lambda:ListFunctions](../actions.md#lambda:listfunctions) |

| `logs` | [logs:CreateLogGroup](../actions.md#logs:createloggroup) |

| `logs` | [logs:DescribeLogGroups](../actions.md#logs:describeloggroups) |

| `logs` | [logs:FilterLogEvents](../actions.md#logs:filterlogevents) |

| `route53` | [route53:CreateHostedZone](../actions.md#route53:createhostedzone) |

| `route53` | [route53:DeleteHostedZone](../actions.md#route53:deletehostedzone) |

| `route53` | [route53:GetHealthCheck](../actions.md#route53:gethealthcheck) |

| `route53` | [route53:GetHostedZone](../actions.md#route53:gethostedzone) |

| `route53` | [route53:ListHostedZonesByName](../actions.md#route53:listhostedzonesbyname) |

| `servicediscovery` | [servicediscovery:CreatePrivateDnsNamespace](../actions.md#servicediscovery:createprivatednsnamespace) |

| `servicediscovery` | [servicediscovery:CreateService](../actions.md#servicediscovery:createservice) |

| `servicediscovery` | [servicediscovery:DeleteService](../actions.md#servicediscovery:deleteservice) |

| `servicediscovery` | [servicediscovery:GetNamespace](../actions.md#servicediscovery:getnamespace) |

| `servicediscovery` | [servicediscovery:GetOperation](../actions.md#servicediscovery:getoperation) |

| `servicediscovery` | [servicediscovery:GetService](../actions.md#servicediscovery:getservice) |

| `servicediscovery` | [servicediscovery:ListNamespaces](../actions.md#servicediscovery:listnamespaces) |

| `servicediscovery` | [servicediscovery:ListServices](../actions.md#servicediscovery:listservices) |

| `servicediscovery` | [servicediscovery:UpdateService](../actions.md#servicediscovery:updateservice) |

| `sns` | [sns:ListTopics](../actions.md#sns:listtopics) |

| `ssm` | [ssm:GetParameter](../actions.md#ssm:getparameter) |

| `ssm` | [ssm:GetParameters](../actions.md#ssm:getparameters) |

| `ssm` | [ssm:GetParametersByPath](../actions.md#ssm:getparametersbypath) |
