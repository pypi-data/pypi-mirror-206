from beards_analytics.public_api.client import BaPublicApiClient
from beards_analytics.public_api.models import LogSeverity
from beards_analytics.public_api._metadata import K_SERVICE, PROJECT_ID
from google.auth.exceptions import GoogleAuthError
from google.auth.credentials import Credentials
import typing as t
import ujson


# TODO: move to utils if needed in other modules
def _singleton(cls):
    instances = {}
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

@_singleton
class Logger:    
    def __init__(self, credentials: t.Optional[Credentials] = None, send_to_ba: bool = True) -> None:
        self._credentials = credentials
        self._ba_api_client = None
        self._send_to_ba = send_to_ba

    def _log(self, severity: LogSeverity, message: str, labels: t.Optional[t.Mapping[str, str]] = None, send_to_ba=False, **kwargs):
        message = str(message)
        log_obj = dict(severity=severity.name, message=message, **kwargs)
        
        if labels:
            log_obj.update(dict(labels=labels))
        
        # print log object to stdout
        print(ujson.dumps(log_obj))

        send_to_ba = send_to_ba and self._send_to_ba
        
        if not send_to_ba or not K_SERVICE or not PROJECT_ID:
            return
        
        client = self._ba_api_client or BaPublicApiClient(credentials=self._credentials)
        self._ba_api_client = client
            
        try:
            if len(message) < 3:
                self.warning(f'Log message "{message}" must be at least 3 chars to be sent to BA.')
                return
            
            client.create_cloud_log(message, severity, k_service=K_SERVICE, project_id=PROJECT_ID, labels=labels, extra=kwargs)
        except (GoogleAuthError, RuntimeWarning) as e:
            self.warning(e, send_to_ba=False)
            
    def deafult(self, message: str, labels: t.Optional[t.Mapping[str, str]] = None, send_to_ba=False, **kwargs):
        return self._log(LogSeverity.DEFAULT, message, send_to_ba=send_to_ba, labels=labels, **kwargs)
    
    def debug(self, message: str, labels: t.Optional[t.Mapping[str, str]] = None, send_to_ba=False, **kwargs):
        return self._log(LogSeverity.DEBUG, message, send_to_ba=send_to_ba, labels=labels, **kwargs)
    
    def info(self, message: str, labels: t.Optional[t.Mapping[str, str]] = None, send_to_ba=False, **kwargs):
        return self._log(LogSeverity.INFO, message, send_to_ba=send_to_ba, labels=labels, **kwargs)
    
    def notice(self, message: str, labels: t.Optional[t.Mapping[str, str]] = None, send_to_ba=False, **kwargs):
        return self._log(LogSeverity.NOTICE, message, send_to_ba=send_to_ba, labels=labels, **kwargs)
        
    def warning(self, message: str, labels: t.Optional[t.Mapping[str, str]] = None, send_to_ba=False, **kwargs):
        return self._log(LogSeverity.WARNING, message, send_to_ba=send_to_ba, labels=labels, **kwargs)
    
    def error(self, message: str, labels: t.Optional[t.Mapping[str, str]] = None, send_to_ba=True, **kwargs):
        return self._log(LogSeverity.ERROR, message, send_to_ba=send_to_ba, labels=labels, **kwargs)
    
    def critical(self, message: str, labels: t.Optional[t.Mapping[str, str]] = None, send_to_ba=True, **kwargs):
        return self._log(LogSeverity.CRITICAL, message, send_to_ba=send_to_ba, labels=labels, **kwargs)
    
    def alert(self, message: str, labels: t.Optional[t.Mapping[str, str]] = None, send_to_ba=True, **kwargs):
        return self._log(LogSeverity.ALERT, message, send_to_ba=send_to_ba, labels=labels, **kwargs)
    
    def emergency(self, message: str, labels: t.Optional[t.Mapping[str, str]] = None, send_to_ba=True, **kwargs):
        return self._log(LogSeverity.EMERGENCY, message, send_to_ba=send_to_ba, labels=labels, **kwargs)
    
    def log_dbt_output(self, output: str):
        # add dbt=true label
        raise NotImplementedError()
