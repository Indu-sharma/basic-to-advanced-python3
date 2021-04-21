from utils.jira_utils import JiraObject
from utils.testrail_utils import TestRail
import jira
import argparse
import sys


def sync_jira_testrail(run_id, days):
    stories_metric = TestRail(run_id=run_id, days=days).qa_metric
    print(f'Total User Stories to update from TestRail to Jira in last {days} days are: {len(stories_metric)}')
    # Update the QA metrics to Jira User Story
    for story in stories_metric:
        Obj = JiraObject()
        try:
            Obj.update_qa_metrics(story, stories_metric[story])
        except jira.exceptions.JIRAError:
            continue
            # Fetch the QA metrics from Jira User Story
        print(story, Obj.get_qa_metrics(story))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync User Stories metrics in Jira from TestRail test run",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-r", "--test_run", help="List of Test Runs to Update to Jira ", nargs="+",
                        required=False)
    parser.add_argument("-d", "--days", help="Number of Historical days to sync metrics from TestRail to Jira",
                        required=False)

    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    run_ids = args.test_run
    days=args.days
    if days is not None:
        days = int(days)
    else: 
        days=7
    if run_ids is not None:
        try:
            run_ids = tuple(map(lambda x: int(x), run_ids))
        except ValueError:
            parser.print_help()
            print(f"The inputs to test_run {run_ids} should contain list of numbers with space seperated")
            sys.exit()
    sync_jira_testrail(run_ids, days)
