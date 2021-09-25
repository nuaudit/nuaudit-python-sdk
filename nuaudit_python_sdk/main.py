from typing import Dict, Any
from nuaudit_python_autogen import Configuration, ApiClient
from nuaudit_python_autogen.models import RecordMutation, ActorRecordMutation, ResourceRecordMutation
from nuaudit_python_autogen.api.records_api import RecordsApi

class Nuaudit:
    def __init__(self, api_key: str, organization_id: str, trail_id: str):
        self.api_key = api_key
        self.organization_id = organization_id
        self.trail_id = trail_id
        
        configuration = Configuration()
        configuration.api_key['APIKeyHeader'] = self.api_key
        self.api_client = ApiClient(configuration=configuration)
        
        self.records_api = RecordsApi(api_client=self.api_client)

    def create_record(self, description: str, actor: Dict[Any, Any], resource: Dict[Any, Any]):
        self.records_api.create_record(
            organization_id=self.organization_id,
            trail_id=self.trail_id,
            record_mutation=RecordMutation(
                description=description,
                actor_record=ActorRecordMutation(
                    data=actor
                ),
                resource_record=ResourceRecordMutation(
                    data=resource
                )
            )
        )

