# Policy: DataScientist

ARN: `arn:aws:iam::aws:policy/job-function/DataScientist`

## Attached Roles

## Attached Services

| Service |
|---------|
| rds |
| fsx |
| kms |
| cloudformation |
| machinelearning |
| lambda |
| firehose |
| logs |
| es |
| ec2 |
| s3 |
| autoscaling |
| iam |
| sagemaker |
| elasticmapreduce |
| elasticfilesystem |
| sns |
| cloudwatch |
| kinesis |
| datapipeline |
| sdb |
| redshift |
| dynamodb |

## Allowed Actions

| Service | Action |
|:-------:|--------|

| `autoscaling` | [autoscaling:*](../actions.md#autoscaling:all) |

| `cloudformation` | [cloudformation:CreateStack](../actions.md#cloudformation:createstack) |

| `cloudformation` | [cloudformation:DescribeStackEvents](../actions.md#cloudformation:describestackevents) |

| `cloudwatch` | [cloudwatch:*](../actions.md#cloudwatch:all) |

| `datapipeline` | [datapipeline:Describe*](../actions.md#datapipeline:describeall) |

| `datapipeline` | [datapipeline:GetPipelineDefinition](../actions.md#datapipeline:getpipelinedefinition) |

| `datapipeline` | [datapipeline:ListPipelines](../actions.md#datapipeline:listpipelines) |

| `datapipeline` | [datapipeline:QueryObjects](../actions.md#datapipeline:queryobjects) |

| `dynamodb` | [dynamodb:*](../actions.md#dynamodb:all) |

| `ec2` | [ec2:CancelSpotFleetRequests](../actions.md#ec2:cancelspotfleetrequests) |

| `ec2` | [ec2:CancelSpotInstanceRequests](../actions.md#ec2:cancelspotinstancerequests) |

| `ec2` | [ec2:CreateTags](../actions.md#ec2:createtags) |

| `ec2` | [ec2:DeleteTags](../actions.md#ec2:deletetags) |

| `ec2` | [ec2:Describe*](../actions.md#ec2:describeall) |

| `ec2` | [ec2:ModifyImageAttribute](../actions.md#ec2:modifyimageattribute) |

| `ec2` | [ec2:ModifyInstanceAttribute](../actions.md#ec2:modifyinstanceattribute) |

| `ec2` | [ec2:ModifySpotFleetRequest](../actions.md#ec2:modifyspotfleetrequest) |

| `ec2` | [ec2:RequestSpotFleet](../actions.md#ec2:requestspotfleet) |

| `ec2` | [ec2:RequestSpotInstances](../actions.md#ec2:requestspotinstances) |

| `ec2` | [ec2:RunInstances](../actions.md#ec2:runinstances) |

| `ec2` | [ec2:TerminateInstances](../actions.md#ec2:terminateinstances) |

| `elasticfilesystem` | [elasticfilesystem:*](../actions.md#elasticfilesystem:all) |

| `elasticmapreduce` | [elasticmapreduce:*](../actions.md#elasticmapreduce:all) |

| `es` | [es:*](../actions.md#es:all) |

| `firehose` | [firehose:*](../actions.md#firehose:all) |

| `fsx` | [fsx:DescribeFileSystems](../actions.md#fsx:describefilesystems) |

| `iam` | [iam:GetInstanceProfile](../actions.md#iam:getinstanceprofile) |

| `iam` | [iam:GetPolicy](../actions.md#iam:getpolicy) |

| `iam` | [iam:GetPolicyVersion](../actions.md#iam:getpolicyversion) |

| `iam` | [iam:GetRole](../actions.md#iam:getrole) |

| `iam` | [iam:ListRoles](../actions.md#iam:listroles) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `iam` | [iam:PassRole](../actions.md#iam:passrole) |

| `kinesis` | [kinesis:*](../actions.md#kinesis:all) |

| `kms` | [kms:List*](../actions.md#kms:listall) |

| `lambda` | [lambda:Create*](../actions.md#lambda:createall) |

| `lambda` | [lambda:Delete*](../actions.md#lambda:deleteall) |

| `lambda` | [lambda:Get*](../actions.md#lambda:getall) |

| `lambda` | [lambda:InvokeFunction](../actions.md#lambda:invokefunction) |

| `lambda` | [lambda:List*](../actions.md#lambda:listall) |

| `lambda` | [lambda:PublishVersion](../actions.md#lambda:publishversion) |

| `lambda` | [lambda:Update*](../actions.md#lambda:updateall) |

| `logs` | [logs:DescribeLogStreams](../actions.md#logs:describelogstreams) |

| `logs` | [logs:GetLogEvents](../actions.md#logs:getlogevents) |

| `machinelearning` | [machinelearning:*](../actions.md#machinelearning:all) |

| `rds` | [rds:*](../actions.md#rds:all) |

| `redshift` | [redshift:*](../actions.md#redshift:all) |

| `s3` | [s3:Abort*](../actions.md#s3:abortall) |

| `s3` | [s3:CreateBucket](../actions.md#s3:createbucket) |

| `s3` | [s3:DeleteObject](../actions.md#s3:deleteobject) |

| `s3` | [s3:Get*](../actions.md#s3:getall) |

| `s3` | [s3:List*](../actions.md#s3:listall) |

| `s3` | [s3:PutAccelerateConfiguration](../actions.md#s3:putaccelerateconfiguration) |

| `s3` | [s3:PutBucketCors](../actions.md#s3:putbucketcors) |

| `s3` | [s3:PutBucketLogging](../actions.md#s3:putbucketlogging) |

| `s3` | [s3:PutBucketNotification](../actions.md#s3:putbucketnotification) |

| `s3` | [s3:PutBucketTagging](../actions.md#s3:putbuckettagging) |

| `s3` | [s3:PutObject](../actions.md#s3:putobject) |

| `s3` | [s3:Replicate*](../actions.md#s3:replicateall) |

| `s3` | [s3:RestoreObject](../actions.md#s3:restoreobject) |

| `sagemaker` | [sagemaker:*](../actions.md#sagemaker:all) |

| `sagemaker` | [sagemaker:*App](../actions.md#sagemaker:allapp) |

| `sagemaker` | [sagemaker:*FlowDefinition](../actions.md#sagemaker:allflowdefinition) |

| `sagemaker` | [sagemaker:*FlowDefinitions](../actions.md#sagemaker:allflowdefinitions) |

| `sagemaker` | [sagemaker:CreatePresignedDomainUrl](../actions.md#sagemaker:createpresigneddomainurl) |

| `sagemaker` | [sagemaker:DescribeDomain](../actions.md#sagemaker:describedomain) |

| `sagemaker` | [sagemaker:DescribeUserProfile](../actions.md#sagemaker:describeuserprofile) |

| `sagemaker` | [sagemaker:ListApps](../actions.md#sagemaker:listapps) |

| `sagemaker` | [sagemaker:ListDomains](../actions.md#sagemaker:listdomains) |

| `sagemaker` | [sagemaker:ListUserProfiles](../actions.md#sagemaker:listuserprofiles) |

| `sdb` | [sdb:*](../actions.md#sdb:all) |

| `sns` | [sns:CreateTopic](../actions.md#sns:createtopic) |

| `sns` | [sns:Get*](../actions.md#sns:getall) |

| `sns` | [sns:List*](../actions.md#sns:listall) |

| `sns` | [sns:ListSubscriptions](../actions.md#sns:listsubscriptions) |

| `sns` | [sns:ListTopics](../actions.md#sns:listtopics) |
