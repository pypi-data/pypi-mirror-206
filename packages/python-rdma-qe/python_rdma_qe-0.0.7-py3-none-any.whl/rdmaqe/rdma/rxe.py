"""rxe.py: Module to check/configure RXE (Software RDMA over Ethernet)."""

__author__ = "Zhaojuan Guo"
__copyright__ = "Copyright (c) 2023 Red Hat, Inc. All ritype rxe netdevghts reserved."

from libsan.host.cmdline import run


def rxe_setup(link_name="rxe_eno2", netdev="eno2"):
    """
    @param link_name: name of the new link
    @param netdev: name of an Ethernet device
    @return: zero if succeed to set up rxe. Otherwise, return non-zero
    """
    _cmd = "modprobe rdma_rxe"
    retcode = run(_cmd)
    if retcode != 0:
        print("ERROR: failed to modprobe rdma_rxe")
        return retcode
    _cmd = "rdma link add " + link_name + " type rxe netdev " + netdev
    retcode = run(_cmd)
    if retcode != 0:
        print("ERROR: add rxe link failed")
        return retcode
    run("rdma link show")
    return retcode


def check_rxe_paras(link_name="rxe_eno2"):
    """
    @param link_name: name of the rxe link
    @return: None
    """
    _cmd = "rdma link show " + "| grep " + link_name
    run(_cmd)
    _cmd = "ibv_devinfo -d " + link_name
    run(_cmd)


def rxe_delete(link_name="rxe_eno2"):
    """
    @param link_name: name of the rxe link
    @return: zero if succeed in deleting the rxe link, otherwise, return non-zero
    """
    _cmd = "rdma link delete " + link_name
    retcode = run(_cmd)
    if retcode != 0:
        print("ERROR: failed to delete the rxe link")
        return retcode
    run("rdma link show")
    return retcode

