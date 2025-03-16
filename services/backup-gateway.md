# Service: backup-gateway

## Attached roles

| Policy ARN | Policy Name |
|------------|-------------|
## Attached Policies

| Policy ARN | Policy Name |
|------------|-------------|
| `arn:aws:iam::aws:policy/ReadOnlyAccess` | [ReadOnlyAccess](../policies.md#readonlyaccess) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSConfigServiceRolePolicy` | [AWSConfigServiceRolePolicy](../policies.md#awsconfigservicerolepolicy) |
| `arn:aws:iam::aws:policy/service-role/AWSBackupServiceRolePolicyForBackup` | [AWSBackupServiceRolePolicyForBackup](../policies.md#awsbackupservicerolepolicyforbackup) |
| `arn:aws:iam::aws:policy/service-role/AWSBackupServiceRolePolicyForRestores` | [AWSBackupServiceRolePolicyForRestores](../policies.md#awsbackupservicerolepolicyforrestores) |
| `arn:aws:iam::aws:policy/AWSBackupFullAccess` | [AWSBackupFullAccess](../policies.md#awsbackupfullaccess) |
| `arn:aws:iam::aws:policy/AWSBackupOperatorAccess` | [AWSBackupOperatorAccess](../policies.md#awsbackupoperatoraccess) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSBackupServiceLinkedRolePolicyForBackup` | [AWSBackupServiceLinkedRolePolicyForBackup](../policies.md#awsbackupservicelinkedrolepolicyforbackup) |
| `arn:aws:iam::aws:policy/service-role/AWS_ConfigRole` | [AWS_ConfigRole](../policies.md#aws_configrole) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSSupportServiceRolePolicy` | [AWSSupportServiceRolePolicy](../policies.md#awssupportservicerolepolicy) |
| `arn:aws:iam::aws:policy/service-role/AWSBackupGatewayServiceRolePolicyForVirtualMachineMetadataSync` | [AWSBackupGatewayServiceRolePolicyForVirtualMachineMetadataSync](../policies.md#awsbackupgatewayservicerolepolicyforvirtualmachinemetadatasync) |
| `arn:aws:iam::aws:policy/AWSPartnerLedSupportReadOnlyAccess` | [AWSPartnerLedSupportReadOnlyAccess](../policies.md#awspartnerledsupportreadonlyaccess) |
| `arn:aws:iam::aws:policy/AIOpsAssistantPolicy` | [AIOpsAssistantPolicy](../policies.md#aiopsassistantpolicy) |

## Allowed Actions

| Action | Service |
|--------|---------|
| [backup-gateway:AssociateGatewayToServer](../actions.md#backup-gateway:associategatewaytoserver) | backup-gateway |
| [backup-gateway:Backup](../actions.md#backup-gateway:backup) | backup-gateway |
| [backup-gateway:CreateGateway](../actions.md#backup-gateway:creategateway) | backup-gateway |
| [backup-gateway:DeleteGateway](../actions.md#backup-gateway:deletegateway) | backup-gateway |
| [backup-gateway:DeleteHypervisor](../actions.md#backup-gateway:deletehypervisor) | backup-gateway |
| [backup-gateway:DisassociateGatewayFromServer](../actions.md#backup-gateway:disassociategatewayfromserver) | backup-gateway |
| [backup-gateway:GetBandwidthRateLimitSchedule](../actions.md#backup-gateway:getbandwidthratelimitschedule) | backup-gateway |
| [backup-gateway:GetGateway](../actions.md#backup-gateway:getgateway) | backup-gateway |
| [backup-gateway:GetHypervisor](../actions.md#backup-gateway:gethypervisor) | backup-gateway |
| [backup-gateway:GetHypervisorPropertyMappings](../actions.md#backup-gateway:gethypervisorpropertymappings) | backup-gateway |
| [backup-gateway:GetVirtualMachine](../actions.md#backup-gateway:getvirtualmachine) | backup-gateway |
| [backup-gateway:ImportHypervisorConfiguration](../actions.md#backup-gateway:importhypervisorconfiguration) | backup-gateway |
| [backup-gateway:List*](../actions.md#backup-gateway:listall) | backup-gateway |
| [backup-gateway:ListGateways](../actions.md#backup-gateway:listgateways) | backup-gateway |
| [backup-gateway:ListHypervisors](../actions.md#backup-gateway:listhypervisors) | backup-gateway |
| [backup-gateway:ListTagsForResource](../actions.md#backup-gateway:listtagsforresource) | backup-gateway |
| [backup-gateway:ListVirtualMachines](../actions.md#backup-gateway:listvirtualmachines) | backup-gateway |
| [backup-gateway:PutBandwidthRateLimitSchedule](../actions.md#backup-gateway:putbandwidthratelimitschedule) | backup-gateway |
| [backup-gateway:PutHypervisorPropertyMappings](../actions.md#backup-gateway:puthypervisorpropertymappings) | backup-gateway |
| [backup-gateway:PutMaintenanceStartTime](../actions.md#backup-gateway:putmaintenancestarttime) | backup-gateway |
| [backup-gateway:Restore](../actions.md#backup-gateway:restore) | backup-gateway |
| [backup-gateway:StartVirtualMachinesMetadataSync](../actions.md#backup-gateway:startvirtualmachinesmetadatasync) | backup-gateway |
| [backup-gateway:TagResource](../actions.md#backup-gateway:tagresource) | backup-gateway |
| [backup-gateway:TestHypervisorConfiguration](../actions.md#backup-gateway:testhypervisorconfiguration) | backup-gateway |
| [backup-gateway:UntagResource](../actions.md#backup-gateway:untagresource) | backup-gateway |
| [backup-gateway:UpdateGatewayInformation](../actions.md#backup-gateway:updategatewayinformation) | backup-gateway |
| [backup-gateway:UpdateHypervisor](../actions.md#backup-gateway:updatehypervisor) | backup-gateway |
| [backup-gateway:getGateway](../actions.md#backup-gateway:getgateway) | backup-gateway |
| [backup-gateway:getHypervisor](../actions.md#backup-gateway:gethypervisor) | backup-gateway |
| [backup-gateway:getHypervisorPropertyMappings](../actions.md#backup-gateway:gethypervisorpropertymappings) | backup-gateway |
| [backup-gateway:getVirtualMachine](../actions.md#backup-gateway:getvirtualmachine) | backup-gateway |
| [backup-gateway:listGateways](../actions.md#backup-gateway:listgateways) | backup-gateway |
| [backup-gateway:listHypervisors](../actions.md#backup-gateway:listhypervisors) | backup-gateway |
| [backup-gateway:listVirtualMachines](../actions.md#backup-gateway:listvirtualmachines) | backup-gateway |