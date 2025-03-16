# Policy: AmazonRedshiftAllCommandsFullAccess

ARN: `arn:aws:iam::aws:policy/AmazonRedshiftAllCommandsFullAccess`

## Attached Roles

## Attached Services

| Service |
|---------|
| glue |
| lambda |
| cloudwatch |
| secretsmanager |
| logs |
| iam |
| sagemaker |
| elasticmapreduce |
| ecr |
| s3 |
| dynamodb |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `cloudwatch` | [cloudwatch:PutMetricData](../actions.md#cloudwatch:putmetricdata) |

| `dynamodb` | [dynamodb:DescribeTable](../actions.md#dynamodb:describetable) |

| `dynamodb` | [dynamodb:Getitem](../actions.md#dynamodb:getitem) |

| `dynamodb` | [dynamodb:Scan](../actions.md#dynamodb:scan) |

| `ecr` | [ecr:BatchCheckLayerAvailability](../actions.md#ecr:batchchecklayeravailability) |

| `ecr` | [ecr:BatchGetImage](../actions.md#ecr:batchgetimage) |

| `ecr` | [ecr:GetAuthorizationToken](../actions.md#ecr:getauthorizationtoken) |

| `ecr` | [ecr:GetDownloadUrlForLayer](../actions.md#ecr:getdownloadurlforlayer) |

| `elasticmapreduce` | [elasticmapreduce:ListInstances](../actions.md#elasticmapreduce:listinstances) |

| `elasticmapreduce` | [elasticmapreduce:ListInstances](../actions.md#elasticmapreduce:listinstances) |

| `glue` | [glue:BatchCreatePartition](../actions.md#glue:batchcreatepartition) |

| `glue` | [glue:BatchDeletePartition](../actions.md#glue:batchdeletepartition) |

| `glue` | [glue:BatchDeleteTable](../actions.md#glue:batchdeletetable) |

| `glue` | [glue:BatchGetPartition](../actions.md#glue:batchgetpartition) |

| `glue` | [glue:CreateDatabase](../actions.md#glue:createdatabase) |

| `glue` | [glue:CreatePartition](../actions.md#glue:createpartition) |

| `glue` | [glue:CreateTable](../actions.md#glue:createtable) |

| `glue` | [glue:DeleteDatabase](../actions.md#glue:deletedatabase) |

| `glue` | [glue:DeletePartition](../actions.md#glue:deletepartition) |

| `glue` | [glue:DeleteTable](../actions.md#glue:deletetable) |

| `glue` | [glue:GetDatabase](../actions.md#glue:getdatabase) |

| `glue` | [glue:GetDatabases](../actions.md#glue:getdatabases) |

| `glue` | [glue:GetPartition](../actions.md#glue:getpartition) |

| `glue` | [glue:GetPartitions](../actions.md#glue:getpartitions) |

| `glue` | [glue:GetTable](../actions.md#glue:gettable) |

| `glue` | [glue:GetTables](../actions.md#glue:gettables) |

| `glue` | [glue:UpdateDatabase](../actions.md#glue:updatedatabase) |

| `glue` | [glue:UpdatePartition](../actions.md#glue:updatepartition) |

| `glue` | [glue:UpdateTable](../actions.md#glue:updatetable) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `lambda` | [lambda:InvokeFunction](../actions.md#lambda:invokefunction) |

| `logs` | [logs:CreateLogGroup](../actions.md#logs:createloggroup) |

| `logs` | [logs:CreateLogStream](../actions.md#logs:createlogstream) |

| `logs` | [logs:DescribeLogStreams](../actions.md#logs:describelogstreams) |

| `logs` | [logs:PutLogEvents](../actions.md#logs:putlogevents) |

| `s3` | [s3:AbortMultipartUpload](../actions.md#s3:abortmultipartupload) |

| `s3` | [s3:CreateBucket](../actions.md#s3:createbucket) |

| `s3` | [s3:DeleteObject](../actions.md#s3:deleteobject) |

| `s3` | [s3:GetBucketAcl](../actions.md#s3:getbucketacl) |

| `s3` | [s3:GetBucketCors](../actions.md#s3:getbucketcors) |

| `s3` | [s3:GetBucketLocation](../actions.md#s3:getbucketlocation) |

| `s3` | [s3:GetEncryptionConfiguration](../actions.md#s3:getencryptionconfiguration) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:GetObject](../actions.md#s3:getobject) |

| `s3` | [s3:ListAllMyBuckets](../actions.md#s3:listallmybuckets) |

| `s3` | [s3:ListBucket](../actions.md#s3:listbucket) |

| `s3` | [s3:ListBucketMultipartUploads](../actions.md#s3:listbucketmultipartuploads) |

| `s3` | [s3:ListMultipartUploadParts](../actions.md#s3:listmultipartuploadparts) |

| `s3` | [s3:PutBucketAcl](../actions.md#s3:putbucketacl) |

| `s3` | [s3:PutBucketCors](../actions.md#s3:putbucketcors) |

| `s3` | [s3:PutObject](../actions.md#s3:putobject) |

| `sagemaker` | [sagemaker:CreateAutoMLJob](../actions.md#sagemaker:createautomljob) |

| `sagemaker` | [sagemaker:CreateCompilationJob](../actions.md#sagemaker:createcompilationjob) |

| `sagemaker` | [sagemaker:CreateEndpoint](../actions.md#sagemaker:createendpoint) |

| `sagemaker` | [sagemaker:CreateModel](../actions.md#sagemaker:createmodel) |

| `sagemaker` | [sagemaker:CreateProcessingJob](../actions.md#sagemaker:createprocessingjob) |

| `sagemaker` | [sagemaker:CreateTrainingJob](../actions.md#sagemaker:createtrainingjob) |

| `sagemaker` | [sagemaker:DescribeAutoMLJob](../actions.md#sagemaker:describeautomljob) |

| `sagemaker` | [sagemaker:DescribeCompilationJob](../actions.md#sagemaker:describecompilationjob) |

| `sagemaker` | [sagemaker:DescribeEndpoint](../actions.md#sagemaker:describeendpoint) |

| `sagemaker` | [sagemaker:DescribeProcessingJob](../actions.md#sagemaker:describeprocessingjob) |

| `sagemaker` | [sagemaker:DescribeTrainingJob](../actions.md#sagemaker:describetrainingjob) |

| `sagemaker` | [sagemaker:DescribeTransformJob](../actions.md#sagemaker:describetransformjob) |

| `sagemaker` | [sagemaker:InvokeEndpoint](../actions.md#sagemaker:invokeendpoint) |

| `sagemaker` | [sagemaker:ListCandidatesForAutoMLJob](../actions.md#sagemaker:listcandidatesforautomljob) |

| `sagemaker` | [sagemaker:StopAutoMLJob](../actions.md#sagemaker:stopautomljob) |

| `sagemaker` | [sagemaker:StopCompilationJob](../actions.md#sagemaker:stopcompilationjob) |

| `sagemaker` | [sagemaker:StopProcessingJob](../actions.md#sagemaker:stopprocessingjob) |

| `sagemaker` | [sagemaker:StopTrainingJob](../actions.md#sagemaker:stoptrainingjob) |

| `secretsmanager` | [secretsmanager:DescribeSecret](../actions.md#secretsmanager:describesecret) |

| `secretsmanager` | [secretsmanager:GetRandomPassword](../actions.md#secretsmanager:getrandompassword) |

| `secretsmanager` | [secretsmanager:GetResourcePolicy](../actions.md#secretsmanager:getresourcepolicy) |

| `secretsmanager` | [secretsmanager:GetSecretValue](../actions.md#secretsmanager:getsecretvalue) |

| `secretsmanager` | [secretsmanager:ListSecretVersionIds](../actions.md#secretsmanager:listsecretversionids) |

| `secretsmanager` | [secretsmanager:ListSecrets](../actions.md#secretsmanager:listsecrets) |
