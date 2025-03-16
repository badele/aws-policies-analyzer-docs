# Policy: AmazonSageMakerCanvasDataPrepFullAccess

ARN: `arn:aws:iam::aws:policy/AmazonSageMakerCanvasDataPrepFullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| events |
| glue |
| athena |
| secretsmanager |
| emr-serverless |
| redshift-data |
| logs |
| iam |
| sagemaker |
| rds |
| elasticmapreduce |
| redshift |
| s3 |
| kms |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `athena` | [athena:GetQueryExecution](../actions.md#athena:getqueryexecution) |

| `athena` | [athena:GetQueryResults](../actions.md#athena:getqueryresults) |

| `athena` | [athena:ListDataCatalogs](../actions.md#athena:listdatacatalogs) |

| `athena` | [athena:ListDatabases](../actions.md#athena:listdatabases) |

| `athena` | [athena:ListTableMetadata](../actions.md#athena:listtablemetadata) |

| `athena` | [athena:StartQueryExecution](../actions.md#athena:startqueryexecution) |

| `athena` | [athena:StopQueryExecution](../actions.md#athena:stopqueryexecution) |

| `elasticmapreduce` | [elasticmapreduce:DescribeCluster](../actions.md#elasticmapreduce:describecluster) |

| `elasticmapreduce` | [elasticmapreduce:ListClusters](../actions.md#elasticmapreduce:listclusters) |

| `elasticmapreduce` | [elasticmapreduce:ListInstanceGroups](../actions.md#elasticmapreduce:listinstancegroups) |

| `emr-serverless` | [emr-serverless:CancelJobRun](../actions.md#emr-serverless:canceljobrun) |

| `emr-serverless` | [emr-serverless:CreateApplication](../actions.md#emr-serverless:createapplication) |

| `emr-serverless` | [emr-serverless:GetApplication](../actions.md#emr-serverless:getapplication) |

| `emr-serverless` | [emr-serverless:GetJobRun](../actions.md#emr-serverless:getjobrun) |

| `emr-serverless` | [emr-serverless:ListApplications](../actions.md#emr-serverless:listapplications) |

| `emr-serverless` | [emr-serverless:ListJobRuns](../actions.md#emr-serverless:listjobruns) |

| `emr-serverless` | [emr-serverless:StartJobRun](../actions.md#emr-serverless:startjobrun) |

| `emr-serverless` | [emr-serverless:TagResource](../actions.md#emr-serverless:tagresource) |

| `emr-serverless` | [emr-serverless:UpdateApplication](../actions.md#emr-serverless:updateapplication) |

| `events` | [events:DescribeRule](../actions.md#events:describerule) |

| `events` | [events:ListTagsForResource](../actions.md#events:listtagsforresource) |

| `events` | [events:PutRule](../actions.md#events:putrule) |

| `events` | [events:PutTargets](../actions.md#events:puttargets) |

| `events` | [events:TagResource](../actions.md#events:tagresource) |

| `glue` | [glue:GetDatabases](../actions.md#glue:getdatabases) |

| `glue` | [glue:GetTable](../actions.md#glue:gettable) |

| `glue` | [glue:GetTables](../actions.md#glue:gettables) |

| `glue` | [glue:SearchTables](../actions.md#glue:searchtables) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `kms` | [kms:DescribeKey](../actions.md#kms:describekey) |

| `kms` | [kms:ListAliases](../actions.md#kms:listaliases) |

| `logs` | [logs:CreateLogGroup](../actions.md#logs:createloggroup) |

| `logs` | [logs:CreateLogStream](../actions.md#logs:createlogstream) |

| `logs` | [logs:PutLogEvents](../actions.md#logs:putlogevents) |

| `rds` | [rds:DescribeDBInstances](../actions.md#rds:describedbinstances) |

| `redshift` | [redshift:GetClusterCredentials](../actions.md#redshift:getclustercredentials) |

| `redshift-data` | [redshift-data:CancelStatement](../actions.md#redshift-data:cancelstatement) |

| `redshift-data` | [redshift-data:DescribeStatement](../actions.md#redshift-data:describestatement) |

| `redshift-data` | [redshift-data:ExecuteStatement](../actions.md#redshift-data:executestatement) |

| `redshift-data` | [redshift-data:GetStatementResult](../actions.md#redshift-data:getstatementresult) |

| `redshift-data` | [redshift-data:ListSchemas](../actions.md#redshift-data:listschemas) |

| `redshift-data` | [redshift-data:ListTables](../actions.md#redshift-data:listtables) |

| `s3` | [s3:AbortMultipartUpload](../actions.md#s3:abortmultipartupload) |

| `s3` | [s3:DeleteObject](../actions.md#s3:deleteobject) |

| `s3` | [s3:GetBucketCors](../actions.md#s3:getbucketcors) |

| `s3` | [s3:GetBucketLocation](../actions.md#s3:getbucketlocation) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:PutObject](../actions.md#s3:putobject) |

| `sagemaker` | [sagemaker:AddTags](../actions.md#sagemaker:addtags) |

| `sagemaker` | [sagemaker:CreateFeatureGroup](../actions.md#sagemaker:createfeaturegroup) |

| `sagemaker` | [sagemaker:CreatePipeline](../actions.md#sagemaker:createpipeline) |

| `sagemaker` | [sagemaker:CreateProcessingJob](../actions.md#sagemaker:createprocessingjob) |

| `sagemaker` | [sagemaker:DeletePipeline](../actions.md#sagemaker:deletepipeline) |

| `sagemaker` | [sagemaker:DescribeFeatureGroup](../actions.md#sagemaker:describefeaturegroup) |

| `sagemaker` | [sagemaker:DescribePipeline](../actions.md#sagemaker:describepipeline) |

| `sagemaker` | [sagemaker:DescribePipelineExecution](../actions.md#sagemaker:describepipelineexecution) |

| `sagemaker` | [sagemaker:DescribeProcessingJob](../actions.md#sagemaker:describeprocessingjob) |

| `sagemaker` | [sagemaker:ListFeatureGroups](../actions.md#sagemaker:listfeaturegroups) |

| `sagemaker` | [sagemaker:ListPipelineExecutionSteps](../actions.md#sagemaker:listpipelineexecutionsteps) |

| `sagemaker` | [sagemaker:ListProcessingJobs](../actions.md#sagemaker:listprocessingjobs) |

| `sagemaker` | [sagemaker:StartPipelineExecution](../actions.md#sagemaker:startpipelineexecution) |

| `sagemaker` | [sagemaker:UpdatePipeline](../actions.md#sagemaker:updatepipeline) |

| `secretsmanager` | [secretsmanager:CreateSecret](../actions.md#secretsmanager:createsecret) |

| `secretsmanager` | [secretsmanager:DescribeSecret](../actions.md#secretsmanager:describesecret) |

| `secretsmanager` | [secretsmanager:GetSecretValue](../actions.md#secretsmanager:getsecretvalue) |
