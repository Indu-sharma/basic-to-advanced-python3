### Goal of this Tool
To update following metrics in a Jira User Story:
* TestRail total test cases
* Tests cases to automate ; This means total test cases are in backlog for automation. 
* Test cases automated 
* First Pass Rate % 
* Latest Pass Rate %   

So that dashboards can be created for above metrics in Jira Dashboards which will provide the visibility on Build Quality & Sprint automation BackLog. 
Based on the trends of above metrics, engineering can fine tune the proccess for producing better quality builds.   
For sample dashboard, please check SampleOutput.png 

### Constraints 
* This works only if your test cases are in TestRail and Integrated with Jira.
* Test Cases in TestRail are linked to User Story as a Reference. 
* Above Metric fields are created in Jira. 
* Jira/TestRail APIs are published and user has  access to them.
* TestRail has is_automatble (A test case is candidate for automation) field and Type(is - Automated after a test is automated) field configured for test case.  

### Steps to update the TestRail Test Run results to Jira

### Execute 
1. Review configs.yml and update the Jira/TestRail APIs and Keys. 
2. pip3 install -r requirements.txt
3. python3 sync_qa_metrics.py -r TEST_RUN  (provide the Test Run ID)

Example: 1)  python3 sync_qa_metric.py -r  10  ; this will sync User Story based on test runs. You can pass space separated list of test runs to update in bulk. 
         2)  python3 sync_qa_metric.py -d 7  ; this will sync the US based on the days test runs created.

Above script updated said metrics from  TestRail tests ex - https://YOUR COMPANY.testrail.io/index.php?/suites/view/11&group_by=cases:section_id&group_id=339&group_order=asc
to Jira User Story : https://YOUR COMPANY.atlassian.net/browse/JIRA_ID

#### Disclaimer 
This script doesn't gurantee to work in all the testRail/Jira setups. In case of failures, do debugging around the constraints provided above. 
