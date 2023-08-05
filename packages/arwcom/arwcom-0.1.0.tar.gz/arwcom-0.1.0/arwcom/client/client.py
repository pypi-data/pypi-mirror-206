def get_dispatch(i_dispatch: str, cls_ctx: str):
    ...


def dispatch(i_dispatch: str, user_name: str = "", cls_ctx: str = ""):
    """Creates a Dispatch based COM object

    :param dispatch: Name # TODO reference appropriate COM docs
    :type dispatch: str
    :param user_name: Name # TODO reference appropriate COM docs
    :type user_name: str
    :param cls_ctx: Name # TODO reference appropriate COM docs
    :type cls_ctx: str
    """
    if len(user_name) == 0:
        user_name = i_dispatch

    dispatch, user_name = get_dispatch(i_dispatch=i_dispatch, cls_ctx=user_name)
