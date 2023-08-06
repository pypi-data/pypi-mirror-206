# FIXME: Need to replace methods from service.py in MPL Commenting out until then

# import json
# from io import BytesIO
# from pathlib import Path
# from random import randint
# from typing import List, Tuple, Union  # , Optional

# import pandas as pd
# import streamlit as st

# # from mpl_toolbox_ui.common.config import Settings
# from xt_st_common.database import Project
# from xt_st_common.storage import FileRef
# from xt_st_common.utils import get_encoding_and_dialect, get_state

# # from bson.objectid import ObjectId

# REPLACE_FILE_HELP_TXT = (
#     "The new file can have a different name but must have the same extension."
#     "Warning: Uploading a new file that is significantly different to the original "
#     "can have catastrophic results."
# )

# # settings = Settings()


# @st.cache
# def get_df_preview(fileref: FileRef, num_rows=10):
#     # if filepath.suffix == ".zip":
#     #     frame = get_gdf_from_file(filepath)
#     #     return frame.iloc[:num_rows, :-1]
#     if fileref.get_ext() == ".csv":
#         file = st.session_state.storage_client.get_file(fileref.path)
#         encoding, dialect = get_encoding_and_dialect(file)
#         return pd.read_csv(file, nrows=num_rows, sep=dialect.delimiter, encoding=encoding)
#     if fileref.get_ext() == ".feather":
#         file = st.session_state.storage_client.get_file(fileref.path)
#         return pd.read_feather(file)

#     return None


# @st.cache
# def get_string_preview(fileref: FileRef):
#     file = st.session_state.storage_client.get_file(fileref.path)
#     return file.getvalue().decode("utf-8")


# def _state_name(project_id: str, folder: str) -> str:
#     return f"{project_id}-{folder}_fs"


# def project_selector(
#     header_text="Projects",
#     select_box_test="Select Project",
#     null_option="-- Select Project --",
#     st_context=st.sidebar,
#     select_on_change=None,
# ) -> Tuple[Union["Project", None], List["Project"]]:
#     """UI to select and create projects
#     Args:
#         root_path (Path): The root Path to where the project folders live
#     """

#     selected_project = get_state("selected_project")

#     if header_text is not None:
#         st_context.subheader(header_text)
#     include_public = st_context.checkbox("Include Public", value=False, key="include_public_projects")
#     projects = get_projects(include_public, st.session_state.project_cache)
#     sel_idx = 0
#     proj_options = {-1: null_option}
#     for idx, proj in enumerate(projects):
#         if selected_project and proj.id == selected_project.id:
#             sel_idx = idx + 1
#         proj_options[idx] = proj.name
#     project_idx = st_context.selectbox(
#         select_box_test,
#         index=sel_idx,
#         options=proj_options.keys(),
#         format_func=lambda x: proj_options[x],
#     )
#     selected_project = projects[project_idx] if project_idx != -1 else None
#     st.session_state.selected_project = selected_project

#     return selected_project, projects


# # def get_state(state_name, default=""):
# #     return st.session_state[state_name] if state_name in st.session_state else default


# def state_reset():
#     st.session_state.file_delete_confirm = ""
#     st.session_state.file_to_delete = None
#     st.session_state.file_success_message = ""
#     st.session_state.file_warning_message = ""


# def load_csv(
#     data_file,
#     st_context=st,
# ):
#     """
#     Takes a csv file and loads it into session_state
#     """

#     try:
#         encoding, dialect = get_encoding_and_dialect(data_file)
#         raw_df = pd.read_csv(
#             data_file,
#             header=None,
#             skip_blank_lines=True,
#             engine="python",
#             sep=None,
#             encoding=encoding,
#         )
#     except Exception as err:
#         raise ValueError("Could not parse txt/csv file.") from err

#     c1, c2 = st.columns([1, 3])
#     c1.header("CSV Data Import")
#     c2.subheader("Import Preview (15 Rows)")
#     if len(raw_df.columns) < 5:
#         c2.info(
#             "If preview has not loaded rows/columns correctly it may mean the wrong seperator has been "
#             + "detected. If that is the case than please check your file and remove unnecessary "
#             + "header information."
#         )
#     c2.write(raw_df.head(15))

