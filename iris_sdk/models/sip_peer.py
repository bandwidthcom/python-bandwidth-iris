#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.sip_peer import SipPeerData

from iris_sdk.models.data.address import Address
from iris_sdk.models.data.calling_name import CallingName
from iris_sdk.models.data.hosts import Hosts
from iris_sdk.models.data.termination_hosts import TerminationHosts
from iris_sdk.models.maps.sip_peer import SipPeerMap

XPATH_SIP_PEER = "/{}"

class SipPeer(BaseResource, SipPeerData):

    """Site SIP peer"""

    _xpath = XPATH_SIP_PEER

    @property
    def name(self):
        return self.peer_name
    @name.setter
    def name(self, name):
        self.peer_name = name

    @property
    def peer_id(self):
        return self._id
    @peer_id.setter
    def peer_id(self, peer_id):
        self._id = peer_id

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        SipPeerData.__init__(self)

    def get(self, id):
        return self.get_data(id)