import datetime
import json
from collections import defaultdict, namedtuple

# define a named tuple for issue fields needed for reporting
Issue = namedtuple('Issue', ['estimate', 'project', 'date', 'design'])

# any of these tags indicates an issue is design and not dev
DESIGN_TAGS = {'design', '🗺️ design', 'Design'}

def load_issues():
    '''Read issues CSV and return as a list of :class:`Issue` sorted
    by date closed.'''
    issues = []
    with open('data/issues.json') as datafile:
        data = json.load(datafile)

        for issue in data:
            # skip any issues that are not yet closed
            if issue['closed'] == 'closed' or not issue['closed']:
                continue

            # for reporting purposes, skip: wontfix, duplicate, invalid
            skip_labels = ['wontfix','🚫 wontfix', 'duplicate', 'invalid', '🖇️ duplicate']
            if any(skip in issue['labels'] for skip in skip_labels):
                continue

            closed_date = datetime.datetime.strptime(
                issue['closed'][:10], '%Y-%m-%d')

            issues.append(Issue(
                # NOTE: integer failing here, not sure why CSV has non-ints
                int(issue['estimate'] or 0),
                issue['project'],
                closed_date,
                DESIGN_TAGS.intersection(set(issue['labels']))
            ))
    # sort issues by date
    return sorted(issues, key=lambda issue: issue.date)


def average(values):
    '''calculate average for use in reporting velocity'''
    return float('%.2f' % (sum(values) / len(values)))


def summarize_iterations():
    """
    Calculate points and issues completed in each iteration, with
    separate totals for issues labeled as design and all other issues.
    Also reports on total issues and points by project in each iteration,
    and calculates rolling velocity for dev and design (average of the
    last three iterations). Resulting iteration information is
    saved as `data/iteration-summary.json`.
    Iterations are defined by dates in `data/iterations.json`.
    """

    issues = load_issues()

    with open('data/iterations.json') as f:
        iteration_data = json.load(f)
        # filter iteration data to those that should be included in summary:
        # - skip any with end date unset (allow future iterations with end date unspecified)
        # - skip any flagged as "skip" for display in dev schedule
        iteration_data = [it for it in iteration_data if not it.get('skip') or 'to' not in it]

        issue_index = 0

        for i, iteration in enumerate(iteration_data):
            # use current iteration start as beginning of date range
            # and next iteration start as end
            # (make sure we account for all events without having to set
            # iteration dates inaccurately)
            start = datetime.datetime.strptime(iteration['from'], '%Y-%m-%d')
            try:
                end = datetime.datetime.strptime(
                    iteration_data[i + 1]['from'], '%Y-%m-%d')
            except IndexError:
                # last iteration has no next start;
                # use iteration end + 1 day since end is excluded
                end = datetime.datetime.strptime(
                    iteration['to'], '%Y-%m-%d') + datetime.timedelta(days=1)

            iteration['dev'] = defaultdict(int)
            iteration['design'] = defaultdict(int)
            iteration['project_issues'] = defaultdict(int)
            iteration['project_points'] = defaultdict(int)

            for i, issue in enumerate(issues[issue_index:]):
                if start <= issue.date < end:
                    devdesign = 'design' if issue.design else 'dev'
                    iteration[devdesign]['points'] += issue.estimate
                    iteration[devdesign]['issues'] += 1
                    iteration['project_issues'][issue.project] += 1
                    iteration['project_points'][issue.project] += \
                        int(issue.estimate)
                elif issue.date >= end:
                    # stop looping at first issue outside this iteration
                    issue_index += i - 1
                    break

    # calculate velocity
    for i, iteration in enumerate(iteration_data):
        # not enough data; skip
        if i < 2:
            continue
        iteration['dev']['velocity'] = average(
            [it['dev']['points'] for it in iteration_data[i - 2:i + 1]])
        iteration['design']['velocity'] = average(
            [it['design']['points'] for it in iteration_data[i - 2:i + 1]])

    with open('data/iteration_summary.json', 'w') as f:
        json.dump(iteration_data, f, indent=4)


if __name__ == '__main__':
    summarize_iterations()
