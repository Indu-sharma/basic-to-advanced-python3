from jira import JIRA
from utils.config_parser import Parser


class JiraObject:
    def __init__(self):
        conf = Parser()
        self.jira_server = conf.get_key("jira_server")
        self.jira_user = conf.get_key("jira_user")
        self.jira_apikey = conf.get_key("jira_apikey")
        self.jira = self.login
        self.fields_map = self.get_jira_fields
        # print([(k, self.fields_map[k]) for k in self.fields_map.keys() if "test" in k.lower() or "pass" in k.lower()])

    @property
    def get_jira_fields(self):
        field_map = {}
        for field in self.jira.fields():
            field_map[field['name']] = [field['id']]
        return field_map

    @property
    def login(self):
        jira_options = {
            'server': self.jira_server
        }
        return JIRA(jira_options, basic_auth=(self.jira_user, self.jira_apikey))

    def get_qa_metrics(self, ticket_key):
        """
        Total #Tests = customfield_10733
        Total #Automated Tests = customfield_10734
        Total #Tests to Automate = customfield_10735
        First Pass Rate % = customfield_10736
        Latest Pass Rate % = customfield_10737
        :param ticket_key:
        :return:
        """
        qa_metrics = {}
        current_issue = self.jira.issue(ticket_key)
        try:
            qa_metrics['Total #Tests'] = current_issue.fields.customfield_10733
            qa_metrics['Total #Automated Tests'] = current_issue.fields.customfield_10734
            qa_metrics['Total #Tests to Automate'] = current_issue.fields.customfield_10735
            qa_metrics['First Pass Rate %'] = current_issue.fields.customfield_10736
            qa_metrics['Latest Pass Rate %'] = current_issue.fields.customfield_10737

        except AttributeError:
            print("One or more QA metrics couldn't fetched")
        return qa_metrics

    def update_qa_metrics(self, ticket_key, qa_metrics=None):
        """
        Total #Tests = customfield_10733
        Total #Automated Tests = customfield_10734
        Total #Tests to Automate = customfield_10735
        First Pass Rate % = customfield_10736
        Latest Pass Rate % = customfield_10737
        Target Test Counts = customfield_10711
        Completed Test Counts = customfield_10713

        :param ticket_key:
        :param qa_metrics:dict
        :return:
        """
        if qa_metrics is None:
            qa_metrics = {"Total #Tests": 1, "Total #Automated Tests": 1, "Total #Tests to Automate": 1}
        try:
            current_issue = self.jira.search_issues("key=%s" % ticket_key)[0]
        except KeyError:
            return
        if qa_metrics is not None and isinstance(qa_metrics, dict):
            for key, value in qa_metrics.items():
                try:
                    key = self.fields_map[key][0]
                except KeyError:
                    print("Wrong QA metrics : {} ".format(key))
                    continue
                current_issue.update(fields={key:  int(value)})
