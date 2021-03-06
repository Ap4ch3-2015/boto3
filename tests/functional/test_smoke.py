# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from nose.tools import assert_true

from boto3.session import Session


def create_session():
    session = Session(aws_access_key_id='dummy',
                      aws_secret_access_key='dummy',
                      region_name='us-east-1')
    return session


def test_can_create_all_resources():
    """Verify we can create all existing resources."""
    session = create_session()
    for service_name in session.get_available_resources():
        yield _test_create_resource, session, service_name


def _test_create_resource(session, service_name):
    resource = session.resource(service_name)
    # Verifying we have a "meta" attr is just an arbitrary
    # sanity check.
    assert_true(hasattr(resource, 'meta'))


def test_can_create_all_clients():
    session = create_session()
    for service_name in session.get_available_services():
        yield _test_create_client, session, service_name


def _test_create_client(session, service_name):
    client = session.client(service_name)
    assert_true(hasattr(client, 'meta'))