#     with c1.form("config_df"):
#         row_options = list(range(16))
#         row_options_wnone = row_options.copy()
#         row_options_wnone.insert(0, "None")
#         header_row = st_context.selectbox(label="Column Names Row", options=row_options)
#         units_row = st_context.selectbox(label="Units Row", options=row_options_wnone)
#         skip_rows = st_context.multiselect(label="Skip Rows", options=list(range(9)))

#         if st.form_submit_button("Save Data"):
#             units = {}
#             if skip_rows is None:
#                 skip_rows = []

#             raw_df.columns = raw_df.iloc[header_row]

#             if units_row is not None and units_row != "None":
#                 units = raw_df.iloc[units_row].to_dict()
#                 if units_row != header_row and units_row not in skip_rows:
#                     raw_df.drop(labels=units_row, inplace=True)

#             if header_row not in skip_rows:
#                 raw_df.drop(labels=header_row, inplace=True)

#             raw_df.drop(labels=skip_rows, inplace=True)
#             raw_df = raw_df.reset_index(drop=True)

#             return raw_df, units
#     return None, None


# def file_manager(
#     project: Project,
#     types: List[str],
#     label: str,
#     st_context=st.sidebar,
#     help: str = None,
#     allow_upload=True,
#     allow_delete=True,
#     allow_replace=True,
#     key_prefix: str = "",
#     expand_file_actions=False,
# ):
#     file_delete_confirm = get_state("file_delete_confirm")
#     file_to_delete = get_state("file_to_delete")
#     file_success_message = get_state("file_success_message")
#     file_warning_message = get_state("file_warning_message")

#     st_context.subheader(f"Files: {project.name}")
#     if file_delete_confirm and file_to_delete:
#         st_context.warning(file_delete_confirm)
#         st_context.button("I'm Sure", on_click=action_delete_file, args=(file_to_delete,))

#     if file_success_message:
#         st_context.success(file_success_message)
#     if file_warning_message:
#         st_context.warning(file_warning_message)
#     # col1, col2 = st.columns([1, 2])
#     folders_dict = project.get_folders_map()
#     folder = st_context.selectbox(
#         "Select Borehole/Run", options=folders_dict.keys(), format_func=lambda x: folders_dict[x]
#     )
#     if folder:
#         path = project.get_folder_path(folder)
#     if path is not None:
#         state = _state_name(project, folder)
#         if state not in st.session_state:
#             st.session_state[state] = 0

#         if allow_upload:
#             if not st.session_state.get("file_manager_upload_file"):
#                 st.session_state["file_manager_upload_file"] = key_prefix + str(randint(1000, 100000000))
#             try_parse_csv = st_context.checkbox(
#                 "Parse CSV/TXT as Dataset",
#                 value=True,
#                 help=(
#                     "If a CSV or TXT file is uploaded you will be given options to help "
#                     + "calibrate it for use as a dataset."
#                 ),
#             )
#             uploaded_file = st_context.file_uploader(
#                 label,
#                 key=st.session_state["file_manager_upload_file"],
#                 type=types,
#                 help=help,
#                 # accept_multiple_files=True,
#             )

#             if (
#                 uploaded_file
#                 and try_parse_csv
#                 and (
#                     uploaded_file.name.lower().endswith(".csv") or uploaded_file.name.lower().endswith(".txt")
#                 )
#             ):
#                 frame = None
#                 try:
#                     frame, units = load_csv(uploaded_file, st)
#                 except ValueError:
#                     st_context.warning(
#                         "Could not parse CSV/TXT as a dataset. "
#                         + "This may mean the file requires special parsing (such as a PWAVE file)"
#                     )
#                     try_parse_csv = not st_context.button("Upload anyway")

#                 if frame is not None:
#                     data_name = f"{Path(uploaded_file.name).stem}.feather"
#                     with BytesIO() as buffer:
#                         frame.to_feather(buffer)
#                         buffer.seek(0)
#                         file_ref = project.add_replace_file(
#                             buffer,
#                             folder=folder,
#                             filename=data_name,
#                             save=True,
#                         )
#                     units_name = ""
#                     if units:
#                         units_name = f"{Path(uploaded_file.name).stem}_units.json"
#                         units_string = json.dumps(units)
#                         file_ref = project.add_replace_file(
#                             units_string,
#                             folder=folder,
#                             filename=units_name,
#                             save=True,
#                             content_type="application/json",
#                         )

