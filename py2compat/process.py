from subprocess import Popen, PIPE
import os
import shutil

_remote_import_dir = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, "_remote"))


def clear_folder(workdir):
    shutil.rmtree(workdir)
    os.mkdir(workdir)


def run_qua_module(python_path, module, env, workdir, shell=False):
    args = [python_path, "-m", module, workdir]
    return _run_python(args, env, shell)


def run_qua_file(python_path, file, env, workdir, shell=False):
    args = [python_path, file, workdir]
    return _run_python(args, env, shell)


def run_qua_file_in_conda_environment(conda_environment, file, env, workdir, shell=False):
    args = ['conda', 'activate', conda_environment, '&&' 'python', file, workdir]
    return _run_python(args, env, shell)


def run_qua_module_in_conda_environment(conda_environment, module, env, workdir, shell=False):
    args = ['conda', 'activate', conda_environment, '&&' 'python', '-m', module, workdir]
    return _run_python(args, env, shell)


def _run_python(args, env, shell):
    full_env = {}
    full_env.update(os.environ)
    full_env.update(env)
    full_env.update({
        "PYTHONPATH": full_env.get("PYTHONPATH", "") + os.pathsep + _remote_import_dir
    })
    proc = Popen(args, env=full_env, stdout=PIPE, stderr=PIPE, shell=shell)
    return proc
