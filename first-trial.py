# Imports
from pathlib import PureWindowsPath

# Global Variables and Stuff
global_folder_path = "C:/Backup Projects/11 November 26/Test proj 1/"
global_reports_list = ["Section_1_Duct-1 CH-240 - Duct-1 CH-300", "Section_2_Duct-2 CH-240 - Duct-2 CH-300",
"Section_3_Duct-1 CH-8 - Duct-1 CH-80", "Section_4_Duct-2 CH-8 - Duct-2 CH-80"]
global_videos_list = ["Duct-1 CH-240 - Duct-1 CH-300_0001", "Duct-2 CH-240 - Duct-2 CH-300_0001",
"Duct-1 CH-8 - Duct-1 CH-80_0001", "Duct-2 CH-8 - Duct-2 CH-80_0001"]

# Functions Go Here
def get_folder_info():
    # Make this come from GUI folder selection
    root_folder_path = global_folder_path
    # Get the name of the root folder from the provided path
    root_folder_name = PureWindowsPath(root_folder_path).name
    
    return root_folder_name

def get_files_names():
    # Function Lists
    report_file_names = []
    report_file_names = global_reports_list
    video_file_names = []
    video_file_names = global_videos_list
    new_report_names = []
    new_video_names = []
    
    # Make this come from folders in previously provided root folder
    
    
    # Get Report Names from File Paths

    
    # Strip the Prefix from Report Names
    for rpt_file_name in report_file_names:
        rpt_name = rpt_file_name.split("_", 2)[-1]
        
        new_report_names.append(rpt_name)
        
    # Strip the Suffix from Video Names
    for vid_file_name in video_file_names:
        vid_name = vid_file_name.rsplit("_", 1)[0]
        
        new_video_names.append(vid_name)
        
    
    # Placeholder
    return new_report_names, new_video_names

# Main Routine Goes Here
print(get_folder_info())
print()
print(get_files_names())