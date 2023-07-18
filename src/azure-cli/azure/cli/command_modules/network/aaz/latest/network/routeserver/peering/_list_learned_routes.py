# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network routeserver peering list-learned-routes",
)
class ListLearnedRoutes(AAZCommand):
    """List all routes the route server bgp connection has learned.

    :example: List.
        az network routeserver peering list-learned-routes -g MyResourceGroup --routeserver MyRouteServer -n MyRouteServerPeer
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/virtualhubs/{}/bgpconnections/{}/learnedroutes", "2022-01-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the Route Server Peering.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.routeserver = AAZStrArg(
            options=["--routeserver"],
            help="The name of the Route Server.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.VirtualHubBgpConnectionsListLearnedRoutes(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class VirtualHubBgpConnectionsListLearnedRoutes(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{hubName}/bgpConnections/{connectionName}/learnedRoutes",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "connectionName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "hubName", self.ctx.args.routeserver,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZDictType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.Element = AAZListType()

            _element = cls._schema_on_200.Element
            _element.Element = AAZObjectType()

            _element = cls._schema_on_200.Element.Element
            _element.as_path = AAZStrType(
                serialized_name="asPath",
                flags={"read_only": True},
            )
            _element.local_address = AAZStrType(
                serialized_name="localAddress",
                flags={"read_only": True},
            )
            _element.network = AAZStrType(
                flags={"read_only": True},
            )
            _element.next_hop = AAZStrType(
                serialized_name="nextHop",
                flags={"read_only": True},
            )
            _element.origin = AAZStrType(
                flags={"read_only": True},
            )
            _element.source_peer = AAZStrType(
                serialized_name="sourcePeer",
                flags={"read_only": True},
            )
            _element.weight = AAZIntType(
                flags={"read_only": True},
            )

            return cls._schema_on_200


class _ListLearnedRoutesHelper:
    """Helper class for ListLearnedRoutes"""


__all__ = ["ListLearnedRoutes"]
