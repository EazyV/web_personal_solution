from fast_bitrix24 import Bitrix


class BitrixClient:
    def __init__(self, webhook):
        self.webhook = webhook
        self.bx = Bitrix(self.webhook)

    def create_lead(self, lead_data):
        response = self.bx.call('crm.lead.add', lead_data)
