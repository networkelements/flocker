# Copyright Hybrid Logic Ltd.  See LICENSE file for details.

"""
Objects related to an in-memory implementation of ``INetwork``.
"""

from zope.interface import implementer
from eliot import Logger

from ._interfaces import INetwork
from ._model import Proxy


@implementer(INetwork)
class MemoryNetwork(object):
    """
    An isolated, in-memory-only implementation of ``INetwork``.

    :ivar set _proxies: A ``set`` of ``Proxy`` instances representing all of
        the proxies supposedly configured on this network.
    """
    logger = Logger()

    def __init__(self):
        self._proxies = set()

    def create_proxy_to(self, ip, port):
        proxy = Proxy(ip=ip, port=port)
        self._proxies.add(proxy)
        return proxy

    def delete_proxy(self, proxy):
        self._proxies.remove(proxy)

    def enumerate_proxies(self):
        return list(self._proxies)


def make_memory_network():
    """
    Create a new, isolated, in-memory-only provider of ``INetwork``.
    """
    return MemoryNetwork()
