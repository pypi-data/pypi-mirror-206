import json
from dataclasses import (
    asdict,
    dataclass,
)
from typing import Optional
from unittest.mock import (
    create_autospec,
    mock_open,
)

import pytest
from terrascript import Terrascript

from reconcile.utils.external_resource_spec import ExternalResourceSpec
from reconcile.utils.secret_reader import SecretReaderBase
from reconcile.utils.terraform.config import TerraformS3BackendConfig
from reconcile.utils.terrascript.cloudflare_client import (
    AccountShardingStrategy,
    CloudflareAccountConfig,
    TerrascriptCloudflareClient,
    TerrascriptCloudflareClientFactory,
    create_cloudflare_terrascript,
)
from reconcile.utils.terrascript.cloudflare_resources import cloudflare_account
from reconcile.utils.terrascript.models import (
    CloudflareAccount,
    Integration,
    TerraformStateS3,
)

INTEGRATION = "qontract-reconcile-integration"


@pytest.fixture
def account_config():
    return CloudflareAccountConfig("account-name", "api-token", "account_id")


@pytest.fixture
def backend_config():
    return TerraformS3BackendConfig(
        "access-key",
        "secret-key",
        "bucket-name",
        "qontract-reconcile.tfstate",
        "us-east-1",
    )


@pytest.fixture
def cloudflare_account_test(account_config):
    cloudflare_account_values = {
        "name": account_config.name,
        "enforce_twofactor": account_config.enforce_twofactor,
        "type": account_config.type,
    }
    return cloudflare_account(
        account_config.name,
        **cloudflare_account_values,
    )


