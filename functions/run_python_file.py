import os
from config import MAX_CHARS
import subprocess
from google.genai import types 

def run_python_file(working_directory, file_path, args=None):

    try:
        working_dir_abs = os.path.abspath(working_directory) #directory where agent works inside
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path)) #absolute path to the file you want to write to
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs 
        #boolean -> returns True or False depending on whether the file is  inside the safe zone
        
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        

        command = ["python", target_dir]

        if args:
            command.extend(args)
        
        cpo = subprocess.run(
            command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30,
        )

    
        
        if cpo.stdout == "" and cpo.stderr == "":
            return f"No output produced"
        
        else:
            output_string = f"STDOUT: {cpo.stdout}\nSTDERR: {cpo.stderr}\n"

        if cpo.returncode != 0:
            output_string += f'Process exited with code {cpo.returncode}'
        
        return output_string
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="run the specified Python file from specified file_path relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to run",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional list of string arguments to pass to the Python script",
                items=types.Schema(
                    type=types.Type.STRING,
                ),
            ),
        },
        required=["file_path"]
    ),
)