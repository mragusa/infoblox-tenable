#!/usr/bin/env python3

import getpass
import sys
import click
from ibx_sdk.nios.exceptions import WapiRequestException
from ibx_sdk.nios.gift import Gift


@click.command()
@click.option("-g", "--grdmgr", required=True, help="Infoblox Grid Manager")
@click.option("-u", "--username", required=True, help="Infoblox Login Username")
def main(grdmgr: str, username: str):
    tenable_nios_ea = [
        {
            "name": "TNBL_Sync",
            "comment": "Sync the object",
            "type": "ENUM",
            "flags": "AI",
            "list_values": [{"value": "true"}, {"value": "false"}],
            "descendants_action": {
                "option_with_ea": "INHERIT",
                "option_delete_ea": "REMOVE",
                "option_without_ea": "INHERIT",
            },
            "default_value": "true",
        },
        {"name": "TNBL_SyncTime", "comment": "Sync Date/Time", "type": "STRING"},
        {
            "name": "TNBL_AddNet",
            "comment": "Add a network to Tenable",
            "type": "ENUM",
            "flags": "AI",
            "list_values": [{"value": "true"}, {"value": "false"}],
            "descendants_action": {
                "option_with_ea": "INHERIT",
                "option_delete_ea": "REMOVE",
                "option_without_ea": "INHERIT",
            },
            "default_value": "true",
        },
        {
            "name": "TNBL_AddRange",
            "comment": "Add a range to Tenable",
            "type": "ENUM",
            "flags": "AI",
            "list_values": [{"value": "true"}, {"value": "false"}],
            "descendants_action": {
                "option_with_ea": "INHERIT",
                "option_delete_ea": "REMOVE",
                "option_without_ea": "INHERIT",
            },
            "default_value": "true",
        },
        {
            "name": "TNBL_ScanOnEvnt",
            "comment": "Scan an asset by an event",
            "type": "ENUM",
            "flags": "AI",
            "list_values": [{"value": "true"}, {"value": "false"}],
            "descendants_action": {
                "option_with_ea": "INHERIT",
                "option_delete_ea": "REMOVE",
                "option_without_ea": "INHERIT",
            },
            "default_value": "true",
        },
        {
            "name": "TNBL_ScanOnAdd",
            "comment": "Scan an asset after provisioning",
            "type": "ENUM",
            "flags": "AI",
            "list_values": [{"value": "true"}, {"value": "false"}],
            "descendants_action": {
                "option_with_ea": "INHERIT",
                "option_delete_ea": "REMOVE",
                "option_without_ea": "INHERIT",
            },
            "default_value": "true",
        },
        {
            "name": "TNBL_ScanTemplate",
            "comment": "Tenable Scan Template",
            "type": "ENUM",
            "flags": "AI",
            "list_values": [{"value": "IB-Scan"}],
            "descendants_action": {
                "option_with_ea": "INHERIT",
                "option_delete_ea": "REMOVE",
                "option_without_ea": "INHERIT",
            },
            "default_value": "IB-Scan",
        },
        {
            "name": "TNBL_ScanTemplateID",
            "comment": "Tenable Scan ID. Updated automatically",
            "type": "INTEGER",
            "flags": "I",
            "descendants_action": {
                "option_with_ea": "INHERIT",
                "option_delete_ea": "REMOVE",
                "option_without_ea": "INHERIT",
            },
            "default_value": "0",
        },
        {
            "name": "TNBL_AssetIP",
            "comment": "Assets Fixed IP",
            "type": "ENUM",
            "flags": "AI",
            "list_values": [{"value": "IB Static"}],
            "descendants_action": {
                "option_with_ea": "INHERIT",
                "option_delete_ea": "REMOVE",
                "option_without_ea": "INHERIT",
            },
            "default_value": "IB Static",
        },
        {
            "name": "TNBL_AssetIPID",
            "comment": "ID Assets Fixed IP. Updated automatically",
            "type": "INTEGER",
            "flags": "I",
            "descendants_action": {
                "option_with_ea": "INHERIT",
                "option_delete_ea": "REMOVE",
                "option_without_ea": "INHERIT",
            },
            "default_value": "0",
        },
        {
            "name": "TNBL_AssetHost",
            "comment": "Assets Fixed Hostnames",
            "type": "ENUM",
            "flags": "AI",
            "list_values": [{"value": "IB Static DNS"}],
            "descendants_action": {
                "option_with_ea": "INHERIT",
                "option_delete_ea": "REMOVE",
                "option_without_ea": "INHERIT",
            },
            "default_value": "IB Static DNS",
        },
        {
            "name": "TNBL_AssetHostID",
            "comment": "ID Assets Fixed Hostnames. Updated automatically",
            "type": "INTEGER",
            "flags": "I",
            "descendants_action": {
                "option_with_ea": "INHERIT",
                "option_delete_ea": "REMOVE",
                "option_without_ea": "INHERIT",
            },
            "default_value": "0",
        },
        {
            "name": "TNBL_ScanTime",
            "comment": "Last Scan Date. Updated automatically",
            "type": "STRING",
            "descendants_action": {
                "option_with_ea": "INHERIT",
                "option_delete_ea": "REMOVE",
                "option_without_ea": "INHERIT",
            },
            "default_value": "0",
        },
        {
            "name": "TNBL_AddByHostname",
            "comment": "Add a host by a hostname",
            "type": "ENUM",
            "flags": "I",
            "list_values": [{"value": "true"}, {"value": "false"}],
            "descendants_action": {
                "option_with_ea": "INHERIT",
                "option_delete_ea": "REMOVE",
                "option_without_ea": "INHERIT",
            },
            "default_value": "true",
        },
    ]

    wapi = Gift()
    wapi.grid_mgr = grdmgr
    password = getpass.getpass("Enter Infoblox Password: ")
    try:
        wapi.connect(username=username, password=password)
    except WapiRequestException as err:
        print(err)
        sys.exit(1)

    for ea in tenable_nios_ea:
        try:
            tnbl_ea = wapi.post("extensibleattributedef", json=ea)
            if tnbl_ea != 201:
                print(tnbl_ea.status_code, tnbl_ea.text)
            else:
                print(tnbl_ea.json())
        except WapiRequestException as err:
            print(err)


if __name__ == "__main__":
    main()