def test_create_cloudflare_resources_terraform_json(account_config, backend_config):
    """
    This test intentionally crosses many boundaries to cover most of the functionality
    from starting with an external resource spec definition to Terraform JSON config.
    The Terraform JSON config was generated by the code initially and tested with a
    `terraform plan`. This serves as a snapshot to ensure that there are not major
    changes in this functionality over time.
    """

    terrascript_client = create_cloudflare_terrascript(
        account_config, backend_config, "3.18"
    )

    cloudflare_client = TerrascriptCloudflareClient(terrascript_client)

    spec = ExternalResourceSpec(
        "cloudflare_zone",
        {"name": "dev", "automationToken": {}},
        {
            "provider": "zone",
            "identifier": "domain-com",
            "zone": "domain.com",
            "plan": "enterprise",
            "type": "partial",
            "records": [
                {
                    "name": "domain.com",
                    "identifier": "domiancomns1",
                    "type": "NS",
                    "ttl": 10,
                    "value": "ns1.domain.com",
                },
                {
                    "name": "domain.com",
                    "identifier": "domiancomns2",
                    "type": "NS",
                    "ttl": 10,
                    "value": "ns2.domain.com",
                },
            ],
            "certificates": [
                {
                    "identifier": "some-cert",
                    "type": "advanced",
                    "hosts": ["domain.com"],
                    "validation_method": "txt",
                    "validity_days": "90",
                    "certificate_authority": "lets_encrypt",
                    "cloudflare_branding": "false",
                    "wait_for_active_status": "false",
                }
            ],
        },
        {},
    )

    cf_account_member_spec = ExternalResourceSpec(
        "cloudflare",
        {"name": "cloudflare-account"},
        {
            "provider": "account_member",
            "identifier": "user1",
            "email_address": "user1@redhat.com",
            "account_id": "1234567890",
            "role_ids": ["abc123"],
            "cloudflare_account_roles": {
                "identifier": "cloudflare-account",
                "account_id": "${var.account_id}",
            },
        },
        {},
    )

    cf_logpush_ownership_challenge_for_zone = ExternalResourceSpec(
        "cloudflare",
        {"name": "cloudflare-account"},
        {
            "provider": "logpush_ownership_challenge",
            "identifier": "logpush_ownership_challenge_zone",
            "zone_name": "test-zone",
            "destination_conf": "s3://bucket/logs?region=us-east-1&sse=AES256",
        },
        {},
    )
    cf_logpush_ownership_challenge_for_account = ExternalResourceSpec(
        "cloudflare",
        {"name": "cloudflare-account"},
        {
            "provider": "logpush_ownership_challenge",
            "identifier": "logpush_ownership_challenge_account",
            "destination_conf": "s3://bucket/logs?region=us-east-1&sse=AES256",
        },
        {},
    )
    cf_logpush_job_for_zone = ExternalResourceSpec(
        "cloudflare",
        {"name": "cloudflare-account"},
        {
            "provider": "logpush_job",
            "identifier": "logpush_job_zone",
            "enabled": True,
            "zone_name": "test-zone",
            "logpull_options": "fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            "destination_conf": "s3://bucket/logs?region=us-east-1&sse=AES256",
            "ownership_challenge": "some-challenge",
            "dataset": "http_requests",
            "frequency": "high",
            "kind": "edge",
        },
        {},
    )
    cf_logpush_job_for_account = ExternalResourceSpec(
        "cloudflare",
        {"name": "cloudflare-account"},
        {
            "provider": "logpush_job",
            "identifier": "logpush_job_account",
            "enabled": True,
            "logpull_options": "fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            "destination_conf": "s3://bucket/logs?region=us-east-1&sse=AES256",
            "ownership_challenge": "some-challenge",
            "dataset": "http_requests",
            "frequency": "high",
            "job_name": "Logpush job for account",
            "filter": '{"key":"BotScore","operator":"lt","value":"30"}',
        },
        {},
    )
    cf_logpull_retention = ExternalResourceSpec(
        "cloudflare",
        {"name": "cloudflare-account"},
        {
            "provider": "logpull_retention",
            "identifier": "test",
            "zone": "test-zone",
            "enabled_flag": True,
        },
        {},
    )
    cloudflare_client.add_spec(spec)
    cloudflare_client.add_spec(cf_account_member_spec)
    cloudflare_client.add_spec(cf_logpush_ownership_challenge_for_zone)
    cloudflare_client.add_spec(cf_logpush_ownership_challenge_for_account)
    cloudflare_client.add_spec(cf_logpush_job_for_zone)
    cloudflare_client.add_spec(cf_logpush_job_for_account)
    cloudflare_client.add_spec(cf_logpull_retention)
    cloudflare_client.populate_resources()

    expected_dict = {
        "terraform": {
            "required_providers": {
                "cloudflare": {
                    "source": "cloudflare/cloudflare",
                    "version": "3.18",
                }
            },
            "backend": {
                "s3": {
                    "access_key": "access-key",
                    "secret_key": "secret-key",
                    "bucket": "bucket-name",
                    "key": "qontract-reconcile.tfstate",
                    "region": "us-east-1",
                }
            },
        },
        "provider": {
            "cloudflare": [
                {
                    "api_token": "api-token",
                    "account_id": "account_id",
                    "rps": 4,
                }
            ]
        },
        "data": {
            "cloudflare_account_roles": {
                "cloudflare-account": {"account_id": "${var.account_id}"}
            },
            "cloudflare_zone": {
                "test-zone": {"account_id": "${var.account_id}", "name": "test-zone"}
            },
        },
        "variable": {"account_id": {"default": "account_id", "type": "string"}},
        "resource": {
            "cloudflare_account_member": {
                "user1": {
                    "account_id": "1234567890",
                    "email_address": "user1@redhat.com",
                    "role_ids": ["abc123"],
                }
            },
            "cloudflare_account": {
                "account-name": {
                    "name": "account-name",
                    "enforce_twofactor": False,
                    "type": "standard",
                }
            },
            "cloudflare_zone": {
                "domain-com": {
                    "account_id": "${var.account_id}",
                    "zone": "domain.com",
                    "plan": "enterprise",
                    "type": "partial",
                }
            },
            "cloudflare_record": {
                "domiancomns1": {
                    "zone_id": "${cloudflare_zone.domain-com.id}",
                    "name": "domain.com",
                    "type": "NS",
                    "ttl": 10,
                    "value": "ns1.domain.com",
                    "depends_on": ["cloudflare_zone.domain-com"],
                },
                "domiancomns2": {
                    "zone_id": "${cloudflare_zone.domain-com.id}",
                    "name": "domain.com",
                    "type": "NS",
                    "ttl": 10,
                    "value": "ns2.domain.com",
                    "depends_on": ["cloudflare_zone.domain-com"],
                },
            },
            "cloudflare_zone_settings_override": {
                "domain-com": {
                    "zone_id": "${cloudflare_zone.domain-com.id}",
                    "settings": {},
                    "depends_on": ["cloudflare_zone.domain-com"],
                }
            },
            "cloudflare_certificate_pack": {
                "some-cert": {
                    "zone_id": "${cloudflare_zone.domain-com.id}",
                    "type": "advanced",
                    "hosts": ["domain.com"],
                    "validation_method": "txt",
                    "validity_days": "90",
                    "certificate_authority": "lets_encrypt",
                    "cloudflare_branding": "false",
                    "wait_for_active_status": "false",
                    "depends_on": ["cloudflare_zone.domain-com"],
                }
            },
            "cloudflare_logpush_ownership_challenge": {
                "logpush_ownership_challenge_zone": {
                    "destination_conf": "s3://bucket/logs?region=us-east-1&sse=AES256",
                    "zone_id": "${data.cloudflare_zone.test-zone.id}",
                },
                "logpush_ownership_challenge_account": {
                    "account_id": "${var.account_id}",
                    "destination_conf": "s3://bucket/logs?region=us-east-1&sse=AES256",
                },
            },
            "cloudflare_logpush_job": {
                "logpush_job_zone": {
                    "zone_id": "${data.cloudflare_zone.test-zone.id}",
                    "dataset": "http_requests",
                    "destination_conf": "s3://bucket/logs?region=us-east-1&sse=AES256",
                    "enabled": True,
                    "frequency": "high",
                    "logpull_options": "fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
                    "ownership_challenge": "some-challenge",
                    "kind": "edge",
                },
                "logpush_job_account": {
                    "account_id": "${var.account_id}",
                    "dataset": "http_requests",
                    "destination_conf": "s3://bucket/logs?region=us-east-1&sse=AES256",
                    "enabled": True,
                    "frequency": "high",
                    "logpull_options": "fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
                    "ownership_challenge": "some-challenge",
                    "name": "Logpush job for account",
                    "filter": '{"key":"BotScore","operator":"lt","value":"30"}',
                },
            },
            "cloudflare_logpull_retention": {
                "test": {
                    "enabled": True,
                    "zone_id": "${data.cloudflare_zone.test-zone.id}",
                }
            },
        },
        "output": {
            "domain-com-zone__validation_records": {
                "value": "${jsonencode({ for value in cloudflare_certificate_pack.some-cert.validation_records: value.txt_name => value.txt_value })}"
            }
        },
    }

    assert json.loads(cloudflare_client.dumps()) == expected_dict


