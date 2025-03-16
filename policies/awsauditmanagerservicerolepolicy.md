# Policy: AWSAuditManagerServiceRolePolicy

ARN: `arn:aws:iam::aws:policy/aws-service-role/AWSAuditManagerServiceRolePolicy`

## Attached Roles

## Attached Services

| Service |
|---------|
| license-manager |
| backup |
| guardduty |
| elasticloadbalancing |
| ecs |
| fsx |
| rds |
| cloudfront |
| kms |
| waf |
| lambda |
| firehose |
| logs |
| securityhub |
| sqs |
| kafka |
| ec2 |
| es |
| s3 |
| autoscaling |
| events |
| cloudtrail |
| route53 |
| config |
| iam |
| sagemaker |
| elasticmapreduce |
| directconnect |
| apigateway |
| elasticfilesystem |
| sns |
| cognito-idp |
| bedrock |
| secretsmanager |
| cloudwatch |
| acm |
| kinesis |
| elasticache |
| eks |
| organizations |
| waf-regional |
| wafv2 |
| redshift |
| dynamodb |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `acm` | [acm:GetAccountConfiguration](../actions.md#acm:getaccountconfiguration) |

| `acm` | [acm:ListCertificates](../actions.md#acm:listcertificates) |

| `apigateway` | [apigateway:GET](../actions.md#apigateway:get) |

| `autoscaling` | [autoscaling:DescribeAutoScalingGroups](../actions.md#autoscaling:describeautoscalinggroups) |

| `backup` | [backup:ListBackupPlans](../actions.md#backup:listbackupplans) |

| `backup` | [backup:ListRecoveryPointsByResource](../actions.md#backup:listrecoverypointsbyresource) |

| `bedrock` | [bedrock:GetCustomModel](../actions.md#bedrock:getcustommodel) |

| `bedrock` | [bedrock:GetFoundationModel](../actions.md#bedrock:getfoundationmodel) |

| `bedrock` | [bedrock:GetModelCustomizationJob](../actions.md#bedrock:getmodelcustomizationjob) |

| `bedrock` | [bedrock:GetModelInvocationLoggingConfiguration](../actions.md#bedrock:getmodelinvocationloggingconfiguration) |

| `bedrock` | [bedrock:ListCustomModels](../actions.md#bedrock:listcustommodels) |

| `bedrock` | [bedrock:ListFoundationModels](../actions.md#bedrock:listfoundationmodels) |

| `bedrock` | [bedrock:ListGuardrails](../actions.md#bedrock:listguardrails) |

| `bedrock` | [bedrock:ListModelCustomizationJobs](../actions.md#bedrock:listmodelcustomizationjobs) |

| `cloudfront` | [cloudfront:GetDistribution](../actions.md#cloudfront:getdistribution) |

| `cloudfront` | [cloudfront:GetDistributionConfig](../actions.md#cloudfront:getdistributionconfig) |

| `cloudfront` | [cloudfront:ListDistributions](../actions.md#cloudfront:listdistributions) |

| `cloudtrail` | [cloudtrail:DescribeTrails](../actions.md#cloudtrail:describetrails) |

| `cloudtrail` | [cloudtrail:GetTrail](../actions.md#cloudtrail:gettrail) |

| `cloudtrail` | [cloudtrail:ListTrails](../actions.md#cloudtrail:listtrails) |

| `cloudtrail` | [cloudtrail:LookupEvents](../actions.md#cloudtrail:lookupevents) |

| `cloudwatch` | [cloudwatch:DescribeAlarms](../actions.md#cloudwatch:describealarms) |

| `cloudwatch` | [cloudwatch:DescribeAlarmsForMetric](../actions.md#cloudwatch:describealarmsformetric) |

| `cloudwatch` | [cloudwatch:GetMetricStatistics](../actions.md#cloudwatch:getmetricstatistics) |

| `cloudwatch` | [cloudwatch:ListMetrics](../actions.md#cloudwatch:listmetrics) |

| `cognito-idp` | [cognito-idp:DescribeUserPool](../actions.md#cognito-idp:describeuserpool) |

| `config` | [config:DescribeConfigRules](../actions.md#config:describeconfigrules) |

| `config` | [config:DescribeDeliveryChannels](../actions.md#config:describedeliverychannels) |

| `config` | [config:ListDiscoveredResources](../actions.md#config:listdiscoveredresources) |

| `directconnect` | [directconnect:DescribeDirectConnectGateways](../actions.md#directconnect:describedirectconnectgateways) |

| `directconnect` | [directconnect:DescribeVirtualGateways](../actions.md#directconnect:describevirtualgateways) |

| `dynamodb` | [dynamodb:DescribeBackup](../actions.md#dynamodb:describebackup) |

| `dynamodb` | [dynamodb:DescribeContinuousBackups](../actions.md#dynamodb:describecontinuousbackups) |

| `dynamodb` | [dynamodb:DescribeTable](../actions.md#dynamodb:describetable) |

| `dynamodb` | [dynamodb:DescribeTableReplicaAutoScaling](../actions.md#dynamodb:describetablereplicaautoscaling) |

| `dynamodb` | [dynamodb:ListBackups](../actions.md#dynamodb:listbackups) |

| `dynamodb` | [dynamodb:ListGlobalTables](../actions.md#dynamodb:listglobaltables) |

| `dynamodb` | [dynamodb:ListTables](../actions.md#dynamodb:listtables) |

| `ec2` | [ec2:DescribeAddresses](../actions.md#ec2:describeaddresses) |

| `ec2` | [ec2:DescribeCustomerGateways](../actions.md#ec2:describecustomergateways) |

| `ec2` | [ec2:DescribeEgressOnlyInternetGateways](../actions.md#ec2:describeegressonlyinternetgateways) |

| `ec2` | [ec2:DescribeFlowLogs](../actions.md#ec2:describeflowlogs) |

| `ec2` | [ec2:DescribeInstanceAttribute](../actions.md#ec2:describeinstanceattribute) |

| `ec2` | [ec2:DescribeInstanceCreditSpecifications](../actions.md#ec2:describeinstancecreditspecifications) |

| `ec2` | [ec2:DescribeInstances](../actions.md#ec2:describeinstances) |

| `ec2` | [ec2:DescribeInternetGateways](../actions.md#ec2:describeinternetgateways) |

| `ec2` | [ec2:DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations](../actions.md#ec2:describelocalgatewayroutetablevirtualinterfacegroupassociations) |

| `ec2` | [ec2:DescribeLocalGatewayVirtualInterfaces](../actions.md#ec2:describelocalgatewayvirtualinterfaces) |

| `ec2` | [ec2:DescribeLocalGateways](../actions.md#ec2:describelocalgateways) |

| `ec2` | [ec2:DescribeNatGateways](../actions.md#ec2:describenatgateways) |

| `ec2` | [ec2:DescribeNetworkAcls](../actions.md#ec2:describenetworkacls) |

| `ec2` | [ec2:DescribeRouteTables](../actions.md#ec2:describeroutetables) |

| `ec2` | [ec2:DescribeSecurityGroupRules](../actions.md#ec2:describesecuritygrouprules) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSnapshots](../actions.md#ec2:describesnapshots) |

| `ec2` | [ec2:DescribeTransitGateways](../actions.md#ec2:describetransitgateways) |

| `ec2` | [ec2:DescribeVolumes](../actions.md#ec2:describevolumes) |

| `ec2` | [ec2:DescribeVpcEndpointConnections](../actions.md#ec2:describevpcendpointconnections) |

| `ec2` | [ec2:DescribeVpcEndpointServiceConfigurations](../actions.md#ec2:describevpcendpointserviceconfigurations) |

| `ec2` | [ec2:DescribeVpcEndpoints](../actions.md#ec2:describevpcendpoints) |

| `ec2` | [ec2:DescribeVpcPeeringConnections](../actions.md#ec2:describevpcpeeringconnections) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `ec2` | [ec2:DescribeVpnConnections](../actions.md#ec2:describevpnconnections) |

| `ec2` | [ec2:DescribeVpnGateways](../actions.md#ec2:describevpngateways) |

| `ec2` | [ec2:GetEbsDefaultKmsKeyId](../actions.md#ec2:getebsdefaultkmskeyid) |

| `ec2` | [ec2:GetEbsEncryptionByDefault](../actions.md#ec2:getebsencryptionbydefault) |

| `ec2` | [ec2:GetLaunchTemplateData](../actions.md#ec2:getlaunchtemplatedata) |

| `ecs` | [ecs:DescribeClusters](../actions.md#ecs:describeclusters) |

| `eks` | [eks:DescribeAddonVersions](../actions.md#eks:describeaddonversions) |

| `elasticache` | [elasticache:DescribeCacheClusters](../actions.md#elasticache:describecacheclusters) |

| `elasticache` | [elasticache:DescribeServiceUpdates](../actions.md#elasticache:describeserviceupdates) |

| `elasticfilesystem` | [elasticfilesystem:DescribeAccessPoints](../actions.md#elasticfilesystem:describeaccesspoints) |

| `elasticfilesystem` | [elasticfilesystem:DescribeFileSystems](../actions.md#elasticfilesystem:describefilesystems) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeLoadBalancers](../actions.md#elasticloadbalancing:describeloadbalancers) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeSslPolicies](../actions.md#elasticloadbalancing:describesslpolicies) |

| `elasticloadbalancing` | [elasticloadbalancing:DescribeTargetGroups](../actions.md#elasticloadbalancing:describetargetgroups) |

| `elasticmapreduce` | [elasticmapreduce:ListClusters](../actions.md#elasticmapreduce:listclusters) |

| `elasticmapreduce` | [elasticmapreduce:ListSecurityConfigurations](../actions.md#elasticmapreduce:listsecurityconfigurations) |

| `es` | [es:DescribeDomain](../actions.md#es:describedomain) |

| `es` | [es:DescribeDomainConfig](../actions.md#es:describedomainconfig) |

| `es` | [es:DescribeDomains](../actions.md#es:describedomains) |

| `es` | [es:ListDomainNames](../actions.md#es:listdomainnames) |

| `events` | [events:DeleteRule](../actions.md#events:deleterule) |

| `events` | [events:DescribeRule](../actions.md#events:describerule) |

| `events` | [events:DescribeRule](../actions.md#events:describerule) |

| `events` | [events:DisableRule](../actions.md#events:disablerule) |

| `events` | [events:EnableRule](../actions.md#events:enablerule) |

| `events` | [events:ListConnections](../actions.md#events:listconnections) |

| `events` | [events:ListEventBuses](../actions.md#events:listeventbuses) |

| `events` | [events:ListEventSources](../actions.md#events:listeventsources) |

| `events` | [events:ListRules](../actions.md#events:listrules) |

| `events` | [events:ListTargetsByRule](../actions.md#events:listtargetsbyrule) |

| `events` | [events:PutRule](../actions.md#events:putrule) |

| `events` | [events:PutTargets](../actions.md#events:puttargets) |

| `events` | [events:RemoveTargets](../actions.md#events:removetargets) |

| `firehose` | [firehose:ListDeliveryStreams](../actions.md#firehose:listdeliverystreams) |

| `fsx` | [fsx:DescribeFileSystems](../actions.md#fsx:describefilesystems) |

| `guardduty` | [guardduty:ListDetectors](../actions.md#guardduty:listdetectors) |

| `iam` | [iam:GenerateCredentialReport](../actions.md#iam:generatecredentialreport) |

| `iam` | [iam:GetAccessKeyLastUsed](../actions.md#iam:getaccesskeylastused) |

| `iam` | [iam:GetAccountAuthorizationDetails](../actions.md#iam:getaccountauthorizationdetails) |

| `iam` | [iam:GetAccountPasswordPolicy](../actions.md#iam:getaccountpasswordpolicy) |

| `iam` | [iam:GetAccountSummary](../actions.md#iam:getaccountsummary) |

| `iam` | [iam:GetCredentialReport](../actions.md#iam:getcredentialreport) |

| `iam` | [iam:GetGroupPolicy](../actions.md#iam:getgrouppolicy) |

| `iam` | [iam:GetPolicy](../actions.md#iam:getpolicy) |

| `iam` | [iam:GetPolicyVersion](../actions.md#iam:getpolicyversion) |

| `iam` | [iam:GetRolePolicy](../actions.md#iam:getrolepolicy) |

| `iam` | [iam:GetUser](../actions.md#iam:getuser) |

| `iam` | [iam:GetUserPolicy](../actions.md#iam:getuserpolicy) |

| `iam` | [iam:ListAccessKeys](../actions.md#iam:listaccesskeys) |

| `iam` | [iam:ListAttachedGroupPolicies](../actions.md#iam:listattachedgrouppolicies) |

| `iam` | [iam:ListAttachedRolePolicies](../actions.md#iam:listattachedrolepolicies) |

| `iam` | [iam:ListAttachedUserPolicies](../actions.md#iam:listattacheduserpolicies) |

| `iam` | [iam:ListEntitiesForPolicy](../actions.md#iam:listentitiesforpolicy) |

| `iam` | [iam:ListGroupPolicies](../actions.md#iam:listgrouppolicies) |

| `iam` | [iam:ListGroups](../actions.md#iam:listgroups) |

| `iam` | [iam:ListGroupsForUser](../actions.md#iam:listgroupsforuser) |

| `iam` | [iam:ListMfaDeviceTags](../actions.md#iam:listmfadevicetags) |

| `iam` | [iam:ListMfaDevices](../actions.md#iam:listmfadevices) |

| `iam` | [iam:ListOpenIdConnectProviders](../actions.md#iam:listopenidconnectproviders) |

| `iam` | [iam:ListPolicies](../actions.md#iam:listpolicies) |

| `iam` | [iam:ListPolicyVersions](../actions.md#iam:listpolicyversions) |

| `iam` | [iam:ListRolePolicies](../actions.md#iam:listrolepolicies) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `iam` | [iam:ListSamlProviders](../actions.md#iam:listsamlproviders) |

| `iam` | [iam:ListUserPolicies](../actions.md#iam:listuserpolicies) |

| `iam` | [iam:ListUsers](../actions.md#iam:listusers) |

| `iam` | [iam:ListVirtualMFADevices](../actions.md#iam:listvirtualmfadevices) |

| `kafka` | [kafka:ListClusters](../actions.md#kafka:listclusters) |

| `kafka` | [kafka:ListKafkaVersions](../actions.md#kafka:listkafkaversions) |

| `kinesis` | [kinesis:ListStreams](../actions.md#kinesis:liststreams) |

| `kms` | [kms:DescribeKey](../actions.md#kms:describekey) |

| `kms` | [kms:GetKeyPolicy](../actions.md#kms:getkeypolicy) |

| `kms` | [kms:GetKeyRotationStatus](../actions.md#kms:getkeyrotationstatus) |

| `kms` | [kms:ListGrants](../actions.md#kms:listgrants) |

| `kms` | [kms:ListKeyPolicies](../actions.md#kms:listkeypolicies) |

| `kms` | [kms:ListKeys](../actions.md#kms:listkeys) |

| `lambda` | [lambda:ListFunctions](../actions.md#lambda:listfunctions) |

| `license-manager` | [license-manager:ListAssociationsForLicenseConfiguration](../actions.md#license-manager:listassociationsforlicenseconfiguration) |

| `license-manager` | [license-manager:ListLicenseConfigurations](../actions.md#license-manager:listlicenseconfigurations) |

| `license-manager` | [license-manager:ListUsageForLicenseConfiguration](../actions.md#license-manager:listusageforlicenseconfiguration) |

| `logs` | [logs:DescribeDestinations](../actions.md#logs:describedestinations) |

| `logs` | [logs:DescribeExportTasks](../actions.md#logs:describeexporttasks) |

| `logs` | [logs:DescribeLogGroups](../actions.md#logs:describeloggroups) |

| `logs` | [logs:DescribeMetricFilters](../actions.md#logs:describemetricfilters) |

| `logs` | [logs:DescribeResourcePolicies](../actions.md#logs:describeresourcepolicies) |

| `logs` | [logs:FilterLogEvents](../actions.md#logs:filterlogevents) |

| `logs` | [logs:GetDataProtectionPolicy](../actions.md#logs:getdataprotectionpolicy) |

| `organizations` | [organizations:DescribeOrganization](../actions.md#organizations:describeorganization) |

| `organizations` | [organizations:DescribePolicy](../actions.md#organizations:describepolicy) |

| `rds` | [rds:DescribeCertificates](../actions.md#rds:describecertificates) |

| `rds` | [rds:DescribeDBClusterEndpoints](../actions.md#rds:describedbclusterendpoints) |

| `rds` | [rds:DescribeDBClusterParameterGroups](../actions.md#rds:describedbclusterparametergroups) |

| `rds` | [rds:DescribeDBClusters](../actions.md#rds:describedbclusters) |

| `rds` | [rds:DescribeDBInstanceAutomatedBackups](../actions.md#rds:describedbinstanceautomatedbackups) |

| `rds` | [rds:DescribeDBInstances](../actions.md#rds:describedbinstances) |

| `rds` | [rds:DescribeDBSecurityGroups](../actions.md#rds:describedbsecuritygroups) |

| `redshift` | [redshift:DescribeClusterSnapshots](../actions.md#redshift:describeclustersnapshots) |

| `redshift` | [redshift:DescribeClusters](../actions.md#redshift:describeclusters) |

| `redshift` | [redshift:DescribeLoggingStatus](../actions.md#redshift:describeloggingstatus) |

| `route53` | [route53:GetQueryLoggingConfig](../actions.md#route53:getqueryloggingconfig) |

| `s3` | [s3:GetBucketAcl](../actions.md#s3:getbucketacl) |

| `s3` | [s3:GetBucketLogging](../actions.md#s3:getbucketlogging) |

| `s3` | [s3:GetBucketOwnershipControls](../actions.md#s3:getbucketownershipcontrols) |

| `s3` | [s3:GetBucketPolicy](../actions.md#s3:getbucketpolicy) |

| `s3` | [s3:GetBucketPublicAccessBlock](../actions.md#s3:getbucketpublicaccessblock) |

| `s3` | [s3:GetBucketTagging](../actions.md#s3:getbuckettagging) |

| `s3` | [s3:GetBucketVersioning](../actions.md#s3:getbucketversioning) |

| `s3` | [s3:GetEncryptionConfiguration](../actions.md#s3:getencryptionconfiguration) |

| `s3` | [s3:GetLifecycleConfiguration](../actions.md#s3:getlifecycleconfiguration) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `sagemaker` | [sagemaker:DescribeAlgorithm](../actions.md#sagemaker:describealgorithm) |

| `sagemaker` | [sagemaker:DescribeDomain](../actions.md#sagemaker:describedomain) |

| `sagemaker` | [sagemaker:DescribeEndpoint](../actions.md#sagemaker:describeendpoint) |

| `sagemaker` | [sagemaker:DescribeEndpointConfig](../actions.md#sagemaker:describeendpointconfig) |

| `sagemaker` | [sagemaker:DescribeFlowDefinition](../actions.md#sagemaker:describeflowdefinition) |

| `sagemaker` | [sagemaker:DescribeHumanTaskUi](../actions.md#sagemaker:describehumantaskui) |

| `sagemaker` | [sagemaker:DescribeLabelingJob](../actions.md#sagemaker:describelabelingjob) |

| `sagemaker` | [sagemaker:DescribeModel](../actions.md#sagemaker:describemodel) |

| `sagemaker` | [sagemaker:DescribeModelBiasJobDefinition](../actions.md#sagemaker:describemodelbiasjobdefinition) |

| `sagemaker` | [sagemaker:DescribeModelCard](../actions.md#sagemaker:describemodelcard) |

| `sagemaker` | [sagemaker:DescribeModelQualityJobDefinition](../actions.md#sagemaker:describemodelqualityjobdefinition) |

| `sagemaker` | [sagemaker:DescribeTrainingJob](../actions.md#sagemaker:describetrainingjob) |

| `sagemaker` | [sagemaker:DescribeUserProfile](../actions.md#sagemaker:describeuserprofile) |

| `sagemaker` | [sagemaker:ListAlgorithms](../actions.md#sagemaker:listalgorithms) |

| `sagemaker` | [sagemaker:ListDomains](../actions.md#sagemaker:listdomains) |

| `sagemaker` | [sagemaker:ListEndpointConfigs](../actions.md#sagemaker:listendpointconfigs) |

| `sagemaker` | [sagemaker:ListEndpoints](../actions.md#sagemaker:listendpoints) |

| `sagemaker` | [sagemaker:ListFlowDefinitions](../actions.md#sagemaker:listflowdefinitions) |

| `sagemaker` | [sagemaker:ListHumanTaskUis](../actions.md#sagemaker:listhumantaskuis) |

| `sagemaker` | [sagemaker:ListLabelingJobs](../actions.md#sagemaker:listlabelingjobs) |

| `sagemaker` | [sagemaker:ListModelBiasJobDefinitions](../actions.md#sagemaker:listmodelbiasjobdefinitions) |

| `sagemaker` | [sagemaker:ListModelCards](../actions.md#sagemaker:listmodelcards) |

| `sagemaker` | [sagemaker:ListModelQualityJobDefinitions](../actions.md#sagemaker:listmodelqualityjobdefinitions) |

| `sagemaker` | [sagemaker:ListModels](../actions.md#sagemaker:listmodels) |

| `sagemaker` | [sagemaker:ListMonitoringAlerts](../actions.md#sagemaker:listmonitoringalerts) |

| `sagemaker` | [sagemaker:ListMonitoringSchedules](../actions.md#sagemaker:listmonitoringschedules) |

| `sagemaker` | [sagemaker:ListTrainingJobs](../actions.md#sagemaker:listtrainingjobs) |

| `sagemaker` | [sagemaker:ListUserProfiles](../actions.md#sagemaker:listuserprofiles) |

| `secretsmanager` | [secretsmanager:DescribeSecret](../actions.md#secretsmanager:describesecret) |

| `secretsmanager` | [secretsmanager:ListSecrets](../actions.md#secretsmanager:listsecrets) |

| `securityhub` | [securityhub:DescribeStandards](../actions.md#securityhub:describestandards) |

| `sns` | [sns:ListTagsForResource](../actions.md#sns:listtagsforresource) |

| `sns` | [sns:ListTopics](../actions.md#sns:listtopics) |

| `sqs` | [sqs:ListQueues](../actions.md#sqs:listqueues) |

| `waf` | [waf:GetRule](../actions.md#waf:getrule) |

| `waf` | [waf:GetRuleGroup](../actions.md#waf:getrulegroup) |

| `waf` | [waf:ListActivatedRulesInRuleGroup](../actions.md#waf:listactivatedrulesinrulegroup) |

| `waf` | [waf:ListRuleGroups](../actions.md#waf:listrulegroups) |

| `waf` | [waf:ListRules](../actions.md#waf:listrules) |

| `waf` | [waf:ListWebAcls](../actions.md#waf:listwebacls) |

| `waf-regional` | [waf-regional:GetLoggingConfiguration](../actions.md#waf-regional:getloggingconfiguration) |

| `waf-regional` | [waf-regional:GetRule](../actions.md#waf-regional:getrule) |

| `waf-regional` | [waf-regional:GetWebAcl](../actions.md#waf-regional:getwebacl) |

| `waf-regional` | [waf-regional:ListRuleGroups](../actions.md#waf-regional:listrulegroups) |

| `waf-regional` | [waf-regional:ListRules](../actions.md#waf-regional:listrules) |

| `waf-regional` | [waf-regional:ListSubscribedRuleGroups](../actions.md#waf-regional:listsubscribedrulegroups) |

| `waf-regional` | [waf-regional:ListWebACLs](../actions.md#waf-regional:listwebacls) |

| `wafv2` | [wafv2:ListWebAcls](../actions.md#wafv2:listwebacls) |
