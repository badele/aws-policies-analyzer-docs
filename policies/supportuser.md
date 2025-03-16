# Policy: SupportUser

ARN: `arn:aws:iam::aws:policy/job-function/SupportUser`

## Attached Roles

## Attached Services

| Service |
|---------|
| discovery |
| ssm |
| workspaces |
| support |
| elasticloadbalancing |
| cognito-identity |
| aws-marketplace |
| ecs |
| rds |
| acm-pca |
| cloudfront |
| kms |
| kinesisanalytics |
| dms |
| inspector |
| iot |
| servicecatalog |
| cloudformation |
| machinelearning |
| waf |
| lambda |
| route53domains |
| workdocs |
| firehose |
| logs |
| sqs |
| glacier |
| ds |
| devicefarm |
| cognito-sync |
| ec2 |
| es |
| s3 |
| autoscaling |
| elasticbeanstalk |
| events |
| ses |
| cloudtrail |
| route53 |
| config |
| codecommit |
| storagegateway |
| iam |
| codedeploy |
| workmail |
| elasticmapreduce |
| gamelift |
| apigateway |
| directconnect |
| elastictranscoder |
| ecr |
| elasticfilesystem |
| opsworks |
| sns |
| cognito-idp |
| swf |
| cloudsearch |
| cloudwatch |
| acm |
| kinesis |
| datapipeline |
| elasticache |
| codepipeline |
| sdb |
| importexport |
| redshift |
| dynamodb |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `acm` | [acm:DescribeCertificate](../actions.md#acm:describecertificate) |

| `acm` | [acm:GetCertificate](../actions.md#acm:getcertificate) |

| `acm` | [acm:List*](../actions.md#acm:listall) |

| `acm-pca` | [acm-pca:DescribeCertificateAuthority](../actions.md#acm-pca:describecertificateauthority) |

| `acm-pca` | [acm-pca:ListCertificateAuthorities](../actions.md#acm-pca:listcertificateauthorities) |

| `apigateway` | [apigateway:GET](../actions.md#apigateway:get) |

| `autoscaling` | [autoscaling:Describe*](../actions.md#autoscaling:describeall) |

| `aws-marketplace` | [aws-marketplace:ViewSubscriptions](../actions.md#aws-marketplace:viewsubscriptions) |

| `cloudformation` | [cloudformation:Describe*](../actions.md#cloudformation:describeall) |

| `cloudformation` | [cloudformation:EstimateTemplateCost](../actions.md#cloudformation:estimatetemplatecost) |

| `cloudformation` | [cloudformation:Get*](../actions.md#cloudformation:getall) |

| `cloudformation` | [cloudformation:List*](../actions.md#cloudformation:listall) |

| `cloudfront` | [cloudfront:Get*](../actions.md#cloudfront:getall) |

| `cloudfront` | [cloudfront:List*](../actions.md#cloudfront:listall) |

| `cloudsearch` | [cloudsearch:Describe*](../actions.md#cloudsearch:describeall) |

| `cloudsearch` | [cloudsearch:List*](../actions.md#cloudsearch:listall) |

| `cloudtrail` | [cloudtrail:DescribeTrails](../actions.md#cloudtrail:describetrails) |

| `cloudtrail` | [cloudtrail:GetTrailStatus](../actions.md#cloudtrail:gettrailstatus) |

| `cloudtrail` | [cloudtrail:ListPublicKeys](../actions.md#cloudtrail:listpublickeys) |

| `cloudtrail` | [cloudtrail:ListTags](../actions.md#cloudtrail:listtags) |

| `cloudtrail` | [cloudtrail:LookupEvents](../actions.md#cloudtrail:lookupevents) |

| `cloudwatch` | [cloudwatch:Describe*](../actions.md#cloudwatch:describeall) |

| `cloudwatch` | [cloudwatch:Get*](../actions.md#cloudwatch:getall) |

| `cloudwatch` | [cloudwatch:List*](../actions.md#cloudwatch:listall) |

| `codecommit` | [codecommit:BatchGetRepositories](../actions.md#codecommit:batchgetrepositories) |

| `codecommit` | [codecommit:Get*](../actions.md#codecommit:getall) |

| `codecommit` | [codecommit:List*](../actions.md#codecommit:listall) |

| `codedeploy` | [codedeploy:Batch*](../actions.md#codedeploy:batchall) |

| `codedeploy` | [codedeploy:Get*](../actions.md#codedeploy:getall) |

| `codedeploy` | [codedeploy:List*](../actions.md#codedeploy:listall) |

| `codepipeline` | [codepipeline:AcknowledgeJob](../actions.md#codepipeline:acknowledgejob) |

| `codepipeline` | [codepipeline:AcknowledgeThirdPartyJob](../actions.md#codepipeline:acknowledgethirdpartyjob) |

| `codepipeline` | [codepipeline:GetPipeline](../actions.md#codepipeline:getpipeline) |

| `codepipeline` | [codepipeline:GetPipelineState](../actions.md#codepipeline:getpipelinestate) |

| `codepipeline` | [codepipeline:ListActionTypes](../actions.md#codepipeline:listactiontypes) |

| `codepipeline` | [codepipeline:ListPipelines](../actions.md#codepipeline:listpipelines) |

| `codepipeline` | [codepipeline:PollForJobs](../actions.md#codepipeline:pollforjobs) |

| `codepipeline` | [codepipeline:PollForThirdPartyJobs](../actions.md#codepipeline:pollforthirdpartyjobs) |

| `cognito-identity` | [cognito-identity:Describe*](../actions.md#cognito-identity:describeall) |

| `cognito-identity` | [cognito-identity:List*](../actions.md#cognito-identity:listall) |

| `cognito-identity` | [cognito-identity:LookupDeveloperIdentity](../actions.md#cognito-identity:lookupdeveloperidentity) |

| `cognito-idp` | [cognito-idp:DescribeResourceServer](../actions.md#cognito-idp:describeresourceserver) |

| `cognito-idp` | [cognito-idp:DescribeRiskConfiguration](../actions.md#cognito-idp:describeriskconfiguration) |

| `cognito-idp` | [cognito-idp:DescribeUserImportJob](../actions.md#cognito-idp:describeuserimportjob) |

| `cognito-idp` | [cognito-idp:DescribeUserPool](../actions.md#cognito-idp:describeuserpool) |

| `cognito-idp` | [cognito-idp:DescribeUserPoolDomain](../actions.md#cognito-idp:describeuserpooldomain) |

| `cognito-idp` | [cognito-idp:List*](../actions.md#cognito-idp:listall) |

| `cognito-sync` | [cognito-sync:Describe*](../actions.md#cognito-sync:describeall) |

| `cognito-sync` | [cognito-sync:GetBulkPublishDetails](../actions.md#cognito-sync:getbulkpublishdetails) |

| `cognito-sync` | [cognito-sync:GetCognitoEvents](../actions.md#cognito-sync:getcognitoevents) |

| `cognito-sync` | [cognito-sync:GetIdentityPoolConfiguration](../actions.md#cognito-sync:getidentitypoolconfiguration) |

| `cognito-sync` | [cognito-sync:List*](../actions.md#cognito-sync:listall) |

| `config` | [config:DescribeConfigRuleEvaluationStatus](../actions.md#config:describeconfigruleevaluationstatus) |

| `config` | [config:DescribeConfigRules](../actions.md#config:describeconfigrules) |

| `config` | [config:DescribeConfigurationRecorderStatus](../actions.md#config:describeconfigurationrecorderstatus) |

| `config` | [config:DescribeConfigurationRecorders](../actions.md#config:describeconfigurationrecorders) |

| `config` | [config:DescribeDeliveryChannelStatus](../actions.md#config:describedeliverychannelstatus) |

| `config` | [config:DescribeDeliveryChannels](../actions.md#config:describedeliverychannels) |

| `config` | [config:GetResourceConfigHistory](../actions.md#config:getresourceconfighistory) |

| `config` | [config:ListDiscoveredResources](../actions.md#config:listdiscoveredresources) |

| `datapipeline` | [datapipeline:DescribeObjects](../actions.md#datapipeline:describeobjects) |

| `datapipeline` | [datapipeline:DescribePipelines](../actions.md#datapipeline:describepipelines) |

| `datapipeline` | [datapipeline:GetPipelineDefinition](../actions.md#datapipeline:getpipelinedefinition) |

| `datapipeline` | [datapipeline:ListPipelines](../actions.md#datapipeline:listpipelines) |

| `datapipeline` | [datapipeline:QueryObjects](../actions.md#datapipeline:queryobjects) |

| `datapipeline` | [datapipeline:ReportTaskProgress](../actions.md#datapipeline:reporttaskprogress) |

| `datapipeline` | [datapipeline:ReportTaskRunnerHeartbeat](../actions.md#datapipeline:reporttaskrunnerheartbeat) |

| `devicefarm` | [devicefarm:Get*](../actions.md#devicefarm:getall) |

| `devicefarm` | [devicefarm:List*](../actions.md#devicefarm:listall) |

| `directconnect` | [directconnect:Describe*](../actions.md#directconnect:describeall) |

| `discovery` | [discovery:Describe*](../actions.md#discovery:describeall) |

| `discovery` | [discovery:ListConfigurations](../actions.md#discovery:listconfigurations) |

| `dms` | [dms:Describe*](../actions.md#dms:describeall) |

| `dms` | [dms:List*](../actions.md#dms:listall) |

| `ds` | [ds:DescribeDirectories](../actions.md#ds:describedirectories) |

| `ds` | [ds:DescribeSnapshots](../actions.md#ds:describesnapshots) |

| `ds` | [ds:GetDirectoryLimits](../actions.md#ds:getdirectorylimits) |

| `ds` | [ds:GetSnapshotLimits](../actions.md#ds:getsnapshotlimits) |

| `ds` | [ds:ListAuthorizedApplications](../actions.md#ds:listauthorizedapplications) |

| `dynamodb` | [dynamodb:DescribeLimits](../actions.md#dynamodb:describelimits) |

| `dynamodb` | [dynamodb:DescribeTable](../actions.md#dynamodb:describetable) |

| `dynamodb` | [dynamodb:ListTables](../actions.md#dynamodb:listtables) |

| `ec2` | [ec2:Describe*](../actions.md#ec2:describeall) |

| `ec2` | [ec2:DescribeHosts](../actions.md#ec2:describehosts) |

| `ec2` | [ec2:DescribeIdFormat](../actions.md#ec2:describeidformat) |

| `ec2` | [ec2:DescribeInstanceAttribute](../actions.md#ec2:describeinstanceattribute) |

| `ec2` | [ec2:DescribeNatGateways](../actions.md#ec2:describenatgateways) |

| `ec2` | [ec2:DescribeReservedInstancesModifications](../actions.md#ec2:describereservedinstancesmodifications) |

| `ec2` | [ec2:DescribeTags](../actions.md#ec2:describetags) |

| `ec2` | [ec2:SearchLocalGatewayRoutes](../actions.md#ec2:searchlocalgatewayroutes) |

| `ec2` | [ec2:describeIdentityIdFormat](../actions.md#ec2:describeidentityidformat) |

| `ecr` | [ecr:BatchCheckLayerAvailability](../actions.md#ecr:batchchecklayeravailability) |

| `ecr` | [ecr:DescribeRepositories](../actions.md#ecr:describerepositories) |

| `ecr` | [ecr:GetRepositoryPolicy](../actions.md#ecr:getrepositorypolicy) |

| `ecr` | [ecr:ListImages](../actions.md#ecr:listimages) |

| `ecs` | [ecs:Describe*](../actions.md#ecs:describeall) |

| `ecs` | [ecs:List*](../actions.md#ecs:listall) |

| `elasticache` | [elasticache:Describe*](../actions.md#elasticache:describeall) |

| `elasticache` | [elasticache:List*](../actions.md#elasticache:listall) |

| `elasticbeanstalk` | [elasticbeanstalk:Check*](../actions.md#elasticbeanstalk:checkall) |

| `elasticbeanstalk` | [elasticbeanstalk:Describe*](../actions.md#elasticbeanstalk:describeall) |

| `elasticbeanstalk` | [elasticbeanstalk:List*](../actions.md#elasticbeanstalk:listall) |

| `elasticbeanstalk` | [elasticbeanstalk:RequestEnvironmentInfo](../actions.md#elasticbeanstalk:requestenvironmentinfo) |

| `elasticbeanstalk` | [elasticbeanstalk:RetrieveEnvironmentInfo](../actions.md#elasticbeanstalk:retrieveenvironmentinfo) |

| `elasticbeanstalk` | [elasticbeanstalk:ValidateConfigurationSettings](../actions.md#elasticbeanstalk:validateconfigurationsettings) |

| `elasticfilesystem` | [elasticfilesystem:Describe*](../actions.md#elasticfilesystem:describeall) |

| `elasticfilesystem` | [elasticfilesystem:DescribeFileSystems](../actions.md#elasticfilesystem:describefilesystems) |

| `elasticloadbalancing` | [elasticloadbalancing:Describe*](../actions.md#elasticloadbalancing:describeall) |

| `elasticmapreduce` | [elasticmapreduce:Describe*](../actions.md#elasticmapreduce:describeall) |

| `elasticmapreduce` | [elasticmapreduce:List*](../actions.md#elasticmapreduce:listall) |

| `elastictranscoder` | [elastictranscoder:List*](../actions.md#elastictranscoder:listall) |

| `elastictranscoder` | [elastictranscoder:ReadJob](../actions.md#elastictranscoder:readjob) |

| `es` | [es:Describe*](../actions.md#es:describeall) |

| `es` | [es:ESHttpGet](../actions.md#es:eshttpget) |

| `es` | [es:ESHttpHead](../actions.md#es:eshttphead) |

| `es` | [es:List*](../actions.md#es:listall) |

| `events` | [events:DescribeRule](../actions.md#events:describerule) |

| `events` | [events:List*](../actions.md#events:listall) |

| `events` | [events:TestEventPattern](../actions.md#events:testeventpattern) |

| `firehose` | [firehose:Describe*](../actions.md#firehose:describeall) |

| `firehose` | [firehose:List*](../actions.md#firehose:listall) |

| `gamelift` | [gamelift:Describe*](../actions.md#gamelift:describeall) |

| `gamelift` | [gamelift:List*](../actions.md#gamelift:listall) |

| `glacier` | [glacier:DescribeJob](../actions.md#glacier:describejob) |

| `glacier` | [glacier:DescribeVault](../actions.md#glacier:describevault) |

| `glacier` | [glacier:Get*](../actions.md#glacier:getall) |

| `glacier` | [glacier:List*](../actions.md#glacier:listall) |

| `glacier` | [glacier:ListVaults](../actions.md#glacier:listvaults) |

| `iam` | [iam:GenerateCredentialReport](../actions.md#iam:generatecredentialreport) |

| `iam` | [iam:GenerateServiceLastAccessedDetails](../actions.md#iam:generateservicelastaccesseddetails) |

| `iam` | [iam:Get*](../actions.md#iam:getall) |

| `iam` | [iam:List*](../actions.md#iam:listall) |

| `importexport` | [importexport:GetStatus](../actions.md#importexport:getstatus) |

| `importexport` | [importexport:ListJobs](../actions.md#importexport:listjobs) |

| `inspector` | [inspector:Describe*](../actions.md#inspector:describeall) |

| `inspector` | [inspector:List*](../actions.md#inspector:listall) |

| `iot` | [iot:Describe*](../actions.md#iot:describeall) |

| `iot` | [iot:Get*](../actions.md#iot:getall) |

| `iot` | [iot:List*](../actions.md#iot:listall) |

| `kinesis` | [kinesis:Describe*](../actions.md#kinesis:describeall) |

| `kinesis` | [kinesis:Get*](../actions.md#kinesis:getall) |

| `kinesis` | [kinesis:List*](../actions.md#kinesis:listall) |

| `kinesisanalytics` | [kinesisanalytics:DescribeApplication](../actions.md#kinesisanalytics:describeapplication) |

| `kinesisanalytics` | [kinesisanalytics:DiscoverInputSchema](../actions.md#kinesisanalytics:discoverinputschema) |

| `kinesisanalytics` | [kinesisanalytics:GetApplicationState](../actions.md#kinesisanalytics:getapplicationstate) |

| `kinesisanalytics` | [kinesisanalytics:ListApplications](../actions.md#kinesisanalytics:listapplications) |

| `kms` | [kms:Describe*](../actions.md#kms:describeall) |

| `kms` | [kms:Get*](../actions.md#kms:getall) |

| `kms` | [kms:List*](../actions.md#kms:listall) |

| `lambda` | [lambda:Get*](../actions.md#lambda:getall) |

| `lambda` | [lambda:List*](../actions.md#lambda:listall) |

| `logs` | [logs:Describe*](../actions.md#logs:describeall) |

| `logs` | [logs:TestMetricFilter](../actions.md#logs:testmetricfilter) |

| `machinelearning` | [machinelearning:Describe*](../actions.md#machinelearning:describeall) |

| `machinelearning` | [machinelearning:Get*](../actions.md#machinelearning:getall) |

| `opsworks` | [opsworks:Describe*](../actions.md#opsworks:describeall) |

| `rds` | [rds:Describe*](../actions.md#rds:describeall) |

| `rds` | [rds:ListTagsForResource](../actions.md#rds:listtagsforresource) |

| `redshift` | [redshift:Describe*](../actions.md#redshift:describeall) |

| `route53` | [route53:Get*](../actions.md#route53:getall) |

| `route53` | [route53:List*](../actions.md#route53:listall) |

| `route53domains` | [route53domains:CheckDomainAvailability](../actions.md#route53domains:checkdomainavailability) |

| `route53domains` | [route53domains:GetDomainDetail](../actions.md#route53domains:getdomaindetail) |

| `route53domains` | [route53domains:GetOperationDetail](../actions.md#route53domains:getoperationdetail) |

| `route53domains` | [route53domains:List*](../actions.md#route53domains:listall) |

| `s3` | [s3:List*](../actions.md#s3:listall) |

| `sdb` | [sdb:GetAttributes](../actions.md#sdb:getattributes) |

| `sdb` | [sdb:List*](../actions.md#sdb:listall) |

| `sdb` | [sdb:Select*](../actions.md#sdb:selectall) |

| `servicecatalog` | [servicecatalog:DescribeProduct](../actions.md#servicecatalog:describeproduct) |

| `servicecatalog` | [servicecatalog:DescribeProductView](../actions.md#servicecatalog:describeproductview) |

| `servicecatalog` | [servicecatalog:DescribeProvisioningParameters](../actions.md#servicecatalog:describeprovisioningparameters) |

| `servicecatalog` | [servicecatalog:DescribeRecord](../actions.md#servicecatalog:describerecord) |

| `servicecatalog` | [servicecatalog:ListLaunchPaths](../actions.md#servicecatalog:listlaunchpaths) |

| `servicecatalog` | [servicecatalog:ListRecordHistory](../actions.md#servicecatalog:listrecordhistory) |

| `servicecatalog` | [servicecatalog:ScanProvisionedProducts](../actions.md#servicecatalog:scanprovisionedproducts) |

| `servicecatalog` | [servicecatalog:SearchProducts](../actions.md#servicecatalog:searchproducts) |

| `ses` | [ses:Get*](../actions.md#ses:getall) |

| `ses` | [ses:List*](../actions.md#ses:listall) |

| `sns` | [sns:Get*](../actions.md#sns:getall) |

| `sns` | [sns:List*](../actions.md#sns:listall) |

| `sqs` | [sqs:GetQueueAttributes](../actions.md#sqs:getqueueattributes) |

| `sqs` | [sqs:GetQueueUrl](../actions.md#sqs:getqueueurl) |

| `sqs` | [sqs:ListQueues](../actions.md#sqs:listqueues) |

| `sqs` | [sqs:ReceiveMessage](../actions.md#sqs:receivemessage) |

| `ssm` | [ssm:Describe*](../actions.md#ssm:describeall) |

| `ssm` | [ssm:List*](../actions.md#ssm:listall) |

| `storagegateway` | [storagegateway:Describe*](../actions.md#storagegateway:describeall) |

| `storagegateway` | [storagegateway:List*](../actions.md#storagegateway:listall) |

| `support` | [support:*](../actions.md#support:all) |

| `swf` | [swf:Count*](../actions.md#swf:countall) |

| `swf` | [swf:Describe*](../actions.md#swf:describeall) |

| `swf` | [swf:Get*](../actions.md#swf:getall) |

| `swf` | [swf:List*](../actions.md#swf:listall) |

| `waf` | [waf:Get*](../actions.md#waf:getall) |

| `waf` | [waf:List*](../actions.md#waf:listall) |

| `workdocs` | [workdocs:Describe*](../actions.md#workdocs:describeall) |

| `workmail` | [workmail:Describe*](../actions.md#workmail:describeall) |

| `workmail` | [workmail:Get*](../actions.md#workmail:getall) |

| `workspaces` | [workspaces:Describe*](../actions.md#workspaces:describeall) |
