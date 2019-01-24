import fnmatch


def is_path_to_be_ignored(event_path, report_path, ignore_patterns):
    """
    answers: Is event_path one among the ignore_patterns?
    strips report path from the event_path
    :param event_path: str
    :param report_path: str
    :param ignore_patterns: list
    :return: bool
    """
    for ignored_pattern in ignore_patterns:
        _, current_file_path = event_path.split(report_path + '/')
        if fnmatch.fnmatch(current_file_path, ignored_pattern):
            return True
    return False
