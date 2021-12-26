import logging

import gitlab


class FoxOps:
    def __init__(self, base_url="https://gitlab.com", access_token=None):
        logging.debug("Initialising foxops class")
        self.base_url = base_url
        self.__access_token = access_token
        self.__gitlab_instance = gitlab.Gitlab(self.base_url, self.__access_token)
        self.__gitlab_instance.auth()

    def __search_projects(self, term: str, mine: bool = False):
        results = self.__gitlab_instance.projects.list(search=term, owned=mine)
        if len(results) > 1:
            raise Exception("Too many project results located, unable to resolve ambiguity")
        elif len(results) == 0:
            raise Exception("No project results located")
        return results[0]

    def __resolve_project_id_from_handle(self, handle: str) -> int:
        search_handle = handle.strip()
        if not search_handle:
            raise LookupError("Provided search identifier is empty")
        return self.__search_projects(search_handle)

    def get_project(self, identifier):
        logging.debug(f"foxops getting project {identifier}")
        if identifier.isnumeric():
            project_id = identifier
        else:
            project_id = self.__resolve_project_id_from_handle(identifier)
        return self.get_project_by_id(project_id)
