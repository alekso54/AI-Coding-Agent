import os
from config import MAX_CHARS

def write_file(working_directory, file_path, content):

     try:  
        working_dir_abs = os.path.abspath(working_directory) #directory where agent works inside
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path)) #absolute path to the file you want to write to
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs 
        #boolean -> returns True or False depending on whether the file is  inside the safe zone 

        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        os.makedirs(os.path.dirname(target_dir), exist_ok=True)

        with open(target_dir, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

     except Exception as e:
        return f"Error: {str(e)}"
   

