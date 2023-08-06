# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any


class CreateModelAsyncPredictRequest(TeaModel):
    def __init__(
        self,
        binary_to_text: bool = None,
        body: str = None,
        content: str = None,
        model_id: int = None,
        model_version: str = None,
        service_name: str = None,
        service_version: str = None,
    ):
        self.binary_to_text = binary_to_text
        self.body = body
        self.content = content
        self.model_id = model_id
        self.model_version = model_version
        self.service_name = service_name
        self.service_version = service_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.binary_to_text is not None:
            result['BinaryToText'] = self.binary_to_text
        if self.body is not None:
            result['Body'] = self.body
        if self.content is not None:
            result['Content'] = self.content
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BinaryToText') is not None:
            self.binary_to_text = m.get('BinaryToText')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class CreateModelAsyncPredictResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateModelAsyncPredictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateModelAsyncPredictResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateModelAsyncPredictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelAsyncPredictRequest(TeaModel):
    def __init__(
        self,
        async_predict_id: int = None,
    ):
        self.async_predict_id = async_predict_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_predict_id is not None:
            result['AsyncPredictId'] = self.async_predict_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncPredictId') is not None:
            self.async_predict_id = m.get('AsyncPredictId')
        return self


class GetModelAsyncPredictResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetModelAsyncPredictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetModelAsyncPredictResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetModelAsyncPredictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PredictClassifierModelRequest(TeaModel):
    def __init__(
        self,
        auto_prediction: bool = None,
        binary_to_text: bool = None,
        body: str = None,
        classifier_id: int = None,
        content: str = None,
    ):
        self.auto_prediction = auto_prediction
        self.binary_to_text = binary_to_text
        self.body = body
        self.classifier_id = classifier_id
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_prediction is not None:
            result['AutoPrediction'] = self.auto_prediction
        if self.binary_to_text is not None:
            result['BinaryToText'] = self.binary_to_text
        if self.body is not None:
            result['Body'] = self.body
        if self.classifier_id is not None:
            result['ClassifierId'] = self.classifier_id
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPrediction') is not None:
            self.auto_prediction = m.get('AutoPrediction')
        if m.get('BinaryToText') is not None:
            self.binary_to_text = m.get('BinaryToText')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('ClassifierId') is not None:
            self.classifier_id = m.get('ClassifierId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class PredictClassifierModelResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PredictClassifierModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PredictClassifierModelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PredictClassifierModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PredictModelRequest(TeaModel):
    def __init__(
        self,
        binary_to_text: bool = None,
        body: str = None,
        content: str = None,
        model_id: int = None,
        model_version: str = None,
    ):
        self.binary_to_text = binary_to_text
        self.body = body
        self.content = content
        self.model_id = model_id
        self.model_version = model_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.binary_to_text is not None:
            result['BinaryToText'] = self.binary_to_text
        if self.body is not None:
            result['Body'] = self.body
        if self.content is not None:
            result['Content'] = self.content
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BinaryToText') is not None:
            self.binary_to_text = m.get('BinaryToText')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        return self


class PredictModelResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PredictModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PredictModelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PredictModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PredictPreTrainModelRequest(TeaModel):
    def __init__(
        self,
        binary_to_text: bool = None,
        body: str = None,
        content: str = None,
        service_name: str = None,
        service_version: str = None,
    ):
        self.binary_to_text = binary_to_text
        self.body = body
        self.content = content
        self.service_name = service_name
        self.service_version = service_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.binary_to_text is not None:
            result['BinaryToText'] = self.binary_to_text
        if self.body is not None:
            result['Body'] = self.body
        if self.content is not None:
            result['Content'] = self.content
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BinaryToText') is not None:
            self.binary_to_text = m.get('BinaryToText')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class PredictPreTrainModelResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PredictPreTrainModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PredictPreTrainModelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PredictPreTrainModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PredictTemplateModelRequest(TeaModel):
    def __init__(
        self,
        binary_to_text: bool = None,
        body: str = None,
        content: str = None,
        task_id: int = None,
    ):
        self.binary_to_text = binary_to_text
        self.body = body
        self.content = content
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.binary_to_text is not None:
            result['BinaryToText'] = self.binary_to_text
        if self.body is not None:
            result['Body'] = self.body
        if self.content is not None:
            result['Content'] = self.content
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BinaryToText') is not None:
            self.binary_to_text = m.get('BinaryToText')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class PredictTemplateModelResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PredictTemplateModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PredictTemplateModelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PredictTemplateModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


