import logging
from pathlib import Path
from typing import Dict, List, Union

import streamlit as st
from odmantic import Model, SyncEngine, query
from pymongo import MongoClient

from .config import StreamlitBaseSettings
from .storage import FileRef

# from streamlit.runtime.uploaded_file_manager import UploadedFile # FIXME: remove if unneeded?


# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def get_engine():
    settings = StreamlitBaseSettings()
    if settings.MONGO_CONNECTION_STRING is None:
        raise ValueError("Can't get mongo engine when connection string is None.")

    client = MongoClient(settings.MONGO_CONNECTION_STRING)
    return SyncEngine(client=client, database=settings.DATABASE_NAME)


class Project(Model):
    name: str
    description: str = ""
    public: bool = False
    application: str = "mpl"  # Name of the application that creates the project
    files: List[FileRef] = []
    folders: List[str] = []
    owner: str = ""
    users: List[str] = []  # Users with access to this project

    def exists(self, engine=None) -> bool:
        if engine is None:
            engine = get_engine()
        return get_engine().count(Project, Project.id == self.id) > 0

    def is_duplicate(self, engine=None) -> bool:
        if engine is None:
            engine = get_engine()
        return (
            engine.count(Project, (Project.id != self.id) & (Project.name == self.name) & (Project.owner == self.owner))
            > 0
        )

    def get_users_string(self):
        return ",".join(self.users)

    def get_folders_map(self):
        fol_dict = {}
        fol_dict["/"] = "Project Root"
        for folder in self.folders:
            parts = folder.strip("/").split("/")
            fol_dict[folder] = " - ".join(parts)
        return fol_dict

    @classmethod
    def list_owned(cls, engine, owner) -> List["Project"]:
        return list(engine.find(cls, Project.owner == owner))

    def save(self) -> "Project":
        _ = get_engine().find_one(Project, Project.id == self.id)
        _.update(self.dict(exclude_unset=True, exclude={"id"}))
        return get_engine().save(_)

    def get_folder_path(self, folder):
        return f"{str(self.id)}/{self.name}/{folder}".strip("/")

    def get_files_in_folder(self, folder: str, include_subfolders=True, extensions=None, null_option=None):
        _files: Dict[str, Union[None, FileRef]] = {} if null_option is None else {null_option: None}

        path = self.get_folder_path(folder)
        for file in self.files:
            if path in file.path:
                file_path = file.path.removeprefix(path).strip("/")
                if (include_subfolders or file_path.find("/") == 0) and (
                    extensions is None or str(Path(file.name).suffix.lower()) in extensions
                ):
                    _files[file_path] = file

        return _files

    def populate_node(self, _dict, part, parts):
        if part not in _dict:
            _dict[part] = {}

        if parts:
            self.populate_node(_dict[part], parts[0], parts[1:])

    def populate_children(self, _dict, key, children, path):
        if child_dict := _dict[key]:
            for child_key in child_dict:
                new_children = None
                new_path = f"{path}/{child_key}"
                if child_dict[child_key]:
                    new_children = []
                    self.populate_children(child_dict, child_key, new_children, new_path)
                children.append({"label": child_key, "value": f"{path}/{child_key}", "children": new_children})

    def get_file_tree(self):
        main_dict = {}
        full_list = (
            [file.path.removeprefix(self.get_folder_path("")).strip("/") for file in self.files] if self.files else []
        )
        if self.folders:
            full_list.extend(self.folders)
        if not full_list:
            return []
        for folder in full_list:
            parts = folder.split("/")
            self.populate_node(main_dict, parts[0], parts[1:])

        nodes = []
        for key in main_dict:
            children = None
            if main_dict[key]:
                children = []
                self.populate_children(main_dict, key, children, key)
            nodes.append({"label": key, "value": key, "children": children})

        return nodes

    def add_replace_file(self, data_file, folder: str, filename: str, save=False, content_type=None) -> FileRef:
        path = f"{self.get_folder_path(folder)}/{filename}".strip("/")
        return self.add_replace_file_by_path(data_file, path, save, content_type=content_type)

    def add_replace_file_by_path(self, data_file, path: str, save=False, content_type=None) -> FileRef:
        file_ref = st.session_state.storage_client.write_file(path, data_file, content_type)
        replaced = False
        for idx, file in enumerate(self.files):
            if file.path == path:
                self.files[idx] = file_ref
                replaced = True
                break
        if not replaced:
            self.files.append(file_ref)
        if save:
            self.save()

        return file_ref

    def delete_file(self, file: FileRef, save=True):
        st.session_state.storage_client.delete_file(file.path)
        try:
            self.files.remove(file)
            if save:
                self.save()
        except ValueError:
            logging.warning(f"File {file.path} didn't exist and couldn't be deleted.")

    def add_folders(self, folders_string: str, save: bool = False):
        folders = set(self.folders)
        new_folders = folders_string.split(",")
        count = 0
        for folder in new_folders:
            folder = folder.strip().replace(" ", "_").strip("/")
            folder_parts = folder.split("/")
            for idx, part in enumerate(folder_parts):
                if idx == 0:
                    folders.add(f"{part}")
                else:
                    folders.add(f"{'/'.join(folder_parts[:idx+1])}")
                count += 1
        try:
            self.folders = list(folders)
        except AttributeError:
            logging.warning("Weird odmatic error, attempting to ignore")

        if save:
            self.save()

        return count

    def delete_folder(self, folder: str, save=False):
        try:
            folder_path = self.get_folder_path(folder)
            self.folders.remove(folder)
            for file in [x for x in self.files if folder_path in x.path]:
                self.delete_file(file)
            if save:
                self.save()
        except ValueError:
            logging.warning(f"Folder {folder} didn't exist and couldn't be deleted.")

    def delete(self):
        engine = get_engine()
        engine.delete(self)

    @classmethod
    def list_accessable(cls, engine, user_email, owner, include_public=False) -> List["Project"]:
        search_query = query.or_(cls.users == user_email, cls.owner == owner)
        if include_public:
            search_query = query.or_(Project.public == True, search_query)  # noqa
        return list(engine.find(cls, search_query))
