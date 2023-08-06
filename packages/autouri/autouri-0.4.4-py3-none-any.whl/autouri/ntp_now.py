"""Accurate now() based on cached offset between NTP server
and local system time.

Make sure not to change system time once the offset is cached.
"""

import logging
from datetime import datetime, timezone

import ntplib

logger = logging.getLogger(__name__)

DEFAULT_NTP_SERVER = "pool.ntp.org"
cached_offset_between_ntp_server_and_local_system = None


def now_utc(ntp_server=DEFAULT_NTP_SERVER):
    global cached_offset_between_ntp_server_and_local_system

    if cached_offset_between_ntp_server_and_local_system is not None:
        return (
            datetime.now(timezone.utc)
            + cached_offset_between_ntp_server_and_local_system
        )

    try:
        resp = ntplib.NTPClient().request(ntp_server)
        adjusted_timestamp = resp.tx_time + resp.delay * 0.5
        ntp_server_time = datetime.fromtimestamp(adjusted_timestamp, timezone.utc)
        # update cache
        cached_offset_between_ntp_server_and_local_system = (
            ntp_server_time - datetime.now(timezone.utc)
        )
        logger.debug(
            "Successfully retrieved time from NTP server {srv}. time:{time}, offset:{offset}".format(
                srv=ntp_server,
                time=ntp_server_time,
                offset=cached_offset_between_ntp_server_and_local_system.total_seconds(),
            )
        )
        return ntp_server_time

    except Exception as e:
        logger.debug(
            "Failed to retrieve time from NTP server {srv}. error {err}".format(
                srv=ntp_server, err=str(e)
            )
        )

    return datetime.now(timezone.utc)


def reset_cached_offset():
    global cached_offset_between_ntp_server_and_local_system
    cached_offset_between_ntp_server_and_local_system = None


def get_cached_offset():
    global cached_offset_between_ntp_server_and_local_system
    return cached_offset_between_ntp_server_and_local_system
