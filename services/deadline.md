# Service: deadline

## Attached roles

| Policy ARN | Policy Name |
|------------|-------------|
## Attached Policies

| Policy ARN | Policy Name |
|------------|-------------|
| `arn:aws:iam::aws:policy/ReadOnlyAccess` | [ReadOnlyAccess](../policies.md#readonlyaccess) |
| `arn:aws:iam::aws:policy/aws-service-role/AWSSupportServiceRolePolicy` | [AWSSupportServiceRolePolicy](../policies.md#awssupportservicerolepolicy) |
| `arn:aws:iam::aws:policy/AWSDeadlineCloud-UserAccessFarms` | [AWSDeadlineCloud-UserAccessFarms](../policies.md#awsdeadlinecloud-useraccessfarms) |
| `arn:aws:iam::aws:policy/AWSDeadlineCloud-UserAccessFleets` | [AWSDeadlineCloud-UserAccessFleets](../policies.md#awsdeadlinecloud-useraccessfleets) |
| `arn:aws:iam::aws:policy/AWSDeadlineCloud-UserAccessJobs` | [AWSDeadlineCloud-UserAccessJobs](../policies.md#awsdeadlinecloud-useraccessjobs) |
| `arn:aws:iam::aws:policy/AWSDeadlineCloud-UserAccessQueues` | [AWSDeadlineCloud-UserAccessQueues](../policies.md#awsdeadlinecloud-useraccessqueues) |
| `arn:aws:iam::aws:policy/AWSDeadlineCloud-FleetWorker` | [AWSDeadlineCloud-FleetWorker](../policies.md#awsdeadlinecloud-fleetworker) |
| `arn:aws:iam::aws:policy/AWSDeadlineCloud-WorkerHost` | [AWSDeadlineCloud-WorkerHost](../policies.md#awsdeadlinecloud-workerhost) |
| `arn:aws:iam::aws:policy/AIOpsAssistantPolicy` | [AIOpsAssistantPolicy](../policies.md#aiopsassistantpolicy) |

## Allowed Actions

| Action | Service |
|--------|---------|
| [deadline:AssociateMemberToFarm](../actions.md#deadline:associatemembertofarm) | deadline |
| [deadline:AssociateMemberToFleet](../actions.md#deadline:associatemembertofleet) | deadline |
| [deadline:AssociateMemberToJob](../actions.md#deadline:associatemembertojob) | deadline |
| [deadline:AssociateMemberToQueue](../actions.md#deadline:associatemembertoqueue) | deadline |
| [deadline:AssumeFleetRoleForRead](../actions.md#deadline:assumefleetroleforread) | deadline |
| [deadline:AssumeFleetRoleForWorker](../actions.md#deadline:assumefleetroleforworker) | deadline |
| [deadline:AssumeQueueRoleForRead](../actions.md#deadline:assumequeueroleforread) | deadline |
| [deadline:AssumeQueueRoleForUser](../actions.md#deadline:assumequeueroleforuser) | deadline |
| [deadline:AssumeQueueRoleForWorker](../actions.md#deadline:assumequeueroleforworker) | deadline |
| [deadline:BatchGetJobEntity](../actions.md#deadline:batchgetjobentity) | deadline |
| [deadline:CreateBudget](../actions.md#deadline:createbudget) | deadline |
| [deadline:CreateJob](../actions.md#deadline:createjob) | deadline |
| [deadline:CreateWorker](../actions.md#deadline:createworker) | deadline |
| [deadline:DeleteBudget](../actions.md#deadline:deletebudget) | deadline |
| [deadline:DisassociateMemberFromFarm](../actions.md#deadline:disassociatememberfromfarm) | deadline |
| [deadline:DisassociateMemberFromFleet](../actions.md#deadline:disassociatememberfromfleet) | deadline |
| [deadline:DisassociateMemberFromJob](../actions.md#deadline:disassociatememberfromjob) | deadline |
| [deadline:DisassociateMemberFromQueue](../actions.md#deadline:disassociatememberfromqueue) | deadline |
| [deadline:GetApplicationVersion](../actions.md#deadline:getapplicationversion) | deadline |
| [deadline:GetBudget](../actions.md#deadline:getbudget) | deadline |
| [deadline:GetFarm](../actions.md#deadline:getfarm) | deadline |
| [deadline:GetFleet](../actions.md#deadline:getfleet) | deadline |
| [deadline:GetJob](../actions.md#deadline:getjob) | deadline |
| [deadline:GetJobTemplate](../actions.md#deadline:getjobtemplate) | deadline |
| [deadline:GetLicenseEndpoint](../actions.md#deadline:getlicenseendpoint) | deadline |
| [deadline:GetMonitor](../actions.md#deadline:getmonitor) | deadline |
| [deadline:GetQueue](../actions.md#deadline:getqueue) | deadline |
| [deadline:GetQueueEnvironment](../actions.md#deadline:getqueueenvironment) | deadline |
| [deadline:GetQueueFleetAssociation](../actions.md#deadline:getqueuefleetassociation) | deadline |
| [deadline:GetSession](../actions.md#deadline:getsession) | deadline |
| [deadline:GetSessionAction](../actions.md#deadline:getsessionaction) | deadline |
| [deadline:GetSessionsStatisticsAggregation](../actions.md#deadline:getsessionsstatisticsaggregation) | deadline |
| [deadline:GetStep](../actions.md#deadline:getstep) | deadline |
| [deadline:GetStorageProfile](../actions.md#deadline:getstorageprofile) | deadline |
| [deadline:GetStorageProfileForQueue](../actions.md#deadline:getstorageprofileforqueue) | deadline |
| [deadline:GetTask](../actions.md#deadline:gettask) | deadline |
| [deadline:GetWorker](../actions.md#deadline:getworker) | deadline |
| [deadline:List*](../actions.md#deadline:listall) | deadline |
| [deadline:ListAvailableMeteredProducts](../actions.md#deadline:listavailablemeteredproducts) | deadline |
| [deadline:ListBudgets](../actions.md#deadline:listbudgets) | deadline |
| [deadline:ListFarmMembers](../actions.md#deadline:listfarmmembers) | deadline |
| [deadline:ListFarms](../actions.md#deadline:listfarms) | deadline |
| [deadline:ListFleetMembers](../actions.md#deadline:listfleetmembers) | deadline |
| [deadline:ListFleets](../actions.md#deadline:listfleets) | deadline |
| [deadline:ListJobMembers](../actions.md#deadline:listjobmembers) | deadline |
| [deadline:ListJobParameterDefinitions](../actions.md#deadline:listjobparameterdefinitions) | deadline |
| [deadline:ListJobs](../actions.md#deadline:listjobs) | deadline |
| [deadline:ListLicenseEndpoints](../actions.md#deadline:listlicenseendpoints) | deadline |
| [deadline:ListMeteredProducts](../actions.md#deadline:listmeteredproducts) | deadline |
| [deadline:ListMonitors](../actions.md#deadline:listmonitors) | deadline |
| [deadline:ListQueueEnvironments](../actions.md#deadline:listqueueenvironments) | deadline |
| [deadline:ListQueueFleetAssociations](../actions.md#deadline:listqueuefleetassociations) | deadline |
| [deadline:ListQueueMembers](../actions.md#deadline:listqueuemembers) | deadline |
| [deadline:ListQueues](../actions.md#deadline:listqueues) | deadline |
| [deadline:ListSessionActions](../actions.md#deadline:listsessionactions) | deadline |
| [deadline:ListSessions](../actions.md#deadline:listsessions) | deadline |
| [deadline:ListSessionsForWorker](../actions.md#deadline:listsessionsforworker) | deadline |
| [deadline:ListStepConsumers](../actions.md#deadline:liststepconsumers) | deadline |
| [deadline:ListStepDependencies](../actions.md#deadline:liststepdependencies) | deadline |
| [deadline:ListSteps](../actions.md#deadline:liststeps) | deadline |
| [deadline:ListStorageProfiles](../actions.md#deadline:liststorageprofiles) | deadline |
| [deadline:ListStorageProfilesForQueue](../actions.md#deadline:liststorageprofilesforqueue) | deadline |
| [deadline:ListTagsForResource](../actions.md#deadline:listtagsforresource) | deadline |
| [deadline:ListTasks](../actions.md#deadline:listtasks) | deadline |
| [deadline:ListWorkers](../actions.md#deadline:listworkers) | deadline |
| [deadline:SearchJobs](../actions.md#deadline:searchjobs) | deadline |
| [deadline:SearchSteps](../actions.md#deadline:searchsteps) | deadline |
| [deadline:SearchTasks](../actions.md#deadline:searchtasks) | deadline |
| [deadline:SearchWorkers](../actions.md#deadline:searchworkers) | deadline |
| [deadline:StartSessionsStatisticsAggregation](../actions.md#deadline:startsessionsstatisticsaggregation) | deadline |
| [deadline:UpdateBudget](../actions.md#deadline:updatebudget) | deadline |
| [deadline:UpdateJob](../actions.md#deadline:updatejob) | deadline |
| [deadline:UpdateSession](../actions.md#deadline:updatesession) | deadline |
| [deadline:UpdateStep](../actions.md#deadline:updatestep) | deadline |
| [deadline:UpdateTask](../actions.md#deadline:updatetask) | deadline |
| [deadline:UpdateWorker](../actions.md#deadline:updateworker) | deadline |
| [deadline:UpdateWorkerSchedule](../actions.md#deadline:updateworkerschedule) | deadline |
| [deadline:listAvailableMeteredProducts](../actions.md#deadline:listavailablemeteredproducts) | deadline |
| [deadline:listBudgets](../actions.md#deadline:listbudgets) | deadline |
| [deadline:listFarmMembers](../actions.md#deadline:listfarmmembers) | deadline |
| [deadline:listFarms](../actions.md#deadline:listfarms) | deadline |
| [deadline:listFleetMembers](../actions.md#deadline:listfleetmembers) | deadline |
| [deadline:listFleets](../actions.md#deadline:listfleets) | deadline |
| [deadline:listJobMembers](../actions.md#deadline:listjobmembers) | deadline |
| [deadline:listJobs](../actions.md#deadline:listjobs) | deadline |
| [deadline:listLicenseEndpoints](../actions.md#deadline:listlicenseendpoints) | deadline |
| [deadline:listMeteredProducts](../actions.md#deadline:listmeteredproducts) | deadline |
| [deadline:listMonitors](../actions.md#deadline:listmonitors) | deadline |
| [deadline:listQueueEnvironments](../actions.md#deadline:listqueueenvironments) | deadline |
| [deadline:listQueueFleetAssociations](../actions.md#deadline:listqueuefleetassociations) | deadline |
| [deadline:listQueueMembers](../actions.md#deadline:listqueuemembers) | deadline |
| [deadline:listQueues](../actions.md#deadline:listqueues) | deadline |
| [deadline:listStorageProfiles](../actions.md#deadline:liststorageprofiles) | deadline |
| [deadline:listWorkers](../actions.md#deadline:listworkers) | deadline |