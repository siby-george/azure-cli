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
    "monitor log-analytics cluster list",
)
class List(AAZCommand):
    """List all cluster instances in a resource group or in current subscription.

    :example: List all cluster instances in a resource group.
        az monitor log-analytics cluster list -g MyResourceGroup

    :example: List all cluster instances in current subscription.
        az monitor log-analytics cluster list
    """

    _aaz_info = {
        "version": "2021-06-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.operationalinsights/clusters", "2021-06-01"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.operationalinsights/clusters", "2021-06-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id)
        condition_1 = has_value(self.ctx.subscription_id) and has_value(self.ctx.args.resource_group) is not True
        if condition_0:
            self.ClustersListByResourceGroup(ctx=self.ctx)()
        if condition_1:
            self.ClustersList(ctx=self.ctx)()
        self.post_operations()

    # @register_callback
    def pre_operations(self):
        pass

    # @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class ClustersListByResourceGroup(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/clusters",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
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
                    "api-version", "2021-06-01",
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

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.identity = AAZObjectType()
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.sku = AAZObjectType()
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.value.Element.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.value.Element.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.associated_workspaces = AAZListType(
                serialized_name="associatedWorkspaces",
                flags={"read_only": True},
            )
            properties.billing_type = AAZStrType(
                serialized_name="billingType",
            )
            properties.capacity_reservation_properties = AAZObjectType(
                serialized_name="capacityReservationProperties",
            )
            properties.cluster_id = AAZStrType(
                serialized_name="clusterId",
                flags={"read_only": True},
            )
            properties.created_date = AAZStrType(
                serialized_name="createdDate",
                flags={"read_only": True},
            )
            properties.is_availability_zones_enabled = AAZBoolType(
                serialized_name="isAvailabilityZonesEnabled",
            )
            properties.key_vault_properties = AAZObjectType(
                serialized_name="keyVaultProperties",
            )
            properties.last_modified_date = AAZStrType(
                serialized_name="lastModifiedDate",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            associated_workspaces = cls._schema_on_200.value.Element.properties.associated_workspaces
            associated_workspaces.Element = AAZObjectType(
                flags={"read_only": True},
            )

            _element = cls._schema_on_200.value.Element.properties.associated_workspaces.Element
            _element.associate_date = AAZStrType(
                serialized_name="associateDate",
                flags={"read_only": True},
            )
            _element.resource_id = AAZStrType(
                serialized_name="resourceId",
                flags={"read_only": True},
            )
            _element.workspace_id = AAZStrType(
                serialized_name="workspaceId",
                flags={"read_only": True},
            )
            _element.workspace_name = AAZStrType(
                serialized_name="workspaceName",
                flags={"read_only": True},
            )

            capacity_reservation_properties = cls._schema_on_200.value.Element.properties.capacity_reservation_properties
            capacity_reservation_properties.last_sku_update = AAZStrType(
                serialized_name="lastSkuUpdate",
                flags={"read_only": True},
            )
            capacity_reservation_properties.min_capacity = AAZIntType(
                serialized_name="minCapacity",
                flags={"read_only": True},
            )

            key_vault_properties = cls._schema_on_200.value.Element.properties.key_vault_properties
            key_vault_properties.key_name = AAZStrType(
                serialized_name="keyName",
            )
            key_vault_properties.key_rsa_size = AAZIntType(
                serialized_name="keyRsaSize",
            )
            key_vault_properties.key_vault_uri = AAZStrType(
                serialized_name="keyVaultUri",
            )
            key_vault_properties.key_version = AAZStrType(
                serialized_name="keyVersion",
            )

            sku = cls._schema_on_200.value.Element.sku
            sku.capacity = AAZIntType()
            sku.name = AAZStrType()

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200

    class ClustersList(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.OperationalInsights/clusters",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
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
                    "api-version", "2021-06-01",
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

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.identity = AAZObjectType()
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.sku = AAZObjectType()
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.value.Element.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.value.Element.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.associated_workspaces = AAZListType(
                serialized_name="associatedWorkspaces",
                flags={"read_only": True},
            )
            properties.billing_type = AAZStrType(
                serialized_name="billingType",
            )
            properties.capacity_reservation_properties = AAZObjectType(
                serialized_name="capacityReservationProperties",
            )
            properties.cluster_id = AAZStrType(
                serialized_name="clusterId",
                flags={"read_only": True},
            )
            properties.created_date = AAZStrType(
                serialized_name="createdDate",
                flags={"read_only": True},
            )
            properties.is_availability_zones_enabled = AAZBoolType(
                serialized_name="isAvailabilityZonesEnabled",
            )
            properties.key_vault_properties = AAZObjectType(
                serialized_name="keyVaultProperties",
            )
            properties.last_modified_date = AAZStrType(
                serialized_name="lastModifiedDate",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            associated_workspaces = cls._schema_on_200.value.Element.properties.associated_workspaces
            associated_workspaces.Element = AAZObjectType(
                flags={"read_only": True},
            )

            _element = cls._schema_on_200.value.Element.properties.associated_workspaces.Element
            _element.associate_date = AAZStrType(
                serialized_name="associateDate",
                flags={"read_only": True},
            )
            _element.resource_id = AAZStrType(
                serialized_name="resourceId",
                flags={"read_only": True},
            )
            _element.workspace_id = AAZStrType(
                serialized_name="workspaceId",
                flags={"read_only": True},
            )
            _element.workspace_name = AAZStrType(
                serialized_name="workspaceName",
                flags={"read_only": True},
            )

            capacity_reservation_properties = cls._schema_on_200.value.Element.properties.capacity_reservation_properties
            capacity_reservation_properties.last_sku_update = AAZStrType(
                serialized_name="lastSkuUpdate",
                flags={"read_only": True},
            )
            capacity_reservation_properties.min_capacity = AAZIntType(
                serialized_name="minCapacity",
                flags={"read_only": True},
            )

            key_vault_properties = cls._schema_on_200.value.Element.properties.key_vault_properties
            key_vault_properties.key_name = AAZStrType(
                serialized_name="keyName",
            )
            key_vault_properties.key_rsa_size = AAZIntType(
                serialized_name="keyRsaSize",
            )
            key_vault_properties.key_vault_uri = AAZStrType(
                serialized_name="keyVaultUri",
            )
            key_vault_properties.key_version = AAZStrType(
                serialized_name="keyVersion",
            )

            sku = cls._schema_on_200.value.Element.sku
            sku.capacity = AAZIntType()
            sku.name = AAZStrType()

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


__all__ = ["List"]