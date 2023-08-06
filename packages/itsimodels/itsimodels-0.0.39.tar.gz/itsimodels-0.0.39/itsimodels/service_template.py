from itsimodels.core.base_models import BaseModel
from itsimodels.core.compat import string_types
from itsimodels.core.fields import ForeignKey, ForeignKeyList, ListField, StringField
from itsimodels.service import EntityRule, Kpi


class ServiceTemplate(BaseModel):
    key = StringField(required=True, alias='_key')

    title = StringField(required=True)

    description = StringField(default='')

    entity_rules = ListField(EntityRule)

    kpis = ListField(Kpi)

    linked_services = ForeignKeyList('itsimodels.service.Service')

    sync_status = StringField()

    team_id = ForeignKey('itsimodels.team.Team', default='default_itsi_security_group', alias='sec_grp')

    template_tags = ListField(string_types)
