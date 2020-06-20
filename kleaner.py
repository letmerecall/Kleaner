import os
import yaml
import schedule
import time
import shutil

with open('config.yaml') as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)


def kleaner(cfg):
    for job_name, job_config in cfg.items():
        job_config.update({'name': job_name})
        repeat_sec = job_config.get('repeat', 60)
        schedule.every(repeat_sec).seconds.do(kleaning_job, job_config)
    while True:
        schedule.run_pending()
        time.sleep(1)
    return 0


def extract_test(job_config):
    available_tests = ['mindepth', 'maxdepth', 'mmin', 'mtime', 'type']
    test_cmd_string = ''
    for test in available_tests:
        test_value = job_config.get(test, None)
        if not test_value:
            continue
        test_cmd_string += f' -{test} {test_value}'
    return test_cmd_string


def kleaning_job(job_config):
    print('\n')
    dir = job_config.get('directory', None)
    dry_run = job_config.get('dry_run', False)
    print(f'Job - {job_config.get("name")}')
    print(f'Dry run - {dry_run}')
    if not dir:
        print("Please pass directory name in the job")
        return 1
    arguments = extract_test(job_config)
    if not arguments:
        return 1
    cmd = f'find {dir}{arguments}'
    print(f'CMD - {cmd}')
    files_to_delete = os.popen(cmd).read().strip().split('\n')
    print(f'Files to be deleted - {files_to_delete}')
    if not dry_run:
        for path in files_to_delete:
            if path:
                try:
                    os.remove(path)
                except IsADirectoryError:
                    shutil.rmtree(path)


if __name__ == '__main__':
    print(
        """
        ,--. ,--.,--.
        |  .'   /|  |    ,---.  ,--,--.,--,--,  ,---. ,--.--.
        |  .   ' |  |   | .-. :' ,-.  ||      \| .-. :|  .--'
        |  |\   \|  '--.\   --.\ '-'  ||  ||  |\   --.|  |
        `--' '--'`-----' `----' `--`--'`--''--' `----'`--'
        """)
    kleaner(cfg)
