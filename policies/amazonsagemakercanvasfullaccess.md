# Policy: AmazonSageMakerCanvasFullAccess

ARN: `arn:aws:iam::aws:policy/AmazonSageMakerCanvasFullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| quicksight |
| glue |
| athena |
| secretsmanager |
| cloudwatch |
| redshift-data |
| logs |
| application-autoscaling |
| emr-serverless |
| forecast |
| iam |
| sagemaker |
| rds |
| redshift |
| ecr |
| s3 |
| ec2 |
| kms |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `application-autoscaling` | [application-autoscaling:DescribeScalingActivities](../actions.md#application-autoscaling:describescalingactivities) |

| `application-autoscaling` | [application-autoscaling:PutScalingPolicy](../actions.md#application-autoscaling:putscalingpolicy) |

| `application-autoscaling` | [application-autoscaling:RegisterScalableTarget](../actions.md#application-autoscaling:registerscalabletarget) |

| `athena` | [athena:ListDataCatalogs](../actions.md#athena:listdatacatalogs) |

| `athena` | [athena:ListDatabases](../actions.md#athena:listdatabases) |

| `athena` | [athena:ListTableMetadata](../actions.md#athena:listtablemetadata) |

| `cloudwatch` | [cloudwatch:DeleteAlarms](../actions.md#cloudwatch:deletealarms) |

| `cloudwatch` | [cloudwatch:DescribeAlarms](../actions.md#cloudwatch:describealarms) |

| `cloudwatch` | [cloudwatch:PutMetricAlarm](../actions.md#cloudwatch:putmetricalarm) |

| `ec2` | [ec2:CreateVpcEndpoint](../actions.md#ec2:createvpcendpoint) |

| `ec2` | [ec2:DescribeSecurityGroups](../actions.md#ec2:describesecuritygroups) |

| `ec2` | [ec2:DescribeSubnets](../actions.md#ec2:describesubnets) |

| `ec2` | [ec2:DescribeVpcEndpointServices](../actions.md#ec2:describevpcendpointservices) |

| `ec2` | [ec2:DescribeVpcEndpoints](../actions.md#ec2:describevpcendpoints) |

| `ec2` | [ec2:DescribeVpcs](../actions.md#ec2:describevpcs) |

| `ecr` | [ecr:BatchGetImage](../actions.md#ecr:batchgetimage) |

| `ecr` | [ecr:GetAuthorizationToken](../actions.md#ecr:getauthorizationtoken) |

| `ecr` | [ecr:GetDownloadUrlForLayer](../actions.md#ecr:getdownloadurlforlayer) |

| `emr-serverless` | [emr-serverless:CancelJobRun](../actions.md#emr-serverless:canceljobrun) |

| `emr-serverless` | [emr-serverless:CreateApplication](../actions.md#emr-serverless:createapplication) |

| `emr-serverless` | [emr-serverless:GetApplication](../actions.md#emr-serverless:getapplication) |

| `emr-serverless` | [emr-serverless:GetJobRun](../actions.md#emr-serverless:getjobrun) |

| `emr-serverless` | [emr-serverless:ListApplications](../actions.md#emr-serverless:listapplications) |

| `emr-serverless` | [emr-serverless:ListJobRuns](../actions.md#emr-serverless:listjobruns) |

| `emr-serverless` | [emr-serverless:StartApplication](../actions.md#emr-serverless:startapplication) |

| `emr-serverless` | [emr-serverless:StartJobRun](../actions.md#emr-serverless:startjobrun) |

| `emr-serverless` | [emr-serverless:StopApplication](../actions.md#emr-serverless:stopapplication) |

| `emr-serverless` | [emr-serverless:TagResource](../actions.md#emr-serverless:tagresource) |

| `emr-serverless` | [emr-serverless:UpdateApplication](../actions.md#emr-serverless:updateapplication) |

| `forecast` | [forecast:CreateAutoPredictor](../actions.md#forecast:createautopredictor) |

| `forecast` | [forecast:CreateDataset](../actions.md#forecast:createdataset) |

| `forecast` | [forecast:CreateDatasetGroup](../actions.md#forecast:createdatasetgroup) |

| `forecast` | [forecast:CreateDatasetImportJob](../actions.md#forecast:createdatasetimportjob) |

| `forecast` | [forecast:CreateExplainability](../actions.md#forecast:createexplainability) |

| `forecast` | [forecast:CreateExplainabilityExport](../actions.md#forecast:createexplainabilityexport) |

| `forecast` | [forecast:CreateForecast](../actions.md#forecast:createforecast) |

| `forecast` | [forecast:CreateForecastEndpoint](../actions.md#forecast:createforecastendpoint) |

| `forecast` | [forecast:CreateForecastExportJob](../actions.md#forecast:createforecastexportjob) |

| `forecast` | [forecast:CreatePredictor](../actions.md#forecast:createpredictor) |

| `forecast` | [forecast:CreatePredictorBacktestExportJob](../actions.md#forecast:createpredictorbacktestexportjob) |

| `forecast` | [forecast:DeleteResourceTree](../actions.md#forecast:deleteresourcetree) |

| `forecast` | [forecast:DescribeAutoPredictor](../actions.md#forecast:describeautopredictor) |

| `forecast` | [forecast:DescribeDataset](../actions.md#forecast:describedataset) |

| `forecast` | [forecast:DescribeDatasetImportJob](../actions.md#forecast:describedatasetimportjob) |

| `forecast` | [forecast:DescribeExplainability](../actions.md#forecast:describeexplainability) |

| `forecast` | [forecast:DescribeExplainabilityExport](../actions.md#forecast:describeexplainabilityexport) |

| `forecast` | [forecast:DescribeForecast](../actions.md#forecast:describeforecast) |

| `forecast` | [forecast:DescribeForecastEndpoint](../actions.md#forecast:describeforecastendpoint) |

| `forecast` | [forecast:DescribeForecastExportJob](../actions.md#forecast:describeforecastexportjob) |

| `forecast` | [forecast:DescribePredictor](../actions.md#forecast:describepredictor) |

| `forecast` | [forecast:DescribePredictorBacktestExportJob](../actions.md#forecast:describepredictorbacktestexportjob) |

| `forecast` | [forecast:GetAccuracyMetrics](../actions.md#forecast:getaccuracymetrics) |

| `forecast` | [forecast:GetRecentForecastContext](../actions.md#forecast:getrecentforecastcontext) |

| `forecast` | [forecast:InvokeForecastEndpoint](../actions.md#forecast:invokeforecastendpoint) |

| `forecast` | [forecast:TagResource](../actions.md#forecast:tagresource) |

| `glue` | [glue:GetDatabases](../actions.md#glue:getdatabases) |

| `glue` | [glue:GetPartitions](../actions.md#glue:getpartitions) |

| `glue` | [glue:GetTables](../actions.md#glue:gettables) |

| `glue` | [glue:SearchTables](../actions.md#glue:searchtables) |

| `iam` | [iam:CreateServiceLinkedRole](../actions.md#iam:createservicelinkedrole) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `kms` | [kms:DescribeKey](../actions.md#kms:describekey) |

| `logs` | [logs:CreateLogGroup](../actions.md#logs:createloggroup) |

| `logs` | [logs:CreateLogStream](../actions.md#logs:createlogstream) |

| `logs` | [logs:PutLogEvents](../actions.md#logs:putlogevents) |

| `quicksight` | [quicksight:ListNamespaces](../actions.md#quicksight:listnamespaces) |

| `rds` | [rds:DescribeDBInstances](../actions.md#rds:describedbinstances) |

| `redshift` | [redshift:GetClusterCredentials](../actions.md#redshift:getclustercredentials) |

| `redshift-data` | [redshift-data:CancelStatement](../actions.md#redshift-data:cancelstatement) |

| `redshift-data` | [redshift-data:DescribeStatement](../actions.md#redshift-data:describestatement) |

| `redshift-data` | [redshift-data:DescribeTable](../actions.md#redshift-data:describetable) |

| `redshift-data` | [redshift-data:ExecuteStatement](../actions.md#redshift-data:executestatement) |

| `redshift-data` | [redshift-data:GetStatementResult](../actions.md#redshift-data:getstatementresult) |

| `redshift-data` | [redshift-data:ListSchemas](../actions.md#redshift-data:listschemas) |

| `redshift-data` | [redshift-data:ListTables](../actions.md#redshift-data:listtables) |

| `s3` | [s3:CreateBucket](../actions.md#s3:createbucket) |

| `s3` | [s3:DeleteObject](../actions.md#s3:deleteobject) |

| `s3` | [s3:GetBucketCors](../actions.md#s3:getbucketcors) |

| `s3` | [s3:GetBucketLocation](../actions.md#s3:getbucketlocation) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:PutObject](../actions.md#s3:putobject) |

| `sagemaker` | [sagemaker:AddTags](../actions.md#sagemaker:addtags) |

| `sagemaker` | [sagemaker:CreateAutoMLJob](../actions.md#sagemaker:createautomljob) |

| `sagemaker` | [sagemaker:CreateAutoMLJobV2](../actions.md#sagemaker:createautomljobv2) |

| `sagemaker` | [sagemaker:CreateCompilationJob](../actions.md#sagemaker:createcompilationjob) |

| `sagemaker` | [sagemaker:CreateEndpoint](../actions.md#sagemaker:createendpoint) |

| `sagemaker` | [sagemaker:CreateEndpointConfig](../actions.md#sagemaker:createendpointconfig) |

| `sagemaker` | [sagemaker:CreateModel](../actions.md#sagemaker:createmodel) |

| `sagemaker` | [sagemaker:CreateModelPackage](../actions.md#sagemaker:createmodelpackage) |

| `sagemaker` | [sagemaker:CreateModelPackageGroup](../actions.md#sagemaker:createmodelpackagegroup) |

| `sagemaker` | [sagemaker:CreateProcessingJob](../actions.md#sagemaker:createprocessingjob) |

| `sagemaker` | [sagemaker:CreateTrainingJob](../actions.md#sagemaker:createtrainingjob) |

| `sagemaker` | [sagemaker:CreateTransformJob](../actions.md#sagemaker:createtransformjob) |

| `sagemaker` | [sagemaker:DeleteApp](../actions.md#sagemaker:deleteapp) |

| `sagemaker` | [sagemaker:DeleteEndpoint](../actions.md#sagemaker:deleteendpoint) |

| `sagemaker` | [sagemaker:DeleteEndpointConfig](../actions.md#sagemaker:deleteendpointconfig) |

| `sagemaker` | [sagemaker:DeleteModel](../actions.md#sagemaker:deletemodel) |

| `sagemaker` | [sagemaker:DescribeAutoMLJob](../actions.md#sagemaker:describeautomljob) |

| `sagemaker` | [sagemaker:DescribeAutoMLJobV2](../actions.md#sagemaker:describeautomljobv2) |

| `sagemaker` | [sagemaker:DescribeCompilationJob](../actions.md#sagemaker:describecompilationjob) |

| `sagemaker` | [sagemaker:DescribeDomain](../actions.md#sagemaker:describedomain) |

| `sagemaker` | [sagemaker:DescribeEndpoint](../actions.md#sagemaker:describeendpoint) |

| `sagemaker` | [sagemaker:DescribeEndpointConfig](../actions.md#sagemaker:describeendpointconfig) |

| `sagemaker` | [sagemaker:DescribeEndpointConfig](../actions.md#sagemaker:describeendpointconfig) |

| `sagemaker` | [sagemaker:DescribeModel](../actions.md#sagemaker:describemodel) |

| `sagemaker` | [sagemaker:DescribeModelPackage](../actions.md#sagemaker:describemodelpackage) |

| `sagemaker` | [sagemaker:DescribeModelPackageGroup](../actions.md#sagemaker:describemodelpackagegroup) |

| `sagemaker` | [sagemaker:DescribeProcessingJob](../actions.md#sagemaker:describeprocessingjob) |

| `sagemaker` | [sagemaker:DescribeTrainingJob](../actions.md#sagemaker:describetrainingjob) |

| `sagemaker` | [sagemaker:DescribeTransformJob](../actions.md#sagemaker:describetransformjob) |

| `sagemaker` | [sagemaker:DescribeUserProfile](../actions.md#sagemaker:describeuserprofile) |

| `sagemaker` | [sagemaker:InvokeEndpoint](../actions.md#sagemaker:invokeendpoint) |

| `sagemaker` | [sagemaker:InvokeEndpointAsync](../actions.md#sagemaker:invokeendpointasync) |

| `sagemaker` | [sagemaker:ListCandidatesForAutoMLJob](../actions.md#sagemaker:listcandidatesforautomljob) |

| `sagemaker` | [sagemaker:ListEndpoints](../actions.md#sagemaker:listendpoints) |

| `sagemaker` | [sagemaker:ListModelPackageGroups](../actions.md#sagemaker:listmodelpackagegroups) |

| `sagemaker` | [sagemaker:ListModelPackages](../actions.md#sagemaker:listmodelpackages) |

| `sagemaker` | [sagemaker:ListTags](../actions.md#sagemaker:listtags) |

| `sagemaker` | [sagemaker:StopAutoMLJob](../actions.md#sagemaker:stopautomljob) |

| `sagemaker` | [sagemaker:StopTrainingJob](../actions.md#sagemaker:stoptrainingjob) |

| `sagemaker` | [sagemaker:StopTransformJob](../actions.md#sagemaker:stoptransformjob) |

| `sagemaker` | [sagemaker:UpdateEndpointWeightsAndCapacities](../actions.md#sagemaker:updateendpointweightsandcapacities) |

| `secretsmanager` | [secretsmanager:CreateSecret](../actions.md#secretsmanager:createsecret) |

| `secretsmanager` | [secretsmanager:DescribeSecret](../actions.md#secretsmanager:describesecret) |

| `secretsmanager` | [secretsmanager:DescribeSecret](../actions.md#secretsmanager:describesecret) |

| `secretsmanager` | [secretsmanager:GetSecretValue](../actions.md#secretsmanager:getsecretvalue) |

| `secretsmanager` | [secretsmanager:GetSecretValue](../actions.md#secretsmanager:getsecretvalue) |

| `secretsmanager` | [secretsmanager:PutResourcePolicy](../actions.md#secretsmanager:putresourcepolicy) |
