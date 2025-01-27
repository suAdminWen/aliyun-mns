from aliyunsdkcore.request import RpcRequest


class QueryTokenForMnsQueueRequest(RpcRequest):

    def __init__(self):
        RpcRequest.__init__(self, 'Dybaseapi', '2017-05-25',
                            'QueryTokenForMnsQueue', 'dybaseapi')

    def get_QueueName(self):
        return self.get_query_params().get('QueueName')

    def set_QueueName(self, QueueName):
        self.add_query_param('QueueName', QueueName)

    def get_ResourceOwnerId(self):
        return self.get_query_params().get('ResourceOwnerId')

    def set_ResourceOwnerId(self, ResourceOwnerId):
        self.add_query_param('ResourceOwnerId', ResourceOwnerId)

    def get_ResourceOwnerAccount(self):
        return self.get_query_params().get('ResourceOwnerAccount')

    def set_ResourceOwnerAccount(self, ResourceOwnerAccount):
        self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)

    def get_MessageType(self):
        return self.get_query_params().get('MessageType')

    def set_MessageType(self, MessageType):
        self.add_query_param('MessageType', MessageType)

    def get_OwnerId(self):
        return self.get_query_params().get('OwnerId')

    def set_OwnerId(self, OwnerId):
        self.add_query_param('OwnerId', OwnerId)