def test_terrascript_cloudflare_client_dump(mocker):
    """
    Tests that dump() properly calls the Python filesystem implementations to write to
    disk.
    """
    mock_builtins_open = mock_open()
    mocker.patch("builtins.open", mock_builtins_open)

    patch_mkdtemp = mocker.patch("tempfile.mkdtemp")
    patch_mkdtemp.return_value = "/tmp/test"

    mock_terrascript = create_autospec(Terrascript)
    mock_terrascript.__str__.return_value = "some data"

    cloudflare_client = TerrascriptCloudflareClient(mock_terrascript)
    cloudflare_client.dump()

    patch_mkdtemp.assert_called_once()
    mock_builtins_open.assert_called_once_with("/tmp/test/config.tf.json", "w")
    mock_builtins_open.return_value.write.assert_called_once_with("some data")


def test_terrascript_cloudflare_client_dump_existing_dir(mocker):
    """
    Tests that dump() properly calls the Python filesystem implementations to write to
    disk when an existing_dir is specified.
    """
    mock_builtins_open = mock_open()
    mocker.patch("builtins.open", mock_builtins_open)

    patch_mkdtemp = mocker.patch("tempfile.mkdtemp")
    patch_mkdtemp.return_value = "/tmp/test"

    mock_terrascript = create_autospec(Terrascript)
    mock_terrascript.__str__.return_value = "some data"

    cloudflare_client = TerrascriptCloudflareClient(mock_terrascript)
    cloudflare_client.dump(existing_dir="/tmp/existing-dir")

    patch_mkdtemp.assert_not_called()
    mock_builtins_open.assert_called_once_with("/tmp/existing-dir/config.tf.json", "w")
    mock_builtins_open.return_value.write.assert_called_once_with("some data")


def test_create_cloudflare_terrascript(account_config, backend_config):
    """Simple test to ensure that the Terrascript object is initialized."""
    ts = create_cloudflare_terrascript(account_config, backend_config, "3.18")

    assert isinstance(ts, Terrascript)


def test_create_cloudflare_terrascript_contain_account(
    account_config, backend_config, cloudflare_account_test
):
    """To ensure that a expected cloudflare account config gets added"""
    ts = create_cloudflare_terrascript(account_config, backend_config, "3.18")

    for t in ts:
        if isinstance(t, cloudflare_account):
            assert t == cloudflare_account_test