#                     uploaded_file.close()
#                     reset_project_cache()
#                     st.session_state["file_manager_upload_file"] = key_prefix + str(randint(1000, 100000000))
#                     st.session_state.file_success_message = (
#                         f"File: {file_ref.name} Uploaded successfully as {data_name} {units_name}"
#                     )
#                     st.experimental_rerun()

#             if not try_parse_csv and uploaded_file:
#                 file_ref = project.add_replace_file(
#                     uploaded_file.getvalue(), folder=folder, filename=uploaded_file.name, save=True
#                 )
#                 uploaded_file.close()
#                 reset_project_cache()
#                 st.session_state["file_manager_upload_file"] = key_prefix + str(randint(1000, 100000000))
#                 st.session_state.file_success_message = f"File: {file_ref.name} Uploaded successfully"
#                 st.experimental_rerun()

#         files = project.get_files_in_folder(folder)
#         if files is not None and len(files) > 0:
#             selected_key = st_context.selectbox(
#                 "Select File", options=files.keys(), key=key_prefix + "file_manager_file_select"
#             )
#             selected_file = files[selected_key] if selected_key in files else None
#             if selected_file is not None:
#                 row = st_context.expander("File Actions", expanded=expand_file_actions)
#                 if len(selected_key) > 30:
#                     row.caption(selected_key)
#                 # options = []
#                 if allow_delete:
#                     row.button(
#                         "Delete",
#                         key=f"{key_prefix}file_delete_btn",
#                         on_click=submit_delete_file,
#                         args=(selected_file,),
#                     )
#                 if selected_key.lower().endswith((".zip", ".csv", ".geojson", ".gpkg", ".feather")):
#                     preview_frame = row.button(
#                         "Preview Frame",
#                         key=f"{key_prefix}file_manager_preview_frame",
#                     )
#                     if preview_frame:
#                         with st.expander(f"**Frame Viewer:** {selected_file.name}", expanded=True):
#                             st.dataframe(get_df_preview(selected_file))
#                 if selected_key.lower().endswith((".json", ".yml", ".yaml", ".txt")):
#                     preview_frame = row.button(
#                         "Preview File",
#                         key=f"{key_prefix}file_manager_preview_file",
#                     )
#                     if preview_frame:
#                         with st.expander(f"**Frame Viewer:** {selected_file.name}", expanded=True):
#                             st.write(get_string_preview(selected_file))
#                 if row.checkbox("Prepare Download", key=key_prefix + "file_manager_download_chbx"):
#                     file_data = st.session_state.storage_client.get_file(selected_file.path)

#                     row.download_button(
#                         "Download",
#                         file_data,
#                         selected_file.name,
#                         key=key_prefix + "file_manager_download_button",
#                     )
#                 if allow_replace:
#                     if not st.session_state.get("file_manager_replace_file"):
#                         st.session_state["file_manager_replace_file"] = key_prefix + str(
#                             randint(1000, 100000000)
#                         )
#                     if uploaded_replace_file := row.file_uploader(
#                         "Replace the selected file",
#                         key=st.session_state["file_manager_replace_file"],
#                         type=selected_file.get_ext(),
#                         help=REPLACE_FILE_HELP_TXT,
#                         accept_multiple_files=False,
#                     ):
#                         project.add_replace_file_by_path(uploaded_replace_file, selected_file.path, save=True)
#                         uploaded_replace_file.close()
#                         st.session_state["file_manager_replace_file"] = key_prefix + str(
#                             randint(1000, 100000000)
#                         )
#                         st.experimental_rerun()
#                         # st.radio(
#                         #     label,
#                         #     options,
#                         #     index=0,
#                         #     format_func=special_internal_function,
#                         #     key=None,
#                         #     help=None,
#                         #     on_change=None,
#                         #     args=None,
#                         #     kwargs=None,
#                         # )
#         else:
#             st_context.info("No files in folder.")

#         state_reset()
#     return path, folder
