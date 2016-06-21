# -*- coding: utf-8 -*-
# @Author: ThomasO


class SwarmConfig(object):
    """
    """
    def __init__(self, swarm_image=None, swarm_master=False, swarm_discovery=None,
                 swarm_strategy=None, swarm_opts=[], swarm_host=None, swarm_addr=None):
        """
        Args:

        """
        self.swarm_image = swarm_image
        self.swarm_master = swarm_master
        self.swarm_discovery = swarm_discovery
        self.swarm_strategy = swarm_strategy
        self.swarm_opts = swarm_opts
        self.swarm_host = swarm_host
        self.swarm_addr = swarm_addr

    def args(self):
        """
        Format all arguments to the docker-machine syntax
        Mostly translating snake_case to spinal-case and adding prefix
        """
        args_list = []
        for k, v in vars(self).iteritems():
            if k == "swarm_master":
                args_list.append(self._format_key(k))
            else:
                key = self._format_key(k)
                value = self._format_val(v)
                if isinstance(value, list):
                    for elem in value:
                        if elem is not None:
                            args_list.append("{}={}".format(key, elem))
                elif value is not None:
                    args_list.append("{}={}".format(key, value))

        return args_list

    def _format_key(self, arg):
        """ format to spinal-case and add '--' """
        return '--{}'.format(arg.replace("_", "-"))

    def _format_val(self, arg):
        """ format boolean args """
        if (isinstance(arg, bool)):
            return 'true' if arg else 'false'
        return arg