def test_create_cloudflare_terrascript_not_include_account(
    account_config, backend_config
):
    """To ensure that cloudflare account not added to Terrascript when it is specified not managed by caller."""
    ts = create_cloudflare_terrascript(
        account_config, backend_config, "3.18", is_managed_account=False
    )

    for t in ts:
        assert not isinstance(t, cloudflare_account)


def secret_reader_side_effect(*args):
    if {
        "path": "automation_token_path",
        "field": "some-field",
        "version": None,
        "q_format": None,
    } == asdict(args[0]):
        aws_acct_creds = {}
        aws_acct_creds["aws_access_key_id"] = "key_id"
        aws_acct_creds["aws_secret_access_key"] = "access_key"
        return aws_acct_creds
    if {
        "path": "creds",
        "field": "some-field",
        "version": None,
        "q_format": None,
    } == asdict(args[0]):
        cf_acct_creds = {}
        cf_acct_creds["api_token"] = "api_token"
        cf_acct_creds["account_id"] = "account_id"
        return cf_acct_creds


@dataclass
class VaultSecret:
    path: str
    field: str
    version: Optional[int]
    q_format: Optional[str]


@pytest.fixture
def terraform_state_s3():
    tf_state_s3 = TerraformStateS3(
        VaultSecret(
            path="automation_token_path",
            field="some-field",
            version=None,
            q_format=None,
        ),
        "app-interface",
        "us-east-1",
        Integration(INTEGRATION.replace("_", "-"), "key"),
    )
    return tf_state_s3


@pytest.fixture
def cloudflare_account_dataclass():
    cf_account = CloudflareAccount(
        "test-account",
        VaultSecret(path="creds", field="some-field", version=None, q_format=None),
        True,
        "enterprise",
        "3.19",
    )
    return cf_account


@pytest.fixture
def secret_reader_fixture(mocker):
    mocked_secret_reader = mocker.Mock(spec=SecretReaderBase)
    mocked_secret_reader.read_all_secret.side_effect = secret_reader_side_effect
    return mocked_secret_reader


def test_cloudflare_client_factory_skip_account_resource(
    terraform_state_s3, cloudflare_account_dataclass, secret_reader_fixture
):
    """
    Tests that cloudflare terrascript resource 'cloudflare_account' is skipped
    """
    is_managed_account = False
    client = TerrascriptCloudflareClientFactory.get_client(
        terraform_state_s3,
        cloudflare_account_dataclass,
        None,
        secret_reader_fixture,
        is_managed_account,
    )

    output = json.loads(client.dumps())

    assert isinstance(client, TerrascriptCloudflareClient)

    with pytest.raises(KeyError):
        _ = output["resource"]["cloudflare_account"]


def test_cloudflare_client_factory_create_account_resource(
    terraform_state_s3, cloudflare_account_dataclass, secret_reader_fixture
):
    """
    Tests that cloudflare terrascript resource 'cloudflare_account' is created
    """

    is_managed_account = True
    client = TerrascriptCloudflareClientFactory.get_client(
        terraform_state_s3,
        cloudflare_account_dataclass,
        None,
        secret_reader_fixture,
        is_managed_account,
    )

    output = json.loads(client.dumps())

    expected_result = {
        "cloudflare_account": {
            "test-account": {
                "name": "test-account",
                "enforce_twofactor": True,
                "type": "enterprise",
            }
        }
    }
    assert isinstance(client, TerrascriptCloudflareClient)

    assert expected_result == output["resource"]


@pytest.mark.parametrize(
    "sharding_strategy,expected_key",
    [
        (None, "key"),
        (
            AccountShardingStrategy(
                CloudflareAccount(
                    "cf-acct",
                    VaultSecret(
                        path="api-credentials-path",
                        field="some-field",
                        version=None,
                        q_format=None,
                    ),
                    None,
                    None,
                    "3.19",
                )
            ),
            "qontract-reconcile-integration-cf-acct.tfstate",
        ),
    ],
)
def test_cloudflare_client_factory_object_key_strategies(
    terraform_state_s3,
    cloudflare_account_dataclass,
    secret_reader_fixture,
    sharding_strategy,
    expected_key,
):
    """
    Tests various sharding strategies for cloudflare terrascript client
    """

    client = TerrascriptCloudflareClientFactory.get_client(
        terraform_state_s3,
        cloudflare_account_dataclass,
        sharding_strategy,
        secret_reader_fixture,
        False,
    )

    output = json.loads(client.dumps())
    assert expected_key == output["terraform"]["backend"]["s3"]["key"]
