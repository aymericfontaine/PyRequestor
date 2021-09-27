from models.requestparam_model import RequestParamModel


class RequestModel:
    id: int
    num: str
    label: str
    req: str

    params = [RequestParamModel]