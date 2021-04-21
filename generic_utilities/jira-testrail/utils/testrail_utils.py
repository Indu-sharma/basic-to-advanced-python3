from utils.config_parser import Parser
from utils.api_utils import APIClient
import os
from pprint import pprint
import datetime


class TestRail:
    def __init__(self, run_id=None, days=1):
        conf = Parser()
        timestamp_pastdays = (datetime.date.today() - datetime.timedelta(days)).strftime("%s")
        self.testrail_user = conf.get_key("testrail_user")
        self.testrail_apikey = conf.get_key("testrail_apikey")
        self.testrail_server = conf.get_key("testrail_server")
        self.client = self.get_connection
        self.zdp_cases = None
        self.testcases_by_project()
        self.first_result = {}
        self.last_result = {}
        self.tests_case_map = {}
        self.stories = []
        if run_id is None:
            run_id = tuple(self.get_all_runs(int(timestamp_pastdays)))
        self.run_id = run_id
        self.qa_metric = {}
        self.test_results(self.run_id)
        self.get_tests_by_run(self.run_id)

    @property
    def get_connection(self):
        os.environ['TESTRAIL_USER_EMAIL'] = self.testrail_user
        os.environ['TESTRAIL_USER_KEY'] = self.testrail_apikey
        os.environ['TESTRAIL_URL'] = self.testrail_server
        client = APIClient(self.testrail_server)
        client.user = self.testrail_user
        client.password = self.testrail_apikey
        return client

    def testcase(self, case_id=7210):
        mycase = self.client.send_get('get_case/'+str(case_id))
        pprint(mycase)

    def testcases_by_project(self, projectid=8):
        zdp_cases = self.client.send_get('get_cases/'+str(projectid))
        self.zdp_cases = zdp_cases

    def get_all_plans(self):
        api_call = 'get_plans/8&is_completed=0'
        all_plans = self.client.send_get(api_call)
        return all_plans

    def get_all_runs(self, timestamp_pastdays):
        plans = self.get_all_plans()
        plan_ids = [plan['id'] for plan in plans]
        run_ids = []
        for plan_id in plan_ids:
            api_call = 'get_plan/'+str(plan_id)
            runs_per_plan = self.client.send_get(api_call)
            for entry in runs_per_plan['entries']:
                for run in entry['runs']:
                    if run['created_on'] > int(timestamp_pastdays):
                        run_ids.append(run['id'])
        return run_ids

    def get_results(self, run_results, first=True):
        mydict = {}
        results = {}
        for i in run_results:
            test_id= i['test_id']
            status_id = i['status_id']
            created_on = i['created_on']
            if status_id is not None:
                if test_id not in mydict:
                    mydict[test_id] = (status_id, created_on)
                    results[test_id] = status_id
                else:
                    if first:
                        if mydict[test_id][1] > created_on:
                            mydict[test_id] = (status_id, created_on)
                            results[test_id] = status_id
                    else:
                        if mydict[test_id][1] < created_on:
                            mydict[test_id] = (status_id, created_on)
                            results[test_id] = status_id
        return results

    def test_results(self, run_id):
        run_results=[]
        if isinstance(run_id, tuple):
            for i in run_id:
                run_results.extend(self.client.send_get('get_results_for_run/'+str(i)))
        else:
            run_results.extend(self.client.send_get('get_results_for_run/' + str(run_id)))
        self.first_result = self.get_results(run_results)
        self.last_result = self.get_results(run_results, first=False)

    def get_tests_by_run(self, run_id):
        tests_by_run = []
        if isinstance(run_id, tuple):
            for i in run_id:
                tests_by_run.extend(self.client.send_get('get_tests/' + str(i)))
        else:
            tests_by_run.extend(self.client.send_get('get_tests/' + str(run_id)))
        for test in tests_by_run:
            test_id = test['id']
            case_id = test['case_id']
            self.tests_case_map[case_id] = test_id
            self.stories.append(test['refs'])
        for story in set(self.stories):
            if story is not None:
                self.qa_metrics_by_story(story)

    def qa_metrics_by_story(self, story):
        first_results_us = {}
        last_results_us = {}
        qa_metrics_for_jira = {}
        tests_cases_by_story = list(filter(lambda x: x['refs'] == str(story).upper()or x['refs'] == str(story).lower(), self.zdp_cases))
        total_tests = len(tests_cases_by_story)
        if total_tests <= 1:
            return
        total_automated_tests = len(list(filter(lambda x: x['type_id'] == 3, tests_cases_by_story)))
        total_tests_to_automate = len(list(filter(lambda x: x['custom_isautomatable'] == 1, tests_cases_by_story)))
        if total_tests_to_automate < total_automated_tests:
            total_tests_to_automate = total_automated_tests
        qa_metrics_for_jira['Total #Tests'] = total_tests
        qa_metrics_for_jira['Total #Automated Tests'] = total_automated_tests
        qa_metrics_for_jira['Total #Tests to Automate'] = total_tests_to_automate - total_automated_tests
        for case in tests_cases_by_story:
            case_id = case['id']
            try:
                test_id = self.tests_case_map[case_id]
            except KeyError:
                continue
            try:
                first_result = self.first_result[test_id]
                last_result = self.last_result[test_id]
            except KeyError:
                continue
            first_results_us[first_result] = 1 + first_results_us.get(first_result, 0)
            last_results_us[last_result] = 1 + last_results_us.get(last_result, 0)
        total_executed_tests = sum(first_results_us.values())
        if not last_results_us:
            return
        if 1 in first_results_us:
            qa_metrics_for_jira['First Pass Rate %'] = round(100*(1.0*first_results_us[1]/total_executed_tests), 2)
        else:
            qa_metrics_for_jira['First Pass Rate %'] = 0
        if 1 in last_results_us:
            qa_metrics_for_jira['Latest Pass Rate %'] = round(100 * (1.0 * last_results_us[1]/total_executed_tests), 2)
        else:
            qa_metrics_for_jira['Latest Pass Rate %'] = 0
        self.qa_metric[story] = qa_metrics_for_jira












