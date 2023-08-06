#!/usr/bin/env python3

# Copyright (c) 2000-2023, Board of Trustees of Leland Stanford Jr. University
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import zeep.exceptions
import zeep.helpers

from lockss.soap.util import _construct_query, _make_client


SERVICE = 'DaemonStatusService'


def get_au_article_urls(node_object, auid):
    res = query_aus(node_object, ['articleUrls'], where=f'auId = "{auid}"')
    return res[0].get('articleUrls', []) if len(res) > 0 else None


def get_au_status(node_object, auid):
    try:
        client = _make_client(node_object, SERVICE)
        ret = client.service.getAuStatus(auId=auid)
        return zeep.helpers.serialize_object(ret)
    except zeep.exceptions.Fault as exc:
        if exc.message == 'No Archival Unit with provided identifier':
            return None
        else:
            raise


def get_au_substance_urls(node_object, auid):
    res = query_aus(node_object, ['substanceUrls'], where=f'auId = "{auid}"')
    return res[0].get('substanceUrls', []) if len(res) > 0 else None


def get_au_type_urls(node_object, auid, typ):
    if typ == 'articleUrls':
        return get_au_article_urls(node_object, auid)
    elif typ == 'substanceUrls':
        return get_au_substance_urls(node_object, auid)
    else:
        raise Exception(f'invalid URL type: {typ}')


def get_au_urls(node_object, auid, prefix=None):
    try:
        client = _make_client(node_object, SERVICE)
        ret = client.service.getAuUrls(auId=auid, url=prefix)
        return ret
    except zeep.exceptions.Fault as exc:
        if exc.message == 'No Archival Unit with provided identifier':
            return None
        else:
            raise


def get_auids(node_object):
    client = _make_client(node_object, SERVICE)
    ret = client.service.getAuIds()
    return zeep.helpers.serialize_object(ret)


def get_peer_agreements(node_object, auid):
    res = query_aus(node_object, ['peerAgreements'], where=f'auId = "{auid}"')
    return zeep.helpers.serialize_object(res[0]).get('peerAgreements') if len(res) > 0 else None


def get_platform_configuration(node_object):
    client = _make_client(node_object, SERVICE)
    ret = client.service.getPlatformConfiguration()
    return zeep.helpers.serialize_object(ret)


def is_daemon_ready(node_object):
    client = _make_client(node_object, SERVICE)
    ret = client.service.isDaemonReady()
    return ret


def query_aus(node_object, select, where=None):
    client = _make_client(node_object, SERVICE)
    query = _construct_query(select, where)
    ret = client.service.queryAus(auQuery=query)
    return zeep.helpers.serialize_object(ret)


def query_crawls(node_object, select, where=None):
    client = _make_client(node_object, SERVICE)
    query = _construct_query(select, where)
    ret = client.service.queryCrawls(crawlQuery=query)
    return zeep.helpers.serialize_object(ret)


def query_polls(node_object, select, where=None):
    client = _make_client(node_object, SERVICE)
    query = _construct_query(select, where)
    ret = client.service.queryPolls(pollQuery=query)
    return zeep.helpers.serialize_object(ret)


def query_tdb_titles(*args, **kwargs):
    raise NotImplementedError('query_tdb_titles()')
