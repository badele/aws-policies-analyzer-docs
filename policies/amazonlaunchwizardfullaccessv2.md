# Policy: AmazonLaunchWizardFullAccessV2

ARN: `arn:aws:iam::aws:policy/AmazonLaunchWizardFullAccessV2`

## Attached Roles

## Attached Services

| Service |
|---------|
| ssm |
| fsx |
| servicecatalog |
| kms |
| cloudformation |
| lambda |
| logs |
| applicationinsights |
| sqs |
| ds |
| launchwizard |
| ec2 |
| tag |
| s3 |
| autoscaling |
| route53 |
| iam |
| elasticfilesystem |
| sns |
| servicequotas |
| resource-groups |
| cloudwatch |
| secretsmanager |
| sts |
| dynamodb |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `applicationinsights` | [applicationinsights:*](../actions.md#applicationinsights:all) |

| `autoscaling` | [autoscaling:AttachInstances](../actions.md#autoscaling:attachinstances) |

| `autoscaling` | [autoscaling:CreateAutoScalingGroup](../actions.md#autoscaling:createautoscalinggroup) |

| `autoscaling` | [autoscaling:CreateLaunchConfiguration](../actions.md#autoscaling:createlaunchconfiguration) |

| `autoscaling` | [autoscaling:CreateOrUpdateTags](../actions.md#autoscaling:createorupdatetags) |

| `autoscaling` | [autoscaling:DeleteAutoScalingGroup](../actions.md#autoscaling:deleteautoscalinggroup) |

| `autoscaling` | [autoscaling:DeleteLaunchConfiguration](../actions.md#autoscaling:deletelaunchconfiguration) |

| `autoscaling` | [autoscaling:Describe*](../actions.md#autoscaling:describeall) |

| `autoscaling` | [autoscaling:UpdateAutoScalingGroup](../actions.md#autoscaling:updateautoscalinggroup) |

| `cloudformation` | [cloudformation:CreateStack](../actions.md#cloudformation:createstack) |

| `cloudformation` | [cloudformation:DeleteStack](../actions.md#cloudformation:deletestack) |

| `cloudformation` | [cloudformation:Describe*](../actions.md#cloudformation:describeall) |

| `cloudformation` | [cloudformation:DescribeAccountLimits](../actions.md#cloudformation:describeaccountlimits) |

| `cloudformation` | [cloudformation:DescribeStack*](../actions.md#cloudformation:describestackall) |

| `cloudformation` | [cloudformation:DescribeStackDriftDetectionStatus](../actions.md#cloudformation:describestackdriftdetectionstatus) |

| `cloudformation` | [cloudformation:Get*](../actions.md#cloudformation:getall) |

| `cloudformation` | [cloudformation:GetTemplateSummary](../actions.md#cloudformation:gettemplatesummary) |

| `cloudformation` | [cloudformation:List*](../actions.md#cloudformation:listall) |

| `cloudformation` | [cloudformation:List*](../actions.md#cloudformation:listall) |

| `cloudformation` | [cloudformation:ListStacks](../actions.md#cloudformation:liststacks) |

| `cloudformation` | [cloudformation:SignalResource](../actions.md#cloudformation:signalresource) |

| `cloudformation` | [cloudformation:TagResource](../actions.md#cloudformation:tagresource) |

| `cloudformation` | [cloudformation:ValidateTemplate](../actions.md#cloudformation:validatetemplate) |

| `cloudwatch` | [cloudwatch:DeleteAlarms](../actions.md#cloudwatch:deletealarms) |

| `cloudwatch` | [cloudwatch:Describe*](../actions.md#cloudwatch:describeall) |

| `cloudwatch` | [cloudwatch:DescribeAlarms](../actions.md#cloudwatch:describealarms) |

| `cloudwatch` | [cloudwatch:Get*](../actions.md#cloudwatch:getall) |

| `cloudwatch` | [cloudwatch:List*](../actions.md#cloudwatch:listall) |

| `cloudwatch` | [cloudwatch:PutMetricAlarm](../actions.md#cloudwatch:putmetricalarm) |

| `ds` | [ds:AddIpRoutes](../actions.md#ds:addiproutes) |

| `ds` | [ds:CreateComputer](../actions.md#ds:createcomputer) |

| `ds` | [ds:CreateMicrosoftAD](../actions.md#ds:createmicrosoftad) |

| `ds` | [ds:DeleteDirectory](../actions.md#ds:deletedirectory) |

| `ds` | [ds:Describe*](../actions.md#ds:describeall) |

| `ds` | [ds:ListAuthorizedApplications](../actions.md#ds:listauthorizedapplications) |

| `dynamodb` | [dynamodb:CreateTable](../actions.md#dynamodb:createtable) |

| `dynamodb` | [dynamodb:DeleteTable](../actions.md#dynamodb:deletetable) |

| `dynamodb` | [dynamodb:DescribeTable](../actions.md#dynamodb:describetable) |

| `ec2` | [ec2:AllocateAddress](../actions.md#ec2:allocateaddress) |

| `ec2` | [ec2:AllocateHosts](../actions.md#ec2:allocatehosts) |

| `ec2` | [ec2:AssignPrivateIpAddresses](../actions.md#ec2:assignprivateipaddresses) |

| `ec2` | [ec2:AssociateAddress](../actions.md#ec2:associateaddress) |

| `ec2` | [ec2:AssociateDhcpOptions](../actions.md#ec2:associatedhcpoptions) |

| `ec2` | [ec2:AssociateRouteTable](../actions.md#ec2:associateroutetable) |

| `ec2` | [ec2:AssociateSubnetCidrBlock](../actions.md#ec2:associatesubnetcidrblock) |

| `ec2` | [ec2:AssociateVpcCidrBlock](../actions.md#ec2:associatevpccidrblock) |

| `ec2` | [ec2:AttachInternetGateway](../actions.md#ec2:attachinternetgateway) |

| `ec2` | [ec2:AttachNetworkInterface](../actions.md#ec2:attachnetworkinterface) |

| `ec2` | [ec2:AttachVolume](../actions.md#ec2:attachvolume) |

| `ec2` | [ec2:AuthorizeSecurityGroupEgress](../actions.md#ec2:authorizesecuritygroupegress) |

| `ec2` | [ec2:AuthorizeSecurityGroupIngress](../actions.md#ec2:authorizesecuritygroupingress) |

| `ec2` | [ec2:CreateDhcpOptions](../actions.md#ec2:createdhcpoptions) |

| `ec2` | [ec2:CreateEgressOnlyInternetGateway](../actions.md#ec2:createegressonlyinternetgateway) |

| `ec2` | [ec2:CreateInternetGateway](../actions.md#ec2:createinternetgateway) |

| `ec2` | [ec2:CreateKeyPair](../actions.md#ec2:createkeypair) |

| `ec2` | [ec2:CreateNatGateway](../actions.md#ec2:createnatgateway) |

| `ec2` | [ec2:CreateNetworkInterface](../actions.md#ec2:createnetworkinterface) |

| `ec2` | [ec2:CreatePlacementGroup](../actions.md#ec2:createplacementgroup) |

| `ec2` | [ec2:CreateRoute](../actions.md#ec2:createroute) |

| `ec2` | [ec2:CreateRouteTable](../actions.md#ec2:createroutetable) |

| `ec2` | [ec2:CreateSecurityGroup](../actions.md#ec2:createsecuritygroup) |

| `ec2` | [ec2:CreateSubnet](../actions.md#ec2:createsubnet) |

| `ec2` | [ec2:CreateTags](../actions.md#ec2:createtags) |

| `ec2` | [ec2:CreateVolume](../actions.md#ec2:createvolume) |

| `ec2` | [ec2:CreateVpc](../actions.md#ec2:createvpc) |

| `ec2` | [ec2:CreateVpcEndpoint](../actions.md#ec2:createvpcendpoint) |

| `ec2` | [ec2:DeleteDhcpOptions](../actions.md#ec2:deletedhcpoptions) |

| `ec2` | [ec2:DeleteInternetGateway](../actions.md#ec2:deleteinternetgateway) |

| `ec2` | [ec2:DeleteKeyPair](../actions.md#ec2:deletekeypair) |

| `ec2` | [ec2:DeleteNatGateway](../actions.md#ec2:deletenatgateway) |

| `ec2` | [ec2:DeleteNetworkAcl](../actions.md#ec2:deletenetworkacl) |

| `ec2` | [ec2:DeleteNetworkInterface](../actions.md#ec2:deletenetworkinterface) |

| `ec2` | [ec2:DeleteNetworkInterfacePermission](../actions.md#ec2:deletenetworkinterfacepermission) |

| `ec2` | [ec2:DeletePlacementGroup](../actions.md#ec2:deleteplacementgroup) |

| `ec2` | [ec2:DeleteRoute](../actions.md#ec2:deleteroute) |

| `ec2` | [ec2:DeleteRouteTable](../actions.md#ec2:deleteroutetable) |

| `ec2` | [ec2:DeleteSecurityGroup](../actions.md#ec2:deletesecuritygroup) |

| `ec2` | [ec2:DeleteSnapshot](../actions.md#ec2:deletesnapshot) |

| `ec2` | [ec2:DeleteSubnet](../actions.md#ec2:deletesubnet) |

| `ec2` | [ec2:DeleteTags](../actions.md#ec2:deletetags) |

| `ec2` | [ec2:DeleteVolume](../actions.md#ec2:deletevolume) |

| `ec2` | [ec2:DeleteVpc](../actions.md#ec2:deletevpc) |

| `ec2` | [ec2:Describe*](../actions.md#ec2:describeall) |

| `ec2` | [ec2:DetachInternetGateway](../actions.md#ec2:detachinternetgateway) |

| `ec2` | [ec2:DetachNetworkInterface](../actions.md#ec2:detachnetworkinterface) |

| `ec2` | [ec2:DetachVolume](../actions.md#ec2:detachvolume) |

| `ec2` | [ec2:DisassociateAddress](../actions.md#ec2:disassociateaddress) |

| `ec2` | [ec2:DisassociateIamInstanceProfile](../actions.md#ec2:disassociateiaminstanceprofile) |

| `ec2` | [ec2:DisassociateRouteTable](../actions.md#ec2:disassociateroutetable) |

| `ec2` | [ec2:DisassociateSubnetCidrBlock](../actions.md#ec2:disassociatesubnetcidrblock) |

| `ec2` | [ec2:DisassociateVpcCidrBlock](../actions.md#ec2:disassociatevpccidrblock) |

| `ec2` | [ec2:Get*](../actions.md#ec2:getall) |

| `ec2` | [ec2:GetConsoleOutput](../actions.md#ec2:getconsoleoutput) |

| `ec2` | [ec2:GetLaunchTemplateData](../actions.md#ec2:getlaunchtemplatedata) |

| `ec2` | [ec2:GetPasswordData](../actions.md#ec2:getpassworddata) |

| `ec2` | [ec2:ModifyInstanceAttribute](../actions.md#ec2:modifyinstanceattribute) |

| `ec2` | [ec2:ModifyInstancePlacement](../actions.md#ec2:modifyinstanceplacement) |

| `ec2` | [ec2:ModifyNetworkInterfaceAttribute](../actions.md#ec2:modifynetworkinterfaceattribute) |

| `ec2` | [ec2:ModifySubnetAttribute](../actions.md#ec2:modifysubnetattribute) |

| `ec2` | [ec2:ModifyVolume](../actions.md#ec2:modifyvolume) |

| `ec2` | [ec2:ModifyVolumeAttribute](../actions.md#ec2:modifyvolumeattribute) |

| `ec2` | [ec2:ModifyVpcAttribute](../actions.md#ec2:modifyvpcattribute) |

| `ec2` | [ec2:ReleaseAddress](../actions.md#ec2:releaseaddress) |

| `ec2` | [ec2:ReplaceRoute](../actions.md#ec2:replaceroute) |

| `ec2` | [ec2:ReplaceRouteTableAssociation](../actions.md#ec2:replaceroutetableassociation) |

| `ec2` | [ec2:RevokeSecurityGroupEgress](../actions.md#ec2:revokesecuritygroupegress) |

| `ec2` | [ec2:RevokeSecurityGroupIngress](../actions.md#ec2:revokesecuritygroupingress) |

| `ec2` | [ec2:RunInstances](../actions.md#ec2:runinstances) |

| `ec2` | [ec2:StartInstances](../actions.md#ec2:startinstances) |

| `ec2` | [ec2:StopInstances](../actions.md#ec2:stopinstances) |

| `ec2` | [ec2:TerminateInstances](../actions.md#ec2:terminateinstances) |

| `elasticfilesystem` | [elasticfilesystem:CreateFileSystem](../actions.md#elasticfilesystem:createfilesystem) |

| `elasticfilesystem` | [elasticfilesystem:CreateMountTarget](../actions.md#elasticfilesystem:createmounttarget) |

| `elasticfilesystem` | [elasticfilesystem:DeleteFileSystem](../actions.md#elasticfilesystem:deletefilesystem) |

| `elasticfilesystem` | [elasticfilesystem:DeleteMountTarget](../actions.md#elasticfilesystem:deletemounttarget) |

| `elasticfilesystem` | [elasticfilesystem:DescribeFileSystems](../actions.md#elasticfilesystem:describefilesystems) |

| `elasticfilesystem` | [elasticfilesystem:DescribeMountTargetSecurityGroups](../actions.md#elasticfilesystem:describemounttargetsecuritygroups) |

| `elasticfilesystem` | [elasticfilesystem:DescribeMountTargets](../actions.md#elasticfilesystem:describemounttargets) |

| `elasticfilesystem` | [elasticfilesystem:TagResource](../actions.md#elasticfilesystem:tagresource) |

| `elasticfilesystem` | [elasticfilesystem:UntagResource](../actions.md#elasticfilesystem:untagresource) |

| `fsx` | [fsx:CreateFileSystem](../actions.md#fsx:createfilesystem) |

| `fsx` | [fsx:CreateStorageVirtualMachine](../actions.md#fsx:createstoragevirtualmachine) |

| `fsx` | [fsx:CreateVolume](../actions.md#fsx:createvolume) |

| `fsx` | [fsx:DeleteFileSystem](../actions.md#fsx:deletefilesystem) |

| `fsx` | [fsx:DeleteStorageVirtualMachine](../actions.md#fsx:deletestoragevirtualmachine) |

| `fsx` | [fsx:DeleteVolume](../actions.md#fsx:deletevolume) |

| `fsx` | [fsx:DescribeFileSystems](../actions.md#fsx:describefilesystems) |

| `fsx` | [fsx:DescribeStorageVirtualMachines](../actions.md#fsx:describestoragevirtualmachines) |

| `fsx` | [fsx:DescribeVolumes](../actions.md#fsx:describevolumes) |

| `fsx` | [fsx:ListTagsForResource](../actions.md#fsx:listtagsforresource) |

| `fsx` | [fsx:TagResource](../actions.md#fsx:tagresource) |

| `fsx` | [fsx:UntagResource](../actions.md#fsx:untagresource) |

| `iam` | [iam:AddRoleToInstanceProfile](../actions.md#iam:addroletoinstanceprofile) |

| `iam` | [iam:CreateInstanceProfile](../actions.md#iam:createinstanceprofile) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:DeleteInstanceProfile](../actions.md#iam:deleteinstanceprofile) |

| `iam` | [iam:GetInstanceProfile](../actions.md#iam:getinstanceprofile) |

| `iam` | [iam:GetPolicy](../actions.md#iam:getpolicy) |

| `iam` | [iam:GetPolicyVersion](../actions.md#iam:getpolicyversion) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `iam` | [iam:GetRolePolicy](../actions.md#iam:getrolepolicy) |

| `iam` | [iam:GetUser](../actions.md#iam:getuser) |

| `iam` | [iam:List*](../actions.md#iam:listall) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `iam` | [iam:RemoveRoleFromInstanceProfile](../actions.md#iam:removerolefrominstanceprofile) |

| `kms` | [kms:ListAliases](../actions.md#kms:listaliases) |

| `kms` | [kms:ListKeys](../actions.md#kms:listkeys) |

| `lambda` | [lambda:CreateFunction](../actions.md#lambda:createfunction) |

| `lambda` | [lambda:DeleteFunction](../actions.md#lambda:deletefunction) |

| `lambda` | [lambda:GetFunction](../actions.md#lambda:getfunction) |

| `lambda` | [lambda:GetFunctionConfiguration](../actions.md#lambda:getfunctionconfiguration) |

| `lambda` | [lambda:InvokeFunction](../actions.md#lambda:invokefunction) |

| `launchwizard` | [launchwizard:*](../actions.md#launchwizard:all) |

| `logs` | [logs:CreateLogGroup](../actions.md#logs:createloggroup) |

| `logs` | [logs:CreateLogStream](../actions.md#logs:createlogstream) |

| `logs` | [logs:DeleteLogGroup](../actions.md#logs:deleteloggroup) |

| `logs` | [logs:DeleteLogStream](../actions.md#logs:deletelogstream) |

| `logs` | [logs:DescribeLogGroups](../actions.md#logs:describeloggroups) |

| `logs` | [logs:DescribeLogStreams](../actions.md#logs:describelogstreams) |

| `logs` | [logs:GetLogDelivery](../actions.md#logs:getlogdelivery) |

| `logs` | [logs:GetLogEvents](../actions.md#logs:getlogevents) |

| `logs` | [logs:GetLogGroupFields](../actions.md#logs:getloggroupfields) |

| `logs` | [logs:GetLogRecord](../actions.md#logs:getlogrecord) |

| `logs` | [logs:ListLogDeliveries](../actions.md#logs:listlogdeliveries) |

| `logs` | [logs:PutLogEvents](../actions.md#logs:putlogevents) |

| `logs` | [logs:TagResource](../actions.md#logs:tagresource) |

| `logs` | [logs:UntagResource](../actions.md#logs:untagresource) |

| `resource-groups` | [resource-groups:CreateGroup](../actions.md#resource-groups:creategroup) |

| `resource-groups` | [resource-groups:DeleteGroup](../actions.md#resource-groups:deletegroup) |

| `resource-groups` | [resource-groups:Get*](../actions.md#resource-groups:getall) |

| `resource-groups` | [resource-groups:List*](../actions.md#resource-groups:listall) |

| `resource-groups` | [resource-groups:List*](../actions.md#resource-groups:listall) |

| `route53` | [route53:ChangeResourceRecordSets](../actions.md#route53:changeresourcerecordsets) |

| `route53` | [route53:GetChange](../actions.md#route53:getchange) |

| `route53` | [route53:ListHostedZones](../actions.md#route53:listhostedzones) |

| `route53` | [route53:ListHostedZones](../actions.md#route53:listhostedzones) |

| `route53` | [route53:ListHostedZonesByName](../actions.md#route53:listhostedzonesbyname) |

| `route53` | [route53:ListResourceRecordSets](../actions.md#route53:listresourcerecordsets) |

| `s3` | [s3:CreateBucket](../actions.md#s3:createbucket) |

| `s3` | [s3:DeleteBucket](../actions.md#s3:deletebucket) |

| `s3` | [s3:GetBucketLocation](../actions.md#s3:getbucketlocation) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:PutBucketVersioning](../actions.md#s3:putbucketversioning) |

| `s3` | [s3:PutObject](../actions.md#s3:putobject) |

| `secretsmanager` | [secretsmanager:CreateSecret](../actions.md#secretsmanager:createsecret) |

| `secretsmanager` | [secretsmanager:DeleteResourcePolicy](../actions.md#secretsmanager:deleteresourcepolicy) |

| `secretsmanager` | [secretsmanager:DeleteSecret](../actions.md#secretsmanager:deletesecret) |

| `secretsmanager` | [secretsmanager:GetRandomPassword](../actions.md#secretsmanager:getrandompassword) |

| `secretsmanager` | [secretsmanager:GetSecretValue](../actions.md#secretsmanager:getsecretvalue) |

| `secretsmanager` | [secretsmanager:ListSecretVersionIds](../actions.md#secretsmanager:listsecretversionids) |

| `secretsmanager` | [secretsmanager:ListSecrets](../actions.md#secretsmanager:listsecrets) |

| `secretsmanager` | [secretsmanager:PutResourcePolicy](../actions.md#secretsmanager:putresourcepolicy) |

| `secretsmanager` | [secretsmanager:TagResource](../actions.md#secretsmanager:tagresource) |

| `secretsmanager` | [secretsmanager:UntagResource](../actions.md#secretsmanager:untagresource) |

| `servicecatalog` | [servicecatalog:AssociatePrincipalWithPortfolio](../actions.md#servicecatalog:associateprincipalwithportfolio) |

| `servicecatalog` | [servicecatalog:AssociateProductWithPortfolio](../actions.md#servicecatalog:associateproductwithportfolio) |

| `servicecatalog` | [servicecatalog:CreateConstraint](../actions.md#servicecatalog:createconstraint) |

| `servicecatalog` | [servicecatalog:CreatePortfolio](../actions.md#servicecatalog:createportfolio) |

| `servicecatalog` | [servicecatalog:CreateProduct](../actions.md#servicecatalog:createproduct) |

| `servicecatalog` | [servicecatalog:CreateProvisioningArtifact](../actions.md#servicecatalog:createprovisioningartifact) |

| `servicecatalog` | [servicecatalog:DescribePortfolio](../actions.md#servicecatalog:describeportfolio) |

| `servicecatalog` | [servicecatalog:TagResource](../actions.md#servicecatalog:tagresource) |

| `servicecatalog` | [servicecatalog:UntagResource](../actions.md#servicecatalog:untagresource) |

| `servicequotas` | [servicequotas:GetServiceQuota](../actions.md#servicequotas:getservicequota) |

| `servicequotas` | [servicequotas:ListServiceQuotas](../actions.md#servicequotas:listservicequotas) |

| `sns` | [sns:CreateTopic](../actions.md#sns:createtopic) |

| `sns` | [sns:DeleteTopic](../actions.md#sns:deletetopic) |

| `sns` | [sns:ListSubscriptions](../actions.md#sns:listsubscriptions) |

| `sns` | [sns:ListSubscriptionsByTopic](../actions.md#sns:listsubscriptionsbytopic) |

| `sns` | [sns:ListTopics](../actions.md#sns:listtopics) |

| `sns` | [sns:Publish](../actions.md#sns:publish) |

| `sns` | [sns:Subscribe](../actions.md#sns:subscribe) |

| `sns` | [sns:Unsubscribe](../actions.md#sns:unsubscribe) |

| `sqs` | [sqs:AddPermission](../actions.md#sqs:addpermission) |

| `sqs` | [sqs:CreateQueue](../actions.md#sqs:createqueue) |

| `sqs` | [sqs:DeleteQueue](../actions.md#sqs:deletequeue) |

| `sqs` | [sqs:GetQueueAttributes](../actions.md#sqs:getqueueattributes) |

| `sqs` | [sqs:GetQueueUrl](../actions.md#sqs:getqueueurl) |

| `sqs` | [sqs:ListQueueTags](../actions.md#sqs:listqueuetags) |

| `sqs` | [sqs:ListQueues](../actions.md#sqs:listqueues) |

| `sqs` | [sqs:SetQueueAttributes](../actions.md#sqs:setqueueattributes) |

| `sqs` | [sqs:TagQueue](../actions.md#sqs:tagqueue) |

| `ssm` | [ssm:AddTagsToResource](../actions.md#ssm:addtagstoresource) |

| `ssm` | [ssm:CreateAssociation](../actions.md#ssm:createassociation) |

| `ssm` | [ssm:CreateDocument](../actions.md#ssm:createdocument) |

| `ssm` | [ssm:CreateOpsMetadata](../actions.md#ssm:createopsmetadata) |

| `ssm` | [ssm:DeleteAssociation](../actions.md#ssm:deleteassociation) |

| `ssm` | [ssm:DeleteDocument](../actions.md#ssm:deletedocument) |

| `ssm` | [ssm:DeleteOpsMetadata](../actions.md#ssm:deleteopsmetadata) |

| `ssm` | [ssm:DeleteParameter*](../actions.md#ssm:deleteparameterall) |

| `ssm` | [ssm:DescribeAutomation*](../actions.md#ssm:describeautomationall) |

| `ssm` | [ssm:DescribeDocument](../actions.md#ssm:describedocument) |

| `ssm` | [ssm:DescribeDocument*](../actions.md#ssm:describedocumentall) |

| `ssm` | [ssm:DescribeInstanceInformation](../actions.md#ssm:describeinstanceinformation) |

| `ssm` | [ssm:DescribeParameters](../actions.md#ssm:describeparameters) |

| `ssm` | [ssm:GetAutomationExecution](../actions.md#ssm:getautomationexecution) |

| `ssm` | [ssm:GetCommandInvocation](../actions.md#ssm:getcommandinvocation) |

| `ssm` | [ssm:GetConnectionStatus](../actions.md#ssm:getconnectionstatus) |

| `ssm` | [ssm:GetDocument](../actions.md#ssm:getdocument) |

| `ssm` | [ssm:GetDocument](../actions.md#ssm:getdocument) |

| `ssm` | [ssm:GetDocument](../actions.md#ssm:getdocument) |

| `ssm` | [ssm:GetParameter*](../actions.md#ssm:getparameterall) |

| `ssm` | [ssm:ListCommand*](../actions.md#ssm:listcommandall) |

| `ssm` | [ssm:ListDocument*](../actions.md#ssm:listdocumentall) |

| `ssm` | [ssm:ListInstanceAssociations](../actions.md#ssm:listinstanceassociations) |

| `ssm` | [ssm:ListTagsForResource](../actions.md#ssm:listtagsforresource) |

| `ssm` | [ssm:PutParameter](../actions.md#ssm:putparameter) |

| `ssm` | [ssm:RemoveTagsFromResource](../actions.md#ssm:removetagsfromresource) |

| `ssm` | [ssm:SendAutomationSignal](../actions.md#ssm:sendautomationsignal) |

| `ssm` | [ssm:SendCommand](../actions.md#ssm:sendcommand) |

| `ssm` | [ssm:SendCommand](../actions.md#ssm:sendcommand) |

| `ssm` | [ssm:StartAutomationExecution](../actions.md#ssm:startautomationexecution) |

| `ssm` | [ssm:StopAutomationExecution](../actions.md#ssm:stopautomationexecution) |

| `sts` | [sts:GetCallerIdentity](../actions.md#sts:getcalleridentity) |

| `tag` | [tag:Get*](../actions.md#tag:getall) |
