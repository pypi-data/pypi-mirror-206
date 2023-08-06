#  _  __
# | |/ /___ ___ _ __  ___ _ _ ®
# | ' </ -_) -_) '_ \/ -_) '_|
# |_|\_\___\___| .__/\___|_|
#              |_|
#
# Keeper Commander
# Copyright 2022 Keeper Security Inc.
# Contact: ops@keepersecurity.com
#

import json
from typing import Optional, Dict, Any

from . import vault_types, vault_online
from .. import utils, crypto, errors


def add_folder(vault: vault_online.VaultOnline, folder_name: str, is_shared_folder: bool=False,
               parent_uid: Optional[str]=None, manage_records: Optional[bool]=None, manage_users: Optional[bool]=None,
               can_share: Optional[bool]=None, can_edit: Optional[bool]=None) -> str:
    parent_type: vault_types.FolderType = 'user_folder'
    folder_type: vault_types.FolderType = 'user_folder'
    shared_folder_uid = None
    if parent_uid:
        folder = vault.get_folder(parent_uid)
        if folder is None:
            raise errors.KeeperError(f'Parent folder UID \"{parent_uid}\" not found.')
        parent_type = folder.folder_type
        if parent_type == 'shared_folder':
            shared_folder_uid = folder.folder_uid
        elif parent_type == 'shared_folder_folder':
            shared_folder_uid = folder.folder_scope_uid
    if is_shared_folder:
        if parent_type != "user_folder":
            raise errors.KeeperError('Shared folder cannot be created.')
        folder_type = "shared_folder"
    else:
        if parent_type != "user_folder":
            folder_type = "shared_folder_folder"
    if folder_type == 'shared_folder_folder':
        assert shared_folder_uid is not None
        encryption_key = vault.get_shared_folder_key(shared_folder_uid)
        if encryption_key is None:
            raise errors.KeeperError('Shared folder key cannot be resolved.')
    else:
        encryption_key = vault.keeper_auth.auth_context.data_key
    folder_uid = utils.generate_uid()
    folder_key = utils.generate_aes_key()
    data = {
        'name': folder_name
    }
    encrypted_data = crypto.encrypt_aes_v1(json.dumps(data).encode(), folder_key)
    rq: Dict[str, Any] = {
        'command': 'folder_add',
        'folder_uid': folder_uid,
        'folder_type': folder_type,
        'key': utils.base64_url_encode(crypto.encrypt_aes_v1(folder_key, encryption_key)),
        'data': utils.base64_url_encode(encrypted_data),
    }
    if parent_uid:
        rq['parent_uid'] = parent_uid
    if shared_folder_uid:
        rq['shared_folder_uid'] = shared_folder_uid
    if is_shared_folder:
        rq['name'] = utils.base64_url_encode(crypto.encrypt_aes_v1(folder_name.encode(), folder_key))
        rq['manage_users'] = manage_users if isinstance(manage_users, bool) else False
        rq['manage_records'] = manage_records if isinstance(manage_records, bool) else False
        rq['can_edit'] = can_edit if isinstance(can_edit, bool) else False
        rq['can_share'] = can_share if isinstance(can_share, bool) else False

    vault.keeper_auth.execute_auth_command(rq)
    vault.sync_requested = True
    return folder_uid


def update_folder(vault: vault_online.VaultOnline, folder_uid: str, folder_name: Optional[str]=None,
                  manage_records: Optional[bool]=None, manage_users: Optional[bool]=None,
                  can_share: Optional[bool]=None, can_edit: Optional[bool]=None) -> None:
    folder = vault.get_folder(folder_uid)
    if folder is None:
        raise ValueError(f'Folder {folder_uid} does not exist')
    data = {
        'name': folder_name or folder.name
    }
    encrypted_data = crypto.encrypt_aes_v1(json.dumps(data).encode(), folder.folder_key)
    rq: Dict[str, Any] = {
        'command': 'folder_update',
        'folder_uid': folder.folder_uid,
        'folder_type': folder.folder_type,
        'data': utils.base64_url_encode(crypto.encrypt_aes_v1(encrypted_data, folder.folder_key)),
    }
    if folder.folder_type == 'shared_folder':
        shared_folder = vault.load_shared_folder(folder_uid)
        if shared_folder is None:
            raise ValueError(f'Shared Folder {folder_uid} does not exist')
        name = folder_name or folder.name
        rq['name'] = utils.base64_url_encode(crypto.encrypt_aes_v1(name.encode(), folder.folder_key))
        rq['manage_users'] = manage_users if isinstance(manage_users, bool) \
            else shared_folder.default_manage_records
        rq['manage_records'] = manage_records if isinstance(manage_records, bool) \
            else shared_folder.default_manage_records
        rq['can_edit'] = can_edit if isinstance(can_edit, bool) else shared_folder.default_can_edit
        rq['can_share'] = can_share if isinstance(can_share, bool) else shared_folder.default_can_share

    vault.keeper_auth.execute_auth_command(rq)
    vault.sync_requested = True
