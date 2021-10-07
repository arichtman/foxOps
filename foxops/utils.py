def resolve_project_id_from_handle(handle: str):
    target = handle.strip()
    if handle and target:
        gl.projects.list(search=target)
